import requests
import gc
from flask import Flask, render_template
app = Flask(__name__)

recipes = [
    {
        'name': 'Spaghetti 2',
        'ingredients': ['spaghetti', 'meatballs', 'sauce'],
        'ingredients_subset': ['spaghetti', 'meatballs', 'sauce','Entree', 'Vegetarian', 'Quick', 'Heather'],
        'directions': 'Preheat oven to 325°. Pat chicken legs dry with paper towels. Arrange chicken, onions, halved garlic heads, and lemon in a 13x9" baking dish; season liberally with salt (remember to season both sides of chicken). Pour in oil and toss everything to coat. Turn garlic cut side down and nestle it in so it is in contact with the baking dish. Roast, rotating pan halfway through, until meat is almost falling off the bone, 50–60 minutes. Meanwhile, finely grate 1 garlic clove into a small bowl. Add yogurt, a big pinch of salt, and 1 Tbsp. water and mix well. Set aside yogurt sauce.',
        'photo': 'http://heatherayvazian.com/images/italy-florence-bust.jpg',
        'tags': ['Entree', 'Vegetarian', 'Quick', 'Heather'],
        'formatted_tags': '',
        'source_name':'Bon Appetit',
        # 'source':'chicken-caesar-sandwich-test.jpg'
        'source': 'http://heatherayvazian.com/images/italy-florence-city.jpg'
    },
    {
        'name': 'Kufta Yakina',
        'ingredients': ['lamb', 'yogurt', 'mint'],
        'ingredients_subset': ['spaghetti', 'meatballs', 'sauce'],
        'directions': 'Make the kuftas, then make the soup. Apostraphes are the undoing of good code.',
        'photo': 'http://heatherayvazian.com/images/italy-florence-city.jpg',
        'tags': ['Armenian', 'Heather', 'Soup', 'Bon Appetit'],
        'formatted_tags': '',
        'source_name':'Bon Appetit',
        # 'source':'chicken-caesar-sandwich-test.jpg'
        'source':'http://heatherayvazian.com/images/italy-florence-city.jpg'
    },
    {
        'name': 'Kufta Yakina3',
        'ingredients': ['lamb', 'yogurt', 'mint','test'],
        'ingredients_subset': ['spaghetti', 'meatballs', 'sauce'],
        'directions': 'Make the kuftas, then make the soup. Apostraphes are the undoing of good code. test',
        'photo': 'http://heatherayvazian.com/images/italy-florence-view.jpg',
        'tags': ['Armenian', 'Heather', 'Soup', 'Bon Appetit'],
        'formatted_tags': '',
        'source_name':'Bon Appetit',
        # 'source':'chicken-caesar-sandwich-test.jpg'
        'source':'http://heatherayvazian.com/images/italy-florence-view.jpg'
    },
    {
        'name': 'Kufta Yakina',
        'ingredients': ['lamb', 'yogurt', 'mint'],
        'ingredients_subset': ['spaghetti', 'meatballs', 'sauce'],
        'directions': 'Make the kuftas, then make the soup. Apostraphes are the undoing of good code.',
        'photo': 'http://heatherayvazian.com/images/italy-florence-city.jpg',
        'tags': ['Armenian', 'Heather', 'Soup', 'Bon Appetit'],
        'formatted_tags': '',
        'source_name':'Bon Appetit',
        # 'source':'chicken-caesar-sandwich-test.jpg'
        'source':'http://heatherayvazian.com/images/italy-florence-city.jpg'
    }
]

def format_tags(): 
    for i in range(len(recipes)):
        recipes[i]['formatted_tags'] = " ".join(recipes[i]['tags'])

format_tags()

tag_list = []
all_tags = set(tag_list)

def master_tag_list():
    for i in range(len(recipes)):
        for tag in recipes[i]['tags']:
            all_tags.add(tag)

master_tag_list()



@app.route('/')
def home(): 
    return render_template('home.html', recipes = recipes)  

@app.route('/<recipe_name>')
def recipe(recipe_name):
    value = {}
    for recipe in recipes:
        if recipe['name'] == recipe_name:
            value = recipe
    return render_template('recipe.html', x=value)

if __name__ == '__main__':
    app.run(debug=True)
