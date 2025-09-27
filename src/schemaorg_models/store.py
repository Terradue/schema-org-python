from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class Store(LocalBusiness):
    """
A retail good store.
    """
    class_: Literal['https://schema.org/Store'] = Field('class', alias='class', serialization_alias='class') # type: ignore
