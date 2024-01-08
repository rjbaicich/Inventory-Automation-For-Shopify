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

      # Warn about unmapped columns
    unmapped_columns = set(df.columns) - set(mapping.keys())
    if unmapped_columns:
        print(f"Warning: Some columns do not have mappings: {', '.join(unmapped_columns)}")

    # Convert 'Variant Price' column to numeric
    df['Variant Price'] = pd.to_numeric(df['Variant Price'], errors='coerce')

    # Apply the mapping to the DataFrame
    df = df.rename(columns=mapping)