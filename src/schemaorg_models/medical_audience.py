from typing import Literal
from pydantic import Field
from schemaorg_models.audience import Audience


class MedicalAudience(Audience):
    """
Medical audience for page.
    """
    class_: Literal['https://schema.org/MedicalAudience'] = Field(default='https://schema.org/MedicalAudience', alias='@type', serialization_alias='@type') # type: ignore
