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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .computer_language import ComputerLanguage
    from .software_application import SoftwareApplication

class SoftwareSourceCode(CreativeWork):
    '''
    Computer programming source code. Example: Full (compile ready) solutions, code snippet samples, scripts, templates.

    Attributes:
        sampleType: What type of code sample: full (compile ready) solution, code snippet, inline code, scripts, template.
        runtimePlatform: Runtime platform or script interpreter dependencies (example: Java v1, Python 2.3, .NET Framework 3.0).
        codeRepository: Link to the repository where the un-compiled, human readable code and related code is located (SVN, GitHub, CodePlex).
        codeSampleType: What type of code sample: full (compile ready) solution, code snippet, inline code, scripts, template.
        runtime: Runtime platform or script interpreter dependencies (example: Java v1, Python 2.3, .NET Framework 3.0).
        targetProduct: Target Operating System / Product to which the code applies.  If applies to several versions, just the product name can be used.
        programmingLanguage: The computer programming language.
    '''
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
    targetProduct: Optional[Union['SoftwareApplication', List['SoftwareApplication']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'targetProduct',
            'https://schema.org/targetProduct'
        ),
        serialization_alias='https://schema.org/targetProduct'
    )
    programmingLanguage: Optional[Union[str, List[str], 'ComputerLanguage', List['ComputerLanguage']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'programmingLanguage',
            'https://schema.org/programmingLanguage'
        ),
        serialization_alias='https://schema.org/programmingLanguage'
    )
