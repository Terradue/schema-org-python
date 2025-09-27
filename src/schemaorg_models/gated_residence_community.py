from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.residence import Residence


class GatedResidenceCommunity(Residence):
    """
Residence type: Gated community.
    """
    type_: Literal['https://schema.org/GatedResidenceCommunity'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/GatedResidenceCommunity'),serialization_alias='class') # type: ignore
