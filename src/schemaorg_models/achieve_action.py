from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.action import Action


class AchieveAction(Action):
    """
The act of accomplishing something via previous efforts. It is an instantaneous action rather than an ongoing process.
    """
    type_: Literal['https://schema.org/AchieveAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AchieveAction'),serialization_alias='class') # type: ignore
