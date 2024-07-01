from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

class RecipeResponse(BaseModel):
    id: int
    title: str
    making_time: str
    serves: str
    ingredients: str
    cost: int

class PostRecipeResponse(RecipeResponse):
    created_at: datetime
    updated_at: datetime

class AllRecipesResponse(BaseModel):
    recipes: List[RecipeResponse]

class GetRecipeMessageResponse(BaseModel):
    message: str
    recipe: RecipeResponse

class PostRecipeMessageResponse(BaseModel):
    message: str
    recipe: PostRecipeResponse

class RecipeRequest(BaseModel):
    title: str
    making_time: str
    serves: str
    ingredients: str
    cost: int

class UpdateRecipeRequest(BaseModel):
    title: str | None = Field(default=None)
    making_time: str | None = Field(default=None)
    serves: str | None = Field(default=None)
    ingredients: str | None = Field(default=None)
    cost: int | None = Field(default=None)

class BaseResponse(BaseModel):
    message: str