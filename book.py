import requests
import gc
from flask import Flask, render_template
app = Flask(__name__)

recipes = [
    # {
    #     'name': 'Template',
    #     'ingredients': [],
    #     'ingredients_subset': [],
    #     'directions': '',
    #     'photo': '/static/images/NAME.jpg',
    #     'tags': ['NAME', 'CATEGORY', 'VEG', 'COUNTRY'],
    #     'formatted_tags': '',
    #     'source_name':'',
    #     'source': ''
    # },
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
    {
        'name': 'Chicken Escabeche',
        'ingredients': [],
        'ingredients_subset': [],
        'directions': '',
        'photo': '/static/images/chicken-escabeche.jpg',
        'tags': ['Kevin', 'Bon Appetit', 'Entree'],
        'formatted_tags': '',
        'source_name':'Bon Appetit',
        'source': 'https://www.bonappetit.com/recipe/chicken-escabeche'
    },
    {
        'name': 'Crispy Chickpea Salad',
        'ingredients': [],
        'ingredients_subset': [],
        'directions': '',
        'photo': '/static/images/chickpea-salad.jpg',
        'tags': ['Kevin', 'Bon Appetit', 'Salad', 'Vegetarian'],
        'formatted_tags': '',
        'source_name':'Bon Appetit',
        'source': 'https://www.bonappetit.com/recipe/chopped-dinner-salad-with-crispy-chickpeas'
    },
    {
        'name': 'Poached Cod in Tomato Curry',
        'ingredients': [],
        'ingredients_subset': [],
        'directions': '',
        'photo': '/static/images/poached-cod-tomato-curry.jpg',
        'tags': ['Kevin', 'Bon Appetit', 'Entree', 'Fish', 'Light'],
        'formatted_tags': '',
        'source_name':'Bon Appetit',
        'source': 'https://www.bonappetit.com/recipe/cod-poached-in-tomato-curry'
    },
    {
        'name': 'Grilled Pork Tenderloin with Peach Sauce',
        'ingredients': [],
        'ingredients_subset': [],
        'directions': '',
        'photo': '/static/images/pork-peach-mustard.jpg',
        'tags': ['Kevin', 'Bon Appetit', 'Entree', 'Grill'],
        'formatted_tags': '',
        'source_name':'Bon Appetit',
        'source': 'https://www.bonappetit.com/recipe/pork-tenderloin-with-peach-mustard-sauce'
    },
    {
        'name': 'Tomato Toast',
        'ingredients': [],
        'ingredients_subset': [],
        'directions': '',
        'photo': '/static/images/tomato-toast.jpg',
        'tags': ['Kevin', 'Bon Appetit', 'Entree', 'Vegetarian', 'Light'],
        'formatted_tags': '',
        'source_name':'Bon Appetit',
        'source': 'https://www.bonappetit.com/recipe/tomato-toast-with-chives-and-sesame-seeds'
    },
    {
        'name': 'Zaatar Chicken',
        'ingredients': [],
        'ingredients_subset': [],
        'directions': '',
        'photo': '/static/images/zaatar-chicken.jpg',
        'tags': ['Kevin', 'Bon Appetit', 'Entree'],
        'formatted_tags': '',
        'source_name':'Bon Appetit',
        'source': 'https://www.bonappetit.com/recipe/zaatar-chicken-with-garlicky-yogurt'
    },
    {
        'name': 'Sesame Ginger Salmon',
        'ingredients': ['1/2 lb salmon per person', 'asparagus', 'rice pilaf', 'sesame seeds (topper)', 'green onions (topper)'],
        'ingredients_subset': ['1/4 cup olive oil', '2 tablespoons soy sauce', '2 tablespoons rice vinegar', '2 tablespoons sesame oil', '2 tablespoons brown sugar', '2 cloves garlic', '1 tablespoon grated fresh ginger', '2 tablespoons honey', '1/2 lemon juice', '1/2 teaspoon Sriracha (optional)'],
        'directions': 'Preheat oven to 450°F and bake for 12-15 min. Marinate salmon for at least 30 min before. Make the rice while marinating; start cooking asparagus when you put the salmon in the oven.',
        'photo': '/static/images/sesame-ginger-salmon.jpg',
        'tags': ['Heather', 'Entree'],
        'formatted_tags': '',
        'source_name':'Online',
        'source': 'https://damndelicious.net/2013/11/13/sesame-ginger-salmon/'
    },
    {
        'name': 'Elote Bowl',
        'ingredients': ['3/4 cup red quinoa', '1 can chickpeas', '2 ears corn', '1 jalapeño','2 radishes', 'fresh cilantro', '1 lime', '2 tbsp yogurt', '2 tbsp mayo', '1/4 tsp cayenne pepper', 'parmesan cheese'],
        'ingredients_subset': [],
        'directions': 'Cook the quinoa (with 1 1/4 cups water, simmer for 12-15 min). Prep the vegetables (slice radishes, cut off corn kernels, mince jalapeño, chop cilantro). Make elote sauce (mix yogurt, mayo, 1/2 lime juice, salt). Crisp chickpeas and corn (heat oil over high heat, cook chickpeas and corn ~4-6 min until crisp & lightly charred in spots. If this does not work, crisp separately). Serve in 2 bowls, top with sauce, radishes, cilantro, parmesan, and the remaining lime juice and cayenne pepper.',
        'photo': '/static/images/elote-bowl.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Bowl', 'Vegetarian', 'Mexican'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Take-out Style Noodles',
        'ingredients': ['8 oz asparagus', '2 tbsp fresh ginger', '4 radishes', '2 tbsp sesame oil', '2 tbsp tamari', '1 tbsp rice vinegar', '1 tbsp peanut butter', '2 tbsp chili garlic sauce', '11 oz fresh ramen noodles', '1/4 cup crispy shallots', '1/4 cup peanuts'],
        'ingredients_subset': [],
        'directions': 'Boil water for the ramen. Prep (cut asaparagus into 1-inch pieces, mince ginger, grate radishes on wide setting). Make the sauce (whisk ginger, sesame oil, tamari, rice vinegar, peanut butter, and chii garlic sauce). Cook ramen noodles (1-2 min, drain and rinse with cold water). Stir fry (heat oil over medium-high heat, cook asapagus 2-3 min, add noodles, sauce, and salt, cook 2-3 more min). Serve in 2 bowls and top with radishes, shallots, and peanuts.',
        'photo': '/static/images/take-out-style-noodles.jpg',
        'tags': ['Heather', 'Entree', 'Vegetarian', 'Asian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Canh Chua Vietnamese Soup',
        'ingredients': ['1 shallot', '2 cloves garlic', '4 oz Swiss chard', '5 oz pineapple', '1 package Wildwood tofu', '1 Thai chile', '1 tbsp red miso paste', '2 tbsp tamari', '2 tsp tamarind paste', '5 oz rice noodles', '1 lime', 'fresh basil'],
        'ingredients_subset': [],
        'directions': 'Boil water for noodles. Prep fruit and vegetables (mince garlic, chop Swiss chard stems and leaves, cut pineapple into bite sized pieces, drain tofu and cut into cubes, thinly slice Thai chile). Fry the shallot (heat oil over medium-high heat, cook 3-5 min, remove and salt). Make the broth (add oil to same pan, add garlic and red miso paste, cook 1 min. Add in tamari and tamarind. Add in 2 1/2 cups water and 1/4 tsp salt. Boil.) Cook the rice noodles (for 4-5 min, drain and rinse with cold water). Once broth is boiling, add Swiss chard, pineapple, and tofu. Return to boil, lower heat, cook 2-3 min. Add 1/2 lime juice. Serve in two bowls, top with lime wedges, basil, shallots, and chile.',
        'photo': '/static/images/canh-chua-vietnamese-soup.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Soup', 'Vegetarian', 'Asian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Fiesta Enchilada Skillet',
        'ingredients': ['1 onion', '2 cloves garlic', '4 oz kale', '1 ear corn', '1 can black beans', '1 can diced tomatoes', '2 tsp mole spice', '1 tsp cumin', '2 corn tortillas', '1/3 cup mozzarella', '1 avacado', '1 lime'],
        'ingredients_subset': [],
        'directions': 'Prepare the vegetables (dice onion, mince garlice, dice tomatoes, destem kale and roughly chop the leaves, cut kernels off, drain and rinse black beans). Start the skillet (heat oil over medium-high heat, add onion, garlic, salt and pepper and cook for 3-5 min. Add kale, black beans, tomatoes, mole spice, cumin, salt, and cook for 4-6 min, stirring occasionally). Crisp the tortillas (thinly slice the corn tortillas, heat oil over medium-high heat, add tortillas and cook for 2-3 min, remove and salt). Finish the bake (broil the oven on low, stir corn kernels the bake and top with mozzerella, broil 3-4 min). Top with sliced avacado and lime juice, serve with tortillas.',
        'photo': '/static/images/fiesta-enchilada-skillet.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian', 'Mexican'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Thai Vegetable Stir-fry',
        'ingredients': ['1 cup jasmine rice', '1/4 cup cachews', '1 zucchini', '1 yellow squash', '2 mini sweet peppers', '1 peach', '5 cloves garlic', '5 Thai chiles', '2 tbsp tamari', '2 tbsp agave', '1 tbsp Worcestershire powder', '2 tbsp hemp seeds'],
        'ingredients_subset': [],
        'directions': 'Cook the rice (with 1 1/4 cups water for 14-16 min). Toast the cashews (heat oil over medium-high heat and cook for 4-6 min). Prepare the vegetables (cut zucchini and squash into half-moons, thinly slice sweet peppers and peach, mince garlice, mince 2 Thai chili peppers). Make the sauce (Mix tamari, agave, and Worcestershire with a whisk). Stir-fry (heat oil over medium heat, add zucchini, squash, and sweet peppers 3-5 min. Add Thai chiles and garlic and cook 30 seconds. Add sauce, peaches, and salt, and cook 2-3 min.). Stir in seeds and 1/2 cashews into rice, serve everything topped with remaining cashews.',
        'photo': '/static/images/thai-vegetable-stir-fry.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian', 'Asian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Japanese Yam Sushi Bowl',
        'ingredients': ['2 Japanese yams', '3/4 cup quinoa speckled rice', '1 cucumber', '2 tsp rice vinegar', '2 tbsp sambal', '1 lime', '3 tbsp mayo', '4 oz baby spinach', '1 tbsp sesame seeds'],
        'ingredients_subset': [],
        'directions': 'Roast the yams (preheat oven to 400°F, cut yams into wedges, toss with oil, salt, and pepper, and bake 20-25 min). Cook the rice (with 1 1/4 cups water for 15-20 min). Marinate the cucumbers (thinly slice cucumbers and add to a bowl with rice vinegar and sambal). Prepare the citrus aioli (Add mayo, 1 tsp lime juice, and salt). Sauté the spinach (heat oil over medium-high heat, add baby spinach, salt, and pepper and cook for 1-2 minutes). Combine into bowls and serve, top with sesame seeds. ',
        'photo': '/static/images/japanese-yam-sushi-bowl.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Bowl', 'Vegetarian', 'Asian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Vegan Mac and Cheese',
        'ingredients': ['1 onion', '2 cloves garlic', '2 tbsp vegan butter', '1 tbsp white miso paste', '1 tbsp flour', '3/4 cup almond flour', '6 oz shell pasta', '6 oz broccoli florets', '6 oz vegan cheddar cheese', '1/3 cup panko breadcrumbs', '1 scallion'],
        'ingredients_subset': [],
        'directions': 'Preheat oven to 400°F. Boil water for the pasta. Prep (chop onion and garlic). Make the sauce (melt butter over medium-high heat, and add the onion, garlice, white miso paste, salt, and pepper. Cook, stirring frequently, until the miso paste dissolved and onion is translucent (~3-5min). Add flour and cook for 1 min, whisking constantly. Lower heat to medium and add almond milk, 1/4 cup at a time, while whisking. Simmer, continuing to whisk, until thick (~2-4 min)). Cook the pasta for 8-10 min. Roast broccoli florets in oven (tossed with oilve oil, salt, and pepper) for 6-8 min. Add the sauce to a blender with cheddar cheese and salt and blend for 1 min. Toast the breadcrumbs (set oven to broil on high, pour cheese sauce over pasta in a baking dish and stir to combine, top with breadcrumbs, drive olive oil, salt, and pepper over top. Broil for 1-2 min). Serve and top with scallions, broccoli on the side.',
        'photo': '/static/images/vegan-mac-and-cheese.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Bahn Mi Burgers',
        'ingredients': ['1/4 cup quinoa', '3 tbsp mayo', '2 Sriracha packets', '1 Persian cucumber', 'fresh cilantro', '4 oz broccoli slaw', '1 lime', '1 can chickpeas', '1/4 cup panko breadcrumbs', '2 ciabatta buns', '2 tbsp Korean black garlic seasoning', '1/4 cup pickled jalapeño'],
        'ingredients_subset': [],
        'directions': 'Cook the quinoa (with 1/2 cup water for 8-10 min). Make the aioli (mix mayo and Sriracha). Make the slaw (mix cilantro leaves, broccoli slaw, and 1/2 lime juice). Prepare burger mix (add cooked quinoa, 1/2 cup chickpeas, breadcrumbs, and salt to a food processor. Blend until well combined, ~10 pulses). Toast the buns (set the oven on low broil, halve buns, toast for 3-5 min). Cook burgers (Form the burger mixture into 2 patties and gently press each side into Korean black garlic seasoning. Heat oil over medium-high heat and cook burgers about 3-5 min each side.). Serve burgers with aioli, sliced cucumber, 1/2 broccoli cilantro slaw, and jalapeño. Add chickpeas to 1/2 slaw and serve as a side. ',
        'photo': '/static/images/bahn-mi-burgers.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian', 'Asian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Coconut Curry Udon Noodles',
        'ingredients': ['6 oz broccoli florets', '2 carrots', '1 shallot', '2 cloves garlic', '1 stalk lemongrass', '2 tbsp green curry paste', '1 can coconut milk', 'fresh cilantro', '1 lime', '6 oz udon noodles', '1/3 cup toasted coconut chips'],
        'ingredients_subset': [],
        'directions': 'Boil water for noodles. Prepare the vegetables (chop broccoli florets into bite-sized peices, thinly slice carrot diagonally, thinly slice shallot, mince garlice, cut lemongrass into pieces 2-3 inches long and press down on them). Cook (heat oil over high heat, add broccoli and carrots and cook for 2-3 min. Reduce heat to low, add oil, shallot, garlic, and green curry paste and cook 1-2 min.). Simmer (add lemongrass, coconut milk, and 1/2 cup water. Boil then simmer for 2-3 min.). Cook udon noodles (in the water 3-5 min, drain and rinse with cold water, add to skillet with 1/2 cilantro and 1/2 lime). Remove and discard lemongrass, serve and garnish with 1/2 cilantro, coconut chips, and lime wedges.', 
        'photo': '/static/images/coconut-curry-udon-noodles.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian', 'Asian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Butternut Squash Gnocchi',
        'ingredients': ['6 oz butternut squash', '4 oz broccoli rabe', 'fresh parsley', '2 tbsp butter', '1/4 cup hazelnuts', '1 package gnocchi', '2 tsp white balsamic vinegar', '1/4 cup dried cranberries'],
        'ingredients_subset': [],
        'directions': 'Boil water for gnocchi. Prepare vegetables (roughly chop butternut squash into 1/2 inch pieces, cut broccoli rabe into 1 inch pieces, finely chop parsley). Toast the nuts (heat oil over medium heat and cook 3-4 min). Cook the vegetables (In same skillet, add squash, broccoli, salt, and pepper and cook 4-6 min). Cook gnocchi (for 3-4 min, save 1/3 cup pasta water. Add gnoccchi to skillet and cook 4-6 min. Add pasta water and white balsamic vinegar until mostly evaporated, ~1 min.). Add cranberries, 1-2 min. Serve, topping with hazelnuts and parsley.',
        'photo': '/static/images/butternut-squash-gnocchi.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Autumn Bibimbap',
        'ingredients': ['3/4 cups sushi rice', '6 oz rainbow carrots', '6 oz Brussels sprouts', '1 tbsp gochujang', '1 cucumber', '1 scallion', '1 clove garlic', '2 tbsp mayo', '2 tbsp sesame oil', '6 oz baby spinach', '1 tbsp sesame seeds', '4 oz kimchi'],
        'ingredients_subset': [],
        'directions': 'Preheat the oven to 400°F. Cook the sushi rice (in 1 1/4 cups water 15-18 min). Prep vegetables (slice carrots, halve Brussels sprouts). Roast vegetables (Toss carrots in oil, toss Brussels sprouts in a glaze of gochujang and 1 tbsp water. Roast for 14-16 min.). Prepare toppings (thinly slice cucumbers and scallion. Mince garlic, add to mayo, salt, 2 tsp water, and 2 tsp sesame oil. Whisk sesame aioli.). Cook the spinach (heat 1 tsp sesame oil over medium-high heat, add spinach and cook 1-2 min). Crisp the rice (Fluff cooked rice, return skillet to medium-high heat and ad remaining sesame oil. Add rice, press into an even layer, and cook until bottom begins to crackle and brown, 5-7 min, do not stir.). Serve and top with aioli, scallion, and sesame seeds. ',
        'photo': '/static/images/autumn-bibimbap.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian', "Asian"],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Tofu Halloumi',
        'ingredients': [],
        'ingredients_subset': [],
        'directions': '',
        'photo': '/static/images/tofu-halloumi.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Buffalo Cauliflower Salad',
        'ingredients': [],
        'ingredients_subset': [],
        'directions': '',
        'photo': '/static/images/buffalo-cauliflower-salad.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Eggplant Flatbreads',
        'ingredients': [],
        'ingredients_subset': [],
        'directions': '',
        'photo': '/static/images/eggplant-flatbreads.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Sweet Potato Black Bean Tacos',
        'ingredients': [],
        'ingredients_subset': [],
        'directions': '',
        'photo': '/static/images/sweet-potato-black-bean-tacos.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Jeweled Biryani',
        'ingredients': [],
        'ingredients_subset': [],
        'directions': '',
        'photo': '/static/images/jeweled-biryani.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Five-spice Tofu Stir-fry',
        'ingredients': [],
        'ingredients_subset': [],
        'directions': '',
        'photo': '/static/images/five-spice-tofu-stir-fry.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Italian Cannellini Bean Stew',
        'ingredients': [],
        'ingredients_subset': [],
        'directions': '',
        'photo': '/static/images/italian-cannellini-bean-stew.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Nicoise Salad',
        'ingredients': [],
        'ingredients_subset': [],
        'directions': '',
        'photo': '/static/images/nicoise-salad.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Corn Crab Dumplings',
        'ingredients': [],
        'ingredients_subset': [],
        'directions': '',
        'photo': '/static/images/corn-crab-dumplings.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Tomato-braised Artichokes',
        'ingredients': [],
        'ingredients_subset': [],
        'directions': '',
        'photo': '/static/images/tomato-braised-artichokes.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Crispy Buckwheat Bowl',
        'ingredients': [],
        'ingredients_subset': [],
        'directions': '',
        'photo': '/static/images/crispy-buckwheat-bowl.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Beef Bulgogi Bowl',
        'ingredients': [],
        'ingredients_subset': [],
        'directions': '',
        'photo': '/static/images/beef-bulgogi-bowls.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Israeli Stuffed Peppers',
        'ingredients': [],
        'ingredients_subset': [],
        'directions': '',
        'photo': '/static/images/israeli-stuffed-peppers.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Watermelon Poke Bowls',
        'ingredients': [],
        'ingredients_subset': [],
        'directions': '',
        'photo': '/static/images/watermelon-poke-bowls.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Chicken Sausage Spinach Ricotta Ravioli',
        'ingredients': [],
        'ingredients_subset': [],
        'directions': '',
        'photo': '/static/images/chicken-sausage-spinach-ricotta-ravioli.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },


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
