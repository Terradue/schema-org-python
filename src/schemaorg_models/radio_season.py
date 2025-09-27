from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work_season import CreativeWorkSeason


class RadioSeason(CreativeWorkSeason):
    """
Season dedicated to radio broadcast and associated online delivery.
    """
    class_: Literal['https://schema.org/RadioSeason'] = Field('class', alias='class', serialization_alias='class') # type: ignore
