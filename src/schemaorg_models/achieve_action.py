from typing import Literal
from pydantic import Field
from schemaorg_models.action import Action


class AchieveAction(Action):
    """
The act of accomplishing something via previous efforts. It is an instantaneous action rather than an ongoing process.
    """
    class_: Literal['https://schema.org/AchieveAction'] = Field(default='https://schema.org/AchieveAction', alias='class', serialization_alias='class') # type: ignore
