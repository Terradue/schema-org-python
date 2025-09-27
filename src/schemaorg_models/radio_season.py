from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work_season import CreativeWorkSeason


class RadioSeason(CreativeWorkSeason):
    """
Season dedicated to radio broadcast and associated online delivery.
    """
    type_: Literal['https://schema.org/RadioSeason'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/RadioSeason'),serialization_alias='class') # type: ignore
