from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.lodging_business import LodgingBusiness


class Resort(LodgingBusiness):
    """
A resort is a place used for relaxation or recreation, attracting visitors for holidays or vacations. Resorts are places, towns or sometimes commercial establishments operated by a single company (source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Resort">http://en.wikipedia.org/wiki/Resort</a>).
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.
    
    """
    type_: Literal['https://schema.org/Resort'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Resort'),serialization_alias='class') # type: ignore
