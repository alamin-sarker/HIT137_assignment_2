from tkinter import * 
from tkinter import ttk 
from tkinter import messagebox
from Geocode import Geocode
from Weather import Weather

class AddressInterface:
    house_number = None
    street_name = None
    suburb = None
    state = None
    postcode = None
    address = None

    def __init__(self, root):
        self.weather_data = None
        
        self.root = root 

        mainframe = ttk.Frame(self.root)
        mainframe['padding'] = 20   # padding inside frame 
        mainframe.grid(column=0, row=0, sticky=(N, S, E, W))

        # Expand the frame if the window is resized
        self.root.columnconfigure(0, weight = 1)
        self.root.rowconfigure(0, weight = 1)

        # Heading Label
        heading_label_style = ttk.Style()
        heading_label_style.configure("HL.TLabel", font = ('Arial', 15))   

        heading_label = ttk.Label(mainframe, text = "Get weather information for your address", style="HL.TLabel")
        heading_label.grid(column = 0, row = 0, columnspan = 2, pady = 10)

        # Label Style
        label_style = ttk.Style()
        label_style.configure("LS.TLabel", font = ('Arial', 12))

        self.__create_form_label(mainframe, "House Number ", 1)
        self.__create_form_label(mainframe, "Street Name ", 2)
        self.__create_form_label(mainframe, "Suburb ", 3)
        self.__create_form_label(mainframe, "State ", 4)
        self.__create_form_label(mainframe, "Postcode ", 5)

        # house number entry 
        house_number = StringVar()
        house_number_entry = self.__create_form_entry(mainframe, house_number, 1)
        street_name = StringVar()
        street_name_entry = self.__create_form_entry(mainframe, street_name, 2)
        suburb = StringVar()
        suburb_entry = self.__create_form_entry(mainframe, suburb, 3) 
        state = StringVar()
        state_entry = self.__create_form_entry(mainframe, state, 4)
        postcode = StringVar()
        postcode_entry = self.__create_form_entry(mainframe, postcode, 5)

        def getAddress():
            self.house_number = house_number_entry.get().strip().lower()
            
            # get the street name and format it
            self.street_name = street_name_entry.get().strip().lower()
            self.street_name = self.street_name.split()
            self.street_name = '+'.join(self.street_name)

            # get the suburb name and format it
            self.suburb = suburb_entry.get().strip().lower()
            self.suburb = self.suburb.split()
            self.suburb = '+'.join(self.suburb)

            self.state = state_entry.get().strip().lower()
            self.postcode = postcode_entry.get().strip().lower()
            
            self.parse_address()

            latitude, longitude = self.get_coordinates_from_address()

            self.weather_data = self.get_weather_from_coordinates(latitude, longitude)

            # print(f"House Number: {self.house_number}")
            # print(f"Street Name: {self.street_name}")
            # print(f"Suburb: {self.suburb}")
            # print(f"State: {self.state}")
            # print(f"Postcode: {self.postcode}")

            self.root.destroy()

        # Get Weather information button 
        address_button = ttk.Button(mainframe, text = "Show weather", command = getAddress)
        address_button.grid(column = 0, row = 7)

        # Get Weather information button 
        exit_button = ttk.Button(mainframe, text = "Exit", command = self.root.destroy)
        exit_button.grid(column = 1, row = 7)
    
    def parse_address(self): 
        if (self.house_number == '') or (self.street_name == '') or (self.suburb == '') or (self.state == ''):  
            messagebox.showerror('ERROR', "[ADDRESS]: Enter a valid address")

        self.address = (f"{self.house_number}+{self.street_name},+{self.suburb},+{self.state}")
        print(f"[ADDRESS] Address: {self.address}")


    def get_coordinates_from_address(self): 
        try: 
            geocode = Geocode()
            latitude, longitude = geocode.get_coordinates_from_address(self.address)
            return latitude, longitude
        except Exception as e: 
            messagebox.showerror('ERROR', e)

    
    def get_weather_from_coordinates(self, lat, lon): 
        weather = Weather(lat, lon)
        try: 
            weather_data = weather.get_weather_api_data()
            print(weather_data)
            return weather_data
        except Exception as e: 
            messagebox.showerror('ERROR', e)


    def get_weather_data(self):
        return self.weather_data 


    def __create_form_entry(self, parent, entry_variable: StringVar, rowposition: int): 
            entry_variable = StringVar()
            entry = ttk.Entry(parent, textvariable = entry_variable)
            entry.grid(column = 1, row = rowposition, sticky = (W), pady = 5)

            return entry_variable


    def __create_form_label(self, parent, label_name: str, row_position: int): 
            label = ttk.Label(parent, text = label_name, style = "LS.TLabel")
            label.grid(column = 0, row = row_position, sticky = (E), pady = 5)

            return label



