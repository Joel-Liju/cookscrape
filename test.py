from bs4 import BeautifulSoup
import requests
import re

path = "./recipes/"

url = "https://www.indianhealthyrecipes.com/chicken-biryani-recipe/"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

ingredients = soup.find_all("li",class_="")

for ingredient in ingredients:
	print(ingredient)