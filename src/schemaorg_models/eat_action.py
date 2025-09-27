from typing import Literal
from pydantic import Field
from schemaorg_models.consume_action import ConsumeAction


class EatAction(ConsumeAction):
    """
The act of swallowing solid objects.
    """
    class_: Literal['https://schema.org/EatAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
