from decouple import config
from email.message import EmailMessage
import ssl
import smtplib
import random
def email_verificaion():
     codigo=random.randrange(1000,9999)
     codigo_enviar=str(codigo)
     passwword_recuperar=config("password_recuperacion")
     email_sender=config("email_sender")
     email_reciver=config("email_reciver")
     em= EmailMessage()
     subject="Código de verificación"
     body=codigo_enviar
     
     em["From"]= email_sender
     em["To"]= email_reciver
     em["Subject"]=subject
     em.set_content(body)
     context=ssl.create_default_context()
     
     with smtplib.SMTP_SSL("smtp.gmail.com",465,context= context) as smtp:
          smtp.login(email_sender,passwword_recuperar)
          smtp.sendmail(email_sender,email_reciver,em.as_string())
     return codigo_enviar   