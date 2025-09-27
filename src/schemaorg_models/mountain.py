from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.landform import Landform


class Mountain(Landform):
    """
A mountain, like Mount Whitney or Mount Everest.
    """
    type_: Literal['https://schema.org/Mountain'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Mountain'),serialization_alias='class') # type: ignore
