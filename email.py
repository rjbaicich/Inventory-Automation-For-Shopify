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
