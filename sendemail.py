import smtplib
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
SUBJECT = "Interview Call"
s = smtplib.SMTP('smtp.gmail.com', 587)

def sendmail(TEXT,email):
    print("sorry we cant process your candidature")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("il.pradeepthi@gmail.com", "oms@1Ram")
    message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    s.sendmail("il.pradeepthi@gmail.com", email, message)
    s.quit()
def sendgridmail(user,TEXT):
    sg = sendgrid.SendGridAPIClient('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')
    from_email = Email("sandeep@thesmartbridge.com")  # Change to your verified sender
    to_email = To(user)  # Change to your recipient
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain",TEXT)
    mail = Mail(from_email, to_email, subject, content)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()
    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)
    

