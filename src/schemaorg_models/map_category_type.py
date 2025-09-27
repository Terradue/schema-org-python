from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class MapCategoryType(Enumeration):
    """
An enumeration of several kinds of Map.
    """
    type_: Literal['https://schema.org/MapCategoryType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MapCategoryType'),serialization_alias='class') # type: ignore
