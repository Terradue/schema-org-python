from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.create_action import CreateAction

from schemaorg_models.language import Language

class WriteAction(CreateAction):
    """
The act of authoring written creative content.
    """
    type_: Literal['https://schema.org/WriteAction'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/WriteAction'),serialization_alias='class') # type: ignore
    language: Optional[Union[Language, List[Language]]] = Field(default=None,validation_alias=AliasChoices('language', 'https://schema.org/language'),serialization_alias='https://schema.org/language')
    inLanguage: Optional[Union[str, List[str], Language, List[Language]]] = Field(default=None,validation_alias=AliasChoices('inLanguage', 'https://schema.org/inLanguage'),serialization_alias='https://schema.org/inLanguage')
