def send_email(to,subject,body):
    return f"To: {to}, the subject: {subject}, and the body: {body}"
mail=send_email(to="shivani",subject="leave for one day",body="am suffering with fever give me leave")
print(mail)