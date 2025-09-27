from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class MedicalBusiness(LocalBusiness):
    """
A particular physical or virtual business of an organization for medical purposes. Examples of MedicalBusiness include different businesses run by health professionals.
    """
    class_: Literal['https://schema.org/MedicalBusiness'] = Field(default='https://schema.org/MedicalBusiness', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
