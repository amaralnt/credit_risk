import pandas as pd
import numpy as np
from pathlib import Path

def process_data():
    # Get the project root directory 
    project_root = Path(__file__).resolve().parents[2]
    
    # Define input and output paths using absolute paths
    input_path = project_root / 'data/raw/csv/accepted.csv'
    output_path = project_root / 'data/interim/parquet'
    
    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Verify input file exists
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found at: {input_path}")
    
    # Define columns to keep
    selected_columns = [
        'loan_amnt', 'term', 'int_rate', 'installment', 'grade', 'sub_grade',
        'emp_title', 'emp_length', 'home_ownership', 'annual_inc',
        'verification_status', 'issue_d', 'loan_status', 'purpose', 'title',
        'zip_code', 'addr_state', 'dti', 'earliest_cr_line', 'open_acc',
        'pub_rec', 'revol_bal', 'revol_util', 'total_acc', 'initial_list_status',
        'application_type', 'mort_acc', 'pub_rec_bankruptcies'
    ]
    
    # Read CSV file with only selected columns
    print("Reading CSV file...")
    df = pd.read_csv(input_path, usecols=selected_columns)
    
    # Take random sample of 2,000,000 rows
    print("Sampling 2,000,000 rows...")
    if len(df) > 2_000_000:
        df = df.sample(n=2_000_000, random_state=42)
    
    # Save as parquet file
    print("Saving to parquet format...")
    df.to_parquet(output_path / 'accepted.parquet', index=False)
    print("Processing complete!")

if __name__ == "__main__":
    process_data()