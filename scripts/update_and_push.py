import os
from pybaseball import batting_stats, pitching_stats
import pandas as pd
import subprocess

# ---------- Ensure folders exist ----------
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
data_folder = os.path.join(repo_root, "data")
os.makedirs(data_folder, exist_ok=True)

# ---------- Pull MLB batting stats ----------
print("Pulling MLB batting stats...")
batting_df = batting_stats(2021, 2025, qual=0)  # qual=0 gets all batters
csv_path = os.path.join(data_folder, "batting_stats.csv")
batting_df.to_csv(csv_path, index=False)
print(f"Saved batting stats to {csv_path}")

csv_path = os.path.join(data_folder, "batting_stats.csv")
batting_df.to_csv(csv_path, index=False)
print(f"Saved batting stats to {csv_path}")

# ---------- Pull MLB pitching stats ----------
print("Pulling MLB pitching stats...")
pitching_df = pitching_stats(2021, 2025, qual=0)  # qual=0 gets all pitchers
csv_path = os.path.join(data_folder, "pitching_stats.csv")
pitching_df.to_csv(csv_path, index=False)
print(f"Saved pitching stats to {csv_path}")


csv_path = os.path.join(data_folder, "pitching_stats.csv")
pitching_df.to_csv(csv_path, index=False)
print(f"Saved pitching stats to {csv_path}")

# ---------- Stage and commit ----------
print("Staging changes...")
subprocess.run(["git", "add", "."], cwd=repo_root)

print("Committing changes...")
subprocess.run(["git", "commit", "-m", "Update batting and pitching stats CSVs"], cwd=repo_root, check=False)

# ---------- Push to GitHub ----------
print("Pushing to GitHub...")
subprocess.run(["git", "push", "origin", "main"], cwd=repo_root, check=False)

print("All done! Your CSVs and scripts are updated on GitHub.")