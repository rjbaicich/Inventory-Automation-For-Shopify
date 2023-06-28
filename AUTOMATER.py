import schedule
import time
import imaplib
import email
import psycopg2
import pandas as pd
import shopify

def process_inventory():
    # Connect to the email server
    mail = imaplib.IMAP4_SSL('imap.example.com')  # Replace with your email server

    # Login to your email account
    mail.login('your_email@example.com', 'your_password')  # Replace with your email credentials

    # Select the mailbox to search for the email
    mail.select('inbox')

    # Search for emails containing the CSV file
    result, data = mail.search(None, 'ALL')  # You can customize the search criteria

    # Get the latest email containing the CSV file
    latest_email_id = data[0].split()[-1]
    result, email_data = mail.fetch(latest_email_id, '(RFC822)')

    # Parse the email data
    raw_email = email_data[0][1]
    email_message = email.message_from_bytes(raw_email)

    # Download the CSV attachment
    for part in email_message.walk():
        if part.get_content_type() == 'text/csv':
            attachment = part.get_payload(decode=True)
            with open('inventory.csv', 'wb') as file:
                file.write(attachment)

    # Read the CSV data into a pandas DataFrame
    data = pd.read_csv('inventory.csv')

    # Clean the data
    # ...

    # Raise the price of each item by 20%
    data['price'] = data['price'] * 1.2

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(dbname='your_dbname', user='your_username',
                            password='your_password', host='your_host')

    cur = conn.cursor()

    # Define the columns for the table
    columns = list(data.columns)  # Use all columns from the CSV

    # Create the table in the database
    create_table_query = f'''
        CREATE TABLE inventory (
            {", ".join([f"{column} VARCHAR(255)" for column in columns])}
        )
    '''

    cur.execute(create_table_query)

    # Insert the data into the database
    for _, row in data.iterrows():
        insert_query = f'''
            INSERT INTO inventory ({", ".join(columns)})
            VALUES ({", ".join(["%s"] * len(columns))})
        '''
        cur.execute(insert_query, tuple(row))

    # Commit the changes to the database
    conn.commit()

    # Close the database connection
    cur.close()
    conn.close()

    # Upload the data to Shopify
    shopify.Shopify().upload_inventory_data(data)  # Replace with your Shopify upload code

    # Save the cleaned data to an Excel file
    output_file = 'output.xlsx'
    data.to_excel(output_file, index=False)

# Schedule the job to run once daily
schedule.every().day.at("08:00").do(process_inventory)  # Adjust the time as per your requirement

# Keep the script running to execute the scheduled jobs
while True:
    schedule.run_pending()
    time.sleep(1)



Questions to be answered to add to above code:


How to clean a csv to fit another format? As in convert to another format?

How to output that new formatted csv file to a saved file that I can upload?

How to automate the last step(the upload to shopify)?

How to take that original csv from an email once daily?

How to run this program once daily automatically?
To automate this process to run daily, you can use a scheduler tool like cron 
(on Unix-based systems) or Task Scheduler (on Windows). 

Do we need a database or sql connection to do this?
if you only need to process the data and perform operations
 without persistent storage, a database might not be necessary. 
 It ultimately depends on your project's requirements and the volume
 of data you're dealing with.


Can I set this up on a server to run automatically or no need?

What parts need to use a scheduler tool like cron 
(on Unix-based systems) or Task Scheduler (on Windows).?

How to raise price of every item by 20% from the original csv on the new one?

using wildcard? ( * )