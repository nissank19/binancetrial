import pandas as pd
from sqlalchemy import create_engine
import os
import time

INPUT_FILE = "/app/cppbinace/build/output.csv"
TEMP_FILE = "/app/cppbinace/build/processing_batch.csv"
DB_URL = 'mysql+pymysql://root:wearegoingtomakeit@db:3306/binance'
engine = create_engine(DB_URL)


def connect_with_retry(engine, retries=10, delay=5):
    for i in range(retries):
        try:
            with engine.connect() as connection:
                print("Connection to MySQL successful.")
                return True
        except Exception:
            print(f"Waiting for MySQL... ({i + 1}/{retries})")
            time.sleep(delay)
    return False


def process_data():
    if os.path.exists(INPUT_FILE) and os.path.getsize(INPUT_FILE) > 0:
        try:
            os.rename(INPUT_FILE, TEMP_FILE)
            df = pd.read_csv(TEMP_FILE)

            if not df.empty:
                pd.set_option('future.no_silent_downcasting', True)
                df = df.replace({True: 1, False: 0}).infer_objects(copy=False)

                if 'timestamp' in df.columns:
                    df['dt'] = pd.to_datetime(df['timestamp'], unit='ms')
                    df['hour'] = df['dt'].dt.hour
                    df['minute'] = df['dt'].dt.minute
                    df['seconds'] = df['dt'].dt.second
                    df_sql = df.drop('dt', axis=1)
                else:
                    df_sql = df

                row_count = len(df_sql)
                # USING 'replace' ONCE TO FIX COLUMN ERRORS
                df_sql.to_sql('data', con=engine, if_exists='append', index=False)
                print(f"Success: Recreated table and added {row_count} rows.")

            os.remove(TEMP_FILE)

        except Exception as e:
            print(f"Error: {e}")
            if os.path.exists(TEMP_FILE) and not os.path.exists(INPUT_FILE):
                os.rename(TEMP_FILE, INPUT_FILE)


if __name__ == "__main__":
    if connect_with_retry(engine):
        print("Cleaner logic is now monitoring...")
        while True:
            process_data()
            time.sleep(5)