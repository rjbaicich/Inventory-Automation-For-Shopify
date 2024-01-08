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


    # Additional formatting or data manipulation if needed

    # Fill NaN values in 'Variant Inventory Tracker'
    df['Variant Inventory Tracker'].fillna('default_tracker', inplace=True)

    # Calculate 'Profit Margin'
    df['Profit Margin'] = (df['Variant Price'] - df['Cost per item']) / df['Variant Price'] * 100

    # Summary statistics
    summary_stats = df.describe(include='all')
    print("Summary Statistics:")
    print(summary_stats)

    # Remove duplicates based on specified columns
    subset_columns = ['Product Title', 'Variant SKU', 'Variant Price']
    df.drop_duplicates(subset=subset_columns, keep='first', inplace=True)


    # Custom data transformation function
    def custom_data_transformation(row):
        # Implement your custom transformation logic here
        # Example: Concatenate Product Title and Variant SKU
        return f"{row['Product Title']} - {row['Variant SKU']}"

    # Apply the custom transformation to a new column
    df['Custom Column'] = df.apply(custom_data_transformation, axis=1)
    # Save the formatted DataFrame as a CSV file
    df.to_csv(output_file, index=False)
    print(f"Converted Shopify inventory saved as {output_file}")

if __name__ == "__main__":
    # Specify the path to your input CSV file
    input_csv_path = "path/to/your/input_file.csv"

    # Convert and save to Shopify format
    convert_to_shopify_format(input_csv_path)

# Inside convert_to_shopify_format function
df['Total Revenue'] = df['Variant Price'] * df['Variant Inventory Qty']
total_revenue = df['Total Revenue'].sum()
print(f"Total Revenue: ${total_revenue:.2f}")