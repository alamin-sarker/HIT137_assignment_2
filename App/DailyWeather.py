from AddressInterface import AddressInterface
from WeatherInterface import WeatherInterface
from FormatWeatherData import FormatWeatherData
from tkinter import * 

class DailyWeather: 
    def __init__(self):
        self.data = {}

        # root window
        self.weather_data = None

        self.root = Tk()
        self.root.geometry("500x300")
        self.root.title("Weather Information")
        
        address_interface = AddressInterface(self.root)

        self.root.mainloop()

        self.weather_data = address_interface.get_weather_data()

        data_manager = FormatWeatherData(self.weather_data)
        self.data = data_manager.format_data()

        print(self.data)

        self.weather_interface = WeatherInterface(self.data) 


if __name__ == "__main__":
    d = DailyWeather()