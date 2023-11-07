from bs4 import BeautifulSoup

import os
from microdataReader import getItem

"""
params : filepath -> this is the path to the file which is going to be read to be scraped..
                the file will contain certain information, which includes   
                url , title , ingredient tag, ingredient identifier, step tag, step identifir
                where the tag is the html tag for the individual item, and the identifier is the id or the class name, directory path
"""
# temp = input()
# page = Request(temp, headers = {'User-Agent':'Chrome/51.0.2704.103'})

# page = urlopen(page).read()
# items = microdata.get_items(page)
# print(items)
# soups = BeautifulSoup(page, 'html.parser')
# recipe = soups.find("script",type = "application/ld+json")
# t = json.loads(recipe.text)
# for ingredient in t["recipeIngredient"]:
    # print(ingredient)
# print(t['recipeInstructions'])
# for step in t['recipeInstructions']:
    # print(step)
    # print(step['text'])
BASE_PATH = './Recipes'
def scrapeMode(url, path):
    # url = input("Please input the URL for you recipe \n")
    # print("please input the type of recipe out off.")
    # for dir in os.listdir(BASE_PATH):
    #     print(dir)
    # print("Or you can make a new one")
    # path = input()
    # f = open(filepath,"r")
    recipe = getItem(url)
    
    if not os.path.isdir(BASE_PATH+"/"+path):
        os.mkdir(BASE_PATH+"/"+path)
    file = open(BASE_PATH+"/"+path+'/'+recipe.getName().strip()+".txt","w+", encoding = "utf-8")
    file.write("URL\n")
    file.write(url+"\n")
    file.write("Times\n")
    file.write("CookTime: "+str(recipe.cookTimes[0])+"\tPrepTime: "+str(recipe.cookTimes[1])+"\tTotalTime: "+str(recipe.cookTimes[2])+"\n")
    file.write("Ingredients\n")
    for num, ingredient in enumerate(recipe.getIngredients(),1):
        file.write(str(num)+") "+ingredient+"\n")
    file.write("Steps\n")
    for num, step in enumerate(recipe.getRecipe(),1):
        print(step)
        file.write(str(num)+") "+step + "\n")
    file.close()
    print("done")
    # for line in f.readlines():
        # try:
            # page = Request(url, headers = {'User-Agent':'Chrome/51.0.2704.103'})
            # page = urlopen(page).read()
            # soups = BeautifulSoup(page, 'html.parser')
            # try:
                # file = open(path+"/"+genre+"/"+title.strip()+".txt","w+", encoding = "utf-8")
            # except:
                # os.mkdir(path+"/"+genre)
                # file = open(path+"/"+genre+"/"+title.strip()+".txt","w+", encoding = "utf-8")
            # recipe = soups.find("script",type = "application/ld+json")
            # file.write("Ingredients\n")
            # for num, ingredient in enumerate(recipe["recipeIngredient"], 1):
                # file.write(str(num)+") "+ingredient.strip() + "\n")   
            # file.write("Steps\n")
            # for stepNum,step in enumerate(steps,1):
                # sentence = str(stepNum) + ". " + step +"\n"
                # file.write(sentence)
            # file.close()
        # except ValueError:
            # pass
    # f.close()

def _recursivelyFindDir():
    pass
'''
given a folder path, it will recursively find all the files within it
'''
def _recursivelyFindFiles(pathToFolder, listOfFiles):
    for file in os.listdir(pathToFolder):
        if os.path.isfile(pathToFolder+"/"+file):
            listOfFiles.append(pathToFolder+"/"+file)
        else:#this is when it is a directory
            _recursivelyFindFiles(pathToFolder+"/"+file, listOfFiles)    
    return listOfFiles
'''
params: ingredient list is the list of all the ingredient you have, needs to be exact match right now
        pathToFolder is the path to the folder containing the recipes.
'''
def findByIngredientMode(ingredientList, pathToFolder):
    files = _recursivelyFindFiles(pathToFolder,[])
    recipeList =[]
    for file in files:
        f = open(file,"r")
        listOfIngredients = []
        for line in f.readlines():
            if line.strip().lower() == "steps":
                break
            listOfIngredients = listOfIngredients + [x.lower() for x in line.strip().split()]
        for ingredient in ingredientList:
            if ingredient.lower() in listOfIngredients:
                recipeList.append(file)
                break
    for recipe in recipeList:
        print(recipe.split("/")[len(recipe.split("/"))-1])
    #print('\n'.join([x.split("/")[len(x.split("/"))-1] for x in recipeList]))
if __name__ == '__main__':
    scrapeMode()
