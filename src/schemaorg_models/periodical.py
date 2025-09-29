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
from .creative_work_series import CreativeWorkSeries

class Periodical(CreativeWorkSeries):
    '''
    A publication in any medium issued in successive parts bearing numerical or chronological designations and intended to continue indefinitely, such as a magazine, scholarly journal, or newspaper.\
\
See also [blog post](https://blog.schema.org/2014/09/02/schema-org-support-for-bibliographic-relationships-and-periodicals/).
    '''
    class_: Literal['https://schema.org/Periodical'] = Field( # type: ignore
        default='https://schema.org/Periodical',
        alias='@type',
        serialization_alias='@type'
    )
