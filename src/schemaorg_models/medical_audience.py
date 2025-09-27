from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.audience import Audience


class MedicalAudience(Audience):
    """
Medical audience for page.
    """
    type_: Literal['https://schema.org/MedicalAudience'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MedicalAudience'),serialization_alias='class') # type: ignore
