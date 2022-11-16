from AddressInterface import AddressInterface

class DailyWeather: 
    def __init__(self):

        # get the address from the user
        try: 
            AddressInterface()
        except Exception as e: 
            print(e)























if __name__ == "__main__":
    d = DailyWeather()