from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.local_business import LocalBusiness

from schemaorg_models.archive_component import ArchiveComponent

class ArchiveOrganization(LocalBusiness):
    """
An organization with archival holdings. An organization which keeps and preserves archival material and typically makes it accessible to the public.
    """
    class_: Literal['https://schema.org/ArchiveOrganization'] = Field(default='https://schema.org/ArchiveOrganization', alias='class', serialization_alias='class') # type: ignore
    archiveHeld: Optional[Union[ArchiveComponent, List[ArchiveComponent]]] = Field(default=None, validation_alias=AliasChoices('archiveHeld', 'https://schema.org/archiveHeld'), serialization_alias='https://schema.org/archiveHeld')
