from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .measurement_method_enum import MeasurementMethodEnum
from .media_object import MediaObject
from .defined_term import DefinedTerm

class DataDownload(MediaObject):
    """
All or part of a [[Dataset]] in downloadable form. 
    """
    class_: Literal['https://schema.org/DataDownload'] = Field( # type: ignore
        default='https://schema.org/DataDownload',
        alias='@type',
        serialization_alias='@type'
    )
    measurementMethod: Optional[Union[DefinedTerm, List[DefinedTerm], str, List[str], MeasurementMethodEnum, List[MeasurementMethodEnum], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementMethod',
            'https://schema.org/measurementMethod'
        ),
        serialization_alias='https://schema.org/measurementMethod'
    )
    measurementTechnique: Optional[Union[DefinedTerm, List[DefinedTerm], MeasurementMethodEnum, List[MeasurementMethodEnum], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementTechnique',
            'https://schema.org/measurementTechnique'
        ),
        serialization_alias='https://schema.org/measurementTechnique'
    )
