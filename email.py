import imaplib
import email
import os
from dotenv import load_dotenv
from shopify import Shopify


# Email Configuration
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SENDER_EMAIL = "specific_sender@example.com"  # Replace with the specific sender's email

# Connect to the email server
mail = imaplib.IMAP4_SSL(EMAIL_HOST)
mail.login(EMAIL_USER, EMAIL_PASSWORD)


# Select the mailbox you want to search (e.g., 'inbox')
mail.select("inbox")

# Search for emails from the specific sender
result, data = mail.search(None, f'(FROM "{SENDER_EMAIL}")')

# Get the latest email (assuming the emails are sorted by date)
latest_email_id = data[0].split()[-1]
result, message_data = mail.fetch(latest_email_id, "(RFC822)")

# Parse the email content
raw_email = message_data[0][1]
email_message = email.message_from_bytes(raw_email)