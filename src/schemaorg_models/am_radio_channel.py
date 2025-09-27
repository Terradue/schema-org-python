from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.radio_channel import RadioChannel


class AMRadioChannel(RadioChannel):
    """
A radio channel that uses AM.
    """
    type_: Literal['https://schema.org/AMRadioChannel'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AMRadioChannel'),serialization_alias='class') # type: ignore
