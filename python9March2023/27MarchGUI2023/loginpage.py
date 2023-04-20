from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox


def handle_login():
    email=email_input.get()
    password=password_input.get()
    
    if email=='abc@gmail.com' and password=='1234':
        messagebox.showinfo("yeah!","Login Successful..")
    else:
        messagebox.showerror("Oops!","Your details incorrect")
    print(email," ",password)

root=Tk()
root.title("Login Page")
root.iconbitmap()
root.minsize(200,200)
root.configure(background='#0096DC')
img=Image.open('Flipkart-Logo.png')
reversed_img=img.resize((70,70))
img=ImageTk.PhotoImage(reversed_img)
img_lable=Label(root,image=img)
img_lable.pack(pady=(10,10))

text_label=Label(root,text='Flipkart',fg='white',bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana',24))

email_label=Label(root,text="Enter email",fg='white',bg='#0096DC')
email_label.pack(pady=(10,10))
email_label.config(font=('verdana',12))

email_input=Entry(root,width='30')
email_input.pack()

password_label=Label(root,text="Enter password",fg='white',bg='#0096DC')
password_label.pack(pady=(20,5))
password_label.config(font=('verdana',12))

password_input=Entry(root,width='30')
password_input.pack()

login_btn=Button(root,text="Login Here",bg='white',fg='black',command=handle_login)
login_btn.pack(pady=(20,20))

root.mainloop()