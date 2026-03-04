from pybaseball import batting_stats
import pandas as pd
import subprocess

# 1️⃣ Pull MLB data
df = batting_stats(2025, qual=0)
csv_path = "data/batting_stats.csv"
df.to_csv(csv_path, index=False)
print("Batting stats saved.")