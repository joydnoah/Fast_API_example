from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from models.postgres.base import Base
from models.response.recipes import RecipeResponse, PostRecipeResponse


class Recipes(Base):
    __tablename__ = "recipes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    making_time: Mapped[str] = mapped_column()
    serves: Mapped[str] = mapped_column()
    ingredients: Mapped[str] = mapped_column()
    cost: Mapped[int] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now())

    def __repr__(self) -> str:
        return f"Recipe({self.id})"
    
    def get_response(self):
        return RecipeResponse(**self.__dict__)
    
    def post_response(self):
        return PostRecipeResponse(**self.__dict__)
    