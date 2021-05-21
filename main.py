from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Easy Tickets")
root.geometry("600x600")
root.config(bg="blue")
header = Label(root, text="Tickets", fg="black", bg="blue", font=('Courier', 44))
header.place(x=180, y=10)
variable = StringVar(root)

class Easy:
    myresult = StringVar()
    variable.set("Select...")
    def __init__ (self, window):
        self.lblnumber = Label(window, text="Enter Cell No: ", bg='blue', font=(10))
        self.lblnumber.place(x=120, y=100)
        self.txtnumber = Entry(window)
        self.txtnumber.place(x=280, y=100)
        self.lblcat = Label(window, text="Select Category here: ", bg='blue', font=(10))
        self.lblcat.place(x=80, y=140)
        self.category = OptionMenu(window, variable, 'Soccer', 'Movies', 'Theatre')
        self.category.place(x=280, y=140)
        self.lbltickets = Label(window, text="Number Of Tickets: ", bg='blue', font=(10))
        self.lbltickets.place(x=110, y=190)
        self.txttickets = Entry(window)
        self.txttickets.place(x=280, y=190)
        self.price = Button(root, text="Buy Now", command=self.calc_prepayment)
        self.price.place(x=250, y=250)
        self.clear = Button(root, text="clear", command=self.clear)
        self.clear.place(x=400, y=250)
        self.border1 = Label(window, text="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", bg="blue")
        self.border2 = Label(window, text="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", bg="blue")
        self.border1.place(x=40, y=280)
        self.border2.place(x=40, y=450)
        self.amount_pay = Label(window, text="", bg="blue")
        self.reserve = Label(window, text="", bg="blue")
        self.cell_label = Label(window, text="", bg="blue")
        self.amount_pay.place(x=50, y=310)
        self.reserve.place(x=50, y=360)
        self.cell_label.place(x=50, y=410)

    # Calculations
    def calc_prepayment(self):
        ticket_no = int(self.txttickets.get())
        vat = 0.14
        try:
            int(self.txtnumber.get())
            if len(self.txtnumber.get()) < 10 or len(self.txtnumber.get()) > 10:
                raise ValueError

            elif variable.get() == "Select...":
                raise ValueError

            elif int(self.txttickets.get()) == 0:
                raise ValueError

            # Soccer
            elif variable.get() == "Soccer":
                price = 40  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ("Amount Payable: R{}".format(price_pay))
                self.amount_pay.config(text=text)

            # Movie
            elif variable.get() == "Movies":
                price = 75  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ("Amount Payable: R{}".format(price_pay))
                self.amount_pay.config(text=text)

            # Theater
            elif variable.get() == "Theatre":
                price = 100  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ("Amount Payable: R{}".format(price_pay))
                self.amount_pay.config(text=text)

            # Reservation
            reserve_text = "Reservation for {} for : {} ".format(variable.get(), ticket_no)
            cell_text = "Reservation Made By: {}".format(self.txtnumber.get())
            self.reserve.config(text=reserve_text)
            self.cell_label.config(text=cell_text)

        except ValueError:  # Error Message
            messagebox.showerror(message="INVALID - Please Try Again")


    def clear(self):
        self.txtnumber.delete(0, END)
        self.txttickets.delete(0, END)
        self.amount_pay.config(text="")
        self.reserve.config(text="")
        self.cell_label.config(text="")


obj_tickets=Easy(root)
root.mainloop()