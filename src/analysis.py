import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# 設定 Seaborn 風格
sns.set_style("whitegrid") 

# 確認資料夾
os.makedirs("output", exist_ok=True)

# 讀取資料
df = pd.read_csv("data/simulated_trades.csv")

# 1️⃣ 總成交量
total_volume = df.groupby("symbol")["quantity"].sum()
print("Total Volume per symbol:\n", total_volume)

plt.figure(figsize=(6,4))
sns.barplot(x=total_volume.index, y=total_volume.values, palette="viridis")
plt.title("Total Volume per Symbol")
plt.ylabel("Quantity")
plt.savefig("output/total_volume.png")
plt.close()

# 2️⃣ Net Position
df["signed_qty"] = df.apply(lambda row: row["quantity"] if row["side"]=="BUY" else -row["quantity"], axis=1)
net_position = df.groupby("symbol")["signed_qty"].sum()
print("\nNet Position per symbol:\n", net_position)

plt.figure(figsize=(6,4))
sns.barplot(x=net_position.index, y=net_position.values, palette="coolwarm")
plt.title("Net Position per Symbol")
plt.ylabel("Net Quantity")
plt.savefig("output/net_position.png")
plt.close()

# 3️⃣ Total PnL
df["pnl"] = df.apply(lambda row: row["price"]*row["quantity"] if row["side"]=="SELL" else 0, axis=1)
total_pnl = df.groupby("symbol")["pnl"].sum()
print("\nTotal PnL per symbol:\n", total_pnl)

plt.figure(figsize=(6,4))
sns.barplot(x=total_pnl.index, y=total_pnl.values, palette="magma")
plt.title("Total PnL per Symbol")
plt.ylabel("PnL")
plt.savefig("output/total_pnl.png")
plt.close()

# 4️⃣ 異常大單
# 過濾出大單
large_trades = df[df["quantity"]>3]

# 把 timestamp 轉成 datetime
large_trades['timestamp'] = pd.to_datetime(large_trades['timestamp'])

# 印出大單
print("\nLarge trades (quantity > 3):\n", large_trades)

plt.figure(figsize=(10,5))
sns.scatterplot(
    data=large_trades,
    x="timestamp",
    y="quantity",
    hue="symbol",
    style="side",
    palette="Set2",
    s=40
)
plt.title("Large Trades (Quantity > 3)")
plt.xlabel("Timestamp")
plt.ylabel("Quantity")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/large_trades.png")
plt.close()

# 5️⃣ Reconciliation
num_trades = len(df)
expected_trades = 2000
print("\nReconciliation check:")
print(f"Total trades: {num_trades}, Expected: {expected_trades}")