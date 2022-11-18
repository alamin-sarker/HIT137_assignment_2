from AddressInterface import AddressInterface
from WeatherInterface import WeatherInterface
from FormatWeatherData import FormatWeatherData
from tkinter import * 


class DailyWeather:
    """ Creating the Weather App """
    
    def __init__(self):
        self.data = {}  # dict for formatted weather data

        # API data
        self.weather_data = None

        # root window for application
        self.root = Tk()
        self.root.geometry("500x300")
        self.root.title("Weather Information")
        
        # UI for fetching user address
        address_interface = AddressInterface(self.root)

        # main event loop for address UI
        self.root.mainloop()

        # populating weather API data
        self.weather_data = address_interface.get_weather_data()

        # formatting weather API data
        data_manager = FormatWeatherData(self.weather_data)
        self.data = data_manager.format_data()

        # print(self.data)

        # Rendering formatted weather data
        self.weather_interface = WeatherInterface(self.data) 