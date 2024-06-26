from dataclasses import dataclass, field
import re
@dataclass
class Recipe:
    name: str = ""
    ingredients: list = field(default_factory=list)
    steps: list = field(default_factory=list)
    time: str = ""

    def makeRecipe(self, name, text) -> None:
        self.name = name
        f = open(text,'r')
        flag = False
        for line in f.readlines():
            line = line.strip()
            if line == "Ingredients":
                flag = True
                continue
            if line == "Steps":
                flag = False
                continue
            line = re.sub(r"^[0-9]+\)",'',line, count=1)
            line = line.strip()
            if flag:
                try:
                    self.ingredients.append(line)
                except:
                    self.ingredients = [line]
            else:
                try:
                    self.steps.append(line)
                except:
                    self.steps = [line]

