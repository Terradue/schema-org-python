from typing import Literal
from pydantic import Field
from schemaorg_models.medical_indication import MedicalIndication


class ApprovedIndication(MedicalIndication):
    """
An indication for a medical therapy that has been formally specified or approved by a regulatory body that regulates use of the therapy; for example, the US FDA approves indications for most drugs in the US.
    """
    class_: Literal['https://schema.org/ApprovedIndication'] = Field('class', alias='class', serialization_alias='class') # type: ignore
