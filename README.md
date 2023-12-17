# Shopify CSV Converter

## Overview

Welcome to the Shopify CSV Converter! This Python script is designed to simplify and automate inventory management for Shopify store owners. By converting a CSV file containing product information into Shopify's required CSV format for product imports, the script streamlines the process of updating and managing your product inventory on the Shopify platform.

## Features

- **Effortless Integration:** Seamlessly integrates with Shopify's platform, allowing for easy product data import.
- **Customizable Mapping:** Customize column mappings to match your specific input CSV file structure.
- **Flexible Architecture:** Designed with a modular and flexible architecture for future integration with other e-commerce platforms.
- **User-Friendly:** Aims to provide a user-friendly interface for efficient inventory tracking and order fulfillment processes.

## Getting Started

1. **Installation:**
   - Ensure you have Python installed on your system.
   - Install required dependencies using `pip install pandas`.

2. **Usage:**
   - Clone the repository and navigate to the project directory.
   - Replace the sample input CSV file path with your own file path in the `if __name__ == "__main__":` section.

```python
# Specify the path to your input CSV file
input_csv_path = "path/to/your/input_file.csv"

# Convert and save to Shopify format
convert_to_shopify_format(input_csv_path)