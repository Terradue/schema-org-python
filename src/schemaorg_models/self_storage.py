from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class SelfStorage(LocalBusiness):
    """
A self-storage facility.
    """
    type_: Literal['https://schema.org/SelfStorage'] = Field(default='https://schema.org/SelfStorage', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
