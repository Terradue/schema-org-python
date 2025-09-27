from typing import Literal
from pydantic import Field
from schemaorg_models.entertainment_business import EntertainmentBusiness


class ArtGallery(EntertainmentBusiness):
    """
An art gallery.
    """
    class_: Literal['https://schema.org/ArtGallery'] = Field(default='https://schema.org/ArtGallery', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
