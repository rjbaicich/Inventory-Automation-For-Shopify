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
   # Connect to the IMAP server
    mail = imaplib.IMAP4_SSL(imap_server, imap_port)
    mail.login(email_address, email_password)

    # Select the mailbox (inbox in this case)
    mail.select("inbox")

    # Search for all emails in the mailbox
    status, messages = mail.search(None, "ALL")
    message_ids = messages[0].split()