from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.government_building import GovernmentBuilding


class Embassy(GovernmentBuilding):
    """
An embassy.
    """
    type_: Literal['https://schema.org/Embassy'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Embassy'),serialization_alias='class') # type: ignore
