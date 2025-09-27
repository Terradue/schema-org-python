from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.intangible import Intangible


class DefinedTerm(Intangible):
    """
A word, name, acronym, phrase, etc. with a formal definition. Often used in the context of category or subject classification, glossaries or dictionaries, product or creative work types, etc. Use the name property for the term being defined, use termCode if the term has an alpha-numeric code allocated, use description to provide the definition of the term.
    """
    type_: Literal['https://schema.org/DefinedTerm'] = Field(default='https://schema.org/DefinedTerm', alias='@type', serialization_alias='@type') # type: ignore
    termCode: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('termCode', 'https://schema.org/termCode'), serialization_alias='https://schema.org/termCode')
    inDefinedTermSet: Optional[Union[HttpUrl, List[HttpUrl], "DefinedTermSet", List["DefinedTermSet"]]] = Field(default=None, validation_alias=AliasChoices('inDefinedTermSet', 'https://schema.org/inDefinedTermSet'), serialization_alias='https://schema.org/inDefinedTermSet')
    @field_serializer('inDefinedTermSet')
    def inDefinedTermSet2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

