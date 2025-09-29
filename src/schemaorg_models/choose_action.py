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
from .assess_action import AssessAction
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .thing import Thing

class ChooseAction(AssessAction):
    '''
    The act of expressing a preference from a set of options or a large or unbounded set of choices/options.

    Attributes:
        option: A sub property of object. The options subject to this action.
        actionOption: A sub property of object. The options subject to this action.
    '''
    class_: Literal['https://schema.org/ChooseAction'] = Field( # type: ignore
        default='https://schema.org/ChooseAction',
        alias='@type',
        serialization_alias='@type'
    )
    option: Optional[Union[str, List[str], 'Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'option',
            'https://schema.org/option'
        ),
        serialization_alias='https://schema.org/option'
    )
    actionOption: Optional[Union[str, List[str], 'Thing', List['Thing']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'actionOption',
            'https://schema.org/actionOption'
        ),
        serialization_alias='https://schema.org/actionOption'
    )
