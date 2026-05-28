import pandas as pd
import requests
import os
from dotenv import load_dotenv

# Load environment variables (Security best practice)
load_dotenv()

def fetch_data(api_url):
    """Fetches data from an API."""
    print(f"Fetching data from {api_url}...")
    # Example logic: response = requests.get(api_url)
    return pd.DataFrame() # Placeholder for your data

def validate_data(df):
    """
    Validates input dataframe for null values and data types.
    Returns: Boolean (True if valid, False otherwise)
    """
    print("Validating data...")
    if df.isnull().values.any():
        return False
    return True

def main():
    """Main execution flow of the pipeline."""
    print("Starting Data Pipeline...")
    
    # 1. Ingest
    data = fetch_data("https://api.example.com/data")
    
    # 2. Validate
    if validate_data(data):
        print("Data is valid. Proceeding with transformation.")
        # 3. Transform/Load logic here
    else:
        print("Data validation failed.")

if __name__ == "__main__":
    main()
