from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible


class Series(Intangible):
    """
A Series in schema.org is a group of related items, typically but not necessarily of the same kind. See also [[CreativeWorkSeries]], [[EventSeries]].
    """
    type_: Literal['https://schema.org/Series'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Series'),serialization_alias='class') # type: ignore
