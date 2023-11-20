import pandas as pd

def convert_to_shopify_format(input_csv, output_csv):
    # Read the input CSV file
    df = pd.read_csv(input_csv)

    # Create a new DataFrame with Shopify's required columns
    shopify_df = pd.DataFrame()

    # Map your existing columns to Shopify's columns
    shopify_df['Title'] = df['Title']
    shopify_df['Body (HTML)'] = df['Description']
    shopify_df['Vendor'] = df['Vendor']
    shopify_df['Type'] = df['Type']
    shopify_df['Tags'] = df['Tags']
    shopify_df['Published'] = 'TRUE'  # Assuming you want all products to be published
    shopify_df['Option1 Name'] = df['Option1 Name']
    shopify_df['Option1 Value'] = df['Option1 Value']
    shopify_df['Option2 Name'] = df['Option2 Name']
    shopify_df['Option2 Value'] = df['Option2 Value']
    shopify_df['Option3 Name'] = df['Option3 Name']
    shopify_df['Option3 Value'] = df['Option3 Value']
    shopify_df['Variant SKU'] = df['SKU']
    shopify_df['Variant Grams'] = df['Weight (grams)']  # Replace with your weight column
    shopify_df['Variant Inventory Tracker'] = 'shopify'
    shopify_df['Variant Inventory Qty'] = df['Inventory']
    shopify_df['Variant Inventory Policy'] = 'deny'  # Adjust as needed
    shopify_df['Variant Fulfillment Service'] = 'manual'  # Adjust as needed
    shopify_df['Variant Price'] = df['Price']
    shopify_df['Variant Compare At Price'] = df['Compare At Price']  # Adjust as needed

    # Write the Shopify-formatted DataFrame to a new CSV file
    shopify_df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    convert_to_shopify_format('input.csv', 'output_shopify.csv')
