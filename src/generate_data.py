import os
import pandas as pd
import random
from datetime import datetime, timedelta

# 確認資料夾存在，不存在就建立
os.makedirs("data", exist_ok=True)

# 模擬參數
num_trades = 2000
symbols = ["BTC", "ETH", "SOL"]
sides = ["BUY", "SELL"]

# 產生交易資料
trades = []
start_time = datetime.now()

for i in range(1, num_trades+1):
    symbol = random.choice(symbols)
    side = random.choice(sides)
    price = round(random.uniform(50, 45000), 2)  # 簡化價格範圍
    quantity = random.randint(1, 5)
    timestamp = start_time + timedelta(seconds=i*10)  # 每筆交易間隔10秒
    trades.append([i, timestamp, symbol, side, price, quantity])

# 轉成 DataFrame
df = pd.DataFrame(trades, columns=["trade_id", "timestamp", "symbol", "side", "price", "quantity"])

# 輸出 CSV
df.to_csv("data/simulated_trades.csv", index=False)

print("Simulated trade data saved to data/simulated_trades.csv")