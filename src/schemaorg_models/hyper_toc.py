from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.hyper_toc_entry import HyperTocEntry
from schemaorg_models.media_object import MediaObject

class HyperToc(CreativeWork):
    """
A HyperToc represents a hypertext table of contents for complex media objects, such as [[VideoObject]], [[AudioObject]]. Items in the table of contents are indicated using the [[tocEntry]] property, and typed [[HyperTocEntry]]. For cases where the same larger work is split into multiple files, [[associatedMedia]] can be used on individual [[HyperTocEntry]] items.
    """
    type_: Literal['https://schema.org/HyperToc'] = Field(default='https://schema.org/HyperToc', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    tocEntry: Optional[Union[HyperTocEntry, List[HyperTocEntry]]] = Field(default=None, validation_alias=AliasChoices('tocEntry', 'https://schema.org/tocEntry'), serialization_alias='https://schema.org/tocEntry')
    associatedMedia: Optional[Union[MediaObject, List[MediaObject]]] = Field(default=None, validation_alias=AliasChoices('associatedMedia', 'https://schema.org/associatedMedia'), serialization_alias='https://schema.org/associatedMedia')
