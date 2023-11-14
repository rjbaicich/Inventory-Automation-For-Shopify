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
        # Process each email
    for msg_id in message_ids:
        # Fetch the email by ID
        status, msg_data = mail.fetch(msg_id, "(RFC822)")
        raw_email = msg_data[0][1]
        
        # Parse the raw email using the email library
        msg = email.message_from_bytes(raw_email)
        
        # Extract information from the email (customize as needed)
        subject, encoding = decode_header(msg["Subject"])[0]
        subject = subject.decode(encoding) if isinstance(subject, bytes) else subject
        
        sender, encoding = decode_header(msg.get("From"))[0]
        sender = sender.decode(encoding) if isinstance(sender, bytes) else sender
        
        # Additional information extraction based on your needs
             
        # For example, print the subject and sender
        print(f"Subject: {subject}")
        print(f"From: {sender}")

        # Process the email content as needed (customize this part)
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))

                if "attachment" in content_disposition:
                    # Handle attachments if needed
                    pass
                else:
                    # Extract and process text content
                    body = part.get_payload(decode=True)
                    print(body.decode("utf-8"))