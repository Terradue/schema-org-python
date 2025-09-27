from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work import CreativeWork


class Season(CreativeWork):
    """
A season in a media series.
    """
    type_: Literal['https://schema.org/Season'] = Field(default='https://schema.org/Season', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
