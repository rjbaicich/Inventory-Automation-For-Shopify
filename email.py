import imaplib
import email
import pandas as pd
from email.header import decode_header

def process_inventory_email():
    # Email credentials and server details
    email_address = 'your_email@example.com'
    email_password = 'your_email_password'
    imap_server = 'imap.example.com'
    imap_port = 993  # Use the appropriate port for your email provider
