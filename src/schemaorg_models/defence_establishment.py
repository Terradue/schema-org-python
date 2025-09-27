from typing import Literal
from pydantic import Field
from schemaorg_models.government_building import GovernmentBuilding


class DefenceEstablishment(GovernmentBuilding):
    """
A defence establishment, such as an army or navy base.
    """
    class_: Literal['https://schema.org/DefenceEstablishment'] = Field('class', alias='class', serialization_alias='class') # type: ignore
