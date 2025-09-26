from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.scholarly_article import ScholarlyArticle


class MedicalScholarlyArticle(ScholarlyArticle):
    """
A scholarly article in the medical domain.
    """
    publicationType: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('publicationType', 'https://schema.org/publicationType'),serialization_alias='https://schema.org/publicationType')
