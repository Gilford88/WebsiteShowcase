import smtplib, ssl


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = 'gilford88@gmail.com'
    password = 'tozdnalucdexoppc'

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, username, message)
