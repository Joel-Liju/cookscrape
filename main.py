from tkinter import ttk
from tkinter import *
import os
from recipe import Recipe

window = Tk()

window.title("Recipe organizer")
window.resizable(True, True)
window.geometry('700x400')
recipeButtons = []
recipeCats = []
recipes = {}
url = StringVar()
if not os.path.exists("recipes"):
    os.mkdir("recipes")
categories = os.listdir("recipes")

Url = ttk.Entry(window, textvariable=url)

Url.pack()
def ScrapeUrl():
    from scrapper import scrapeMode
    scrapeMode(url.get(),"Temp")
    url.set("")
    Url.delete(0,END)

UrlButton = Button(window, command= ScrapeUrl, text="Scrape")
UrlButton.pack() 
# recipeWindow = Text(window,height=5,width=25,bg="light cyan")
# recipeWindow.grid(row=10,column=1)

# def display_ingredients(recipe):
#     global recipeWindow
#     recipeWindow.delete('1.0', END)
#     for index,ingredient in enumerate(recipe.ingredients):
#         recipeWindow.insert(str(index+1)+".0", str(index+1)+". "+ingredient+"\n")
# for index, name in enumerate(categories):
#     recipeButtons.append(Label(text=name))
#     recipeButtons[index].grid(row=1,column=index+1)
#     for i,recipeName in enumerate(os.listdir("recipes/"+name)):
#         recipes[recipeName] = Recipe()
#         recipes[recipeName].makeRecipe(recipeName,"recipes/"+name+"/"+recipeName)

        # try:
        #     recipeButtons[index].append(ttk.Button(window,text=recipeName, command=lambda m=recipeName: display_ingredients(recipes[m])))
        # except:
        #     recipeButtons[index] = [ttk.Button(window, text=recipeName, command=lambda m=recipeName: display_ingredients(recipes[m]))]
        # recipeButtons[index][i].grid(row = (2+i),column = index+1)
window.mainloop()