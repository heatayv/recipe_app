import csv

class Account:
    def __init__(self, owner, recipes):
        self.owner = owner
        self.recipes = recipes

recipes_heather = [
    {
        'name': 'Beans on Toast',
        'ingredients': [],
        'ingredients_subset': [],
        'directions': '',
        'photo': '/static/images/beans-on-toast.jpg',
        'tags': ['Kevin', 'Bon Appetit', 'Entree'],
        'formatted_tags': '',
        'source_name':'Bon Appetit',
        'source': 'https://www.bonappetit.com/recipe/weeknight-beans-on-toast'
    },
    {
        'name': 'Chicken Caeser Sandwiches',
        'ingredients': [],
        'ingredients_subset': [],
        'directions': '',
        'photo': '/static/images/chicken-caesar-sandwich.jpg',
        'tags': ['Kevin', 'Bon Appetit', 'Entree', 'Grill'],
        'formatted_tags': '',
        'source_name':'Bon Appetit',
        'source':'https://www.bonappetit.com/recipe/grilled-chicken-sandwich-with-mustard-mayo'
    },
]

recipes_laurel = [
     {  
        'name': 'Buffalo Mac and Cheese',
        'ingredients': [''],
        'ingredients_subset': [],
        'directions': [''],
        'photo': '/static/images/buffalo-mac-and-cheese.jpg',
        'tags': ['Kevin', 'Entrees', 'Favorite'],
        'formatted_tags': '',
        'source_name':'',
        'source': '',
     },
]

Heather = Account("Heather", recipes_heather)
Laurel = Account("Laurel", recipes_laurel)


headers = ["owner", "name", "ingredients", "ingredients_subset", "directions", "photo", "tags", "formatted_tags", "source_name", "source"]

with open('test.csv', 'w', newline='') as csvfile:
    x = csv.DictWriter(csvfile, fieldnames = headers)
    x.writeheader()
    for i in range(len(Heather.recipes)): 
      recipes_heather[i]["owner"] = "Heather"
    for recipe in Heather.recipes: 
        x.writerow(recipe)
    for i in range(len(Laurel.recipes)): 
      recipes_laurel[i]["owner"] = "Laurel"
    for recipe in Laurel.recipes: 
        x.writerow(recipe)

with open('test.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['owner'] == "Heather": 
            print(row['name'])  


