from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work import CreativeWork


class Painting(CreativeWork):
    """
A painting.
    """
    class_: Literal['https://schema.org/Painting'] = Field(default='https://schema.org/Painting', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
