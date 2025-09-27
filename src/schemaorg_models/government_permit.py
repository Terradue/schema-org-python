from typing import Literal
from pydantic import Field
from schemaorg_models.permit import Permit


class GovernmentPermit(Permit):
    """
A permit issued by a government agency.
    """
    class_: Literal['https://schema.org/GovernmentPermit'] = Field(default='https://schema.org/GovernmentPermit', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
