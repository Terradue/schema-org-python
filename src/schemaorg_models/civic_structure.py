from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.place import Place


class CivicStructure(Place):
    """
A public structure, such as a town hall or concert hall.
    """
    openingHours: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('openingHours', 'https://schema.org/openingHours'),serialization_alias='https://schema.org/openingHours')
