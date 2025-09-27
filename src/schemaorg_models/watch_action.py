from typing import Literal
from pydantic import Field
from schemaorg_models.consume_action import ConsumeAction


class WatchAction(ConsumeAction):
    """
The act of consuming dynamic/moving visual content.
    """
    class_: Literal['https://schema.org/WatchAction'] = Field(default='https://schema.org/WatchAction', alias='class', serialization_alias='class') # type: ignore
