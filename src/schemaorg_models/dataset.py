from typing import Union, List, Optional
from datetime import datetime
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.property import Property
from schemaorg_models.data_catalog import DataCatalog
from schemaorg_models.defined_term import DefinedTerm

class Dataset(CreativeWork):
    """
A dataset contained in this catalog.
    """
    issn: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('issn', 'https://schema.org/issn'),serialization_alias='https://schema.org/issn')
    variableMeasured: Optional[Union[Property, List[Property], "StatisticalVariable", List["StatisticalVariable"], str, List[str], "PropertyValue", List["PropertyValue"]]] = Field(default=None,validation_alias=AliasChoices('variableMeasured', 'https://schema.org/variableMeasured'),serialization_alias='https://schema.org/variableMeasured')
    includedDataCatalog: Optional[Union[DataCatalog, List[DataCatalog]]] = Field(default=None,validation_alias=AliasChoices('includedDataCatalog', 'https://schema.org/includedDataCatalog'),serialization_alias='https://schema.org/includedDataCatalog')
    includedInDataCatalog: Optional[Union[DataCatalog, List[DataCatalog]]] = Field(default=None,validation_alias=AliasChoices('includedInDataCatalog', 'https://schema.org/includedInDataCatalog'),serialization_alias='https://schema.org/includedInDataCatalog')
    catalog: Optional[Union[DataCatalog, List[DataCatalog]]] = Field(default=None,validation_alias=AliasChoices('catalog', 'https://schema.org/catalog'),serialization_alias='https://schema.org/catalog')
    variablesMeasured: Optional[Union[str, List[str], "PropertyValue", List["PropertyValue"]]] = Field(default=None,validation_alias=AliasChoices('variablesMeasured', 'https://schema.org/variablesMeasured'),serialization_alias='https://schema.org/variablesMeasured')
    distribution: Optional[Union["DataDownload", List["DataDownload"]]] = Field(default=None,validation_alias=AliasChoices('distribution', 'https://schema.org/distribution'),serialization_alias='https://schema.org/distribution')
    measurementTechnique: Optional[Union[DefinedTerm, List[DefinedTerm], "MeasurementMethodEnum", List["MeasurementMethodEnum"], str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('measurementTechnique', 'https://schema.org/measurementTechnique'),serialization_alias='https://schema.org/measurementTechnique')
    @field_serializer('measurementTechnique')
    def measurementTechnique2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    datasetTimeInterval: Optional[Union[datetime, List[datetime]]] = Field(default=None,validation_alias=AliasChoices('datasetTimeInterval', 'https://schema.org/datasetTimeInterval'),serialization_alias='https://schema.org/datasetTimeInterval')
    measurementMethod: Optional[Union[DefinedTerm, List[DefinedTerm], str, List[str], "MeasurementMethodEnum", List["MeasurementMethodEnum"], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('measurementMethod', 'https://schema.org/measurementMethod'),serialization_alias='https://schema.org/measurementMethod')
    @field_serializer('measurementMethod')
    def measurementMethod2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

