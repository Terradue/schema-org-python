from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class BusinessEntityType(Enumeration):
    """
A business entity type is a conceptual entity representing the legal form, the size, the main line of business, the position in the value chain, or any combination thereof, of an organization or business person.\
\
Commonly used values:\
\
* http://purl.org/goodrelations/v1#Business\
* http://purl.org/goodrelations/v1#Enduser\
* http://purl.org/goodrelations/v1#PublicInstitution\
* http://purl.org/goodrelations/v1#Reseller
    
    """
    type_: Literal['https://schema.org/BusinessEntityType'] = Field(default='https://schema.org/BusinessEntityType', alias='@type', serialization_alias='@type') # type: ignore
