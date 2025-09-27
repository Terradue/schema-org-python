from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.software_application import SoftwareApplication


class MobileApplication(SoftwareApplication):
    """
A software application designed specifically to work well on a mobile device such as a telephone.
    """
    type_: Literal['https://schema.org/MobileApplication'] = Field(default='https://schema.org/MobileApplication', alias='@type', serialization_alias='@type') # type: ignore
    carrierRequirements: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('carrierRequirements', 'https://schema.org/carrierRequirements'), serialization_alias='https://schema.org/carrierRequirements')
