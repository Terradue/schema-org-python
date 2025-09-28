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
from .defined_term import DefinedTerm
from .creative_work import CreativeWork
from .dataset import Dataset

class DataCatalog(CreativeWork):
    """
A collection of datasets.
    """
    class_: Literal['https://schema.org/DataCatalog'] = Field( # type: ignore
        default='https://schema.org/DataCatalog',
        alias='@type',
        serialization_alias='@type'
    )
    measurementTechnique: Optional[Union[DefinedTerm, List[DefinedTerm], MeasurementMethodEnum, List[MeasurementMethodEnum], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementTechnique',
            'https://schema.org/measurementTechnique'
        ),
        serialization_alias='https://schema.org/measurementTechnique'
    )
    dataset: Optional[Union[Dataset, List[Dataset]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'dataset',
            'https://schema.org/dataset'
        ),
        serialization_alias='https://schema.org/dataset'
    )
    measurementMethod: Optional[Union[DefinedTerm, List[DefinedTerm], str, List[str], MeasurementMethodEnum, List[MeasurementMethodEnum], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementMethod',
            'https://schema.org/measurementMethod'
        ),
        serialization_alias='https://schema.org/measurementMethod'
    )
