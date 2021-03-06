
train_data = [
	('you can use corn, or flour tortillas', ['O','O','O','B-PRODUCT','O','O','B-PRODUCT','L-PRODUCT']),
	('you can use corn, or flour tortillas', ['O','O','O','O','O','O','B-PRODUCT','L-PRODUCT']),
	('you can use corn, or flour tortillas', ['O','O','O','B-PRODUCT','O','O','O','L-PRODUCT']),
	('some people like whole grain, or wheat muffins', ['O','O','O','B-PRODUCT','I-PRODUCT','O','O','B-PRODUCT','L-PRODUCT']),
	('Seafood, poultry and vegetarian burgers are finding favor on grills across the country.', ['B-PRODUCT','O','O','O','O','L-PRODUCT','O','O','O','O','O','O','O','O','O']),
	('1/2 lemon, peeled',  [(4, 9, 'PRODUCT')]),
	('1/4" ginger, peeled',  [(5, 11, 'PRODUCT')]),
	('2 cups green tea',  [(7, 16, 'PRODUCT')]),
	('1 beet, chopped',  [(2, 6, 'PRODUCT')]),
	('3 medium apples, peeled and cored',  [(9, 15, 'PRODUCT')]),
	('1 cup almond milk',  [(6, 17, 'PRODUCT')]),
	('2 medium pears, cored and peeled',  [(9, 14, 'PRODUCT')]),
	('3 cups red grapes',  [(7, 17, 'PRODUCT')]),
	('1 cup watercress',  [(6, 16, 'PRODUCT')]),
	('1 cup ice',  [(6, 9, 'PRODUCT')]),
	('1 medium cucumber',  [(9, 17, 'PRODUCT')]),
	('1 cup ice',  [(6, 9, 'PRODUCT')]),
	('1 cup chopped iceberg lettuce',  [(14, 29, 'PRODUCT')]),
	('2 cups almond milk',  [(7, 18, 'PRODUCT')]),
	('1/2 cantaloupe, rind and seeds removed',  [(4, 14, 'PRODUCT')]),
	('1 celery stalk',  [(2, 8, 'PRODUCT')]),
	('1 tsp. organic maple syrup',  [(15, 26, 'PRODUCT')]),
	('1 celery stalk',  [(2, 8, 'PRODUCT')]),
	('2 cups plain coconut milk',  [(13, 25, 'PRODUCT')]),
	('2 large English cucumbers',  [(16, 25, 'PRODUCT')]),
	('2 medium green apples, peeled and cored',  [(15, 21, 'PRODUCT')]),
	('1/2 cup watercress',  [(8, 18, 'PRODUCT')]),
	('1 small white onion, small diced',  [(8, 19, 'PRODUCT')]),
	('2 large skinless, boneless chicken thighs',  [(18, 41, 'PRODUCT')]),
	('5 cups chicken broth',  [(7, 20, 'PRODUCT')]),
	('1 small carrot, peeled and small diced',  [(8, 14, 'PRODUCT')]),
	('1/4 tsp. black pepper',  [(9, 21, 'PRODUCT')]),
	('1 celery stalk, thinly sliced',  [(2, 8, 'PRODUCT')]),
	('1/2 tsp. salt',  [(9, 13, 'PRODUCT')]),
	('1 cup very small cooked pasta, such as stars or pastina',  [(24, 29, 'PRODUCT')]),
	('1/4 cup fresh chopped chives',  [(22, 28, 'PRODUCT')]),
	('1/2 tsp. salt',  [(9, 13, 'PRODUCT')]),
	('1 bay leaf',  [(2, 10, 'PRODUCT')]),
	('2 Idaho potatoes, peeled and cubed',  [(8, 16, 'PRODUCT')]),
	('4 strips bacon, finely chopped',  [(9, 14, 'PRODUCT')]),
	('1 tsp. fresh thyme leaves',  [(13, 18, 'PRODUCT')]),
	('1/2 cup clam juice',  [(8, 18, 'PRODUCT')]),
	('1 cup heavy cream',  [(6, 17, 'PRODUCT')]),
	('1/4 tsp. black pepper',  [(9, 21, 'PRODUCT')]),
	('1 lb. chunk cod fillet, about 11/2  thick, cut in half',  [(12, 15, 'PRODUCT')]),
	('1 large egg',  [(8, 11, 'PRODUCT')]),
	('1 medium banana',  [(9, 15, 'PRODUCT')]),
	('1 cup whole blueberries',  [(12, 23, 'PRODUCT')]),
	('1 Tbsp. cocoa powder',  [(8, 20, 'PRODUCT')]),
	('1/4 cup plus 1 Tbsp. molasses',  [(21, 29, 'PRODUCT')]),
	('1 cup rolled oats ',  [(13, 17, 'PRODUCT')]),
	('1 3/4 cups warm milk',  [(16, 20, 'PRODUCT')]),
	('34 cups bread flour',  [(8, 19, 'PRODUCT')]),
	('1 3/4 tsp. active dry yeast ',  [(22, 27, 'PRODUCT')]),
	('2 Tbsp. canola oil',  [(8, 18, 'PRODUCT')]),
	('1 Tbsp. hot water',  [(12, 17, 'PRODUCT')]),
	('1 cup whole wheat flour',  [(12, 23, 'PRODUCT')]),
	('1 1/2 tsp. kosher salt',  [(11, 22, 'PRODUCT')]),
	('1 cup rye flour',  [(6, 15, 'PRODUCT')]),
	('1/4 cup chopped parsley',  [(16, 23, 'PRODUCT')]),
	('6 cups vegetable or beef broth',  [(20, 30, 'PRODUCT')]),
	('2 large sweet onions, peeled and sliced',  [(8, 20, 'PRODUCT')]),
	('1/4 tsp. salt',  [(9, 13, 'PRODUCT')]),
	('1/4 tsp. black pepper',  [(9, 21, 'PRODUCT')]),
	('1 cup chopped cilantro',  [(14, 22, 'PRODUCT')]),
	('1 cup Valentina Mexican Chili Sauce',  [(24, 35, 'PRODUCT')]),
	('2 cups salsa',  [(7, 12, 'PRODUCT')]),
	('2 Tbsp. minced garlic',  [(15, 21, 'PRODUCT')]),
	('3 lbs. boneless, skinless chicken breast',  [(26, 40, 'PRODUCT')]),
	('1/2 tsp. salt',  [(9, 13, 'PRODUCT')]),
	('2 cups lettuce',  [(7, 14, 'PRODUCT')]),
	('3/4 cup cooked quinoa',  [(15, 21, 'PRODUCT')]),
	('1 large tomato, sliced',  [(8, 14, 'PRODUCT')]),
	('3/4 cup shredded carrots',  [(17, 24, 'PRODUCT')]),
	('1 can  black beans, drained and rinsed',  [(7, 18, 'PRODUCT')]),
	('1 medium avocado, peeled, pitted, and sliced',  [(9, 16, 'PRODUCT')]),
	('1/2 small red onion, peeled and sliced',  [(10, 19, 'PRODUCT')]),
	('1 Tbsp. olive oil',  [(8, 17, 'PRODUCT')]),
	('1 tsp. chili powder',  [(7, 19, 'PRODUCT')]),
	('1/4 cup canned Mexican-style tomatoes',  [(29, 37, 'PRODUCT')]),
	('1/2 cups cauliflower rice',  [(9, 25, 'PRODUCT')]),
	('2/3 cup kidney beans',  [(8, 20, 'PRODUCT')]),
	('1/4 cup chopped cilantro',  [(16, 24, 'PRODUCT')]),
	('1/4 cup canned corn, drained',  [(15, 19, 'PRODUCT')]),
	('1 Tbsp. taco seasoning mix',  [(8, 22, 'PRODUCT')]),
	('1/2 cup fresh cilantro, chopped',  [(14, 22, 'PRODUCT')]),
	('1 Tbsp. taco seasoning',  [(8, 22, 'PRODUCT')]),
	('2 tsp. extra-virgin olive oil',  [(20, 29, 'PRODUCT')]),
	('1 cup cooked lentils',  [(13, 20, 'PRODUCT')]),
	('4 leaves romaine lettuce',  [(9, 16, 'PRODUCT')]),
	('1/2 cup red onion, sliced thin',  [(8, 17, 'PRODUCT')]),
	('1 cup whole wheat flour',  [(12, 23, 'PRODUCT')]),
	('23 cups bread flour',  [(8, 19, 'PRODUCT')]),
	('1 Tbsp. white sesame seeds',  [(8, 26, 'PRODUCT')]),
	('1 cup warm milk',  [(11, 15, 'PRODUCT')]),
	('1 Tbsp. flax seeds',  [(8, 18, 'PRODUCT')]),
	('1 Tbsp. black sesame seeds',  [(8, 26, 'PRODUCT')]),
	('1 tsp. plus 1 pinch kosher salt',  [(20, 31, 'PRODUCT')]),
	('1 Tbsp. poppy seeds',  [(8, 19, 'PRODUCT')]),
	('1 egg',  [(2, 5, 'PRODUCT')]),
	('1 Tbsp. fennel seeds',  [(8, 20, 'PRODUCT')]),
	('1 Tbsp. cream',  [(8, 13, 'PRODUCT')]),
	('2 Tbsp. honey',  [(8, 13, 'PRODUCT')]),
	('1/4 cup  unsalted butter',  [(18, 24, 'PRODUCT')]),
	('1 3/4 tsp. active dry yeast ',  [(22, 27, 'PRODUCT')]),
	('23 cups bread flour',  [(8, 19, 'PRODUCT')]),
	('1 3/4 tsp. active dry yeast ',  [(22, 27, 'PRODUCT')]),
	('1/2 cup buttermilk',  [(8, 18, 'PRODUCT')]),
	('1 cup 7-grain cereal',  [(14, 20, 'PRODUCT')]),
	('1 cup warm water',  [(11, 16, 'PRODUCT')]),
	('1 cup whole wheat flour',  [(12, 23, 'PRODUCT')]),
	('1 1/2 tsp. kosher salt',  [(11, 22, 'PRODUCT')]),
	('1 Tbsp. olive oil',  [(8, 17, 'PRODUCT')]),
	('2 eggs',  [(2, 6, 'PRODUCT')]),
	('2 Tbsp. cornmeal',  [(8, 16, 'PRODUCT')]),
	('1 Tbsp. honey',  [(8, 13, 'PRODUCT')]),
	('1/2 cup vanilla almond milk',  [(8, 27, 'PRODUCT')]),
	('1 cup iceberg lettuce',  [(6, 21, 'PRODUCT')]),
	('1 banana, peeled',  [(2, 8, 'PRODUCT')]),
	('1 pint blueberries',  [(7, 18, 'PRODUCT')]),
	('1 pint strawberries',  [(7, 19, 'PRODUCT')]),
	('1/2 cup ice cubes',  [(8, 17, 'PRODUCT')]),
	('1 banana, peeled',  [(2, 8, 'PRODUCT')]),
	('1 pint raspberries',  [(7, 18, 'PRODUCT')]),
	('1 cup vanilla soymilk',  [(6, 21, 'PRODUCT')]),
	('2 cups mixed baby greens',  [(13, 24, 'PRODUCT')]),
	('1 pint blueberries',  [(7, 18, 'PRODUCT')]),
	('2 cups purified water',  [(16, 21, 'PRODUCT')]),
	('1/2 cantaloupe, rind and seeds removed',  [(4, 14, 'PRODUCT')]),
	('1 medium pear, cored',  [(9, 13, 'PRODUCT')]),
	('1 banana, peeled',  [(2, 8, 'PRODUCT')]),
	('1 medium cucumber, peeled',  [(9, 17, 'PRODUCT')]),
	('1 box  spice cake mix',  [(7, 21, 'PRODUCT')]),
	('3 medium apples, cored, peeled, and chopped',  [(9, 15, 'PRODUCT')]),
	('1/2 cup cold water',  [(13, 18, 'PRODUCT')]),
	('1/2 cup vegetable oil',  [(8, 21, 'PRODUCT')]),
	('1 box  butterscotch instant pudding mix',  [(7, 39, 'PRODUCT')]),
	('4 eggs',  [(2, 6, 'PRODUCT')]),
	('1 cup dried cranberries',  [(12, 23, 'PRODUCT')]),
	('2 cups purified water',  [(16, 21, 'PRODUCT')]),
	('1 cup romaine lettuce',  [(6, 21, 'PRODUCT')]),
	('1/8 cup ground flaxseed',  [(8, 23, 'PRODUCT')]),
	('1/4 cup walnuts',  [(8, 15, 'PRODUCT')]),
	('2 bananas, peeled',  [(2, 9, 'PRODUCT')]),
	('1/4 cup almonds',  [(8, 15, 'PRODUCT')]),
	('1 can  stewed tomatoes',  [(7, 22, 'PRODUCT')]),
	('1/2 tsp. black pepper',  [(9, 21, 'PRODUCT')]),
	('1 lb. frozen shoestring potatoes, cooked',  [(6, 32, 'PRODUCT')]),
	('1/4 tsp. onion powder',  [(9, 21, 'PRODUCT')]),
	('1/2 tsp. garlic powder',  [(9, 22, 'PRODUCT')]),
	('1 lb. cod fillets',  [(6, 17, 'PRODUCT')]),
	('1/8 tsp. sugar',  [(9, 14, 'PRODUCT')]),
	('1 tsp. salt',  [(7, 11, 'PRODUCT')]),
	('1 cup baby arugula',  [(6, 18, 'PRODUCT')]),
	('1 cup unbleached all-purpose flour',  [(29, 34, 'PRODUCT')]),
	('3 Tbsp. canola oil',  [(8, 18, 'PRODUCT')]),
	('1 Tbsp. pure vanilla extract',  [(13, 28, 'PRODUCT')]),
	('1/4 cup nondairy milk',  [(8, 21, 'PRODUCT')]),
	('1/4 cup white whole-wheat flour',  [(14, 31, 'PRODUCT')]),
	('1 1/2 tsp. sodium-free baking powder',  [(23, 36, 'PRODUCT')]),
	('2 medium carrots, shredded',  [(9, 16, 'PRODUCT')]),
	('2 medium apples, chopped',  [(9, 15, 'PRODUCT')]),
	('1 ripe medium banana, mashed',  [(14, 20, 'PRODUCT')]),
	('1/4 cup brown sugar',  [(8, 19, 'PRODUCT')]),
	('1/2 cup low-fat milk',  [(16, 20, 'PRODUCT')]),
	('1 egg',  [(2, 5, 'PRODUCT')]),
	('1 cup finely chopped, skinless apples',  [(31, 37, 'PRODUCT')]),
	('1 1/4 tsp. cinnamon, divided',  [(11, 19, 'PRODUCT')]),
	('3/4 cup, plus 1 Tbsp. sugar, divided',  [(22, 27, 'PRODUCT')]),
	('1 tsp. vanilla',  [(7, 14, 'PRODUCT')]),
	('1 tsp. baking soda',  [(7, 18, 'PRODUCT')]),
	('2 1/2 cups all-purpose flour',  [(23, 28, 'PRODUCT')]),
	('1/2 cup canola oil',  [(8, 18, 'PRODUCT')]),
	('1/4 tsp. salt',  [(9, 13, 'PRODUCT')]),
	('1/2 tsp. stevia',  [(9, 15, 'PRODUCT')]),
	('1 tsp. white chia seeds',  [(13, 23, 'PRODUCT')]),
	('1/8 cup raspberries',  [(8, 19, 'PRODUCT')]),
	('1/22/3 cup coconut water',  [(11, 24, 'PRODUCT')]),
	('1/2 small passion fruit',  [(18, 23, 'PRODUCT')]),
	('1/2 Tbsp. coconut flakes',  [(10, 24, 'PRODUCT')]),
	('1/8 cup blackberries',  [(8, 20, 'PRODUCT')]),
	('1 Tbsp. pomegranate seeds',  [(8, 25, 'PRODUCT')]),
	('1 tsp. sunflower seeds',  [(7, 22, 'PRODUCT')]),
	('1/2 Tbsp. chopped pistachios',  [(18, 28, 'PRODUCT')]),
	('1/2 small kiwi, sliced',  [(10, 14, 'PRODUCT')]),
	('1/2 medium ripe avocado, pitted and peeled',  [(16, 23, 'PRODUCT')]),
	('1 Tbsp. ground flaxseed',  [(8, 23, 'PRODUCT')]),
	('1 Tbsp. acai powder',  [(8, 19, 'PRODUCT')]),
	('1 Tbsp. ground chia seeds',  [(15, 25, 'PRODUCT')]),
	('1 Tbsp. sliced almonds',  [(15, 22, 'PRODUCT')]),
	('2 Tbsp. hemp hearts',  [(8, 19, 'PRODUCT')]),
	('1 1/2 cups frozen blueberries',  [(18, 29, 'PRODUCT')]),
	('2 Tbsp. olive oil',  [(8, 17, 'PRODUCT')]),
	('1 1/2 cups durum wheat  flour',  [(17, 29, 'PRODUCT')]),
	('1 Tbsp. water',  [(8, 13, 'PRODUCT')]),
	('2 large eggs',  [(8, 12, 'PRODUCT')]),
	('1/4 cup fresh-grated Parmesan cheese',  [(21, 36, 'PRODUCT')]),
	('1/2 tsp. ground cinnamon',  [(16, 24, 'PRODUCT')]),
	('1/2 cup unsweetened coconut milk',  [(20, 32, 'PRODUCT')]),
	('1/4 tsp. ground black pepper',  [(16, 28, 'PRODUCT')]),
	('1 Tbsp. lemon juice',  [(8, 19, 'PRODUCT')]),
	('1/2 cup chopped onion',  [(16, 21, 'PRODUCT')]),
	('1/4 tsp. ground cumin',  [(16, 21, 'PRODUCT')]),
	('2 medium sized acorn squash, peeled and cut into cubes',  [(21, 27, 'PRODUCT')]),
	('1/4 tsp. ground coriander',  [(16, 25, 'PRODUCT')]),
	('These less conventional grinds provide a great canvas for experimenting with exciting toppings, from fresh summer produce to creative homemade condiments.', [(143, 153, 'PRODUCT')]),
	('Spread on smoky chipotle ketchup (made by mixing 1 cup ketchup with chopped chipotle chiles in adobo, to taste).', [(16, 32, 'PRODUCT'), (55, 62, 'PRODUCT'), (76, 91, 'PRODUCT'), (95, 100, 'PRODUCT')]),
	('1 cup shredded Monterey jack cheese', [(15, 35, 'PRODUCT')]),
	('Then top with tomato and sliced jalapenos.', [(14, 20, 'PRODUCT')]),
	('Then top with tomato and sliced jalapenos.', [(32, 41, 'PRODUCT')]),
	(' Play up the taco flavor with fresh pico de gallo, cotija cheese, thinly sliced radishes and shredded iceberg lettuce.', [(13, 17, 'PRODUCT')]),
	(' Play up the taco flavor with fresh pico de gallo, cotija cheese, thinly sliced radishes and shredded iceberg lettuce.', [(36, 49, 'PRODUCT')]),
	(' Play up the taco flavor with fresh pico de gallo, cotija cheese, thinly sliced radishes and shredded iceberg lettuce.', [(51, 64, 'PRODUCT')]),
	(' Play up the taco flavor with fresh pico de gallo, cotija cheese, thinly sliced radishes and shredded iceberg lettuce.', [(80, 88, 'PRODUCT')]),
	(' Play up the taco flavor with fresh pico de gallo, cotija cheese, thinly sliced radishes and shredded iceberg lettuce.', [(102, 117, 'PRODUCT')]),
	('Reserve 1 Tbsp. liquid from chickpeas.', [(28, 37, 'PRODUCT')]),
	('Process oats in food processor until powdery.', [(8, 12, 'PRODUCT')]),
	('Add parsley through cumin; pulse until roughly chopped.', [(4, 11, 'PRODUCT')]),
	('Add parsley through cumin; pulse until roughly chopped.', [(20, 25, 'PRODUCT')]),
	('Add chickpeas, lemon juice, and reserved 1 Tbsp. liquid; pulse until chickpeas are finely ground.', [(4, 13, 'PRODUCT')]),
	('Add chickpeas, lemon juice, and reserved 1 Tbsp. liquid; pulse until chickpeas are finely ground.', [(15, 26, 'PRODUCT')]),
	('Serve on toasted buns with desired toppings, refrigerating any leftovers.', [(17, 21, 'PRODUCT')]),
	('Create a creamy yogurt-cucumber sauce by mixing together 1 cup plain yogurt, 1/2 seeded, peeled cucumber (finely diced), a minced garlic clove, a little lemon zest and a pinch of cayenne pepper.', [(69, 75, 'PRODUCT')]),
	('Create a creamy yogurt-cucumber sauce by mixing together 1 cup plain yogurt, 1/2 seeded, peeled cucumber (finely diced), a minced garlic clove, a little lemon zest and a pinch of cayenne pepper.', [(94, 102, 'PRODUCT')]),
	('Create a creamy yogurt-cucumber sauce by mixing together 1 cup plain yogurt, 1/2 seeded, peeled cucumber (finely diced), a minced garlic clove, a little lemon zest and a pinch of cayenne pepper.', [(128, 134, 'PRODUCT')]),
	('Create a creamy yogurt-cucumber sauce by mixing together 1 cup plain yogurt, 1/2 seeded, peeled cucumber (finely diced), a minced garlic clove, a little lemon zest and a pinch of cayenne pepper.', [(151, 156, 'PRODUCT')]),
	('Create a creamy yogurt-cucumber sauce by mixing together 1 cup plain yogurt, 1/2 seeded, peeled cucumber (finely diced), a minced garlic clove, a little lemon zest and a pinch of cayenne pepper.', [(177, 191, 'PRODUCT')]),
	('Keep things fresh and simple with slices of ripe avocado and juicy, golden heirloom tomatoes.', [(49, 56, 'PRODUCT')]),
	('Keep things fresh and simple with slices of ripe avocado and juicy, golden heirloom tomatoes.', [(75, 92, 'PRODUCT')]),
	('The addition of fresh herbs and garlic dials up the flavor of lean ground turkey.', [(16, 27, 'PRODUCT')]),
	('The addition of fresh herbs and garlic dials up the flavor of lean ground turkey.', [(32, 38, 'PRODUCT')]),
	('The addition of fresh herbs and garlic dials up the flavor of lean ground turkey.', [(67, 80, 'PRODUCT')]),
	('Mix together olive oil, ground turkey, herbs, garlic, salt and pepper.', [(13, 22, 'PRODUCT')]),
	('Mix together olive oil, ground turkey, herbs, garlic, salt and pepper.', [(24, 37, 'PRODUCT')]),
	('Mix together olive oil, ground turkey, herbs, garlic, salt and pepper.', [(39, 44, 'PRODUCT')]),
	('Mix together olive oil, ground turkey, herbs, garlic, salt and pepper.', [(46, 52, 'PRODUCT')]),
	('Mix together olive oil, ground turkey, herbs, garlic, salt and pepper.', [(54, 58, 'PRODUCT')]),
	('Mix together olive oil, ground turkey, herbs, garlic, salt and pepper.', [(63, 69, 'PRODUCT')]),
	('Lightly brush the grill grates with vegetable oil, then grill the patties about 5 minutes.', [(36, 49, 'PRODUCT')]),
	('Top with a smear of olive oil mayo.', [(20, 34, 'PRODUCT')]),
	('Then add a sweet and savory topping made by sauteing 1 diced Granny Smith apple and a thinly sliced Vidalia onion in 2 tsp. olive oil until softened and caramelized.', [(61, 79, 'PRODUCT')]),
	('Then add a sweet and savory topping made by sauteing 1 diced Granny Smith apple and a thinly sliced Vidalia onion in 2 tsp. olive oil until softened and caramelized.', [(100, 113, 'PRODUCT')]),
	('Then add a sweet and savory topping made by sauteing 1 diced Granny Smith apple and a thinly sliced Vidalia onion in 2 tsp. olive oil until softened and caramelized.', [(124, 133, 'PRODUCT')]),
	('For an Italian twist, top with a slice of mozzarella cheese, sauteed slices of bell pepper and warm marinara sauce.', [(42, 59, 'PRODUCT')]),
	('For an Italian twist, top with a slice of mozzarella cheese, sauteed slices of bell pepper and warm marinara sauce.', [(79, 90, 'PRODUCT')]),
	('For an Italian twist, top with a slice of mozzarella cheese, sauteed slices of bell pepper and warm marinara sauce.', [(100, 114, 'PRODUCT')]),
	('Plain kombucha is fizzy with a subtle sweetness and a taste that is a bit like tart green apples mixed with sour stone fruits.', [(6, 14, 'PRODUCT')]),
	('Plain kombucha is fizzy with a subtle sweetness and a taste that is a bit like tart green apples mixed with sour stone fruits.', [(83, 95, 'PRODUCT')]),
	('Plain kombucha is fizzy with a subtle sweetness and a taste that is a bit like tart green apples mixed with sour stone fruits.', [(112, 124, 'PRODUCT')]),
	('It can be made with black or green tea and flavored with a variety of fruits and spices.', ['O','O','O','O','O','B-PRODUCT','O','B-PRODUCT','L-PRODUCT','O','O','O','O','O','O','O','O','O','O']),
	('Whether you are julienning basil to top crisp crostini or chopping cilantro to mix into guacamole, it can be tough to get herbs to stay put.', [(26, 31, 'PRODUCT')]),
	('Whether you are julienning basil to top crisp crostini or chopping cilantro to mix into guacamole, it can be tough to get herbs to stay put.', [(66, 74, 'PRODUCT')]),
	('Whether you are julienning basil to top crisp crostini or chopping cilantro to mix into guacamole, it can be tough to get herbs to stay put.', [(87, 96, 'PRODUCT')]),
	('Whether you are julienning basil to top crisp crostini or chopping cilantro to mix into guacamole, it can be tough to get herbs to stay put.', [(121, 126, 'PRODUCT')])
]

train_data2 = train_data[0:99]
train_data3 = train_data[0:49]
train_data4 = train_data[0:4]
train_data5 = []


