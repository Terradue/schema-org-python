from typing import Literal
from pydantic import Field
from schemaorg_models.item_list import ItemList


class HowToStep(ItemList):
    """
A step in the instructions for how to achieve a result. It is an ordered list with HowToDirection and/or HowToTip items.
    """
    class_: Literal['https://schema.org/HowToStep'] = Field('class', alias='class', serialization_alias='class') # type: ignore
