from typing import Literal
from pydantic import Field
from schemaorg_models.periodical import Periodical


class ComicSeries(Periodical):
    """
A sequential publication of comic stories under a
    	unifying title, for example "The Amazing Spider-Man" or "Groo the
    	Wanderer".
    """
    class_: Literal['https://schema.org/ComicSeries'] = Field('class', alias='class', serialization_alias='class') # type: ignore
