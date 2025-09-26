from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.publication_issue import PublicationIssue

from schemaorg_models.person import Person

class ComicIssue(PublicationIssue):
    """
Individual comic issues are serially published as
    	part of a larger series. For the sake of consistency, even one-shot issues
    	belong to a series comprised of a single issue. All comic issues can be
    	uniquely identified by: the combination of the name and volume number of the
    	series to which the issue belongs; the issue number; and the variant
    	description of the issue (if any).
    """
    variantCover: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('variantCover', 'https://schema.org/variantCover'),serialization_alias='https://schema.org/variantCover')
    colorist: Optional[Union[Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('colorist', 'https://schema.org/colorist'),serialization_alias='https://schema.org/colorist')
    artist: Optional[Union[Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('artist', 'https://schema.org/artist'),serialization_alias='https://schema.org/artist')
    penciler: Optional[Union[Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('penciler', 'https://schema.org/penciler'),serialization_alias='https://schema.org/penciler')
    inker: Optional[Union[Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('inker', 'https://schema.org/inker'),serialization_alias='https://schema.org/inker')
    letterer: Optional[Union[Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('letterer', 'https://schema.org/letterer'),serialization_alias='https://schema.org/letterer')
