from typing import List, Literal, Optional, Union
from datetime import datetime
from pydantic import AliasChoices, Field
from schemaorg_models.event import Event


class DeliveryEvent(Event):
    """
An event involving the delivery of an item.
    """
    class_: Literal['https://schema.org/DeliveryEvent'] = Field(default='https://schema.org/DeliveryEvent', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    availableThrough: Optional[Union[datetime, List[datetime]]] = Field(default=None, validation_alias=AliasChoices('availableThrough', 'https://schema.org/availableThrough'), serialization_alias='https://schema.org/availableThrough')
    availableFrom: Optional[Union[datetime, List[datetime]]] = Field(default=None, validation_alias=AliasChoices('availableFrom', 'https://schema.org/availableFrom'), serialization_alias='https://schema.org/availableFrom')
    hasDeliveryMethod: Optional[Union["DeliveryMethod", List["DeliveryMethod"]]] = Field(default=None, validation_alias=AliasChoices('hasDeliveryMethod', 'https://schema.org/hasDeliveryMethod'), serialization_alias='https://schema.org/hasDeliveryMethod')
    accessCode: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('accessCode', 'https://schema.org/accessCode'), serialization_alias='https://schema.org/accessCode')
