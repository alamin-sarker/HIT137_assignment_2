from timezonefinder import TimezoneFinder
import pytz
import datetime


class FormatWeatherData: 
    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.data = {}
        print(self.weather_data)
        print(f"Visibility: {self.weather_data['visibility'] / 1000}")


    def format_data(self): 
        '''Format weather API data into a dictionary'''
        self.data['weather'] = self.weather_data['weather'][0]['main']
        self.data['description'] = self.weather_data['weather'][0]['description']
        self.data['temp'] = int(self.weather_data['main']['temp'] - 273)
        self.data['feels_like'] = int(self.weather_data['main']['feels_like'] - 273) 
        self.data['pressure'] = self.weather_data['main']['pressure']
        self.data['humidity'] = self.weather_data['main']['humidity']
        self.data['visibility'] = int(self.weather_data['visibility'] / 1000)
        lon = self.weather_data['coord']['lon']
        lat = self.weather_data['coord']['lat']
        self.data['longitude'] = lon
        self.data['latitude'] = lat

        # find the timezone for the given lat and longitude
        timezonefinder = TimezoneFinder()
        timezone = timezonefinder.timezone_at(lng=lon, lat = lat)  # tf.timezone_at(lng=13.358, lat=52.5061)  # 'Europe/Berlin'
        self.data['timezone'] = timezone

        # Calculate the location timezone
        location = pytz.timezone(timezone)
        location_datetime = datetime.datetime.now(location).strftime("%d/%m/%y  %I:%M %p")
        self.data['location'] = location
        self.data['location_datetime'] = location_datetime

        # Calculate sunrise and sunset datetime
        sunrise = datetime.datetime.fromtimestamp(int(self.weather_data['sys']['sunrise'])).strftime('%d/%m/%y  %I:%M %p') 
        sunset = datetime.datetime.fromtimestamp(int(self.weather_data['sys']['sunset'])).strftime('%d/%m/%y  %I:%M %p') 
        self.data['sunrise'] = sunrise 
        self.data['sunset'] = sunset

        self.data['image_icon_url'] = f"http://openweathermap.org/img/wn/{self.weather_data['weather'][0]['icon']}@2x.png" 

        return self.data

