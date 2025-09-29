from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .enumeration import Enumeration

class DeliveryMethod(Enumeration):
    '''
    A delivery method is a standardized procedure for transferring the product or service to the destination of fulfillment chosen by the customer. Delivery methods are characterized by the means of transportation used, and by the organization or group that is the contracting party for the sending organization or person.\
\
Commonly used values:\
\
* http://purl.org/goodrelations/v1#DeliveryModeDirectDownload\
* http://purl.org/goodrelations/v1#DeliveryModeFreight\
* http://purl.org/goodrelations/v1#DeliveryModeMail\
* http://purl.org/goodrelations/v1#DeliveryModeOwnFleet\
* http://purl.org/goodrelations/v1#DeliveryModePickUp\
* http://purl.org/goodrelations/v1#DHL\
* http://purl.org/goodrelations/v1#FederalExpress\
* http://purl.org/goodrelations/v1#UPS
        
    '''
    class_: Literal['https://schema.org/DeliveryMethod'] = Field( # type: ignore
        default='https://schema.org/DeliveryMethod',
        alias='@type',
        serialization_alias='@type'
    )
