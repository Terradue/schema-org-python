from typing import Literal
from pydantic import Field
from schemaorg_models.assess_action import AssessAction


class ReactAction(AssessAction):
    """
The act of responding instinctively and emotionally to an object, expressing a sentiment.
    """
    class_: Literal['https://schema.org/ReactAction'] = Field('class', alias='class', serialization_alias='class') # type: ignore
