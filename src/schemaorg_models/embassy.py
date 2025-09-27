from typing import Literal
from pydantic import Field
from schemaorg_models.government_building import GovernmentBuilding


class Embassy(GovernmentBuilding):
    """
An embassy.
    """
    class_: Literal['https://schema.org/Embassy'] = Field(default='https://schema.org/Embassy', alias='class', serialization_alias='class') # type: ignore
