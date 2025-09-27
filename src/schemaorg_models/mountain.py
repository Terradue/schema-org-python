from typing import Literal
from pydantic import Field
from schemaorg_models.landform import Landform


class Mountain(Landform):
    """
A mountain, like Mount Whitney or Mount Everest.
    """
    class_: Literal['https://schema.org/Mountain'] = Field(default='https://schema.org/Mountain', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
