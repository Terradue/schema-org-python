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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .software_application import SoftwareApplication
    from .computer_language import ComputerLanguage

class SoftwareSourceCode(CreativeWork):
    """
Computer programming source code. Example: Full (compile ready) solutions, code snippet samples, scripts, templates.
    """
    class_: Literal['https://schema.org/SoftwareSourceCode'] = Field( # type: ignore
        default='https://schema.org/SoftwareSourceCode',
        alias='@type',
        serialization_alias='@type'
    )
    sampleType: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sampleType',
            'https://schema.org/sampleType'
        ),
        serialization_alias='https://schema.org/sampleType'
    )
    runtimePlatform: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'runtimePlatform',
            'https://schema.org/runtimePlatform'
        ),
        serialization_alias='https://schema.org/runtimePlatform'
    )
    codeRepository: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'codeRepository',
            'https://schema.org/codeRepository'
        ),
        serialization_alias='https://schema.org/codeRepository'
    )
    codeSampleType: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'codeSampleType',
            'https://schema.org/codeSampleType'
        ),
        serialization_alias='https://schema.org/codeSampleType'
    )
    runtime: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'runtime',
            'https://schema.org/runtime'
        ),
        serialization_alias='https://schema.org/runtime'
    )
    targetProduct: Optional[Union["SoftwareApplication", List["SoftwareApplication"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'targetProduct',
            'https://schema.org/targetProduct'
        ),
        serialization_alias='https://schema.org/targetProduct'
    )
    programmingLanguage: Optional[Union[str, List[str], "ComputerLanguage", List["ComputerLanguage"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'programmingLanguage',
            'https://schema.org/programmingLanguage'
        ),
        serialization_alias='https://schema.org/programmingLanguage'
    )
