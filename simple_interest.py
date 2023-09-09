from tkinter import *
window  = Tk()

window.geometry("380x400")
window.title("Simple Interest GUI")
window.configure(bg="lightgrey")

heading_label = Label(window, text="Simple Interest", fg="black", bg="lightgrey", font=("Calibri", 20), bd=5)
heading_label.place(x=100,y=10)

principle_label = Label(window, text="Principle", fg="black", bg="lightgrey", font=("Calibri", 15), bd=1)
principle_label.place(x=110,y=80)

principle_entry = Entry(window, text="", bd=3, width=22)
principle_entry.place(x=110, y=100)

rate_label = Label(window, text="Rate", fg="black", bg="lightgrey", font=("Calibri", 15), bd=1)
rate_label.place(x=110,y=150)

rate_entry = Entry(window, text="", bd=3, width=22)
rate_entry.place(x=110, y=170)

time_label = Label(window, text="Time", fg="black", bg="lightgrey", font=("Calibri", 15), bd=1)
time_label.place(x=110,y=210)

time_entry = Entry(window, text="", bd=3, width=22)
time_entry.place(x=110, y=260)

def calculate_interest():
    p = float(principle_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())
    i = (p*r*t)/100
    interest = round(i,2)
    show_label.destroy()
    message = Label(result_frame, text="Interest on is. " + str(0) + " at rate of interest " + str(r) + " 1 for " + str(t) + " years is " + str(interest), bg="lightgrey", font=("Calibri", 12), width = 55)

calculate = Button(window, text="Calculate", command=calculate_interest)
calculate.place(x=110, y=290)

result_frame = LabelFrame(window,text="Result", bg="lightgrey", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=310)

show_label = Label(result_frame, text="Your result will be displayed here", bg="lightgrey", font=("Calibri", 12), width = 55)
show_label.place(x=20,y=20)
show_label.pack()


window.mainloop()