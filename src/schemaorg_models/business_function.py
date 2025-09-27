from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class BusinessFunction(Enumeration):
    """
The business function specifies the type of activity or access (i.e., the bundle of rights) offered by the organization or business person through the offer. Typical are sell, rental or lease, maintenance or repair, manufacture / produce, recycle / dispose, engineering / construction, or installation. Proprietary specifications of access rights are also instances of this class.\
\
Commonly used values:\
\
* http://purl.org/goodrelations/v1#ConstructionInstallation\
* http://purl.org/goodrelations/v1#Dispose\
* http://purl.org/goodrelations/v1#LeaseOut\
* http://purl.org/goodrelations/v1#Maintain\
* http://purl.org/goodrelations/v1#ProvideService\
* http://purl.org/goodrelations/v1#Repair\
* http://purl.org/goodrelations/v1#Sell\
* http://purl.org/goodrelations/v1#Buy
        
    """
    class_: Literal['https://schema.org/BusinessFunction'] = Field(default='https://schema.org/BusinessFunction', alias='class', serialization_alias='class') # type: ignore
