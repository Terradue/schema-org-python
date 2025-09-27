from typing import Literal
from pydantic import Field
from schemaorg_models.consume_action import ConsumeAction


class ReadAction(ConsumeAction):
    """
The act of consuming written content.
    """
    class_: Literal['https://schema.org/ReadAction'] = Field(default='https://schema.org/ReadAction', alias='class', serialization_alias='class') # type: ignore
