from tkinter import * 
from PIL import Image,ImageTk

class WeatherInterface: 
    def __init__(self, weather_data):
        self.weather_data = weather_data
        print(f"[WEATHERINTERFACE] Data Received")
        weather_root = Tk()
        weather_root.title("API Interface")
        weather_root.geometry("800x480")
        weather_root.resizable(False, False)

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

        # exit and reset button
        Button(text='Exit',font=("Georgia",16,"bold"),bg='orange',fg='black',width=7,relief='groove',command=weather_root.destroy).place(x=680,y=420)

        temperature['text'] = "foo"
        humidity['text'] = "foo"
        pressure['text'] = "foo"
        vis['text'] = "foo"
        sunrise['text'] = "Sunrise : foo"
        sunset['text'] = "Sunset : foo"

        weather_root.mainloop()