from typing import Literal
from pydantic import Field
from schemaorg_models.item_list import ItemList


class HowToStep(ItemList):
    """
A step in the instructions for how to achieve a result. It is an ordered list with HowToDirection and/or HowToTip items.
    """
    class_: Literal['https://schema.org/HowToStep'] = Field(default='https://schema.org/HowToStep', alias='@type', serialization_alias='@type') # type: ignore
