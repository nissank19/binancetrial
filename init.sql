CREATE TABLE IF NOT EXISTS data (
    aggregate_trade_id BIGINT,
    price DECIMAL(18,8),
    quantity DECIMAL(20,8),
    first_trade_id BIGINT,
    last_trade_id BIGINT,
    buyer_is_maker TINYINT,
    best_price_match TINYINT,
    hour INT,
    minute INT,
    seconds INT
);