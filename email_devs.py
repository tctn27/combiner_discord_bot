import smtplib
import ssl

def error_email(error):
    port = 465

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("Beemsbot@gmail.com", "BeemsyBot54")

        server.sendmail("Beemsbot@gmail.com", "tomcatthenommer@gmail.com", "Error on Beems bot\n\n" + str(error))