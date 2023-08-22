-- Insert data into Category table
use recipe;
show tables;
INSERT IGNORE  INTO recipe_category (title, img, active)
VALUES
    ('Main Course', 'category/main-course.jpg', 1),
    ('Desserts', 'category/desserts.jpg', 1),
    ('Appetizers', 'category/appetizers.jpg', 1),
    ('Salads', 'category/salads.jpg', 1),
    ('Beverages', 'category/beverages.jpg', 1),
    ('Breakfast', 'category/breakfast.jpg', 1),
    ('Soups', 'category/soups.jpg', 1),
    ('Breakfast', 'category/Breakfast.jpg', 1),
    ('Lunch', 'category/Lunch.jpg', 1),
    ('Dinner', 'category/Dinner.jpg', 1);

-- Insert data into Ingredient table
-- Insert more data into Ingredient table
INSERT IGNORE  INTO recipe_ingredient (IngredientName)
VALUES
    ('Garlic'),
    ('Pepper'),
    ('Olive Oil'),
    ('Basil'),
    ('Ground Beef'),
    ('Bell Pepper'),
    ('Cheddar Cheese'),
    ('Mayonnaise'),
    ('Mustard'),
    ('Cucumber'),
    ('Carrot'),
    ('Pineapple'),
    ('Vanilla Extract'),
    ('Cinnamon'),
    ('Nutmeg'),
    ('Honey'),
    ('Olive Oil'),
    ('Garlic'),
    ('Pepper'),
    ('Parsley'),
    ('Lime'),
    ('Mint Leaves'),
    ('Honey'),
    ('Vinegar'),
    ('Balsamic Vinegar'),
    ('Yogurt'),
    ('Chili Powder'),
    ('Cilantro'),
    ('Avocado'),
    ('Soy Sauce'),
    ('Ginger'),
    ('Sesame Oil'),
    ('Oregano'),
    ('Thyme'),
    ('Rosemary'),
    ('Paprika');


