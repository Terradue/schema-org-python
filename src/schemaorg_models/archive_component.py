from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.place import Place

class ArchiveComponent(CreativeWork):
    """
An intangible type to be applied to any archive content, carrying with it a set of properties required to describe archival items and collections.
    """
    type_: Literal['https://schema.org/ArchiveComponent'] = Field(default='https://schema.org/ArchiveComponent', alias='@type', serialization_alias='@type') # type: ignore
    holdingArchive: Optional[Union["ArchiveOrganization", List["ArchiveOrganization"]]] = Field(default=None, validation_alias=AliasChoices('holdingArchive', 'https://schema.org/holdingArchive'), serialization_alias='https://schema.org/holdingArchive')
    itemLocation: Optional[Union["PostalAddress", List["PostalAddress"], str, List[str], Place, List[Place]]] = Field(default=None, validation_alias=AliasChoices('itemLocation', 'https://schema.org/itemLocation'), serialization_alias='https://schema.org/itemLocation')
