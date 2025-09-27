from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.role import Role

from schemaorg_models.language import Language

class LinkRole(Role):
    """
A Role that represents a Web link, e.g. as expressed via the 'url' property. Its linkRelationship property can indicate URL-based and plain textual link types, e.g. those in IANA link registry or others such as 'amphtml'. This structure provides a placeholder where details from HTML's link element can be represented outside of HTML, e.g. in JSON-LD feeds.
    """
    class_: Literal['https://schema.org/LinkRole'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    inLanguage: Optional[Union[str, List[str], Language, List[Language]]] = Field(default=None,validation_alias=AliasChoices('inLanguage', 'https://schema.org/inLanguage'), serialization_alias='https://schema.org/inLanguage')
    linkRelationship: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('linkRelationship', 'https://schema.org/linkRelationship'), serialization_alias='https://schema.org/linkRelationship')
