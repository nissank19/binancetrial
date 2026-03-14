# 1. Use a Python base image (Debian-based)
FROM python:3.10-slim

# 2. Install system-level dependencies for C++, CMake, and Networking
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    g++ \
    libcurl4-openssl-dev \
    nlohmann-json3-dev \
    && rm -rf /var/lib/apt/lists/*

# 3. Set the working directory inside the container
WORKDIR /app

# 4. Install Python libraries
RUN pip install --no-cache-dir \
    pandas \
    scikit-learn \
    sqlalchemy \
    pymysql \
    cryptography

# 5. Copy all project files into the container
COPY . .

# 6. Build the C++ Tracker
# This creates the 'build' folder and compiles CryptoTracker automatically
RUN cd cppbinace && \
    mkdir -p build && \
    cd build && \
    cmake .. && \
    make

# 7. Start the Data Pipeline
# - 'cd cppbinace/build && ./CryptoTracker' starts the data collection
# - '&' allows it to run in the background
# - 'python3 -u' starts the cleaner and forces logs to show up immediately
CMD ["sh", "-c", "cd /app/cppbinace/build && ./CryptoTracker & python3 -u /app/bianpyt/cleaner.py"]