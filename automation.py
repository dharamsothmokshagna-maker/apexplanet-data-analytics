# =====================================================
# ApexPlanet Internship
# Task 5 - Data Automation Pipeline
# =====================================================

import pandas as pd
import os

# -----------------------------------------------------
# Project Paths
# -----------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_FOLDER = os.path.join(BASE_DIR, "data")
REPORT_FOLDER = os.path.join(BASE_DIR, "reports")

RAW_DATA = os.path.join(DATA_FOLDER, "Sample_Superstore_Full_Dataset.csv")
CLEAN_DATA = os.path.join(DATA_FOLDER, "cleaned_superstore.csv")

KPI_REPORT = os.path.join(REPORT_FOLDER, "Business_KPIs.xlsx")

# Create reports folder if it doesn't exist
os.makedirs(REPORT_FOLDER, exist_ok=True)

# -----------------------------------------------------
# Load Dataset
# -----------------------------------------------------

print("Loading dataset...")

df = pd.read_csv(RAW_DATA, encoding="latin1")

print("Dataset Loaded Successfully!")
print(f"Rows : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

# -----------------------------------------------------
# Data Cleaning
# -----------------------------------------------------

print("\nCleaning Dataset...")

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

print("Cleaning Completed!")
print(f"Remaining Rows : {len(df)}")

# -----------------------------------------------------
# Save Cleaned Dataset
# -----------------------------------------------------

df.to_csv(CLEAN_DATA, index=False)

print("\nCleaned Dataset Saved Successfully!")

# -----------------------------------------------------
# Calculate Business KPIs
# -----------------------------------------------------

print("\nCalculating Business KPIs...")

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = len(df)
average_discount = df["Discount"].mean()

print("KPIs Calculated Successfully!")

# -----------------------------------------------------
# Export KPIs to Excel
# -----------------------------------------------------

kpi_df = pd.DataFrame({
    "Metric": [
        "Total Sales",
        "Total Profit",
        "Total Orders",
        "Average Discount"
    ],
    "Value": [
        total_sales,
        total_profit,
        total_orders,
        average_discount
    ]
})

kpi_df.to_excel(KPI_REPORT, index=False)

print("\nBusiness KPIs Exported Successfully!")
print(f"KPI Report Saved At:\n{KPI_REPORT}")

print("\n======================================")
print("Automation Pipeline Completed!")
print("======================================")