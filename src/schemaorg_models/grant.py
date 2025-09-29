from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .product import Product
    from .medical_entity import MedicalEntity
    from .event import Event
    from .person import Person
    from .creative_work import CreativeWork
    from .organization import Organization
    from .bio_chem_entity import BioChemEntity

class Grant(Intangible):
    '''
    A grant, typically financial or otherwise quantifiable, of resources. Typically a [[funder]] sponsors some [[MonetaryAmount]] to an [[Organization]] or [[Person]],
    sometimes not necessarily via a dedicated or long-lived [[Project]], resulting in one or more outputs, or [[fundedItem]]s. For financial sponsorship, indicate the [[funder]] of a [[MonetaryGrant]]. For non-financial support, indicate [[sponsor]] of [[Grant]]s of resources (e.g. office space).

Grants support  activities directed towards some agreed collective goals, often but not always organized as [[Project]]s. Long-lived projects are sometimes sponsored by a variety of grants over time, but it is also common for a project to be associated with a single grant.

The amount of a [[Grant]] is represented using [[amount]] as a [[MonetaryAmount]].
    

    Attributes:
        sponsor: A person or organization that supports a thing through a pledge, promise, or financial contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.
        funder: A person or organization that supports (sponsors) something through some kind of financial contribution.
        fundedItem: Indicates something directly or indirectly funded or sponsored through a [[Grant]]. See also [[ownershipFundingInfo]].
    '''
    class_: Literal['https://schema.org/Grant'] = Field( # type: ignore
        default='https://schema.org/Grant',
        alias='@type',
        serialization_alias='@type'
    )
    sponsor: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    funder: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    fundedItem: Optional[Union['Event', List['Event'], 'MedicalEntity', List['MedicalEntity'], 'BioChemEntity', List['BioChemEntity'], 'Product', List['Product'], 'CreativeWork', List['CreativeWork'], 'Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
