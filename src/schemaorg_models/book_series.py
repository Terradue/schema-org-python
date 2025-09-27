from typing import Literal
from pydantic import Field
from schemaorg_models.creative_work_series import CreativeWorkSeries


class BookSeries(CreativeWorkSeries):
    """
A series of books. Included books can be indicated with the hasPart property.
    """
    class_: Literal['https://schema.org/BookSeries'] = Field(default='https://schema.org/BookSeries', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
