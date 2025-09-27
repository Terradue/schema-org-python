from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.place import Place


class CivicStructure(Place):
    """
A public structure, such as a town hall or concert hall.
    """
    type_: Literal['https://schema.org/CivicStructure'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/CivicStructure'),serialization_alias='class') # type: ignore
    openingHours: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('openingHours', 'https://schema.org/openingHours'),serialization_alias='https://schema.org/openingHours')
