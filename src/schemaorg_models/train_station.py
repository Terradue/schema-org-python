from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.civic_structure import CivicStructure


class TrainStation(CivicStructure):
    """
A train station.
    """
    type_: Literal['https://schema.org/TrainStation'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/TrainStation'),serialization_alias='class') # type: ignore
