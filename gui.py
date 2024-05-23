from tkinter import *

class Ticket:
    def __init__(self, name, price, quantity, tvname):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.tvname = tvname
        ticket_name_list.append(self.name)
        ticket_list.append(self)

    def var_name(self):
        return self.name

    def var_price(self):
        return self.price

    def var_tv(self):
        return self.tvname

    def calc(test=None):
        answer.set(f"${total}")

class Window:
    def __init__ (self):
        self.win_stat = True

    def val_getter(self):
        value = int(TEXTVARIABLES[0].get())
        return value

    def ex_window (self):
        # Variable label entry print
        for i in range(len(ticket_name_list)):
            lable = Label(root, text=f'{ticket_list[i].var_name()} ticket {ticket_list[i].var_price()}', fg= "black", font = ("Arial", 20, "bold")).grid(column=1, row=(((i+1)*2)-1), sticky= "NESW")
            ticket_name_list[i] = Entry(root, textvariable=ticket_list[i].var_tv(), borderwidth = 2, relief="solid", justify='center', font = ("Arial", 20, "bold"))
            ticket_name_list[i].bind("<Leave>", calc)
            ticket_name_list[i].grid(column=3, row=(((i+1)*2)-1), sticky= "NESW")

        # Total
        global answer
        answer = IntVar()
        total_button = Label(root, text= "Total price:", font = ("Arial", 20, "bold")).grid(column=1, row=7, sticky= "NESW")
        total_label = Label(root, textvariable= answer, font = ("Arial", 20, "bold")).grid(column=3, row=7, sticky= "NESW")

        # Submit button
        submit_frame = Frame(root, bg="white")
        submit_frame.grid(column= 1, columnspan=3, row=9, sticky = "NESW")
        submit_frame.columnconfigure((0,2), weight = 2)
        submit_frame.columnconfigure((1), weight = 6)
        submit_frame.rowconfigure((0), weight=1)
        submit = Button(submit_frame, text="Submit", font = ("Arial", 20, "bold")).grid(column= 1, row=0,sticky = "NESW")

        root.mainloop()
        self.win_stat = False

def calc(test=None):
    global answer
    total = (int(ticket_name_list[0].get())*Adult_tick.var_price()) + (int(ticket_name_list[1].get())*Child_tick.var_price()) + (int(ticket_name_list[2].get())*Concession_tick.var_price())
    answer.set(f"${total}")

# Window
root = Tk()
root.geometry("800x400")
root.title("Ticket booking system")
root.configure(bg="white")

# IntVars
Adult = IntVar()
Child = IntVar()
Concession = IntVar()

# Tickets
global ticket_list 
ticket_list = []
ticket_name_list = []
Adult_tick = Ticket("Adult", 15, None, Adult)
Child_tick = Ticket("Child", 5, None, Child)
Concession_tick = Ticket("Concession", 10, None, Concession)
for i in range(len(ticket_list)):
    print(ticket_list[i])

# Window Sizing
root.columnconfigure((0,2,4), weight= 1)
root.columnconfigure((1), weight = 4)
root.columnconfigure((3), weight = 2)
root.rowconfigure((0,1,2,3,4,5,6,7,8,9,10), weight = 1)

run = Window().ex_window ()
