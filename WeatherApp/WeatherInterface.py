from tkinter import * 
from PIL import Image,ImageTk


class WeatherInterface: 
    """Creating weather interface with data from openweather API"""

    def __init__(self, weather_data):
        self.weather_data = weather_data
        print(f"[WEATHERINTERFACE] Data Received")

        # creating root window to render Weather API data
        weather_root = Tk()
        weather_root.title("API Interface")
        weather_root.geometry("700x480")
        weather_root.resizable(False, False)

        # bottom bar
        finalimg6=ImageTk.PhotoImage(image=Image.open(r'/Users/alaminsarker/Documents/HIT137_assignment_2/WeatherApp/Images/bottom_bar.png').resize((770,70)))
        Label(image=finalimg6,bg='#00b7ff').place(x = 5, y = 35)

        # creating the current weather label to display the city name and city time
        Label(text="Current Weather", font="Calibri 15 bold", bg='#00b7ff', fg='white').place(x = 35, y = 35)

        # location label 
        location=Label(text="",font=("Calibri",15,'bold'),bg='#00b7ff',fg='black')
        location.place(x = 30 ,y = 60)  

        # creating the label to display the temperature
        temperature=Label(text="",font=("Cambria",75,'bold'))
        temperature.place(x=250,y=120)
        degree=Label(text="",font="Cambria 40 bold")
        degree.place(x=390,y=135)

        # feels like label and sunny or fog like labels
        feel=Label(text="",font=("Nirmala UI",16,"bold"))
        feel.place(x=280,y=225)

        # current date and time
        timelbl=Label(text="",font=("Nirmala UI",16,"bold"))
        timelbl.place(x=280,y=265)

        # Sunrise heading label
        Label(text="Sunrise", font="Calibri 15 bold", bg='#00b7ff', fg='white').place(x = 300, y = 35)
        # sunrise label
        sunrise = Label(text="", font=("Calibri",15,'bold'), bg='#00b7ff', fg='black')
        sunrise.place(x = 250, y = 60)

        # Sunset heading label
        Label(text="Sunset", font="Calibri 15 bold", bg='#00b7ff', fg='white').place(x = 500, y = 35)
        # sunset label 
        sunset = Label(text="", font=("Calibri",15,'bold'), bg='#00b7ff', fg='black')
        sunset.place(x = 500, y = 60)

        # bottom bar
        finalimg6=ImageTk.PhotoImage(image=Image.open(r'/Users/alaminsarker/Documents/HIT137_assignment_2/WeatherApp/Images/bottom_bar.png').resize((770,70)))
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
        Button(text='Exit',font=("Georgia",16,"bold"),bg='orange',fg='black',width=7,relief='groove',command=weather_root.destroy).place(x=580,y=420)

        # update the text for labels 
        feel['text'] = f"Feels Like {self.weather_data['feels_like']}° | {self.weather_data['weather']}"
        timelbl['text'] = f"{self.weather_data['location_datetime']}"
        temperature['text'] = f"{self.weather_data['temp']} ºC"
        humidity['text'] = f"{self.weather_data['humidity']} %"
        pressure['text'] = f"{self.weather_data['pressure']} mBar"
        des['text'] = f"{self.weather_data['description']}"
        vis['text'] = f"{self.weather_data['visibility']} km"
        location['text'] = f"{self.weather_data['location']}"
        sunrise['text'] = f"{self.weather_data['sunrise']}"
        sunset['text'] = f"{self.weather_data['sunset']}"

        # event loop for API Interface window
        weather_root.mainloop()