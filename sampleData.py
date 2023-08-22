from django.contrib.auth import get_user_model
from recipe.models import Category, Ingredient, Recipe, RecipeIngredient, UserFavorites, PopularRecipe
import random
import lorem
from django.db import transaction
sample_categories = [Category(title="Main Course", img="category/main-course.jpg", active=True),Category(title="Desserts", img="category/desserts.jpg", active=True),Category(title="Appetizers", img="category/appetizers.jpg", active=True),Category(title="Salads", img="category/salads.jpg", active=True),Category(title="Beverages", img="category/beverages.jpg", active=True),Category(title="Breakfast", img="category/breakfast.jpg", active=True),Category(title="Soups", img="category/soups.jpg", active=True),]
sample_units = ["grams", "kilograms", "pounds", "ounces", "liters", "milliliters", "teaspoons", "tablespoons", "cups", "pieces","slices", "cans", "packages", "bunches", "pinches", "cloves", "heads"]
sample_ingredients = [Ingredient(IngredientName="Tomatoes"),Ingredient(IngredientName="Cheese"),Ingredient(IngredientName="Chicken"),Ingredient(IngredientName="Flour"),Ingredient(IngredientName="Sugar"),Ingredient(IngredientName="Salt"),Ingredient(IngredientName="Lettuce"),Ingredient(IngredientName="Onions"),Ingredient(IngredientName="Lemons"),Ingredient(IngredientName="Eggs"),Ingredient(IngredientName="Butter"),Ingredient(IngredientName="Milk"),Ingredient(IngredientName="Rice"),Ingredient(IngredientName="Pasta"),Ingredient(IngredientName="Chocolate"),Ingredient(IngredientName="Bread"),]
with transaction.atomic():
    existing_categories = {category.title: category for category in Category.objects.all()}
    existing_ingredients = {ingredient.IngredientName: ingredient for ingredient in Ingredient.objects.all()}
    categories = []
    for category_data in sample_categories:
        if category_data.title not in existing_categories:
            category = Category(title=category_data.title, img=category_data.img, active=category_data.active)
            categories.append(category)
    existing_ingredients = {ingredient.IngredientName: ingredient.id for ingredient in Ingredient.objects.all()}
    ingredients = []
    for ingredient_data in sample_ingredients:
        if ingredient_data.IngredientName not in existing_ingredients:
            ingredient = Ingredient(IngredientName=ingredient_data.IngredientName)
            ingredients.append(ingredient)
    Category.objects.bulk_create(categories)
    Ingredient.objects.bulk_create(ingredients)
    recipes = []
    num_recipes = 50
    for _ in range(num_recipes):
        categories_list = random.sample(existing_categories.values(), random.randint(1, 2))
        recipe = Recipe(RecipeName=lorem.sentence(), Difficulty_Level=random.choice(["Easy", "Moderate", "Challenging"]), DurationTime=f"{random.randint(10, 120)} mins", IngredientDesc=lorem.paragraph(), RecipeInfo=lorem.paragraph(), ImageUrl=f"recipe/image_{random.randint(1, 10)}.jpg", videoUrl=f"https://www.youtube.com/watch?v=video_{random.randint(1, 10)}", active=random.choice([True, False]), Recipe_Procedure=lorem.paragraph(), RecipeDesc=lorem.paragraph(),)
        recipe.save()
        available_ingredient_names = list(existing_ingredients.keys())
        num_ingredients = random.randint(2, min(5, len(available_ingredient_names)))
        sampled_ingredient_names = random.sample(available_ingredient_names, num_ingredients)
        for ingredient_name in sampled_ingredient_names:
            ingredient = existing_ingredients[ingredient_name]
            quantity = random.uniform(0.1, 2.0)
            unit = random.choice(sample_units)
            recipe_ingredient = RecipeIngredient.objects.create(recipe=recipe,ingredient=ingredient,quantity=quantity,unit=unit)