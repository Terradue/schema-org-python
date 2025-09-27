from typing import Literal
from pydantic import Field
from schemaorg_models.consume_action import ConsumeAction


class WatchAction(ConsumeAction):
    """
The act of consuming dynamic/moving visual content.
    """
    class_: Literal['https://schema.org/WatchAction'] = Field(default='https://schema.org/WatchAction', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
