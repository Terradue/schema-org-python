from typing import Literal
from pydantic import Field
from schemaorg_models.audience import Audience


class MedicalAudience(Audience):
    """
Medical audience for page.
    """
    class_: Literal['https://schema.org/MedicalAudience'] = Field('class', alias='class', serialization_alias='class') # type: ignore
