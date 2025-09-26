from typing import Union, List, Optional
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.defined_term import DefinedTerm

class DataCatalog(CreativeWork):
    """
A collection of datasets.
    """
    measurementTechnique: Optional[Union[DefinedTerm, List[DefinedTerm], "MeasurementMethodEnum", List["MeasurementMethodEnum"], str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('measurementTechnique', 'https://schema.org/measurementTechnique'),serialization_alias='https://schema.org/measurementTechnique')
    @field_serializer('measurementTechnique')
    def measurementTechnique2str(self, val) -> str:
        if isinstance(val, HttpUrl): ### This magic! If isinstance(val, HttpUrl) - error
            return str(val)
        return val

    dataset: Optional[Union["Dataset", List["Dataset"]]] = Field(default=None,validation_alias=AliasChoices('dataset', 'https://schema.org/dataset'),serialization_alias='https://schema.org/dataset')
    measurementMethod: Optional[Union[DefinedTerm, List[DefinedTerm], str, List[str], "MeasurementMethodEnum", List["MeasurementMethodEnum"], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('measurementMethod', 'https://schema.org/measurementMethod'),serialization_alias='https://schema.org/measurementMethod')
    @field_serializer('measurementMethod')
    def measurementMethod2str(self, val) -> str:
        if isinstance(val, HttpUrl): ### This magic! If isinstance(val, HttpUrl) - error
            return str(val)
        return val

