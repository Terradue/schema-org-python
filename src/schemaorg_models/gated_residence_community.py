from typing import Literal
from pydantic import Field
from schemaorg_models.residence import Residence


class GatedResidenceCommunity(Residence):
    """
Residence type: Gated community.
    """
    type_: Literal['https://schema.org/GatedResidenceCommunity'] = Field(default='https://schema.org/GatedResidenceCommunity', alias='@type', serialization_alias='@type') # type: ignore
