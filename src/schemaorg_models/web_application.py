from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.software_application import SoftwareApplication


class WebApplication(SoftwareApplication):
    """
Web applications.
    """
    type_: Literal['https://schema.org/WebApplication'] = Field(default='https://schema.org/WebApplication', alias='@type', serialization_alias='@type') # type: ignore
    browserRequirements: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('browserRequirements', 'https://schema.org/browserRequirements'), serialization_alias='https://schema.org/browserRequirements')
