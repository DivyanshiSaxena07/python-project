import smtplib
s_mail="divyanshi1001@gmail.com"
s_password="mpvv nyst ipsm bzcy"

r_email = "amanmourya6263@gmail.com"
subject = "Auto reply"
body = "Thank you for your email This is auto response"

smtp_server = "smtp.gmail.com"
smtp_port = 587
try:
    smtp_connection = smtplib.SMTP(smtp_server,smtp_port)
    smtp_connection.starttls()
    smtp_connection.login(s_mail,s_password)

    msg = f"Subject:{subject}\n\n{body}"

    smtp_connection.sendmail(s_mail,r_email,msg)

    smtp_connection.quit()

    print("reply successfully!")
except:
    print("mail not send")