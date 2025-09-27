from typing import List, Literal, Optional, Union
from datetime import datetime
from pydantic import AliasChoices, Field
from schemaorg_models.structured_value import StructuredValue

from schemaorg_models.organization import Organization
from schemaorg_models.person import Person
from schemaorg_models.product import Product
from schemaorg_models.service import Service

class OwnershipInfo(StructuredValue):
    """
A structured value providing information about when a certain organization or person owned a certain product.
    """
    type_: Literal['https://schema.org/OwnershipInfo'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/OwnershipInfo'),serialization_alias='class') # type: ignore
    ownedFrom: Optional[Union[datetime, List[datetime]]] = Field(default=None,validation_alias=AliasChoices('ownedFrom', 'https://schema.org/ownedFrom'),serialization_alias='https://schema.org/ownedFrom')
    acquiredFrom: Optional[Union[Organization, List[Organization], Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('acquiredFrom', 'https://schema.org/acquiredFrom'),serialization_alias='https://schema.org/acquiredFrom')
    typeOfGood: Optional[Union[Product, List[Product], Service, List[Service]]] = Field(default=None,validation_alias=AliasChoices('typeOfGood', 'https://schema.org/typeOfGood'),serialization_alias='https://schema.org/typeOfGood')
    ownedThrough: Optional[Union[datetime, List[datetime]]] = Field(default=None,validation_alias=AliasChoices('ownedThrough', 'https://schema.org/ownedThrough'),serialization_alias='https://schema.org/ownedThrough')
