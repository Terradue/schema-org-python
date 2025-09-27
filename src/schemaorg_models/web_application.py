from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.software_application import SoftwareApplication


class WebApplication(SoftwareApplication):
    """
Web applications.
    """
    class_: Literal['https://schema.org/WebApplication'] = Field(default='https://schema.org/WebApplication', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    browserRequirements: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('browserRequirements', 'https://schema.org/browserRequirements'), serialization_alias='https://schema.org/browserRequirements')
