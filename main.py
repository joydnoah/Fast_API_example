from fastapi import FastAPI
from models.response.recipes import GetRecipeMessageResponse, RecipeRequest, PostRecipeMessageResponse, RecipeResponse, UpdateRecipeRequest, BaseResponse, AllRecipesResponse
from models.response.errors import MissingFieldsError
from adapters.recipes import get_recipe, insert_recipe, get_all_recipes, update_recipe, delete_recipe
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse, JSONResponse
from typing import List
from typing import Callable, List

from fastapi import Body, FastAPI, HTTPException, Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.routing import APIRoute

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    errors = exc.errors()
    missing_validation = []
    for error in errors:
        if error['type'] == 'missing':
            missing_validation.append(error['loc'][1])
        else:
            return PlainTextResponse(str(exc), status_code=404)
    return JSONResponse(content={
        "message": "Recipe creation failed!",
        "required": ', '.join(missing_validation)
    })

@app.get("/recipes")
def get_all_recipes_response() -> AllRecipesResponse:
    recipes = get_all_recipes()
    all_recipes = [recipe.get_response().model_dump() for recipe in recipes]
    return AllRecipesResponse(
        recipes=all_recipes
    )

@app.get("/recipes/{id}")
def get_recipe_response(id: int) -> GetRecipeMessageResponse:
    recipe = get_recipe(id)
    if recipe:
        recipe = [recipe.get_response().model_dump()]
    else:
        recipe = []
    return GetRecipeMessageResponse(
        message="Recipe details by id",
        recipe=recipe
    )

@app.post("/recipes")
def insert_recipe_response(recipe: RecipeRequest) -> PostRecipeMessageResponse:
    recipe = insert_recipe(recipe)
    return PostRecipeMessageResponse(
        message="Recipe successfully created!",
        recipe=[recipe.post_response().model_dump()]
    )

@app.patch("/recipes/{id}")
def update_recipe_response(id: int, recipe_data: UpdateRecipeRequest) -> GetRecipeMessageResponse:
    recipe = update_recipe(id, recipe_data)
    if recipe:
        recipe = [recipe.get_response().model_dump()]
    else:
        recipe = []
    return GetRecipeMessageResponse(
        message="Recipe successfully updated!",
        recipe=recipe
    )

@app.delete("/recipes/{id}")
def delete_recipe_response(id: int) -> PlainTextResponse:
    recipe = get_recipe(id)
    if recipe:
        delete_recipe(id)
        return BaseResponse(message="Recipe successfully removed!")
    return BaseResponse(message="No recipe found")