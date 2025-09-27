from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.item_list import ItemList


class HowToStep(ItemList):
    """
A step in the instructions for how to achieve a result. It is an ordered list with HowToDirection and/or HowToTip items.
    """
    type_: Literal['https://schema.org/HowToStep'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/HowToStep'),serialization_alias='class') # type: ignore
