from pydantic import BaseModel,Field

class SCount(BaseModel):
    count :int = Field(ge=1,le=1000)