-- Insert more data into Recipe table
INSERT ignore INTO recipe_recipe (RecipeName, Difficulty_Level, DurationTime, IngredientDesc, RecipeInfo, ImageUrl, videoUrl, active, Recipe_Procedure, RecipeDesc, creatAt) VALUES
    ('Delicious Pasta', 'Easy', '30 mins', 'Fresh ingredients for a perfect pasta dish.', 'Learn how to make the best pasta ever!', 'recipe/image_1.jpg', 'https://www.youtube.com/watch?v=video_1', 1, 'Cook pasta, prepare sauce, combine, and enjoy!', 'A simple and tasty pasta recipe.', NOW()),
    ('Chocolate Cake', 'Moderate', '60 mins', 'Flour, sugar, cocoa for the cake, butter and sugar for the frosting.', 'Create a decadent chocolate cake for any occasion.', 'recipe/image_2.jpg', 'https://www.youtube.com/watch?v=video_2', 1, 'Bake the cake, make the frosting, and decorate.', 'Indulge in this rich and moist chocolate cake.', NOW()),
    ('Greek Salad', 'Easy', '15 mins', 'Fresh vegetables and feta cheese.', 'A simple and healthy Greek salad recipe.', 'recipe/image_4.jpg', 'https://www.youtube.com/watch?v=video_4', 1, 'Chop vegetables, mix with feta cheese, and drizzle with olive oil.', 'Enjoy the flavors of the Mediterranean with this refreshing salad.', NOW()),
    ('Mango Smoothie', 'Easy', '5 mins', 'Mango, yogurt, honey.', 'Blend together for a refreshing mango smoothie.', 'recipe/image_5.jpg', 'https://www.youtube.com/watch?v=video_5', 1, 'Combine mango, yogurt, and honey in a blender.', 'Cool off with this delicious and nutritious mango smoothie.', NOW()),
    ('Scrambled Eggs', 'Easy', '10 mins', 'Eggs, butter, salt, pepper.', 'Learn how to make fluffy scrambled eggs.', 'recipe/image_6.jpg', 'https://www.youtube.com/watch?v=video_6', 1, 'Whisk eggs, cook with butter, and season with salt and pepper.', 'Start your day right with these perfect scrambled eggs.', NOW()),
    ('Pasta with Tomato Sauce', 'Easy', '25 mins', 'Simple pasta recipe with tomato sauce', 'Delicious pasta dish with homemade tomato sauce', 'recipe/image_3.jpg', 'https://www.youtube.com/watch?v=video_3', 1, 'Boil pasta and prepare tomato sauce. Combine and serve.', 'A quick and tasty pasta recipe.', NOW()),
    ('Grilled Chicken Salad', 'Moderate', '40 mins', 'Healthy salad with grilled chicken and veggies', 'A light and nutritious salad with grilled chicken', 'recipe/image_4.jpg', 'https://www.youtube.com/watch?v=video_4', 1, 'Grill chicken, chop veggies, and assemble the salad.', 'A satisfying salad for a balanced meal.', NOW()),
    ('Chocolate Chip Cookies', 'Easy', '15 mins', 'Classic cookie recipe with chocolate chips', 'Homemade chocolate chip cookies for dessert', 'recipe/image_5.jpg', 'https://www.youtube.com/watch?v=video_5', 1, 'Mix ingredients, drop spoonfuls on a baking sheet, and bake.', 'Everyone\'s favorite cookie treat.', NOW()),
    ('Fruit Smoothie Bowl', 'Easy', '10 mins', 'Refreshing fruit smoothie in a bowl', 'A colorful and refreshing smoothie bowl', 'recipe/image_6.jpg', 'https://www.youtube.com/watch?v=video_6', 1, 'Blend fruits and yogurt, pour into a bowl, and add toppings.', 'A delightful way to start your day.', NOW()),
	('Chicken Alfredo', 'Moderate', '40 mins', 'Chicken, fettuccine, heavy cream, parmesan cheese.', 'Indulge in a creamy and flavorful chicken Alfredo pasta.', 'recipe/image_1.jpg', 'https://www.youtube.com/watch?v=video_1', 1, 'Cook chicken and fettuccine, prepare Alfredo sauce, and combine.', 'Enjoy this classic Italian dish with tender chicken and rich sauce.', NOW()),
    ('Chocolate Cake', 'Moderate', '60 mins', 'Flour, sugar, cocoa powder, eggs, butter.', 'Satisfy your sweet tooth with a homemade chocolate cake.', 'recipe/image_2.jpg', 'https://www.youtube.com/watch?v=video_2', 1, 'Mix dry and wet ingredients, bake the cake, and frost with chocolate ganache.', 'Indulge in the irresistible goodness of this moist and decadent chocolate cake.', NOW()),
    ('Stuffed Mushrooms', 'Moderate', '30 mins', 'Mushrooms, cream cheese, garlic, breadcrumbs.', 'Delight your taste buds with these savory stuffed mushrooms.', 'recipe/image_3.jpg', 'https://www.youtube.com/watch?v=video_3', 1, 'Clean mushrooms, mix filling, stuff mushrooms, and bake.', 'These cheesy and flavorful stuffed mushrooms are perfect for any gathering.', NOW());
-- Insert data into recipe_recipeingredient table for the first few recipes
-- This is just a sample. You can generate data similarly for all recipes.
INSERT IGNORE  INTO recipe_recipeingredient (recipe_id, ingredient_id, quantity, unit)
VALUES
    (759, 297, 0.25, 'cups'),
    (759, 276, 0.5, 'cup'),
    (759, 276, 1, 'cup'),
    (760, 283, 0.5, 'pound'),
    (760, 295, 1, 'piece'),
    (760, 296, 1, 'tablespoon'),
    (761, 286, 0.5, 'teaspoon'),
    (761, 282, 1, 'cup'),
    (761, 273, 0.5, 'teaspoon'),
    (762, 299, 1, 'cup'),
    (762, 277, 0.5, 'cup'),
    (762, 288, 0.25, 'teaspoon'),
    (761, 290, 300, 'grams'),  -- Chicken
    (761, 291, 250, 'grams'),  -- Fettuccine
    (761, 281, 200, 'ml'),     -- Heavy cream
    (761, 287, 100, 'grams'),
    (762, 275, 300, 'grams'),  -- Flour
    (762, 301, 250, 'grams'),  -- Sugar
    (762, 304, 50, 'grams'),   -- Cocoa powder
    (762, 289, 4, 'pieces'),   -- Eggs
    (762, 303, 150, 'grams'),
    (762, 302, 12, 'pieces'),  -- Mushrooms
    (765, 285, 200, 'grams'),  -- Cream cheese
    (765, 292, 2, 'cloves'),   -- Garlic
    (765, 294, 100, 'grams');
