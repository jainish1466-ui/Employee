from pydantic import BaseModel
from typing import Optional

# Employee model
class Employee(BaseModel):
    id: Optional[str] = None
    name: str
    email: str
    department: str
    salary: float