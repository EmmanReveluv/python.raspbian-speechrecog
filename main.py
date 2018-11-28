from Tkinter import *
import smtplib
import tkMessageBox
import speech_recognition as sr

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

#initialize user interface
top = Tk()
top.resizable(width=False, height=False)
top.title("Module")
top.geometry('480x250')
var = StringVar()
var.set("Welcome!")

def login():
    try:
        #var.set(txtPassword.get())
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

        print("connected")
        #Next, log in to the server
        user=txtEmail.get()
        passw=txtPassword.get()
        server.login(user,passw)
        print("Logged in")
        
        #show messagebox
        tkMessageBox.showinfo( "", "Login Success")

        #forget/hide yung mga napack na
        lblWelcome.pack_forget()
        lblEmail.pack_forget()
        lblPassword.pack_forget()
        txtEmail.pack_forget()
        txtPassword.pack_forget()
        btnLogin.pack_forget()

        #show the new packs

        lblSendTo.pack()
        txtToEmail.pack()
        lblBody.pack()
        txtBody.pack()
        btnRecord.pack()
        btnSend.pack()
    except:
        tkMessageBox.showinfo( "", "Login Failed")


def send():
    try:
        msgFrom=txtEmail.get()
        msgTo=txtToEmail.get()
        msgBody= txtBody.get("1.0",END)
        print(msgBody)
        print(msgFrom)
        print(msgTo)

        user=txtEmail.get()
        passw=txtPassword.get()
        
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

        server.login(user,passw)
        server.sendmail(msgFrom, msgTo, msgBody)
        print("message sent")
        tkMessageBox.showinfo( "", "Message sent")

    except Exception as e:
        print(e)
        tkMessageBox.showinfo( "", "Message not sent")

def record():

    
    # Speech recognition using Google Speech Recognition
    try:
        
            # Record Audio
        r = sr.Recognizer()
        r.energy_threshold = 3000

        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
         

        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        text=r.recognize_google(audio)
        text=text+' '
        print("You said: " + text)
        txtBody.insert(INSERT, text)
        print(txtBody.get("1.0",END))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    print("recorded")

#labels
lblWelcome = Label( top, textvariable=var)
lblEmail = Label( top, text="Email Address")
lblPassword = Label( top, text="Password")

lblSendTo= Label(top, text="Send to:")
lblBody= Label(top, text="Message: ")

#buttons
btnLogin = Button(top,text="Login",command=login)

btnSend=Button(top,text="Send",command=send)
btnRecord=Button(top,text="Record", command=record)

#entry fields
txtEmail = Entry(top,width=30)
txtPassword= Entry(top,width=30, show="*")

txtToEmail = Entry(top,width=30)
txtBody=Text(top,width=30,height=5)

#arrangements
lblWelcome.pack()
lblEmail.pack()
txtEmail.pack()
lblPassword.pack()
txtPassword.pack()
btnLogin.pack()



top.mainloop()
