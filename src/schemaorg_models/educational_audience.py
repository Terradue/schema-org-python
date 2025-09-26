from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.audience import Audience


class EducationalAudience(Audience):
    """
An EducationalAudience.
    """
    educationalRole: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('educationalRole', 'https://schema.org/educationalRole'),serialization_alias='https://schema.org/educationalRole')
