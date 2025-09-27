from typing import Literal
from pydantic import Field
from schemaorg_models.audience import Audience


class MedicalAudience(Audience):
    """
Medical audience for page.
    """
    class_: Literal['https://schema.org/MedicalAudience'] = Field(default='https://schema.org/MedicalAudience', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
