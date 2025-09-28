from __future__ import annotations

from .enumeration import Enumeration    

from pydantic import (
    Field
)
from typing import (
    Literal
)

class BusinessFunction(Enumeration):
    """
The business function specifies the type of activity or access (i.e., the bundle of rights) offered by the organization or business person through the offer. Typical are sell, rental or lease, maintenance or repair, manufacture / produce, recycle / dispose, engineering / construction, or installation. Proprietary specifications of access rights are also instances of this class.\
\
Commonly used values:\
\
* http://purl.org/goodrelations/v1#ConstructionInstallation\
* http://purl.org/goodrelations/v1#Dispose\
* http://purl.org/goodrelations/v1#LeaseOut\
* http://purl.org/goodrelations/v1#Maintain\
* http://purl.org/goodrelations/v1#ProvideService\
* http://purl.org/goodrelations/v1#Repair\
* http://purl.org/goodrelations/v1#Sell\
* http://purl.org/goodrelations/v1#Buy
        
    """
    class_: Literal['https://schema.org/BusinessFunction'] = Field( # type: ignore
        default='https://schema.org/BusinessFunction',
        alias='@type',
        serialization_alias='@type'
    )
