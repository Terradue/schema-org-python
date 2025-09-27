from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.entertainment_business import EntertainmentBusiness


class ArtGallery(EntertainmentBusiness):
    """
An art gallery.
    """
    type_: Literal['https://schema.org/ArtGallery'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ArtGallery'),serialization_alias='class') # type: ignore
