from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .media_object import MediaObject
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .defined_term import DefinedTerm
    from .measurement_method_enum import MeasurementMethodEnum

class DataDownload(MediaObject):
    '''
    All or part of a [[Dataset]] in downloadable form. 

    Attributes:
        measurementMethod: A subproperty of [[measurementTechnique]] that can be used for specifying specific methods, in particular via [[MeasurementMethodEnum]].
        measurementTechnique: A technique, method or technology used in an [[Observation]], [[StatisticalVariable]] or [[Dataset]] (or [[DataDownload]], [[DataCatalog]]), corresponding to the method used for measuring the corresponding variable(s) (for datasets, described using [[variableMeasured]]; for [[Observation]], a [[StatisticalVariable]]). Often but not necessarily each [[variableMeasured]] will have an explicit representation as (or mapping to) an property such as those defined in Schema.org, or other RDF vocabularies and "knowledge graphs". In that case the subproperty of [[variableMeasured]] called [[measuredProperty]] is applicable.
    
The [[measurementTechnique]] property helps when extra clarification is needed about how a [[measuredProperty]] was measured. This is oriented towards scientific and scholarly dataset publication but may have broader applicability; it is not intended as a full representation of measurement, but can often serve as a high level summary for dataset discovery. 

For example, if [[variableMeasured]] is: molecule concentration, [[measurementTechnique]] could be: "mass spectrometry" or "nmr spectroscopy" or "colorimetry" or "immunofluorescence". If the [[variableMeasured]] is "depression rating", the [[measurementTechnique]] could be "Zung Scale" or "HAM-D" or "Beck Depression Inventory". 

If there are several [[variableMeasured]] properties recorded for some given data object, use a [[PropertyValue]] for each [[variableMeasured]] and attach the corresponding [[measurementTechnique]]. The value can also be from an enumeration, organized as a [[MeasurementMetholdEnumeration]].
    '''
    class_: Literal['https://schema.org/DataDownload'] = Field( # type: ignore
        default='https://schema.org/DataDownload',
        alias='@type',
        serialization_alias='@type'
    )
    measurementMethod: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str], 'MeasurementMethodEnum', List['MeasurementMethodEnum'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    measurementTechnique: Optional[Union['DefinedTerm', List['DefinedTerm'], 'MeasurementMethodEnum', List['MeasurementMethodEnum'], str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
