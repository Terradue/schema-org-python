from typing import Literal
from pydantic import Field
from schemaorg_models.use_action import UseAction


class WearAction(UseAction):
    """
The act of dressing oneself in clothing.
    """
    class_: Literal['https://schema.org/WearAction'] = Field(default='https://schema.org/WearAction', alias='class', serialization_alias='class') # type: ignore
