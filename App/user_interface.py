from tkinter import * 
from tkinter import ttk 

# root window
root = Tk()
root.geometry("500x300")
root.title("Weather Information")

mainframe = ttk.Frame(root)
mainframe['padding'] = 20   # padding inside frame 
mainframe.grid(column=0, row=0, sticky=(N, S, E, W))

# Expand the frame if the window is resized
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

# Heading Label
heading_label_style = ttk.Style()
heading_label_style.configure("HL.TLabel", font = ('Arial', 15))   

heading_label = ttk.Label(mainframe, text = "Get weather information for your address", style="HL.TLabel")
heading_label.grid(column = 0, row = 0, columnspan = 2, pady = 10)

# Label Style
label_style = ttk.Style()
label_style.configure("LS.TLabel", font = ('Arial', 12))

def create_form_label(label_name: str, row_position: int): 
    label = ttk.Label(mainframe, text = label_name, style = "LS.TLabel")
    label.grid(column = 0, row = row_position, sticky = (E), pady = 5)

house_number_label = create_form_label("House Number ", 1)
street_name_label = create_form_label("Street Name ", 2)
suburb_label = create_form_label("Suburb ", 3)
state_label = create_form_label("State ", 4)
postcode_label = create_form_label("Postcode ", 5)

def create_from_entry(entry_variable: StringVar, rowposition: int): 
    entry_variable = StringVar()
    entry = ttk.Entry(mainframe, textvariable = entry_variable)
    entry.grid(column = 1, row = rowposition, sticky = (W), pady = 5)

    return entry_variable

# house number entry 
house_number = StringVar()
house_number_entry = create_from_entry(house_number, 1)
street_name = StringVar()
street_name_entry = create_from_entry(street_name, 2)
suburb = StringVar()
suburb_entry = create_from_entry(suburb, 3) 
state = StringVar()
state_entry = create_from_entry(state, 4)
postcode = StringVar()
postcode_entry = create_from_entry(postcode, 5)

def getAddress():
    house_number = house_number_entry.get()
    street_name = street_name_entry.get()
    suburb = suburb_entry.get()
    state = state_entry.get()
    postcode = postcode_entry.get()
    print(f"House Number: {house_number}")
    print(f"Street Name: {street_name}")
    print(f"Suburb: {suburb}")
    print(f"State: {state}")
    print(f"Postcode: {postcode}")


# Get Weather information button 
address_button = ttk.Button(mainframe, text = "Show weather", command = getAddress)
address_button.grid(column = 1, row = 7)

root.mainloop()


