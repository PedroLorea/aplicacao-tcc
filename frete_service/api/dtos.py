from typing import Optional
from pydantic import BaseModel

class FreteDTO(BaseModel):
    id: Optional[int] = None
    produto: str
