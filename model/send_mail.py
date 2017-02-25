# -*- coding : utf-8 -*-

import smtplib
from email.utils import formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Send_Mail():
    """Send value and predict result to each byb mail."""
    def __init__(
            self,
            addresss="osamura.akinori@gmail.com",
            passwd="Mitsuya90",
            smtp="smtp.gmail.com",
            port=587,
            subject="stock_project"
            ):
        self.addresss = addresss
        self.passwd = passwd
        self.smtp = smtp
        self.port = port
        self.subject = subject

    def create_message(from_addr, to_addr, subject, body, mime=None):
        msg = MIMEMultipart()
        msg["From"] = from_addr
        msg["To"] = to_addr
        msg["Date"] = formatdate()
        msg["Subject"] = subject
        body = MIMEText(body)
        msg.attach(body)

        return msg