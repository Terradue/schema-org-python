from typing import Literal
from pydantic import Field
from schemaorg_models.resort import Resort


class SkiResort(Resort):
    """
A ski resort.
    """
    class_: Literal['https://schema.org/SkiResort'] = Field(default='https://schema.org/SkiResort', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
