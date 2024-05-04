from bs4 import BeautifulSoup
import requests
import re
import json

path = "./recipes/"

#url = "https://www.indianhealthyrecipes.com/chicken-biryani-recipe/"
url = "https://www.myhouseofpizza.com/poolish-pizza-dough-recipe/"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
items = soup.find("script",type = "application/ld+json")# this is what it looks for
jsonObject = json.loads(items.get_text())

for item in jsonObject["@graph"]:
	if "Recipe" in item["@type"]:
		print(item["recipeInstructions"])