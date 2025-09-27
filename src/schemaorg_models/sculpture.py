from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work import CreativeWork


class Sculpture(CreativeWork):
    """
A piece of sculpture.
    """
    class_: Literal['https://schema.org/Sculpture'] = Field(default='https://schema.org/Sculpture', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
