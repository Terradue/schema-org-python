from typing import Literal
from pydantic import Field
from schemaorg_models.periodical import Periodical


class Newspaper(Periodical):
    """
A publication containing information about varied topics that are pertinent to general information, a geographic area, or a specific subject matter (i.e. business, culture, education). Often published daily.
    """
    type_: Literal['https://schema.org/Newspaper'] = Field(default='https://schema.org/Newspaper', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
