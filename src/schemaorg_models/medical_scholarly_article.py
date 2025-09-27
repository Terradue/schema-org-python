from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.scholarly_article import ScholarlyArticle


class MedicalScholarlyArticle(ScholarlyArticle):
    """
A scholarly article in the medical domain.
    """
    type_: Literal['https://schema.org/MedicalScholarlyArticle'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/MedicalScholarlyArticle'),serialization_alias='class') # type: ignore
    publicationType: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('publicationType', 'https://schema.org/publicationType'),serialization_alias='https://schema.org/publicationType')
