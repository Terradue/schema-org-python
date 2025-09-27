from typing import Literal
from pydantic import Field
from schemaorg_models.find_action import FindAction


class DiscoverAction(FindAction):
    """
The act of discovering/finding an object.
    """
    class_: Literal['https://schema.org/DiscoverAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
