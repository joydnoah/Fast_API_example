from handlers.postgres import get_engine
from models.postgres.recipes import Recipes
from models.response.recipes import RecipeRequest, UpdateRecipeRequest
from sqlalchemy.orm import Session
from typing import List

engine = get_engine()

def get_recipe(recipe_id: int) -> Recipes:
    session = Session(engine)
    recipe = session.query(Recipes).filter_by(id=recipe_id).first()
    session.close()
    return recipe

def get_all_recipes() -> List[Recipes]:
    session = Session(engine)
    recipe = session.query(Recipes).all()
    session.close()
    return recipe

def update_recipe(recipe_id: int, recipe_data: UpdateRecipeRequest) -> Recipes:
    session = Session(engine)
    data = recipe_data.model_dump(exclude_none=True)
    recipe = session.query(Recipes).filter_by(id=recipe_id).first()
    if "title" in data:
        recipe.title = data["title"]
    if "making_time" in data:
        recipe.making_time = data["making_time"]
    if "serves" in data:
        recipe.serves = data["serves"]
    if "ingredients" in data:
        recipe.title = data["ingredients"]
    if "cost" in data:
        recipe.cost = data["cost"]
    session.commit()
    session.refresh(recipe)
    session.close()
    return recipe

def insert_recipe(recipe_data: RecipeRequest) -> Recipes:
    session = Session(engine)
    recipe = Recipes(
        title=recipe_data.title,
        making_time=recipe_data.making_time,
        serves=recipe_data.serves,
        ingredients=recipe_data.ingredients,
        cost=recipe_data.cost,
    )
    session.add(recipe)
    session.commit()
    session.refresh(recipe)
    session.close()
    return recipe

def delete_recipe(recipe_id: int) -> None:
    session = Session(engine)
    session.query(Recipes).filter_by(id=recipe_id).delete()
    session.commit()
    session.close()
