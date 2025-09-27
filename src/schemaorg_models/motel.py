from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.lodging_business import LodgingBusiness


class Motel(LodgingBusiness):
    """
A motel.
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    """
    type_: Literal['https://schema.org/Motel'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Motel'),serialization_alias='class') # type: ignore
