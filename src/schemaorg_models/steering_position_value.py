from typing import Literal
from pydantic import Field
from schemaorg_models.qualitative_value import QualitativeValue


class SteeringPositionValue(QualitativeValue):
    """
A value indicating a steering position.
    """
    class_: Literal['https://schema.org/SteeringPositionValue'] = Field(default='https://schema.org/SteeringPositionValue', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
