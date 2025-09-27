from typing import List, Literal, Optional, Union
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.media_object import MediaObject

from schemaorg_models.defined_term import DefinedTerm
from schemaorg_models.measurement_method_enum import MeasurementMethodEnum

class DataDownload(MediaObject):
    """
All or part of a [[Dataset]] in downloadable form. 
    """
    class_: Literal['https://schema.org/DataDownload'] = Field(default='https://schema.org/DataDownload', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    measurementMethod: Optional[Union[DefinedTerm, List[DefinedTerm], str, List[str], MeasurementMethodEnum, List[MeasurementMethodEnum], HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('measurementMethod', 'https://schema.org/measurementMethod'), serialization_alias='https://schema.org/measurementMethod')
    @field_serializer('measurementMethod')
    def measurementMethod2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    measurementTechnique: Optional[Union[DefinedTerm, List[DefinedTerm], MeasurementMethodEnum, List[MeasurementMethodEnum], str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('measurementTechnique', 'https://schema.org/measurementTechnique'), serialization_alias='https://schema.org/measurementTechnique')
    @field_serializer('measurementTechnique')
    def measurementTechnique2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

