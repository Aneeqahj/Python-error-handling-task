from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("500x250")
window.resizable("false", "false")
window.title("Authentication")
window["bg"] = "grey"


class Info:
    def __init__(self, window):
        self.username = Label(window, text="Username", bg="grey")
        self.username.place(x=50, y=50)
        self.username_ent = Entry(window)
        self.username_ent.place(x=200, y=50)
        self.password = Label(window, text="Password", bg="grey")
        self.password.place(x=50, y=100)
        self.password_ent = Entry(window)
        self.password_ent.place(x=200, y=100)
        self.verify = Button(window, text="Verify", command=self.verify, bg="lightpink", borderwidth=7)
        self.verify.place(x=50, y=150)
        self.clear = Button(window, text="Clear", command=self.clear, bg="lightpink", borderwidth=7)
        self.clear.place(x=200, y=150)
        self.exit = Button(window, text="Exit", command=self.exit, bg="lightpink", borderwidth=7)
        self.exit.place(x=350, y=150)
        self.user_pass =  {'Aneeqah': '90sbabe', 'Adam': 'BigJ', 'Ronald': 'blondeboy', 'Zoe': 'Pisces01',
                                                        'Byron': 'Toby29'}

    def verify(self):
        username = self.username_ent.get()
        password = self.password_ent.get()
        if username == "" or password == "":
            messagebox.showerror(message="Please enter details")

        elif username in self.user_pass:
            if password == self.user_pass[username]:
                messagebox.showinfo(message="Access granted")
                import window.py
            else:
                messagebox.showerror(message="Password Incorrect")
        else:
            messagebox.showerror(message="Username not FOUND")

    def exit(self):
        msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application",
                                         icon='warning')
        if msg_box == "yes":
            window.destroy()
        else:
            messagebox.showinfo("Return", "You will now return to the App", icon="warning")

    def clear(self):
        self.username_ent.delete(0, END)
        self.password_ent.delete(0, END)


obj = Info(window)
window.mainloop()
