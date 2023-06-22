import smtplib as sm
import os
from email.mime.text import MIMEText


class Email:
    def __init__(self):
        self.naver_username = os.environ["naver_username"]
        self.naver_password = os.environ["naver_password"]

    def send_email(self, data):
        with sm.SMTP("smtp.naver.com", port=587) as connection:
            connection.ehlo()
            connection.starttls()
            connection.login(self.naver_username, self.naver_password)
            msg = MIMEText(f"Product {data['product_title']} is now on sale!\n\nYou can buy it now in {data['price_now']}$.\n\nlink:\n{data['product_url']}")
            msg["From"] = "dlrkd1122@naver.com"
            msg["Subject"] = f"You can purchase {data['product_title']} now in low price!. Buy it now!"
            msg["To"] = "dlrkd1122@gmail.com"
            connection.sendmail("dlrkd1122@naver.com", "dlrkd1122@gmail.com", msg.as_string())


email = Email()
email.send_email({
    "product_title": "none",
    "product_url": "none",
    "price_now": "none"

})