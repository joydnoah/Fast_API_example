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
    recipes: List[dict]

class GetRecipeMessageResponse(BaseModel):
    message: str
    recipe: List[RecipeResponse]

class PostRecipeMessageResponse(BaseModel):
    message: str
    recipe: List[PostRecipeResponse]

class RecipeRequest(BaseModel):
    title: str
    making_time: str
    serves: str
    ingredients: str
    cost: int

    def __init__(self, **data) -> None:
      print(data)
      super().__init__(**data)

class UpdateRecipeRequest(BaseModel):
    title: str | None = Field(default=None)
    making_time: str | None = Field(default=None)
    serves: str | None = Field(default=None)
    ingredients: str | None = Field(default=None)
    cost: int | None = Field(default=None)

    def __init__(self, **data) -> None:
      print(data)
      super().__init__(**data)


class BaseResponse(BaseModel):
    message: str