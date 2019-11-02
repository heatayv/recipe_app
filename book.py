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
        'name': 'za\'atarChicken',
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
        'tags': ['Heather', 'Entree', 'Favorite', 'Easy'],
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
        'tags': ['Heather', 'Entree', 'Vegetarian', 'Asian', 'Favorite'],
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
        'ingredients': ['1 clove garlic', '2 tbsp red wine vinegar', '1 tbsp agave', '8 oz watermelon', 'fresh mint', '1 zucchini', '1 package Wildwood tofu', '2 tbsp zaatar', '2 tbsp nutritional yeast', '2 tbsp almonds'],
        'ingredients_subset': [],
        'directions': 'Prep marinade (mince garlic, add red wine vingar and agave. Whisk well to combine and gradually add 3 tbsp olive oil.). Marinate watermelon (slice watermelon, roughly chop mint, add to marinade with salt and coat the watermelon). Prep Zucchini (cut into thirds and then slice into 1/2 inch planks the long way). Prepare the halloumi (drain tofu and slice length-wise into 6 pieces. Combine zaatar, yeast, salt, and pepper and coat the tofu.). Char the zucchini (heat a skillet over medium heat, toast almonds for 3-4 min, increase heat to high and add oil. Add sliced zucchini and cook 2-3 min, add salt and pepper.). Sear the halloumi (return skillet to medium-high heat, add oil, add tofu, cook 3-4 min per side. Serve topped with watermelon mint salad and toasted almonds.',
        'photo': '/static/images/tofu-halloumi.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Buffalo Cauliflower Salad',
        'ingredients': ['1/2 cup faro', '1/2 cup hot sauce', '3 tbsp butter', '1 tsp garlic powder', '6 oz cauliflower florets', '1 head green leaf lettuce', '4 oz heirloom cherry tomatoes', '1 carrot', '1 celery stalk', '1/4 cup ranch'],
        'ingredients_subset': [],
        'directions': 'Preheat oven to 425 degrees F. Cook farro (with water 1 inch above farro, for 18-20 min). Make sauce (combine hot sauce, butter, garlic powder, salt in saucepan over medium heat. Whisk until butter melted, remove from heat.). Bake cauliflower (cut cauliflower into bite-sized pieces, coat with buffalo sauce, bake 15-18 min. Reserve extra sauce.). Make salad (roughly chop lettuce, quarter tomatoes, shred carrot on thickest setting, slice celery. Toss with 1/2 ranch.). Serve and drizzle with remaining buffalo sauce and ranch. ',
        'photo': '/static/images/buffalo-cauliflower-salad.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Salad', 'Vegetarian', 'Mediterranean'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Eggplant Flatbreads',
        'ingredients': ['1 eggplant', '1/2 cup bulgur wheat', '1 celery stalk', '4 oz heirloom cherry tomoatoes', '1 shallot', 'fresh parsley', '2 tsp za\'atar', '2 tbsp + 2 tsp champagne vinegar', '3 tbsp tahini', '2 tbsp mango chutney', '2 whole wheat pitas'],
        'ingredients_subset': [],
        'directions': 'Make bulgur (boil 1 1/4 cups water, pour 3/4 cups into bowl with bulgur, cover and sit 18-20 min). Prepare produce (dice celery, quarter tomoatoes, mince shallot, roughly chop parsley). Broil eggplant Prep eggplant (set oven to broil on high, cut eggplant into 1 inch thick rounds, place on baking sheet, add oil, za\'atar, and salt. Broil 5-8 min on each side.). Toss celery tabbouleh (add celery, tomatoes, shallot, and parsley to finished bulgar. Add 2 tbsp champagne vinegar, 2 tbsp olive oil, salt, and pepper.). Make the mango tahini amba (combine and stir remaining vinegar, tahini, mango chutney, and salt). Warm pitas in foil in oven, 2-4 min. Serve with everything in the pita, with any extra tabbouleh and mango tahini amba on the side.',
        'photo': '/static/images/eggplant-flatbreads.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Sweet Potato Black Bean Tacos',
        'ingredients': ['1 sweet potato', '1 peach', '1/2 cup kimchi', '1 scallion', '1 can black beans', '1 lime', '1/4 cup mayo', '6 tortillas', '2 oz green cabbage', '1 lemon'],
        'ingredients_subset': [],
        'directions': 'Roast sweet potato (preheat oven to 450 degrees F. Dice sweet potato (no need to peel), add to baking sheet with 2 tsp oil, salt, and pepper. Roast 10-15 min.). Mix the kimchi (thinly slice peach, roughly chop kimchi, combine). Prep aioli (combine and mix lime zest, 1/2 lemon juice, mayo, and salt). Cook black beans (heat skillet over medium-high heat, add black beans and 1/2 cup water, cook 2-3 min. Mash about half of them, cook 2-3 more min and salt.). Crisp tortillas in oil over medium-high heat. Fill tacos with sweet potato and black beans, top with peach kimchi, sliced scallion, green cabbage, and aioli.',
        'photo': '/static/images/sweet-potato-black-bean-tacos.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Mexican'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Jeweled Biryani',
        'ingredients': ['1/2 cup green lentils', '1/2 cup jasmine rice', '6 oz butternut squash', '2 tsp curry powder', '1 cucumber', '2 tsp lemon juice', '2 scallions', 'fresh mint', '1.5 oz dried apricots', '2 tsp coconut oil', '1/4 cup golden raisins', '1/4 cup cashews'],
        'ingredients_subset': [],
        'directions': 'Preheat oven to 425 degrees F. Cook lentis with 2 1/2 cups water for 12 min, add in jasmine rice and cook 10-12 more min. Cube the butternut squash, toss with curry powder, 2 tbsp oil, salt, and pepper, and spread on baking sheet. Roast 15-18 min. Thinly slice cucumbers and let sit in 1/2 lemon juice, 1 tsp olive oil, and salt. Prep (thinly slice scallions, tear mint leaves, dice apricots). Heat coconut oil over medium-low heat and cook apricots, raisins, and cashews for 3-4 min. Add finished rice & lentils to skillet, add 1/2 scallions, remaining lemon juice, and salt. Fold in squash. Serve and top with mint and remaining scallions, with cucumbers on the side. ',
        'photo': '/static/images/jeweled-biryani.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Asian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Five-spice Tofu Stir-fry',
        'ingredients': ['1 package tofu', '1/2 tsp Chinese five-spice', '2 cloves garlic', '1 red bell pepper', '6 oz bok choy', '1 tbsp gochujang', '2 tbsp apricot preserves', '6 oz soba noodles', '1 tbsp sesame oil', '1 tbsp sesame seeds'],
        'ingredients_subset': [],
        'directions': 'Boil water for noodles. Drain, dry, and cut tofu into 1 inch cubes. Heat oil over medium-high heat, add tofu, Chinese five-spice, and salt. Cook 4-5 min. Prep vegetables (mince garlic, slice red bell pepper, chop bok choy). Make the sauce (whisk gochujang, apricot preserves, and 2 tbsp water). Cook noodles (for 4-5 min, drain, run under cold water, and toss with 1 tsp sesame oil). Saute vegetables (heat remaining sesame oil over medium-high heat, add bok choy, salt, pepper and cook 1-2 min. Add garlic, bell pepper, and sesame seeds, cook 1 min. Add tofu, chile-apricot sauce, cook 1-2 min. Serve stir-fry on top of noodles.',
        'photo': '/static/images/five-spice-tofu-stir-fry.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian', 'Asian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Italian Cannellini Bean Stew',
        'ingredients': ['1 carrot', '1 onion', '1 celery stalk', '2 cloves garlic', '1 lemon', '6 oz sausage', '1 can cannellini beans', '1 tsp Herbs de Provence', '2 tbsp tomato paste', '2 packets vegetable broth concentrate', '4 oz mustard greens', '2 tsp parmesan'],
        'ingredients_subset': [],
        'directions': 'Prep vegetables (slice carrots into thin rounds, chop onion, chop celery, mince garlic, halve lemon). Cook the sausage (slice into rounds, heat oil over medium-high heat in a big pot, cook 3-5 min). Begin the stew (return pot to medium-high heat, add carrots, onions, celery, garlic, and cook 3-5 min. Add cannellini beans, Herbs de Provence, tomato paste, vegetable broth concentrate, and 2 cups water. Bring to a boil then reduce heat to a simmer. Remove mustard green stems, chop leaves, add to pot and simmer 3-5 more min. Add 1/2 lemon juice. Season stew with salt and pepper and top with sausage, parmesan, and lemon wedges.',
        'photo': '/static/images/italian-cannellini-bean-stew.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Soup', 'Italian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Black Bean Burgers',
        'ingredients': ['1 sweet potato', '1 can black beans', '1 can black beans', '1 clove garlic', '1 1/2 tsp cumin', '1 tbsp Worcestershire powder', '1 tbsp flaxseed meal', '2 tbsp garbanzo bean flour', '2 tsp Aleppo pepper flakes','2 tbsp mayo', '2 tsp ketchup', '2 buns', '2 oz pickles', '2 lettuce leaves'],
        'ingredients_subset': [],
        'directions': 'Preheat oven to 425 degrees F. Bake the fries (cut sweet potato into wedges, transfer to baking sheet and toss with oil, salt, and pepper, bake for 18-22 min). Blend the burger mix (Add black beans, garlic, cumin, Worcestershire powder, flaxseed meal, garbanzo bean flour, Aleppo pepper flakes, and salt to a blender. Pulse a few times until combined, form into 2 patties and chill in fridge.). Mix the sauce (combine mayo, ketchup, and salt). Sear the burgers (heat oil over medium-high heat, add burgers and cook 3-5 min each side). Serve and top with pickles, lettuce, and sauce.',
        'photo': '/static/images/black-bean-burgers.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Nicoise Salad',
        'ingredients': ['3/4 cup French lentils', '8 oz new potatoes', '1 clove garlic', '6 oz green beens', '1 cucumber', '1 tbsp French mustard herb blend', '4 oz heirloom cherry tomatoes', '1 tbsp lemon juice', 'French tarragon', '2 oz baby spinach', '1/4 cup walnuts', '1/4 cup kalamata olives'],
        'ingredients_subset': [],
        'directions': 'Preheat oven to 425 degrees F. Prepare lentils (with 2 cups water for 18-20 min, season with salt and pepper). Boil 1 inch of water for green beans. Prepare vegetables (quarter potatoes, thinly slice garlic and cucumber, trim green beans). Roast potatoes (add to baking sheet and toss with French mustard herb blend, oil, salt, pepper, and roast for 18-22 min). Steam green beans for 1 min in the boiling water, drain and rinse with cold water. Cook tomatoes (heat oil over medium heat, add garlic and cook 30 seconds, add tomatoes and salt, cook 4-6 min). Prepare vinaigrette (Remove and roughly chop garlic and tomatoes, combine in a bowl with tarragon leaves, 1 tbsp olive oil, lemon juice, salt, and pepper. Serve and top with walnuts and olives.',
        'photo': '/static/images/nicoise-salad.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Salad', 'Vegetarian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Corn Crab Dumplings',
        'ingredients': ['1/2 cup black rice', '2 tsp fresh ginger', '3 scallions', '1 ear corn', '1/2 cup hearts of palm', '1 tbsp cream cheese', '1 1/2 tsp Old Bay Seasoning', '2 tsp Sriracha', '14 wonton wrappers', '1 tbsp sesame oil', '2 tsp tamari', '1/4 cup sweet chili sauce'],
        'ingredients_subset': [],
        'directions': 'Cook black rice (with 1 cup water for 30-35 min). Prepare produce (mince ginger, thinly slice scallions, cut off corn kernels, drain hearts of palm). Make dumpling mix (combine cream cheese, Old Bay Seasoning, and Sriracha, 1/4 cup scallion, corn, and hearts of palm, and salt.) Fill the wonton wrappers with dumpling mix. Sear the dumplings (heat oil over medium heat, add dumplings and cook until browned and crispy, 2-3 min. Flip and cook additional min. Add 1/3 cup water, reduce heat to medium, and cover. Steam 3-4 min.). Wipe skillet, heat sesame oil over medium-high heat, add ginger and cook for 30 seconds. Add cooked rice, remaining scallions, tamari, and salt. Cool 1-2 min. Serve with sweet chili sauce for dipping. ',
        'photo': '/static/images/corn-crab-dumplings.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian', 'Asian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Tomato-braised Artichokes',
        'ingredients': ['3/4 cup quinoa', '1 shallot', '3 cloves garlic', '1/4 cup cured black olives', '8 oz artichoke hearts', '1 can crushed tomatoes', '1 cucumber', 'fresh dill', '1 tbsp lemon juice', '1 tbsp white vinegar', '1/4 cup mayo'],
        'ingredients_subset': [],
        'directions': 'Cook the quinoa (with 1 1/4 cup water for 12-15 min). Prepare vegetables (mince shallot and garlic, remove olive pits and roughly chop, drain artichokes). Begin to braise (heat oil over medium-high heat, add shallot and garlic and cook for 1 min. Add artichokes, crushed tomatoes, 1 cup of water, bring to a boil and simmer until it thickens). Prepare the sauce (grate cucumber on large setting into a bowl and mix with finely chopped dill, lemon juice, white vinegar, mayo, and salt). Serve topped with cucumer dill sauce and olives. ',
        'photo': '/static/images/tomato-braised-artichokes.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Crispy Buckwheat Bowl',
        'ingredients': ['1 cup buckwheat groats', '6 oz broccolini', '4 radishes', '4 oz snap peas', '1 lemon', '1/2 cup black-eyed peas', '1/4 cup pecans', '1 scallion', '2 tbsp cilantro chutney'],
        'ingredients_subset': [],
        'directions': 'Cook the buckwheat (in 2 cups of water for 8-10 min). Prepare vegetables (trim broccolini stems, thinly slice radishes, cut snap peas in half diagonally). Marinate vegetables (In a bowl combine radishes, snap peas, black-eyed peas, 1/2 lemon juice, 1 tbsp olive oil, salt, and pepper). Prepare pesto (finely chop pecans, thinly slice scallion. In a bowl combine pecans, scallion, cilantro chutney, 2 tsp lemon juice, 1 tsp olive oil, and salt). Crisp the buckwheat (heat oil over medium-high heat, add cooked buckwheat and cook 3-5 min, stir, cook 2 more min and season with salt and lemon. Add broccolini with 1/4 cup water and cook 3-5 min.). Serve bowls topped with marinated vegetables and cilantro pesto.)) ',
        'photo': '/static/images/crispy-buckwheat-bowl.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Lunch' 'Vegetarian'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Beef Bulgogi Bowl',
        'ingredients': ['1/2 cup jasmine rice', '2 scallions', '5 tsp white wine vinegar', '1 cucumber', '4 oz shredded carrots', '10 oz ground beef', '1 tbsp sesame seeds', '4 oz bulgogi sauce', '4 tbsp sour cream', '1 tsp sriracha' ],
        'ingredients_subset': [],
        'directions': 'Cook rice (with 3/4 cup water for 15 min). Thinly slice scallions, separating whites from greens. Pickle cucumber (shave cucumber length-wise into thick ribbons, rotating until you get to the seedy core and then discard. Toss in a bowl with 1/2 vinegar, 1/2 tsp sugar, and salt. Drain before adding to bowls at the end.). Cook carrots (heat oil over medium-high heat, add shredded carrots, salt, and pepper and cook for 1 min). Cook beef (heat more oil over medium-high heat, add scallion whites and cook 30 seconds. Add beef, salt, and pepper and cook 5-7 min. Add 1/2 sesame seeds and remaining vinegar, cook for 30 seconds. Add bulgogi sauce and bring to simmer, add more salt and pepper.). Make sriracha cream (in a bowl, combine sour cream, sriracha, salt, and 1 tsp of water at a time until mixture is a drizzlying consistency). Mix in 1 tbsp butter, salt, and pepper to rice. Combine everything into bowls, top with scallion greens and remaining sesame seeds.',
        'photo': '/static/images/beef-bulgogi-bowls.jpg',
        'tags': ['Heather', 'Entree', 'Bowl', 'Asian',],
        'formatted_tags': '',
        'source_name':'Hello Fresh',
        'source': ''
    },
    {
        'name': 'Israeli Stuffed Peppers',
        'ingredients': ['3/4 cup saffron rice', '1 beef bouillon cube', '1 carrot', '1 onion', '3 cloves garlic', '2 Anaheim peppers', '1/4 cup almonds', '1 1/4 tsp Israeli spice blend', '2 tbsp dried cherries', '4 oz baby spinach'],
        'ingredients_subset': [],
        'directions': 'Preheat oven to 425 degrees F. Cook rice (with 1 1/4 cups water for 15-20 min). Prep (dissolve bouillon cube in 1/2 cup hot water, dice carrot and onion, thinly slice garlic, butterfly the peppers). Make the filling (heat oil over medium-high heat, add carrot, onion, 1/2 garlic, salt, and cook 5-6 min. Increase heat to high, add oil and bouillon broth, cook 4-6 more min. Add almonds, Israeli spice blend, and dried cherries and cook 2-3 min.). Stuff the peppers and roast in oven 8-10 min. Saute spinach (heat oil over high heat, add remaining garlic, baby spinach, salt, pepper, and cook 2-3 min). Serve peppers over rice with spinach on side. ) ',
        'photo': '/static/images/israeli-stuffed-peppers.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian', 'Favorite'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Watermelon Poke Bowls',
        'ingredients': ['3/4 cup sushi rice', '2 radishes', '1 cucumber', '1 oz macademia nuts', '2 tsp sesame oil', '2 tbsp tamari', '1 tbsp rice vinegar', '1 avacado', '7 oz watermelon'],
        'ingredients_subset': [],
        'directions': 'Cook rice (with 1 1/4 cups water for 12-15 min, let stand for 5). Prepare toppings (thinly slice radishes and cucumber, slice avacado, cut watermelon into small cubes, roughly chop macademia nuts). Make dressing (whisk sesame oil, tamari, rice vinegar, salt, and pepper). Serve in bowls. ',
        'photo': '/static/images/watermelon-poke-bowls.jpg',
        'tags': ['Heather', 'Purple Carrot', 'Entree', 'Vegetarian', 'Asian', 'Easy'],
        'formatted_tags': '',
        'source_name':'Purple Carrot',
        'source': ''
    },
    {
        'name': 'Chicken Sausage Spinach Ricotta Ravioli',
        'ingredients': ['2 scallions', '1 tomato', '1 lemon', '9 oz Italian sausage', '1 tbsp Italian seasoning', '9 oz spinach and ricotta ravioli', '1 package chicken stock concentrate', '4 tbsp sour cream'],
        'ingredients_subset': [],
        'directions': 'Boil water for pasta. Prep (slice scallions, dice tomato, wedge lemon). Cook sausage (heat oil over medium-high heat, add scallion whites, sausage, Italian seasoning, and cook for 3-5 min. Add tomato and cook 1-2 min, then turn off heat.). Cook ravioli (for 4-5 min and reserve 1/2 cup water). Turn sausage pan back on low heat and add stock concentrate, squeeze of lemon juice, splash of pasta water, and cook for 1-2 min. Add sour cream, 1 tbsp butter, salt, and pepper. Add more pasta water as needed until creamy consistency. Add ravioli, salt, pepper, and lemon juice. Serve and top with scallion greens and lemon wedges. ',
        'photo': '/static/images/chicken-sausage-spinach-ricotta-ravioli.jpg',
        'tags': ['Heather', 'Entree'],
        'formatted_tags': '',
        'source_name':'Hello Fresh',
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
