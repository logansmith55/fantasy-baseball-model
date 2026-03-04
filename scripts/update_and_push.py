import os
from pybaseball import batting_stats
import pandas as pd
import subprocess

# Make sure data folder exists
os.makedirs("../data", exist_ok=True)

# Pull MLB batting stats
df = batting_stats(2025, qual=0)

# Save CSV
csv_path = "../data/batting_stats.csv"
df.to_csv(csv_path, index=False)
print("Batting stats saved!")

# Stage all changes
subprocess.run(["git", "add", "."], check=False)

# Commit changes
subprocess.run(["git", "commit", "-m", "update batting stats CSV"], check=False)

# Push to GitHub
subprocess.run(["git", "push", "origin", "main"], check=False)
print("Changes pushed to GitHub!")