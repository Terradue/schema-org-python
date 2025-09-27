from typing import Literal
from pydantic import Field
from schemaorg_models.find_action import FindAction


class DiscoverAction(FindAction):
    """
The act of discovering/finding an object.
    """
    type_: Literal['https://schema.org/DiscoverAction'] = Field(default='https://schema.org/DiscoverAction', alias='@type', serialization_alias='@type') # type: ignore
