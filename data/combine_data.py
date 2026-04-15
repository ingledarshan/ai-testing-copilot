# combine_data.py

import pandas as pd

# Load datasets
manual = pd.read_csv("data/test_cases.csv")
synthetic = pd.read_csv("data/synthetic_queries.csv")
adversarial = pd.read_csv("data/adversarial_queries.csv")

# Standardize columns
manual_df = manual[["query"]].copy()
manual_df["type"] = "manual"
manual_df["intent"] = "refund"

synthetic_df = synthetic.copy()
synthetic_df["type"] = "synthetic"
synthetic_df["intent"] = "refund"


adversarial_df = adversarial.copy()
adversarial_df["type"] = "adversarial"
adversarial_df["intent"] = "refund"

# Combine all
combined_df = pd.concat([manual_df, synthetic_df, adversarial_df])

# Remove duplicates
combined_df = combined_df.drop_duplicates()

# Save final dataset
combined_df.to_csv("data/final_dataset.csv", index=False)

print("Combined dataset created successfully.")

# Run:
# python data/combine_data.py

evaluation/run_pipeline.py
