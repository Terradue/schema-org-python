from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class NonprofitType(Enumeration):
    """
NonprofitType enumerates several kinds of official non-profit types of which a non-profit organization can be.
    """
    type_: Literal['https://schema.org/NonprofitType'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/NonprofitType'),serialization_alias='class') # type: ignore
