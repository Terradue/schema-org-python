from typing import Literal
from pydantic import Field
from schemaorg_models.entertainment_business import EntertainmentBusiness


class ArtGallery(EntertainmentBusiness):
    """
An art gallery.
    """
    type_: Literal['https://schema.org/ArtGallery'] = Field(default='https://schema.org/ArtGallery', alias='@type', serialization_alias='@type') # type: ignore
