from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class Thesis(CreativeWork):
    """
A thesis or dissertation document submitted in support of candidature for an academic degree or professional qualification.
    """
    type_: Literal['https://schema.org/Thesis'] = Field(default='https://schema.org/Thesis', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
    inSupportOf: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('inSupportOf', 'https://schema.org/inSupportOf'), serialization_alias='https://schema.org/inSupportOf')
