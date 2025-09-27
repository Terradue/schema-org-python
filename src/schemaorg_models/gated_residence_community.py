from typing import Literal
from pydantic import Field
from schemaorg_models.residence import Residence


class GatedResidenceCommunity(Residence):
    """
Residence type: Gated community.
    """
    class_: Literal['https://schema.org/GatedResidenceCommunity'] = Field('class', alias='class', serialization_alias='class') # type: ignore
