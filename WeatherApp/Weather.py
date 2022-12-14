import requests 

class Weather:
    """Getting waether data from openweathermap API"""

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    API_KEY = "b9ae805fd470d789469e26f46158619e"
    latitude = None
    longitude = None

    def __init__(self, lat, lon):
        self.latitude = lat
        self.longitude = lon

    # https://api.openweathermap.org/data/2.5/weather?lat=37.4226618&lon=-122.0829302&appid=b9ae805fd470d789469e26f46158619e
    def get_weather_api_data(self): 
        '''Fetch weather API data for given latitude and longitude'''

        # forming request URL with required parameters (latitude & logitude from google api)
        request_url = f"{self.BASE_URL}?lat={self.latitude}&lon={self.longitude}&appid={self.API_KEY}" 
        # getting response by weather API request
        response = requests.get(request_url)

        # checking for valid response code
        if response.status_code == 200: 
            print("[WEATHER] The API response was succcessful")
            return response.json()
        else: 
            raise Exception(f"[WEATHER] ERROR: {response.message}")