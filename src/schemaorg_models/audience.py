from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible

from schemaorg_models.administrative_area import AdministrativeArea

class Audience(Intangible):
    """
Intended audience for an item, i.e. the group for whom the item was created.
    """
    class_: Literal['https://schema.org/Audience'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    geographicArea: Optional[Union[AdministrativeArea, List[AdministrativeArea]]] = Field(default=None,validation_alias=AliasChoices('geographicArea', 'https://schema.org/geographicArea'), serialization_alias='https://schema.org/geographicArea')
    audienceType: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('audienceType', 'https://schema.org/audienceType'), serialization_alias='https://schema.org/audienceType')
