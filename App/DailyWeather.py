from AddressInterface import AddressInterface
from WeatherInterface import WeatherInterface
from tkinter import * 

class DailyWeather: 
    def __init__(self):
        # root window
        self.weather_data = None

        self.root = Tk()
        self.root.geometry("500x300")
        self.root.title("Weather Information")
        
        weather_data = AddressInterface(self.root)

        self.root.mainloop()

        self.weather_interface = WeatherInterface(weather_data) 























if __name__ == "__main__":
    d = DailyWeather()