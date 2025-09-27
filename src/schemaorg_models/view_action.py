from typing import Literal
from pydantic import Field
from schemaorg_models.consume_action import ConsumeAction


class ViewAction(ConsumeAction):
    """
The act of consuming static visual content.
    """
    class_: Literal['https://schema.org/ViewAction'] = Field(default='https://schema.org/ViewAction', alias='class', serialization_alias='class') # type: ignore
