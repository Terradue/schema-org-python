from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.tech_article import TechArticle


class APIReference(TechArticle):
    """
Reference documentation for application programming interfaces (APIs).
    """
    class_: Literal['https://schema.org/APIReference'] = Field(default='https://schema.org/APIReference', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    assembly: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('assembly', 'https://schema.org/assembly'), serialization_alias='https://schema.org/assembly')
    targetPlatform: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('targetPlatform', 'https://schema.org/targetPlatform'), serialization_alias='https://schema.org/targetPlatform')
    executableLibraryName: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('executableLibraryName', 'https://schema.org/executableLibraryName'), serialization_alias='https://schema.org/executableLibraryName')
    assemblyVersion: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('assemblyVersion', 'https://schema.org/assemblyVersion'), serialization_alias='https://schema.org/assemblyVersion')
    programmingModel: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('programmingModel', 'https://schema.org/programmingModel'), serialization_alias='https://schema.org/programmingModel')
