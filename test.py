from handlers.postgres import get_engine
from models.postgres.recipes import Recipes
from sqlalchemy.orm import Session

def get_recipe(recipe_id):
    engine = get_engine()
    session = Session(engine)
    result = session.query(Recipes).filter_by(id=1).first()
    print(type(result))

get_recipe(1)