from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.creative_work import CreativeWork
from schemaorg_models.item_list import ItemList

class HowToSection(CreativeWork):
    """
A sub-grouping of steps in the instructions for how to achieve a result (e.g. steps for making a pie crust within a pie recipe).
    """
    type_: Literal['https://schema.org/HowToSection'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/HowToSection'),serialization_alias='class') # type: ignore
    steps: Optional[Union[str, List[str], CreativeWork, List[CreativeWork], ItemList, List[ItemList]]] = Field(default=None,validation_alias=AliasChoices('steps', 'https://schema.org/steps'),serialization_alias='https://schema.org/steps')
