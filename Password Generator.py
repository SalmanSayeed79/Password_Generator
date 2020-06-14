import random
from tkinter import *
import smtplib


# creating a random password

def random_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    upper = []
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for i in letters:
        i = i.upper()
        upper.append(i)
    letters = letters + upper + numbers
    random_list = []
    for i in range(10):
        random_list.append(letters[random.randint(0, 59)])
    global password
    password = ''.join(random_list)
    return password


# sending the mail
def sending_mail():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('CODER.1905079@gmail.com', 'Gaming5345')
        print('login')
        mailID=email_entry.get()
        print(mailID)
        subject = 'Sending the password for your mail'
        body = 'Here is your password: \n' + random_pass()
        message = 'Subject: {} \n \n {}'.format(subject, body)
        print('message creation')
        smtp.sendmail('CODER.1905079@gmail.com',mailID, message)
        print('mail sent')
        label=Label(root,text='Check your mail to see the generated password')
        label.grid(row=8,column=1)
# building the gui

root = Tk()
root.title('Password Generator')
root.iconbitmap('icon.ico')
root.geometry('500x500')
#root.configure(bg='red')
# the entry field

title=Label(root,text='Enter your Email-ID below to get your generated password   ',font='Cambria')
title.grid(row=0,column=1)

empty=Label(root)
empty.grid(row=1,column=0)
empty=Label(root)
empty.grid(row=2,column=0)

Label1 = Label(root, font="Cambria", text="EMAIL-ID: ")
Label1.grid(row=3,column=0)

email_entry = Entry(root, font="Cambria",width=40)
email_entry.grid(row=3,column=1)
#mailID = email_entry.get()
#print(mailID)

empty=Label(root)
empty.grid(row=4,column=1)
empty=Label(root)
empty.grid(row=5,column=1)


button = Button(root, text='Generate Password',command=sending_mail)
button.grid(row=7,column=1)

root.mainloop()










