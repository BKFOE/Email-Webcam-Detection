import smtplib
import imghdr
from email.message import EmailMessage

PASSWORD = "xguwhtthdkeflwna"
SENDER = "bkfoepython@gmail.com"
RECEIVER = "bkfoepython@gmail.com"


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New object recognized in camera"
    email_message.set_content("We recognized activity on your "
                              "camera. It looks like an object has "
                              "entered the frame")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email(image_path="images/34.png")