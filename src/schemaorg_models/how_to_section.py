from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.creative_work import CreativeWork
from schemaorg_models.item_list import ItemList

class HowToSection(CreativeWork):
    """
A sub-grouping of steps in the instructions for how to achieve a result (e.g. steps for making a pie crust within a pie recipe).
    """
    class_: Literal['https://schema.org/HowToSection'] = Field(default='https://schema.org/HowToSection', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    steps: Optional[Union[str, List[str], CreativeWork, List[CreativeWork], ItemList, List[ItemList]]] = Field(default=None, validation_alias=AliasChoices('steps', 'https://schema.org/steps'), serialization_alias='https://schema.org/steps')
