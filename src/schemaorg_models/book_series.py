from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work_series import CreativeWorkSeries


class BookSeries(CreativeWorkSeries):
    """
A series of books. Included books can be indicated with the hasPart property.
    """
    type_: Literal['https://schema.org/BookSeries'] = Field(default='https://schema.org/BookSeries', alias='@type', serialization_alias='@type') # type: ignore
