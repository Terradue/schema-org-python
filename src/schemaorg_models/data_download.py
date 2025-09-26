from typing import Union, List, Optional
from pydantic import AliasChoices, Field, HttpUrl
from schemaorg_models.media_object import MediaObject

from schemaorg_models.defined_term import DefinedTerm
from schemaorg_models.measurement_method_enum import MeasurementMethodEnum

class DataDownload(MediaObject):
    """
All or part of a [[Dataset]] in downloadable form. 
    """
    measurementMethod: Optional[Union[DefinedTerm, List[DefinedTerm], str, List[str], MeasurementMethodEnum, List[MeasurementMethodEnum], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('measurementMethod', 'https://schema.org/measurementMethod'),serialization_alias='https://schema.org/measurementMethod')
    measurementTechnique: Optional[Union[DefinedTerm, List[DefinedTerm], MeasurementMethodEnum, List[MeasurementMethodEnum], str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('measurementTechnique', 'https://schema.org/measurementTechnique'),serialization_alias='https://schema.org/measurementTechnique')
