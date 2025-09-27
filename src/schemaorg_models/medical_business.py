from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class MedicalBusiness(LocalBusiness):
    """
A particular physical or virtual business of an organization for medical purposes. Examples of MedicalBusiness include different businesses run by health professionals.
    """
    class_: Literal['https://schema.org/MedicalBusiness'] = Field(default='https://schema.org/MedicalBusiness', alias='class', serialization_alias='class') # type: ignore
