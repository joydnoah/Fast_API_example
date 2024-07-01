from pydantic import BaseModel
from typing import List

class MissingFieldsError(BaseModel):
    message: str = "Recipe creation failed!"
    required: List[str]