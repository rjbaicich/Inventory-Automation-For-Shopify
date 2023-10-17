import schedule
import time
import imaplib
import email
import psycopg2
import pandas as pd
import shopify

def process_inventory():
    # Connect to the email server
    mail = imaplib.IMAP4_SSL('r**********@gmail.com')  #Replace with your email server

    # Login to your email account
    mail.login('r**********@gmail.com', '***********')  #Replace with your email credentials

    #Select the mailbox to search for the email
    mail.select('inbox')

    #Search for emails containing the CSV file
    result, data = mail.search(None, 'ALL')  #You can customize the search criteria

    #Get the latest email containing the CSV file
    latest_email_id = data[0].split()[-1]
    result, email_data = mail.fetch(latest_email_id, '(RFC822)')

    #Parse the email data
    raw_email = email_data[0][1]
    email_message = email.message_from_bytes(raw_email)

    #Download the CSV attachment
    for part in email_message.walk():
        if part.get_content_type() == 'text/csv':
            attachment = part.get_payload(decode=True)
            with open('inventory.csv', 'wb') as file:
                file.write(attachment)

    #Read the CSV data into a pandas DataFrame
    data = pd.read_csv('inventory.csv')

    #Clean the data
 
    #Raise the price of each item by 20%
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

    Insert the data into the database
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


# Automating Shopify Operations

## 1. Scheduling Shopify Updates

**Question:** Is it better to do Shopify steps manually, or is there an automated alternative for scheduling updates?

**Comments:** Automating repetitive tasks can save time and reduce errors. For scheduling, you can use tools like Task Scheduler (Windows) or cron jobs (Unix) to automate routine Shopify updates or data imports.

## 2. Data Format Transformation

**Question:** How to clean a CSV to fit another format, such as converting it to a different format?

**Comments:** Consider using data transformation tools or programming languages like Python with libraries like Pandas to clean and convert CSV data to your desired format.

## 3. Exporting Formatted Data

**Question:** How to output the newly formatted CSV file to a saved file that can be uploaded to Shopify?

**Comments:** Use programming languages like Python or tools like Excel to save the formatted data to a new CSV file, ready for upload.

## 4. Automating Upload to Shopify

**Question:** How to automate the last step, i.e., the upload to Shopify?

**Comments:** You can use Shopify APIs or Shopify Apps to automate the data upload process. Consider using Shopify's REST API or third-party apps that can connect to your data source.

## 5. Retrieving Data from Email

**Question:** How to take the original CSV from an email daily?

**Comments:** You can use email automation tools, Python's email libraries, or email forwarding rules to retrieve CSV attachments from emails.

## 6. Scheduling Daily Execution

**Question:** How to run this program once daily automatically?

**Comments:** Use a scheduler tool like Task Scheduler (Windows) or cron jobs (Unix) to set up the program to run automatically at a specific time each day.
# Open Task Scheduler
# Create a Basic Task
# Choose a Trigger
# Choose the Action
# Set the Start Date and Time
# Review and Finish
# Test the Task
## 7. Database or SQL Connection

**Question:** Do we need a database or SQL connection for this?

**Comments:** If your operation is stateless and you only need to process data without persistent storage, you may not need a database. However, if you need to store, retrieve, or manipulate structured data, a database could be useful.
import sqlite3

# Example data: List of users
users = [
    {"id": 1, "name": "Alice", "age": 28},
    {"id": 2, "name": "Bob", "age": 32},
    {"id": 3, "name": "Charlie", "age": 25},
]# Scenario 1: Stateless Operations (in-memory)
print("Scenario 1: Stateless Operations (in-memory)")
sorted_users = sorted(users, key=lambda user: user["age"])
for user in sorted_users:
    print(f"{user['name']} - Age: {user['age']}")

# Scenario 2: Structured Data and Data Retrieval (using SQLite database)
print("\nScenario 2: Structured Data and Data Retrieval (using SQLite database)")

## 8. Running on a Server

**Question:** Can I set this up on a server to run automatically?

**Comments:** Yes, you can set up your automation script or program on a server. Cloud-based servers like AWS, Google Cloud, or Azure are suitable for this purpose.

## 9. Increasing Prices

**Question:** How to raise the price of every item by 20% from the original CSV in the new one?

**Comments:** You can perform this operation using programming languages like Python or data transformation tools. Use mathematical operations to increase prices by 20%, for example, by multiplying each price by 1.20.

