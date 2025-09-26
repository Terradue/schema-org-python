from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.physician import Physician

from schemaorg_models.medical_organization import MedicalOrganization

class IndividualPhysician(Physician):
    """
An individual medical practitioner. For their official address use [[address]], for affiliations to hospitals use [[hospitalAffiliation]]. 
The [[practicesAt]] property can be used to indicate [[MedicalOrganization]] hospitals, clinics, pharmacies etc. where this physician practices.
    """
    practicesAt: Optional[Union[MedicalOrganization, List[MedicalOrganization]]] = Field(default=None,validation_alias=AliasChoices('practicesAt', 'https://schema.org/practicesAt'),serialization_alias='https://schema.org/practicesAt')
