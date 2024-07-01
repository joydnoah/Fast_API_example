from fastapi import FastAPI
from models.response.recipes import GetRecipeMessageResponse, RecipeRequest, PostRecipeMessageResponse, RecipeResponse, UpdateRecipeRequest, BaseResponse
from models.response.errors import MissingFieldsError
from adapters.recipes import get_recipe, insert_recipe, get_all_recipes, update_recipe, delete_recipe
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from typing import List

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    errors = exc.errors()
    missing_validation = []
    for error in errors:
        if error['type'] == 'missing':
            missing_validation.append(error['loc'][1])
        else:
            return PlainTextResponse(str(exc), status_code=400)
    response = MissingFieldsError(required=missing_validation)
    return PlainTextResponse(response.model_dump_json(), status_code=400)

@app.get("/recipes")
def get_all_recipes_response() -> List[RecipeResponse]:
    recipes = get_all_recipes()
    return [recipe.get_response() for recipe in recipes]

@app.get("/recipes/{recipe_id}")
def get_recipe_response(recipe_id: int) -> GetRecipeMessageResponse:
    recipe = get_recipe(recipe_id)
    return GetRecipeMessageResponse(
        message="Recipe details by id",
        recipe=recipe.get_response()
    )

@app.post("/recipes")
def insert_recipe_response(recipe: RecipeRequest) -> PostRecipeMessageResponse:
    recipe = insert_recipe(recipe)
    return PostRecipeMessageResponse(
        message="Recipe successfully created!",
        recipe=recipe.post_response()
    )

@app.patch("/recipes/{recipe_id}")
def update_recipe_response(recipe_id: int, recipe_data: UpdateRecipeRequest) -> GetRecipeMessageResponse:
    recipe = update_recipe(recipe_id, recipe_data)
    return GetRecipeMessageResponse(
        message="Recipe successfully updated!",
        recipe=recipe.get_response()
    )

@app.delete("/recipes/{recipe_id}")
def delete_recipe_response(recipe_id: int) -> PlainTextResponse:
    recipe = get_recipe(recipe_id)
    if recipe:
        delete_recipe(recipe_id)
        return BaseResponse(message="Recipe successfully removed!")
    return BaseResponse(message="No recipe found")