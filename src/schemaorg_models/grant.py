from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible

from schemaorg_models.organization import Organization
from schemaorg_models.person import Person
from schemaorg_models.event import Event
from schemaorg_models.medical_entity import MedicalEntity
from schemaorg_models.bio_chem_entity import BioChemEntity
from schemaorg_models.product import Product
from schemaorg_models.creative_work import CreativeWork

class Grant(Intangible):
    """
A grant, typically financial or otherwise quantifiable, of resources. Typically a [[funder]] sponsors some [[MonetaryAmount]] to an [[Organization]] or [[Person]],
    sometimes not necessarily via a dedicated or long-lived [[Project]], resulting in one or more outputs, or [[fundedItem]]s. For financial sponsorship, indicate the [[funder]] of a [[MonetaryGrant]]. For non-financial support, indicate [[sponsor]] of [[Grant]]s of resources (e.g. office space).

Grants support  activities directed towards some agreed collective goals, often but not always organized as [[Project]]s. Long-lived projects are sometimes sponsored by a variety of grants over time, but it is also common for a project to be associated with a single grant.

The amount of a [[Grant]] is represented using [[amount]] as a [[MonetaryAmount]].
    
    """
    type_: Literal['https://schema.org/Grant'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Grant'),serialization_alias='class') # type: ignore
    sponsor: Optional[Union[Organization, List[Organization], Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('sponsor', 'https://schema.org/sponsor'),serialization_alias='https://schema.org/sponsor')
    funder: Optional[Union[Organization, List[Organization], Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('funder', 'https://schema.org/funder'),serialization_alias='https://schema.org/funder')
    fundedItem: Optional[Union[Event, List[Event], MedicalEntity, List[MedicalEntity], BioChemEntity, List[BioChemEntity], Product, List[Product], CreativeWork, List[CreativeWork], Person, List[Person], Organization, List[Organization]]] = Field(default=None,validation_alias=AliasChoices('fundedItem', 'https://schema.org/fundedItem'),serialization_alias='https://schema.org/fundedItem')
