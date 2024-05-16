from tkinter import *
import time

TICKET_PRICING = {"Adult":15,
                  "Child":5,
                  "Concession":10}

def calc(test=None):
    print(test.char)
    total = (int(adults.get())*TICKET_PRICING["Adult"]) + (int(children.get())*TICKET_PRICING["Child"]) + (int(concession.get())*TICKET_PRICING["Concession"])
    answer.set(f"${total}")

root = Tk()
root.geometry("800x400")
root.title("Ticket booking system")
root.configure(bg="white")

# IntVars
adults = IntVar()
children = IntVar()
concession = IntVar()

# Sizing
root.columnconfigure((0,2,4), weight= 1)
root.columnconfigure((1), weight = 4)
root.columnconfigure((3), weight = 2)
root.rowconfigure((0,1,2,3,4,5,6,7,8,9,10), weight = 1)

# label 1 + entry 1 (adult)
adult_label = Label(root, text="Adult ticket $15", fg= "black", font = ("Arial", 20, "bold")).grid(column=1, row=1, sticky= "NESW")
adult_entry = Entry(root, textvariable=adults, borderwidth = 2, relief="solid", justify='center', font = ("Arial", 20, "bold"))
adult_entry.bind("<Leave>", calc)
adult_entry.grid(column=3, row=1, sticky= "NESW")


# Label 2 + entry 2 (child)
child_label = Label(root, text="Child ticket $5", fg= "black", font = ("Arial", 20, "bold")).grid(column=1, row=3, sticky= "NESW")
child_entry = Entry(root, textvariable=children, borderwidth = 2, relief="solid", justify='center', font = ("Arial", 20, "bold"))
child_entry.bind("<Leave>", calc)
child_entry.grid(column=3, row=3, sticky= "NESW")

# Label 3 + entry 3 (senior/student)
concession_label = Label(root, text="Senior / Student ticket $10", fg= "black", font = ("Arial", 20, "bold")).grid(column=1, row=5, sticky= "NESW")
concession_entry = Entry(root, textvariable=concession,borderwidth = 2, relief="solid", justify='center', font = ("Arial", 20, "bold"))
concession_entry.bind("<Leave>", calc)
concession_entry.grid(column=3, row=5, sticky= "NESW")

# Total
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