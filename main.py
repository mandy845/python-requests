import requests
from tkinter import *
from tkinter import messagebox

#   CREATE THE FRAME FOR TKINTER
window = Tk()
window.title("Chuck Norris Jokes")
window.geometry("500x500")


def get_joke():
    try:
        #   CREATE A GET REQUEST AND PASS IN THE url AS A PARAMETER
        response = requests.get("https://api.chucknorris.io/jokes/random")
        #   ONCE WE GET THE RESPONSE BACK, WE CHANGE IT TO JSON FORMAT
        parsed_data = response.json()
        #   WE GET THE JOKE BY GETTING THE VALUE
        joke = parsed_data["value"]
        #   CALL THE display_joke FUNCTION, TO SHOW THE USER THE JOKE
        display_joke(joke)
    #   CATCH THE EXCEPTION IS THERE IS NO INTERNET CONNECTION
    except requests.ConnectionError:
        #   NOTIFY THE USER
        messagebox.showerror("Connection Error", message="Please check your network connection")


def display_joke(joke):
    #   DISPLAY THE Joke IN A messagebox
    messagebox.showinfo(title="Chuck Norris Joke", message=joke)


joke_btn = Button(window, text="get joke", command=get_joke, fg="blue").place(x=200, y=150)
window.mainloop()