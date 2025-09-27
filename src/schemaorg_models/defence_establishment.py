from typing import Literal
from pydantic import Field
from schemaorg_models.government_building import GovernmentBuilding


class DefenceEstablishment(GovernmentBuilding):
    """
A defence establishment, such as an army or navy base.
    """
    type_: Literal['https://schema.org/DefenceEstablishment'] = Field(default='https://schema.org/DefenceEstablishment', alias='@type', serialization_alias='@type') # type: ignore
