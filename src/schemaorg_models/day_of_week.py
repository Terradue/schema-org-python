from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class DayOfWeek(Enumeration):
    """
The day of the week for which these opening hours are valid.
    """
    class_: Literal['https://schema.org/DayOfWeek'] = Field(default='https://schema.org/DayOfWeek', alias='class', serialization_alias='class') # type: ignore
