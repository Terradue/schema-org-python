from typing import Literal
from pydantic import Field
from schemaorg_models.intangible import Intangible


class Series(Intangible):
    """
A Series in schema.org is a group of related items, typically but not necessarily of the same kind. See also [[CreativeWorkSeries]], [[EventSeries]].
    """
    type_: Literal['https://schema.org/Series'] = Field(default='https://schema.org/Series', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
