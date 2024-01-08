import pandas as pd

def convert_to_shopify_format(input_file, output_file="Inventory_update.csv"):
    # Read the input CSV file
    df = pd.read_csv(input_file)

    # Map your columns to Shopify columns
    mapping = {
        'Handle': 'Product Title',
        'Title': 'Product Title',
        'Body (HTML)': 'Product Description',
        # ... (other mappings)
        'Status': 'Status',
        # Add more mappings as needed
    }