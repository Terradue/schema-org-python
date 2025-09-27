from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class RVPark(CivicStructure):
    """
A place offering space for "Recreational Vehicles", Caravans, mobile homes and the like.
    """
    class_: Literal['https://schema.org/RVPark'] = Field(default='https://schema.org/RVPark', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
