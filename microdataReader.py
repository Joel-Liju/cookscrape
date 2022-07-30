from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json

class _Item:
    def __init__(self,name,ingredients, steps):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
    def __repr__(self):
        return self.name
    def getRecipe(self):
        return self.steps
    def getIngredients(self):
        return self.ingredients
    pass
    
def getItem(url):
    page = Request(url, headers = {'User-Agent':'Chrome/51.0.2704.103'})
    page = urlopen(page).read()
    soups = BeautifulSoup(page, 'html.parser')
    recipe = soups.find("script",type = "application/ld+json")
    temp = json.loads(recipe.text)
    # for ingredient in temp["recipeIngredient"]:
        # print(ingredient)
    # try:
    steps = []
    try:#this happpens if there is no @graph in the microdata
        if temp['@type'] == "Recipe":
            temp["recipeInstructions"]
    except  KeyError:
        for item in temp['@graph']:
            if item["@type"] =="Recipe":
                temp = item
    
    if not type(temp["recipeInstructions"]) == type("words"):
        for step in temp["recipeInstructions"]:
            try:
                steps.append(step["text"])
            except:
                steps.append(step)
    else:
        steps.append(temp["recipeInstructions"].split('.'))
    return _Item(temp["name"],temp["recipeIngredient"],steps)
    # except:
        # print(temp["recipeInstructions"])