from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.periodical import Periodical


class Newspaper(Periodical):
    """
A publication containing information about varied topics that are pertinent to general information, a geographic area, or a specific subject matter (i.e. business, culture, education). Often published daily.
    """
    type_: Literal['https://schema.org/Newspaper'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Newspaper'),serialization_alias='class') # type: ignore
