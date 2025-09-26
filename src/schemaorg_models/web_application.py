from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.software_application import SoftwareApplication


class WebApplication(SoftwareApplication):
    """
Web applications.
    """
    browserRequirements: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('browserRequirements', 'https://schema.org/browserRequirements'),serialization_alias='https://schema.org/browserRequirements')
