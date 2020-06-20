import gc

class Account:
    def __init__(self, owner, recipes):
        self.owner = owner
        self.recipes = recipes

recipes_heather = [
    {
        'name': 'Beans on Toast',
        'photo': '/static/images/beans-on-toast.jpg',
    },
    {
        'name': 'Chicken Caeser Sandwiches',
        'photo': '/static/images/chicken-caesar-sandwich.jpg',

    },
]

recipes_laurel = [
     {  
        'name': 'Buffalo Mac and Cheese',
        'photo': '/static/images/buffalo-mac-and-cheese.jpg',
     },
]

# This creates class objects 
Heather = Account("Heather", recipes_heather)
Laurel = Account("Laurel", recipes_laurel)

# This creates a list of all objects/instances of the class Accounts 
accounts = [] 
for obj in gc.get_objects():
    if isinstance(obj, Account):
        accounts.append(obj)

# This print 
# for account in accounts: 
#     print(account.owner)
#     print(account.recipes)

x = Heather

print (x.recipes)

for recipe in x.recipes: 
    print(recipe['name'])




