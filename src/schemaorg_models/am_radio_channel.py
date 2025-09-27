from typing import Literal
from pydantic import Field
from schemaorg_models.radio_channel import RadioChannel


class AMRadioChannel(RadioChannel):
    """
A radio channel that uses AM.
    """
    class_: Literal['https://schema.org/AMRadioChannel'] = Field(default='https://schema.org/AMRadioChannel', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
