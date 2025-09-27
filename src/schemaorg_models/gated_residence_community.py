from typing import Literal
from pydantic import Field
from schemaorg_models.residence import Residence


class GatedResidenceCommunity(Residence):
    """
Residence type: Gated community.
    """
    class_: Literal['https://schema.org/GatedResidenceCommunity'] = Field(default='https://schema.org/GatedResidenceCommunity', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
