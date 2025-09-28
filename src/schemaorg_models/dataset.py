from __future__ import annotations
from datetime import (
    datetime
)
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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .statistical_variable import StatisticalVariable
    from .measurement_method_enum import MeasurementMethodEnum
    from .defined_term import DefinedTerm
    from .property import Property
    from .property_value import PropertyValue
    from .data_download import DataDownload
    from .data_catalog import DataCatalog

class Dataset(CreativeWork):
    """
A dataset contained in this catalog.
    """
    class_: Literal['https://schema.org/Dataset'] = Field( # type: ignore
        default='https://schema.org/Dataset',
        alias='@type',
        serialization_alias='@type'
    )
    issn: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'issn',
            'https://schema.org/issn'
        ),
        serialization_alias='https://schema.org/issn'
    )
    variableMeasured: Optional[Union[Property, List[Property], StatisticalVariable, List[StatisticalVariable], str, List[str], PropertyValue, List[PropertyValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'variableMeasured',
            'https://schema.org/variableMeasured'
        ),
        serialization_alias='https://schema.org/variableMeasured'
    )
    includedDataCatalog: Optional[Union[DataCatalog, List[DataCatalog]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'includedDataCatalog',
            'https://schema.org/includedDataCatalog'
        ),
        serialization_alias='https://schema.org/includedDataCatalog'
    )
    includedInDataCatalog: Optional[Union[DataCatalog, List[DataCatalog]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'includedInDataCatalog',
            'https://schema.org/includedInDataCatalog'
        ),
        serialization_alias='https://schema.org/includedInDataCatalog'
    )
    catalog: Optional[Union[DataCatalog, List[DataCatalog]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'catalog',
            'https://schema.org/catalog'
        ),
        serialization_alias='https://schema.org/catalog'
    )
    variablesMeasured: Optional[Union[str, List[str], PropertyValue, List[PropertyValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'variablesMeasured',
            'https://schema.org/variablesMeasured'
        ),
        serialization_alias='https://schema.org/variablesMeasured'
    )
    distribution: Optional[Union[DataDownload, List[DataDownload]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'distribution',
            'https://schema.org/distribution'
        ),
        serialization_alias='https://schema.org/distribution'
    )
    measurementTechnique: Optional[Union[DefinedTerm, List[DefinedTerm], MeasurementMethodEnum, List[MeasurementMethodEnum], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementTechnique',
            'https://schema.org/measurementTechnique'
        ),
        serialization_alias='https://schema.org/measurementTechnique'
    )
    datasetTimeInterval: Optional[Union[datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'datasetTimeInterval',
            'https://schema.org/datasetTimeInterval'
        ),
        serialization_alias='https://schema.org/datasetTimeInterval'
    )
    measurementMethod: Optional[Union[DefinedTerm, List[DefinedTerm], str, List[str], MeasurementMethodEnum, List[MeasurementMethodEnum], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'measurementMethod',
            'https://schema.org/measurementMethod'
        ),
        serialization_alias='https://schema.org/measurementMethod'
    )
