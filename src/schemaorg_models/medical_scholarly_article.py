from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.scholarly_article import ScholarlyArticle


class MedicalScholarlyArticle(ScholarlyArticle):
    """
A scholarly article in the medical domain.
    """
    class_: Literal['https://schema.org/MedicalScholarlyArticle'] = Field(default='https://schema.org/MedicalScholarlyArticle', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    publicationType: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('publicationType', 'https://schema.org/publicationType'), serialization_alias='https://schema.org/publicationType')
