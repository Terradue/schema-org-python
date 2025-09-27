from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work_season import CreativeWorkSeason


class RadioSeason(CreativeWorkSeason):
    """
Season dedicated to radio broadcast and associated online delivery.
    """
    type_: Literal['https://schema.org/RadioSeason'] = Field(default='https://schema.org/RadioSeason', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
