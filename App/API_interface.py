from tkinter import * 
from PIL import Image,ImageTk


root = Tk()
root.title("API Interface")
root.geometry("800x400")
root.resizable(False, False)

# creating the current weather label to display the city name and city time
Label(text="Current Weather :",font='Arial 14 bold',fg="red").place(x=590,y=7)

# location label 
location=Label(text='',font='Calibri 15')
location.place(x=620,y=34)

# time label for the searched city
timelbl=Label(text="",font=("Cambria",16))
timelbl.place(x=590,y=60)

# creating the label to display the temperature
temperature=Label(text="",font=("Cambria",75,'bold'))
temperature.place(x=270,y=140)
degree=Label(text="",font="Cambria 40 bold")
degree.place(x=390,y=135)

# feels like label and sunny or fog like labels
feel=Label(text="",font=("Nirmala UI",16,"bold"))
feel.place(x=280,y=245)

# sunrise logo
finalimg4=ImageTk.PhotoImage(image=Image.open(r"Images/sunrise.png").resize((40,40)))
Label(image=finalimg4).place(x=560,y=150)
sunrise=Label(text="Sunrise : ",font=("Segoe UI",14,'bold'))
sunrise.place(x=603,y=155)

#sunset logo
finalimg5=ImageTk.PhotoImage(image=Image.open(r"Images/sunset.png").resize((40,30)))
Label(image=finalimg5).place(x=560,y=215)
sunset=Label(text="Sunset : ",font=("Segoe UI",14,'bold'))
sunset.place(x=603,y=210)

# bottom bar
finalimg6=ImageTk.PhotoImage(image=Image.open(r'Images/bottom_bar.png').resize((770,70)))
Label(image=finalimg6,bg='#00b7ff').place(x=5,y=330)

# placing the labels
Label(text="Humidity",font="Calibri 15 bold",bg='#00b7ff',fg='white').place(x=35,y=335)
Label(text="Pressure",font="Calibri 15 bold",bg='#00b7ff',fg='white').place(x=210,y=335)
Label(text="Description",font="Calibri 15 bold",bg='#00b7ff',fg='white').place(x=400,y=335)
Label(text="Visibility",font="Calibri 15 bold",bg='#00b7ff',fg='white').place(x=600,y=335)

# humidity label
humidity=Label(text="",font=("Calibri",15,'bold'),bg='#00b7ff',fg='black')
humidity.place(x=50,y=361)

# pressure label
pressure=Label(text="",font=("Calibri",15,'bold'),bg='#00b7ff',fg='black')
pressure.place(x=203,y=361)

# description label
des=Label(text="",font=("Calibri",15,'bold'),bg='#00b7ff',fg='black')
des.place(x=405,y=361)

# visibility label
vis=Label(text="",font=("Calibri",15,'bold'),bg='#00b7ff',fg='black')
vis.place(x=610,y=361)

def clear(): 
    pass

# exit and reset button
Button(text='Exit',font=("Georgia",16,"bold"),bg='orange',fg='black',width=7,relief='groove',command=exit).place(x=680,y=420)
Button(text='Reset',font=("Georgia",16,"bold"),bg='orange',fg='black',width=7,relief='groove',activebackground="blue",activeforeground='white',command=clear).place(x=560,y=420)

temperature['text'] = "foobar"
humidity['text'] = "foobar"
pressure['text'] = "foobar"
vis['text'] = "foobar"
sunrise['text'] = f"Sunrise : foobar"
sunset['text'] = f"Sunset : foobar"

root.mainloop()