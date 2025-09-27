from typing import Literal
from pydantic import Field
from schemaorg_models.lodging_business import LodgingBusiness


class Motel(LodgingBusiness):
    """
A motel.
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    """
    class_: Literal['https://schema.org/Motel'] = Field(default='https://schema.org/Motel', alias='@type', serialization_alias='@type') # type: ignore
