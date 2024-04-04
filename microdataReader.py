from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json
import re


class _Item:
    def __init__(self,name,ingredients, steps, cookTimes):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.cookTimes = cookTimes
    def __repr__(self):
        return self.name
    def getRecipe(self):
        return self.steps
    def getIngredients(self):
        return self.ingredients
    def getName(self):
        return self.name
    pass
    
def getItem(url):
    page = Request(url, headers = {'User-Agent':'Chrome/51.0.2704.103'})
    page = urlopen(page).read()
    soups = BeautifulSoup(page, 'html.parser')
    recipe = soups.find("script",type = "application/ld+json")# this is what it looks for
    temp = json.loads(recipe.text)
    # for ingredient in temp["recipeIngredient"]:
        # print(ingredient)
    # try:
    steps = []
    prepTime = re.findall('"prepTime":"PT(\d*)', recipe.text)# " for not json loaded text, but ' for json loaded text
    cookTime = re.findall('"cookTime":"PT(\d*)', recipe.text)
    totalTime = re.findall('"totalTime":"PT(\d*)', recipe.text)
    print(recipe.text)
    print(prepTime,cookTime,totalTime)
    times= re.findall('PT(\d+)M(\d+)S|PT(\d+)M|PT(\d+)S',recipe.text)# doesn't work at the moment
    CookTimes = []
    for i in range(3):
        for j in times[i]:
            try:
                CookTimes.append(int(j))
                break
            except:
                pass
    # total_secs = 60*int(m) + int(s)
    # print(total_secs)
    #first it can be a string or a list
    def gettingRecipeItem(word, RecipeItem):
        try:#this happpens if there is no @graph in the microdata
            if word in RecipeItem['@type']:
                return RecipeItem
        except  KeyError:
            for item in RecipeItem['@graph']:
                if item["@type"] ==word:
                    return item
    if isinstance(temp, (list, tuple)):
        # print(temp)
        for t in temp:
            if gettingRecipeItem("Recipe",t) is not None:
                temp = gettingRecipeItem("Recipe",t)
    else:#this means it is a dictionary
        
        temp = gettingRecipeItem("Recipe",temp)
    
    if not type(temp["recipeInstructions"]) == type("words"):
        for step in temp["recipeInstructions"]:
            try:
                steps.append(step["text"])
            except:
                steps.append(step)
    else:
        steps.append(temp["recipeInstructions"].split('.'))
    
    return _Item(temp["name"],temp["recipeIngredient"],steps, CookTimes)
    # except:
        # print(temp["recipeInstructions"])