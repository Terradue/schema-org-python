from typing import Literal
from pydantic import Field
from schemaorg_models.government_building import GovernmentBuilding


class Embassy(GovernmentBuilding):
    """
An embassy.
    """
    class_: Literal['https://schema.org/Embassy'] = Field(default='https://schema.org/Embassy', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
