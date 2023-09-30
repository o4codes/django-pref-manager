import json
from typing import Any, Type, Iterable, Mapping

from pydantic import BaseModel, Field


class PreferenceSchema(BaseModel):
    name: str
    type: Type[Any]
    default: Any = Field(default=None)
    is_env: bool = Field(default=False)
    
    def parse_value(self, value: Any = None):
        primitive_types = (bool, int, float, str)
        
        if value is None:
            return None
        
        if self.type in primitive_types:
            return self.type(value)
        
        if self.type in [Mapping, Iterable]:
            return json.loads(value)