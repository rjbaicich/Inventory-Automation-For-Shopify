import pandas as pd

def convert_to_shopify_format(input_file, output_file="Inventory_update.csv"):
    
    # Read the input CSV file
    df = pd.read_csv(input_file)

    # Customize this section based on your specific mapping requirements
  # Map your columns to Shopify columns

    mapping = {
        'Handle': 'Product Title',
        'Title': 'Product Title',
        'Body (HTML)': 'Product Description',
        'Vendor': 'Vendor',
        'Product Category': 'Category',  # Replace 'Category' with the actual column name in your input file
        'Type': 'Type',
        'Tags': 'Tags',
        'Published': 'Published',
        'Option1 Name': 'Option1 Name',
        'Option1 Value': 'Option1 Value',
        'Option2 Name': 'Option2 Name',
        'Option2 Value': 'Option2 Value',
        'Option3 Name': 'Option3 Name',
        'Option3 Value': 'Option3 Value',
        'Variant SKU': 'Variant SKU',
        'Variant Grams': 'Variant Grams',
        'Variant Inventory Tracker': 'Variant Inventory Tracker',
        'Variant Inventory Qty': 'Variant Inventory Qty',
        'Variant Inventory Policy': 'Variant Inventory Policy',
        'Variant Fulfillment Service': 'Variant Fulfillment Service',
        'Variant Price': 'Variant Price',
        'Variant Compare At Price': 'Variant Compare At Price',
        'Variant Requires Shipping': 'Variant Requires Shipping',
        'Variant Taxable': 'Variant Taxable',
        'Variant Barcode': 'Variant Barcode',
        'Image Src': 'Image Src',
        'Image Position': 'Image Position',
        'Image Alt Text': 'Image Alt Text',
        'Gift Card': 'Gift Card',
        'SEO Title': 'SEO Title',
        'SEO Description': 'SEO Description',
        'Google Shopping / Google Product Category': 'Google Shopping / Google Product Category',
        'Variant Image': 'Variant Image',
        'Variant Weight Unit': 'Variant Weight Unit',
        'Variant Tax Code': 'Variant Tax Code',
        'Cost per item': 'Cost per item',
        'Included / [Primary]': 'Included / [Primary]',
        'Included / International': 'Included / International',
        'Price / International': 'Price / International',
        'Compare At Price / International': 'Compare At Price / International',
        'Status': 'Status',

        # Add more mappings as needed
        
    }

# Inside convert_to_shopify_format function
unmapped_columns = set(df.columns) - set(mapping.keys())
if unmapped_columns:
    print(f"Warning: Some columns do not have mappings: {', '.join(unmapped_columns)}")

# Inside convert_to_shopify_format function
df['Variant Price'] = pd.to_numeric(df['Variant Price'], errors='coerce')

      # Apply the mapping to the DataFrame

    df = df.rename(columns=mapping)

    # Additional formatting or data manipulation if needed

    # Save the formatted DataFrame as a CSV file

    df.to_csv(output_file, index=False)
    print(f"Converted Shopify inventory saved as {output_file}")

# Inside convert_to_shopify_format function
df['Variant Inventory Tracker'].fillna('default_tracker', inplace=True)

# Inside convert_to_shopify_format function
df['Profit Margin'] = (df['Variant Price'] - df['Cost per item']) / df['Variant Price'] * 100

# Inside convert_to_shopify_format function
summary_stats = df.describe(include='all')
print("Summary Statistics:")
print(summary_stats)

# Inside convert_to_shopify_format function
subset_columns = ['Product Title', 'Variant SKU', 'Variant Price']
df.drop_duplicates(subset=subset_columns, keep='first', inplace=True)


if __name__ == "__main__":
    
    # Specify the path to your input CSV file

    input_csv_path = "path/to/your/input_file.csv"

    # Convert and save to Shopify format

    convert_to_shopify_format(input_csv_path)