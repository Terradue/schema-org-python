from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.government_building import GovernmentBuilding


class DefenceEstablishment(GovernmentBuilding):
    """
A defence establishment, such as an army or navy base.
    """
    type_: Literal['https://schema.org/DefenceEstablishment'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DefenceEstablishment'),serialization_alias='class') # type: ignore
