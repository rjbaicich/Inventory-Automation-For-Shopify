import pandas as pd

def convert_to_shopify_format(input_file, output_file="Inventory_update.csv"):
    # Read the input CSV file
    df = pd.read_csv(input_file)

    # Customize this section based on your specific mapping requirements
    # Map your columns to Shopify columns
    mapping = {
        'Product Title': 'Title',
        'Product Description': 'Body (HTML)',
        'Vendor': 'Vendor',
        # Add more mappings as needed
    }
      # Apply the mapping to the DataFrame
    df = df.rename(columns=mapping)

    # Additional formatting or data manipulation if needed

    # Save the formatted DataFrame as a CSV file
    df.to_csv(output_file, index=False)
    print(f"Converted Shopify inventory saved as {output_file}")
