import os
recipePath = "./recipes/"
absolutePath = "C:\\Users\\Dare\\Desktop\\extras\\Recipes\\Recipes\\"

def func(title, genre):
    file = open(recipePath+"/"+genre+"/" + title+".txt","r")

    try:
        saver = open(absolutePath+"/"+genre+"/"+ title+".md" , "w+")
    except:
        os.mkdir(absolutePath+"/"+genre)
        saver = open(absolutePath+"/"+genre+"/"+ title+".md" , "w+")
    for line in file.readlines():
        if line.strip() == "Ingredients":
            saver.write("# Ingredients\n")
            ingredientFlag = True
            continue
        if line.strip() == "Steps":
            saver.write("# Steps\n")
            ingredientFlag = False
            continue
        if ingredientFlag:
            saver.write("- [ ] "+line.strip()+"\n")
            continue
        saver.write(line.strip()+"\n")
    saver.close()