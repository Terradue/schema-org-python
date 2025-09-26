from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.software_application import SoftwareApplication


class MobileApplication(SoftwareApplication):
    """
A software application designed specifically to work well on a mobile device such as a telephone.
    """
    carrierRequirements: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('carrierRequirements', 'https://schema.org/carrierRequirements'),serialization_alias='https://schema.org/carrierRequirements')
