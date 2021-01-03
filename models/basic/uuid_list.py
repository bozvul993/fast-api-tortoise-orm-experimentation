from typing import List
from pydantic import BaseModel
from typing import List


class UUIDList(BaseModel):
    ids: List[str]
