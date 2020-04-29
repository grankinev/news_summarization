
# coding: utf-8

# In[ ]:


# функция для отправки почтовых сообщений на заданный адрес

def sendmailto(target_mail, subject_name, message_text, *file_names):
    """Передать переменные:
    1)адрес получателя
    2)тема письма
    3)текст сообщения
    4)опционально: имена прикрепляемых файлов 
    (должны быть в одной директории с ядром робота)"""
    
    import email, smtplib, ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email import encoders
    from email.mime.base import MIMEBase
    
    port = 465  # For SSL
    password = "Stalker1987"
    sender_email = "egran.bot@gmail.com"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    body = message_text
    message["From"] = sender_email
    message["To"] = target_mail
    message["Subject"] = subject_name
    
    # Add body to email
    message.attach(MIMEText(body, "plain"))
    if file_names:
        for file_name in file_names:
            try:
                # Open  file in binary mode
                with open(file_name, "rb") as attachment:
                    # Add file as application/octet-stream
                    # Email client can usually download this automatically as attachment
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())

                # Encode file in ASCII characters to send by email    
                encoders.encode_base64(part)

                # Add header as key/value pair to attachment part
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {file_name}",
                )

                # Add attachment to message and convert message to string
                message.attach(part)
                text = message.as_string()

#                     # Log in to server using secure context and send email
#                 context = ssl.create_default_context()
#                 with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#                     server.login('egran.bot@gmail.com', password)
#                     server.sendmail('egran.bot@gmail.com', target_mail, text)
            except:
                file_error = '\n\nНе удалось обнаружить один из файлов: ' + str(file_name)
                message.attach(MIMEText(file_error, "plain"))
                text = message.as_string()
#             # Log in to server using secure context and send email
#             context = ssl.create_default_context()
#             with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#                 server.login('egran.bot@gmail.com', password)
#                 server.sendmail('egran.bot@gmail.com', target_mail, text)
#             message = MIMEMultipart()
#             message.attach(MIMEText(body, "plain"))
    else:
        text = message.as_string()
        # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login('egran.bot@gmail.com', password)
        server.sendmail('egran.bot@gmail.com', target_mail, text)
    
    
    


# In[ ]:


# функция для отправки почтовых сообщений на заданный адрес

def sendbulkmailto(target_mail, subject_name, message_text, files_list):
    """Передать переменные:
    1)адрес получателя
    2)тема письма
    3)текст сообщения
    4)Список имен прикрепляемых файлов 
    (должны быть в одной директории с ядром робота)"""
    
    import email, smtplib, ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email import encoders
    from email.mime.base import MIMEBase
    
    port = 465  # For SSL
    password = "Stalker1987"
    sender_email = "egran.bot@gmail.com"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    body = message_text
    message["From"] = sender_email
    message["To"] = target_mail
    message["Subject"] = subject_name
    
    # Add body to email
    message.attach(MIMEText(body, "plain"))
    if files_list:
        for file_name in files_list:
            try:
                # Open  file in binary mode
                with open(file_name, "rb") as attachment:
                    # Add file as application/octet-stream
                    # Email client can usually download this automatically as attachment
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())

                # Encode file in ASCII characters to send by email    
                encoders.encode_base64(part)

                # Add header as key/value pair to attachment part
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {file_name}",
                )

                # Add attachment to message and convert message to string
                message.attach(part)
                text = message.as_string()

#                     # Log in to server using secure context and send email
#                 context = ssl.create_default_context()
#                 with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#                     server.login('egran.bot@gmail.com', password)
#                     server.sendmail('egran.bot@gmail.com', target_mail, text)
            except:
                file_error = '\n\nНе удалось обнаружить один из файлов: ' + str(file_name)
                message.attach(MIMEText(file_error, "plain"))
                text = message.as_string()
#             # Log in to server using secure context and send email
#             context = ssl.create_default_context()
#             with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#                 server.login('egran.bot@gmail.com', password)
#                 server.sendmail('egran.bot@gmail.com', target_mail, text)
#             message = MIMEMultipart()
#             message.attach(MIMEText(body, "plain"))
    else:
        text = message.as_string()
        # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login('egran.bot@gmail.com', password)
        server.sendmail('egran.bot@gmail.com', target_mail, text)
    
    
    


# In[34]:


