from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class RestrictedDiet(Enumeration):
    """
A diet restricted to certain foods or preparations for cultural, religious, health or lifestyle reasons. 
    """
    class_: Literal['https://schema.org/RestrictedDiet'] = Field(default='https://schema.org/RestrictedDiet', alias='class', serialization_alias='class') # type: ignore
