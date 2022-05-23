import smtplib 
try: 
    #Create your SMTP session 
    smtp = smtplib.SMTP('smtp.gmail.com', 587) 

   #Use TLS to add security 
    smtp.starttls() 
    #User Authentication 
    sender_email_id = "emailsender382@gmail.com"
    sender_email_id_password = "sender_password"
    smtp.login(sender_email_id,sender_email_id_password)

    #Defining The Message 
    subject = input("Enter the subject ")
    text = input("Enter the message you need to send ")
    receiver_email_id = input("Enter receiver's email id ")
    #Sending the Email
    message = 'Subject: {}\n\n{}'.format(subject, text)
    smtp.sendmail(sender_email_id, receiver_email_id,message) 

    #Terminating the session 
    smtp.quit() 
    print ("Email sent successfully!") 

except Exception as ex: 
    print("Something went wrong....",ex)
