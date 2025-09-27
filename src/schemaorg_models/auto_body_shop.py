from typing import Literal
from pydantic import Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class AutoBodyShop(AutomotiveBusiness):
    """
Auto body shop.
    """
    class_: Literal['https://schema.org/AutoBodyShop'] = Field(default='https://schema.org/AutoBodyShop', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
