from typing import Literal
from pydantic import Field
from schemaorg_models.home_and_construction_business import HomeAndConstructionBusiness


class GeneralContractor(HomeAndConstructionBusiness):
    """
A general contractor.
    """
    class_: Literal['https://schema.org/GeneralContractor'] = Field(default='https://schema.org/GeneralContractor', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
