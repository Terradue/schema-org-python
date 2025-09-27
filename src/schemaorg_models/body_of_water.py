from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.landform import Landform


class BodyOfWater(Landform):
    """
A body of water, such as a sea, ocean, or lake.
    """
    type_: Literal['https://schema.org/BodyOfWater'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/BodyOfWater'),serialization_alias='class') # type: ignore
