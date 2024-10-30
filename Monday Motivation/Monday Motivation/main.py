import smtplib
import random
import datetime

time=datetime.datetime.now()
print(time.weekday())
c=True
while True:
    if time.weekday() == 1 and c:
        with open('./quotes.txt') as f:
            txt=f.readlines()
            t=random.choice(txt)
        myemail="your mail"
        password="your pass"
        con=smtplib.SMTP("smtp.gmail.com", 587)
        con.starttls()
        con.login(user=myemail,password=password)
        con.sendmail(from_addr=myemail,to_addrs="sathwikshetty9876@gmail.com",msg=f"Subject:Motivation Maga \n\n {t}")
        con.close()
        c=False
    else:
        c=True