from typing import Literal
from pydantic import Field
from schemaorg_models.civic_structure import CivicStructure


class TrainStation(CivicStructure):
    """
A train station.
    """
    class_: Literal['https://schema.org/TrainStation'] = Field(default='https://schema.org/TrainStation', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
