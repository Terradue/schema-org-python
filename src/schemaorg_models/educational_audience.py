from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.audience import Audience


class EducationalAudience(Audience):
    """
An EducationalAudience.
    """
    type_: Literal['https://schema.org/EducationalAudience'] = Field(default='https://schema.org/EducationalAudience', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    educationalRole: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('educationalRole', 'https://schema.org/educationalRole'), serialization_alias='https://schema.org/educationalRole')
