# scripts/analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure outputs folder exists
os.makedirs("../outputs", exist_ok=True)

# ----------------------------
# Task 1: Load & Explore Data
# ----------------------------

try:
    df = pd.read_csv("../data/CRMreport.csv")
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: Dataset not found. Check the path to CRMreport.csv")
    exit()

# Preview
print("\n--- First 5 rows ---")
print(df.head())

# Dataset info
print("\n--- Info ---")
print(df.info())

# Check missing values
print("\n--- Missing values ---")
print(df.isnull().sum())

# Drop duplicates
df = df.drop_duplicates()

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# ----------------------------
# Task 2: Basic Data Analysis
# ----------------------------

print("\n--- Summary statistics ---")
print(df.describe(include="all"))

# Grouping example: Average DAYS per Package
if "pkg" in df.columns and "days" in df.columns:
    avg_days_pkg = df.groupby("pkg")["days"].mean().sort_values(ascending=False)
    print("\n--- Average DAYS per Package ---")
    print(avg_days_pkg)

# ----------------------------
# Task 3: Data Visualizations
# ----------------------------

sns.set(style="whitegrid")

# 1. Line chart: Installs over time
if "installdate" in df.columns:
    df["installdate"] = pd.to_datetime(df["installdate"], errors="coerce")
    installs_over_time = df.groupby(df["installdate"].dt.to_period("M")).size()
    installs_over_time.plot(kind="line", marker="o")
    plt.title("Installations Over Time")
    plt.xlabel("Month")
    plt.ylabel("Number of Installs")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("../outputs/line.png")
    plt.close()

# 2. Bar chart: Average DAYS per Package
if "pkg" in df.columns and "days" in df.columns:
    sns.barplot(x="pkg", y="days", data=df, estimator="mean", ci=None, order=df["pkg"].value_counts().index)
    plt.title("Average DAYS per Package")
    plt.xlabel("Package")
    plt.ylabel("Average DAYS")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("../outputs/bar.png")
    plt.close()

# 3. Histogram: Distribution of DAYS
if "days" in df.columns:
    plt.hist(df["days"].dropna(), bins=20, edgecolor="black")
    plt.title("Distribution of DAYS")
    plt.xlabel("Days")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("../outputs/histogram.png")
    plt.close()

# 4. Scatter plot: DAYS vs BAND
if "days" in df.columns and "band" in df.columns:
    sns.scatterplot(x="days", y="band", data=df)
    plt.title("Days vs Band")
    plt.xlabel("Days")
    plt.ylabel("Band")
    plt.tight_layout()
    plt.savefig("../outputs/scatter.png")
    plt.close()

print("\nAnalysis complete. Charts saved in outputs/ folder.")
