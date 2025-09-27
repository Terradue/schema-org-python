from typing import Literal
from pydantic import Field
from schemaorg_models.medical_clinic import MedicalClinic


class CovidTestingFacility(MedicalClinic):
    """
A CovidTestingFacility is a [[MedicalClinic]] where testing for the COVID-19 Coronavirus
      disease is available. If the facility is being made available from an established [[Pharmacy]], [[Hotel]], or other
      non-medical organization, multiple types can be listed. This makes it easier to re-use existing schema.org information
      about that place, e.g. contact info, address, opening hours. Note that in an emergency, such information may not always be reliable.
      
    """
    class_: Literal['https://schema.org/CovidTestingFacility'] = Field(default='https://schema.org/CovidTestingFacility', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
