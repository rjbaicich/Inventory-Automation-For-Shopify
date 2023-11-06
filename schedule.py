import schedule
import time

from email_processing import process_inventory_email
from database_operations import create_inventory_table
from shopify_operations import upload_inventory_to_shopify
from data_transformation import transform_data

# Schedule the job to run once daily
schedule.every().day.at("08:00").do(process_inventory_email)  # Adjust the time as per your requirement

# Keep the script running to execute the scheduled jobs
while True:
    schedule.run_pending()
    time.sleep(1)
