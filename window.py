from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("500x250")
window.resizable("false", "false")
window.title("Exception Handling")
window["bg"] = "grey"


class Amount:
    def __init__(self, window):
        self.amount = Label(window, text="Please enter amount in your account", bg="grey")
        self.amount.place(x=120, y=30)
        self.amountent = Entry(window)
        self.amountent.place(x=160, y=60)
        self.verify = Button(window, text="Check qualification", command=self.verify, bg="lightpink", borderwidth=7)
        self.verify.place(x=160, y=120)
        self.exit = Button(window, text="Exit", command=self.exit, bg="lightpink", borderwidth=7, width=15)
        self.exit.place(x=160, y=200)

    def verify(self):
        try:
            money = float(self.amountent.get())
            if money < 3000:
                messagebox.showerror("Insufficient funds", "Please deposit more funds for this excursion.")
                self.amountent.delete(0, END)
            else:
                messagebox.showinfo("Accepted", "Congratulations. You qualify to go to Malaysia")
                self.amountent.delete(0, END)
        except ValueError:
            messagebox.showerror("Invalid input", "Please put in an amount in numbers.")
            self.amountent.delete(0, END)

    def exit(self):
        msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application",
                                         icon='warning')
        if msg_box == "yes":
            window.destroy()
        else:
            messagebox.showinfo("Return", "You will now return to the App", icon="warning")


obj = Amount(window)
window.mainloop()
