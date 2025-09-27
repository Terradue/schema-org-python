from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class StatusEnumeration(Enumeration):
    """
Lists or enumerations dealing with status types.
    """
    class_: Literal['https://schema.org/StatusEnumeration'] = Field(default='https://schema.org/StatusEnumeration', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
