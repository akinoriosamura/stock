# -*- coding : utf-8 -*-

import smtplib
from email.utils import formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Send_Mail():
    """Send value and predict result to each byb mail."""
    def __init__(
            self,
            address="osamura.akinori@gmail.com",
            passwd="Mitsuya90",
            smtp="smtp.gmail.com",
            port=587,
            subject="stock_project"):
        self.address = address
        self.passwd = passwd
        self.smtp = smtp
        self.port = port
        self.subject = subject

    def create_message(self, from_addr, to_addr, subject, body, mime=None):
        msg = MIMEMultipart()
        msg["From"] = from_addr
        msg["To"] = to_addr
        msg["Date"] = formatdate()
        msg["Subject"] = subject
        body = MIMEText(body)
        msg.attach(body)

        return msg

    def send(self, from_addr, to_addrs, msg):
        smtpobj = smtplib.SMTP(self.smtp, self.port)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.ehlo()
        smtpobj.login(self.address, self.passwd)
        smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
        smtpobj.close()

    def email_main(self, body):
        msg = self.create_message(self.address,
                                  self.address,
                                  self.subject,
                                  body
                                  )

        self.send(self.address, [self.address], msg)
