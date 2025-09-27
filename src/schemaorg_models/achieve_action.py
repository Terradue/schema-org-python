from typing import Literal
from pydantic import Field
from schemaorg_models.action import Action


class AchieveAction(Action):
    """
The act of accomplishing something via previous efforts. It is an instantaneous action rather than an ongoing process.
    """
    type_: Literal['https://schema.org/AchieveAction'] = Field(default='https://schema.org/AchieveAction', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
