from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.article import Article


class TechArticle(Article):
    """
A technical article - Example: How-to (task) topics, step-by-step, procedural troubleshooting, specifications, etc.
    """
    proficiencyLevel: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('proficiencyLevel', 'https://schema.org/proficiencyLevel'),serialization_alias='https://schema.org/proficiencyLevel')
    dependencies: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('dependencies', 'https://schema.org/dependencies'),serialization_alias='https://schema.org/dependencies')
