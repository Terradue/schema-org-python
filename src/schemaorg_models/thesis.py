from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.creative_work import CreativeWork


class Thesis(CreativeWork):
    """
A thesis or dissertation document submitted in support of candidature for an academic degree or professional qualification.
    """
    class_: Literal['https://schema.org/Thesis'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    inSupportOf: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('inSupportOf', 'https://schema.org/inSupportOf'), serialization_alias='https://schema.org/inSupportOf')
