from typing import Literal
from pydantic import Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class AutoWash(AutomotiveBusiness):
    """
A car wash business.
    """
    class_: Literal['https://schema.org/AutoWash'] = Field(default='https://schema.org/AutoWash', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
