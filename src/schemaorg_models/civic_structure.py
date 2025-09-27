from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.place import Place


class CivicStructure(Place):
    """
A public structure, such as a town hall or concert hall.
    """
    class_: Literal['https://schema.org/CivicStructure'] = Field(default='https://schema.org/CivicStructure', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    openingHours: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('openingHours', 'https://schema.org/openingHours'), serialization_alias='https://schema.org/openingHours')
