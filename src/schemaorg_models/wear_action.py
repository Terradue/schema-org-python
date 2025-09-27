from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.use_action import UseAction


class WearAction(UseAction):
    """
The act of dressing oneself in clothing.
    """
    type_: Literal['https://schema.org/WearAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/WearAction'),serialization_alias='class') # type: ignore
