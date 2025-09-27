from typing import Literal
from pydantic import Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class AutoRepair(AutomotiveBusiness):
    """
Car repair business.
    """
    class_: Literal['https://schema.org/AutoRepair'] = Field(default='https://schema.org/AutoRepair', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
