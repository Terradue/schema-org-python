from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work_series import CreativeWorkSeries


class BookSeries(CreativeWorkSeries):
    """
A series of books. Included books can be indicated with the hasPart property.
    """
    type_: Literal['https://schema.org/BookSeries'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/BookSeries'),serialization_alias='class') # type: ignore
