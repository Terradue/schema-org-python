from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.how_to_item import HowToItem


class HowToTool(HowToItem):
    """
A tool used (but not consumed) when performing instructions for how to achieve a result.
    """
    type_: Literal['https://schema.org/HowToTool'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/HowToTool'),serialization_alias='class') # type: ignore
