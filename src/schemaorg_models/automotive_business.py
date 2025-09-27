from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class AutomotiveBusiness(LocalBusiness):
    """
Car repair, sales, or parts.
    """
    class_: Literal['https://schema.org/AutomotiveBusiness'] = Field(default='https://schema.org/AutomotiveBusiness', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
