from typing import Literal
from pydantic import Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class AutoRental(AutomotiveBusiness):
    """
A car rental business.
    """
    class_: Literal['https://schema.org/AutoRental'] = Field(default='https://schema.org/AutoRental', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
