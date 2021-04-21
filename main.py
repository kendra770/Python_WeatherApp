import requests
import tkinter as tk
from tkinter import *
import json
from PIL import ImageTk,  Image


class WeatherApp:

    def get_data(city):

        image_type = "default.jpg"

        # API KEY and URL for pulling the Weather Data#
        global api_key
        api_key = "953eb70905fdaf52a9643c9ba78140b0"

        global url
        url = "https://api.openweathermap.org/data/2.5/weather/"

        # API query#
        global arguments
        arguments = {"APPID": api_key, "q": city, "units": "imperial"}

        global data
        data = requests.get(url, params=arguments).json()

         #print(json.dumps(data))#

        try:
            name = data['name']
            desc = data['weather'][0]['description']
            temp = data['main']['temp']
            wind = data['wind']['speed']
            feels_like = data['main']['feels_like']
            full_string = 'Location: {} \n Conditions : {} \n' 'Temperature (F): {} \n' 'Wind (MPH): {} \n' 'Feels Like (F): {}'.format(
            name, desc, temp, wind, feels_like)

            image_type
            image_type =WeatherApp.get_image_type(desc)





        except:
            full_string = "No matching location found. Please check location and try again"


        label['text'] = full_string
        
 #Create a new image object and set it to our App background#
        
        new_image = ImageTk.PhotoImage(Image.open(image_type))
        background_label.configure(image=new_image)
        background_label.image = new_image

 #Function to choose the correct background image based on JSON Weather Description#       
        
    def get_image_type(description):
        global image_type
        if "rain" in description:
            image_type = "rain.jpg"
        elif "snow" in description:
          image_type = "snow.jpg"
        else:
          image_type = "sunny.jpg"
        return image_type

 #Main Method of the WeatherApp Class#

    def __init__(self):

     self.MyGui = Tk()
     self.MyGui.title("WeatherApp")
     self.MyGui.geometry("300x300")

    #Create a background image for Gui#
     global background_image
     background_image = tk.PhotoImage()

    #Create a background_label for background_image#
     global background_label
     background_label = Label(self.MyGui, image=background_image)
     background_label.place(relwidth=1, relheight=1)


    #Creating Frame 1 and 2 to place buttons; entry box and output#
     frame1 = Frame(self.MyGui,bg="white")
     frame2 = Frame(self.MyGui,bg="white", bd=8)
     frame1.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")
     frame2.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

     global label
     label = Label(frame2, font=('Arial', 13))
     label.place(relwidth=1, relheight=1)

    #Creating entry and button and placing it within Frame#
     entry = Entry(frame1, font =('Arial', 14))
     entry.place(relwidth=0.65, relheight=1)
     whats_the_weather = Button(frame1, text="What's the Weather", fg='blue', font=('Arial', 10), command=lambda:WeatherApp.get_data(entry.get()))
     whats_the_weather.pack(side=RIGHT)


     mainloop()








WeatherApp()

