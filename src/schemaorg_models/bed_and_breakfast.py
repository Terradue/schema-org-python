from typing import Literal
from pydantic import Field
from schemaorg_models.lodging_business import LodgingBusiness


class BedAndBreakfast(LodgingBusiness):
    """
Bed and breakfast.
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    """
    class_: Literal['https://schema.org/BedAndBreakfast'] = Field('class', alias='class', serialization_alias='class') # type: ignore
