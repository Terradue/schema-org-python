from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.creative_work import CreativeWork

from schemaorg_models.defined_term import DefinedTerm

class DataCatalog(CreativeWork):
    """
A collection of datasets.
    """
    type_: Literal['https://schema.org/DataCatalog'] = Field(default='https://schema.org/DataCatalog', alias='@type', serialization_alias='@type') # type: ignore
    measurementTechnique: Optional[Union[DefinedTerm, List[DefinedTerm], "MeasurementMethodEnum", List["MeasurementMethodEnum"], str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('measurementTechnique', 'https://schema.org/measurementTechnique'), serialization_alias='https://schema.org/measurementTechnique')
    @field_serializer('measurementTechnique')
    def measurementTechnique2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    dataset: Optional[Union["Dataset", List["Dataset"]]] = Field(default=None, validation_alias=AliasChoices('dataset', 'https://schema.org/dataset'), serialization_alias='https://schema.org/dataset')
    measurementMethod: Optional[Union[DefinedTerm, List[DefinedTerm], str, List[str], "MeasurementMethodEnum", List["MeasurementMethodEnum"], HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('measurementMethod', 'https://schema.org/measurementMethod'), serialization_alias='https://schema.org/measurementMethod')
    @field_serializer('measurementMethod')
    def measurementMethod2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

