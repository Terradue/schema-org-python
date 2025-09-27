from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.article import Article


class TechArticle(Article):
    """
A technical article - Example: How-to (task) topics, step-by-step, procedural troubleshooting, specifications, etc.
    """
    class_: Literal['https://schema.org/TechArticle'] = Field(default='https://schema.org/TechArticle', alias='class', serialization_alias='class') # type: ignore
    proficiencyLevel: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('proficiencyLevel', 'https://schema.org/proficiencyLevel'), serialization_alias='https://schema.org/proficiencyLevel')
    dependencies: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('dependencies', 'https://schema.org/dependencies'), serialization_alias='https://schema.org/dependencies')
