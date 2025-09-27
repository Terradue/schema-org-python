from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work import CreativeWork


class Atlas(CreativeWork):
    """
A collection or bound volume of maps, charts, plates or tables, physical or in media form illustrating any subject.
    """
    type_: Literal['https://schema.org/Atlas'] = Field(default='https://schema.org/Atlas', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
