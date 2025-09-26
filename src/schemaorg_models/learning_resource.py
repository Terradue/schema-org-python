from typing import Union, List, Optional
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.defined_term import DefinedTerm
from schemaorg_models.alignment_object import AlignmentObject

class LearningResource(CreativeWork):
    """
The LearningResource type can be used to indicate [[CreativeWork]]s (whether physical or digital) that have a particular and explicit orientation towards learning, education, skill acquisition, and other educational purposes.

[[LearningResource]] is expected to be used as an addition to a primary type such as [[Book]], [[VideoObject]], [[Product]] etc.

[[EducationEvent]] serves a similar purpose for event-like things (e.g. a [[Trip]]). A [[LearningResource]] may be created as a result of an [[EducationEvent]], for example by recording one.
    """
    educationalLevel: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], DefinedTerm, List[DefinedTerm]]] = Field(default=None,validation_alias=AliasChoices('educationalLevel', 'https://schema.org/educationalLevel'),serialization_alias='https://schema.org/educationalLevel')
    @field_serializer('educationalLevel')
    def educationalLevel2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    educationalAlignment: Optional[Union[AlignmentObject, List[AlignmentObject]]] = Field(default=None,validation_alias=AliasChoices('educationalAlignment', 'https://schema.org/educationalAlignment'),serialization_alias='https://schema.org/educationalAlignment')
    teaches: Optional[Union[DefinedTerm, List[DefinedTerm], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('teaches', 'https://schema.org/teaches'),serialization_alias='https://schema.org/teaches')
    educationalUse: Optional[Union[DefinedTerm, List[DefinedTerm], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('educationalUse', 'https://schema.org/educationalUse'),serialization_alias='https://schema.org/educationalUse')
    competencyRequired: Optional[Union[DefinedTerm, List[DefinedTerm], str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('competencyRequired', 'https://schema.org/competencyRequired'),serialization_alias='https://schema.org/competencyRequired')
    @field_serializer('competencyRequired')
    def competencyRequired2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    learningResourceType: Optional[Union[DefinedTerm, List[DefinedTerm], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('learningResourceType', 'https://schema.org/learningResourceType'),serialization_alias='https://schema.org/learningResourceType')
    assesses: Optional[Union[DefinedTerm, List[DefinedTerm], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('assesses', 'https://schema.org/assesses'),serialization_alias='https://schema.org/assesses')
