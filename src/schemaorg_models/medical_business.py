from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.local_business import LocalBusiness


class MedicalBusiness(LocalBusiness):
    """
A particular physical or virtual business of an organization for medical purposes. Examples of MedicalBusiness include different businesses run by health professionals.
    """
    type_: Literal['https://schema.org/MedicalBusiness'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MedicalBusiness'),serialization_alias='class') # type: ignore
