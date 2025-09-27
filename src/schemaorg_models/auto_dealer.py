from typing import Literal
from pydantic import Field
from schemaorg_models.automotive_business import AutomotiveBusiness


class AutoDealer(AutomotiveBusiness):
    """
An car dealership.
    """
    type_: Literal['https://schema.org/AutoDealer'] = Field(default='https://schema.org/AutoDealer', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
