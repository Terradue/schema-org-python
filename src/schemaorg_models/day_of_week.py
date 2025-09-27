from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class DayOfWeek(Enumeration):
    """
The day of the week for which these opening hours are valid.
    """
    type_: Literal['https://schema.org/DayOfWeek'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/DayOfWeek'),serialization_alias='class') # type: ignore
