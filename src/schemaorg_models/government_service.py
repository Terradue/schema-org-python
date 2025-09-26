from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.service import Service

from schemaorg_models.administrative_area import AdministrativeArea
from schemaorg_models.organization import Organization

class GovernmentService(Service):
    """
A service provided by a government organization, e.g. food stamps, veterans benefits, etc.
    """
    jurisdiction: Optional[Union[str, List[str], AdministrativeArea, List[AdministrativeArea]]] = Field(default=None,validation_alias=AliasChoices('jurisdiction', 'https://schema.org/jurisdiction'),serialization_alias='https://schema.org/jurisdiction')
    serviceOperator: Optional[Union[Organization, List[Organization]]] = Field(default=None,validation_alias=AliasChoices('serviceOperator', 'https://schema.org/serviceOperator'),serialization_alias='https://schema.org/serviceOperator')