# # функция для отправки почтовых сообщений на заданный адрес

# def sendmailto(target_mail, subject_name, message_text, *file_names):
#     """Передать переменные:
#     1)адрес получателя
#     2)тема письма
#     3)текст сообщения
#     4)опционально: имена прикрепляемых файлов 
#     (должны быть в одной директории с ядром робота)"""
    
#     import email, smtplib, ssl
#     from email.mime.text import MIMEText
#     from email.mime.multipart import MIMEMultipart
#     from email import encoders
#     from email.mime.base import MIMEBase
    
#     port = 465  # For SSL
#     password = "Stalker1987"
#     sender_email = "egran.bot@gmail.com"

#     # Create a multipart message and set headers
#     message = MIMEMultipart()
#     body = message_text
#     message["From"] = sender_email
#     message["To"] = target_mail
#     message["Subject"] = subject_name
    
#     # Add body to email
#     message.attach(MIMEText(body, "plain"))
#     if file_names:
#         for file_name in file_names:
#             try:
#                 # Open  file in binary mode
#                 with open(file_name, "rb") as attachment:
#                     # Add file as application/octet-stream
#                     # Email client can usually download this automatically as attachment
#                     part = MIMEBase("application", "octet-stream")
#                     part.set_payload(attachment.read())

#                 # Encode file in ASCII characters to send by email    
#                 encoders.encode_base64(part)

#                 # Add header as key/value pair to attachment part
#                 part.add_header(
#                     "Content-Disposition",
#                     f"attachment; filename= {file_name}",
#                 )

#                 # Add attachment to message and convert message to string
#                 message.attach(part)
#                 text = message.as_string()

#                     # Log in to server using secure context and send email
#                 context = ssl.create_default_context()
#                 with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#                     server.login('egran.bot@gmail.com', password)
#                     server.sendmail('egran.bot@gmail.com', target_mail, text)
#             except:
#                 file_error = '\n\nНе удалось обнаружить один из файлов: ' + str(file_name)
#                 message.attach(MIMEText(file_error, "plain"))
#                 text = message.as_string()
#                 # Log in to server using secure context and send email
#                 context = ssl.create_default_context()
#                 with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#                     server.login('egran.bot@gmail.com', password)
#                     server.sendmail('egran.bot@gmail.com', target_mail, text)
#             message = MIMEMultipart()
#             message.attach(MIMEText(body, "plain"))
#     else:
#         text = message.as_string()
#         # Log in to server using secure context and send email
#         context = ssl.create_default_context()
#         with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#             server.login('egran.bot@gmail.com', password)
#             server.sendmail('egran.bot@gmail.com', target_mail, text)
    
    
    
    


# In[35]:


#sendmailto('grankin.ev@gmail.com', 'testing', 'test message text', 'test.csv', 'asfas.txt')


# In[ ]:


# import email, smtplib, ssl
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email import encoders
# from email.mime.base import MIMEBase

# sender_email = "egran.bot@gmail.com"
# receiver_email = "grankin.ev@gmail.com"
# message = """\
# Subject: Hi there

# This message is sent from Python."""

# # Send email here

# port = 465  # For SSL
# password = "Stalker1987"

# # Create a secure SSL context
# context = ssl.create_default_context()

# with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#     server.login("egran.bot@gmail.com", password)
#     server.sendmail(sender_email, receiver_email, message)

# message = MIMEMultipart("alternative")
# message["Subject"] = "multipart test"
# message["From"] = sender_email
# message["To"] = receiver_email

# # Create the plain-text and HTML version of your message
# text = """\
# Hi,
# How are you?
# Real Python has many great tutorials:
# www.realpython.com"""
# html = """\
# <html>
#   <body>
#     <p>Hi,<br>
#        How are you?<br>
#        <a href="http://www.realpython.com">Real Python</a> 
#        has many great tutorials.
#     </p>
#   </body>
# </html>
# """

# # Turn these into plain/html MIMEText objects
# part1 = MIMEText(text, "plain")
# part2 = MIMEText(html, "html")

# # Add HTML/plain-text parts to MIMEMultipart message
# # The email client will try to render the last part first
# message.attach(part1)
# message.attach(part2)

# # Create secure connection with server and send email
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(
#         sender_email, receiver_email, message.as_string()
#     )

