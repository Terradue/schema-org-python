from typing import Literal
from pydantic import Field
from schemaorg_models.entertainment_business import EntertainmentBusiness


class ArtGallery(EntertainmentBusiness):
    """
An art gallery.
    """
    class_: Literal['https://schema.org/ArtGallery'] = Field('class', alias='class', serialization_alias='class') # type: ignore
