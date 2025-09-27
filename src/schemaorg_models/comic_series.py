from typing import Literal
from pydantic import Field
from schemaorg_models.periodical import Periodical


class ComicSeries(Periodical):
    """
A sequential publication of comic stories under a
    	unifying title, for example "The Amazing Spider-Man" or "Groo the
    	Wanderer".
    """
    class_: Literal['https://schema.org/ComicSeries'] = Field(default='https://schema.org/ComicSeries', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
