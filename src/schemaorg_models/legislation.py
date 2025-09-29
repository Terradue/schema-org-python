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
from .creative_work import CreativeWork
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .legal_force_status import LegalForceStatus
    from .administrative_area import AdministrativeArea
    from .organization import Organization
    from .category_code import CategoryCode
    from .person import Person

class Legislation(CreativeWork):
    '''
    A legal document such as an act, decree, bill, etc. (enforceable or not) or a component of a legal act (like an article).

    Attributes:
        legislationApplies: Indicates that this legislation (or part of a legislation) somehow transfers another legislation in a different legislative context. This is an informative link, and it has no legal value. For legally-binding links of transposition, use the <a href="/legislationTransposes">legislationTransposes</a> property. For example an informative consolidated law of a European Union's member state "applies" the consolidated version of the European Directive implemented in it.
        legislationCountersignedBy: The person or organization that countersigned the legislation. Depending on the legal context, a countersignature can indicate that the signed authority undertakes to assume responsibility for texts emanating from a person who is inviolable and irresponsible, (for example a King, Grand Duc or President), or that the authority is in charge of the implementation of the text.
        legislationChanges: Another legislation that this legislation changes. This encompasses the notions of amendment, replacement, correction, repeal, or other types of change. This may be a direct change (textual or non-textual amendment) or a consequential or indirect change. The property is to be used to express the existence of a change relationship between two acts rather than the existence of a consolidated version of the text that shows the result of the change. For consolidation relationships, use the <a href="/legislationConsolidates">legislationConsolidates</a> property.
        legislationCommences: Another legislation that this one sets into force.
        legislationRepeals: Another legislation that this legislation repeals (cancels, abrogates).
        legislationType: The type of the legislation. Examples of values are "law", "act", "directive", "decree", "regulation", "statutory instrument", "loi organique", "règlement grand-ducal", etc., depending on the country.
        jurisdiction: Indicates a legal jurisdiction, e.g. of some legislation, or where some government service is based.
        legislationJurisdiction: The jurisdiction from which the legislation originates.
        legislationCorrects: Another legislation in which this one introduces textual changes, like correction of spelling mistakes, with no legal impact (for modifications that have legal impact, use <a href="/legislationAmends">legislationAmends</a>).
        legislationTransposes: Indicates that this legislation (or part of legislation) fulfills the objectives set by another legislation, by passing appropriate implementation measures. Typically, some legislations of European Union's member states or regions transpose European Directives. This indicates a legally binding link between the 2 legislations.
        legislationDate: The date of adoption or signature of the legislation. This is the date at which the text is officially aknowledged to be a legislation, even though it might not even be published or in force.
        legislationEnsuresImplementationOf: Indicates that this Legislation ensures the implementation of another Legislation, for example by modifying national legislations so that they do not contradict to an EU regulation or decision. This implies a legal meaning. Transpositions of EU Directive should be captured with <a href="/legislationTransposes">legislationTransposes</a>.
        legislationPassedBy: The person or organization that originally passed or made the law: typically parliament (for primary legislation) or government (for secondary legislation). This indicates the "legal author" of the law, as opposed to its physical author.
        legislationConsolidates: Indicates another legislation taken into account in this consolidated legislation (which is usually the product of an editorial process that revises the legislation). This property should be used multiple times to refer to both the original version or the previous consolidated version, and to the legislations making the change.
        legislationDateOfApplicability: The date at which the Legislation becomes applicable. This can sometimes be distinct from the date of entry into force : a text may come in force today, and state it will become applicable in 3 months.
        legislationIdentifier: An identifier for the legislation. This can be either a string-based identifier, like the CELEX at EU level or the NOR in France, or a web-based, URL/URI identifier, like an ELI (European Legislation Identifier) or an URN-Lex.
        legislationLegalForce: Whether the legislation is currently in force, not in force, or partially in force.
        legislationAmends: Another legislation that this legislation amends, introducing legal changes.
        legislationDateVersion: The point-in-time at which the provided description of the legislation is valid (e.g.: when looking at the law on the 2016-04-07 (= dateVersion), I get the consolidation of 2015-04-12 of the "National Insurance Contributions Act 2015")
        legislationResponsible: An individual or organization that has some kind of responsibility for the legislation. Typically the ministry who is/was in charge of elaborating the legislation, or the adressee for potential questions about the legislation once it is published.
    '''
    class_: Literal['https://schema.org/Legislation'] = Field( # type: ignore
        default='https://schema.org/Legislation',
        alias='@type',
        serialization_alias='@type'
    )
    legislationApplies: Optional[Union['Legislation', List['Legislation']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legislationApplies',
            'https://schema.org/legislationApplies'
        ),
        serialization_alias='https://schema.org/legislationApplies'
    )
    legislationCountersignedBy: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legislationCountersignedBy',
            'https://schema.org/legislationCountersignedBy'
        ),
        serialization_alias='https://schema.org/legislationCountersignedBy'
    )
    legislationChanges: Optional[Union['Legislation', List['Legislation']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legislationChanges',
            'https://schema.org/legislationChanges'
        ),
        serialization_alias='https://schema.org/legislationChanges'
    )
    legislationCommences: Optional[Union['Legislation', List['Legislation']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legislationCommences',
            'https://schema.org/legislationCommences'
        ),
        serialization_alias='https://schema.org/legislationCommences'
    )
    legislationRepeals: Optional[Union['Legislation', List['Legislation']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legislationRepeals',
            'https://schema.org/legislationRepeals'
        ),
        serialization_alias='https://schema.org/legislationRepeals'
    )
    legislationType: Optional[Union[str, List[str], 'CategoryCode', List['CategoryCode']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legislationType',
            'https://schema.org/legislationType'
        ),
        serialization_alias='https://schema.org/legislationType'
    )
    jurisdiction: Optional[Union[str, List[str], 'AdministrativeArea', List['AdministrativeArea']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'jurisdiction',
            'https://schema.org/jurisdiction'
        ),
        serialization_alias='https://schema.org/jurisdiction'
    )
    legislationJurisdiction: Optional[Union[str, List[str], 'AdministrativeArea', List['AdministrativeArea']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legislationJurisdiction',
            'https://schema.org/legislationJurisdiction'
        ),
        serialization_alias='https://schema.org/legislationJurisdiction'
    )
    legislationCorrects: Optional[Union['Legislation', List['Legislation']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legislationCorrects',
            'https://schema.org/legislationCorrects'
        ),
        serialization_alias='https://schema.org/legislationCorrects'
    )
    legislationTransposes: Optional[Union['Legislation', List['Legislation']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legislationTransposes',
            'https://schema.org/legislationTransposes'
        ),
        serialization_alias='https://schema.org/legislationTransposes'
    )
    legislationDate: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legislationDate',
            'https://schema.org/legislationDate'
        ),
        serialization_alias='https://schema.org/legislationDate'
    )
    legislationEnsuresImplementationOf: Optional[Union['Legislation', List['Legislation']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legislationEnsuresImplementationOf',
            'https://schema.org/legislationEnsuresImplementationOf'
        ),
        serialization_alias='https://schema.org/legislationEnsuresImplementationOf'
    )
    legislationPassedBy: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legislationPassedBy',
            'https://schema.org/legislationPassedBy'
        ),
        serialization_alias='https://schema.org/legislationPassedBy'
    )
    legislationConsolidates: Optional[Union['Legislation', List['Legislation']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legislationConsolidates',
            'https://schema.org/legislationConsolidates'
        ),
        serialization_alias='https://schema.org/legislationConsolidates'
    )
    legislationDateOfApplicability: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legislationDateOfApplicability',
            'https://schema.org/legislationDateOfApplicability'
        ),
        serialization_alias='https://schema.org/legislationDateOfApplicability'
    )
    legislationIdentifier: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legislationIdentifier',
            'https://schema.org/legislationIdentifier'
        ),
        serialization_alias='https://schema.org/legislationIdentifier'
    )
    legislationLegalForce: Optional[Union['LegalForceStatus', List['LegalForceStatus']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legislationLegalForce',
            'https://schema.org/legislationLegalForce'
        ),
        serialization_alias='https://schema.org/legislationLegalForce'
    )
    legislationAmends: Optional[Union['Legislation', List['Legislation']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legislationAmends',
            'https://schema.org/legislationAmends'
        ),
        serialization_alias='https://schema.org/legislationAmends'
    )
    legislationDateVersion: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legislationDateVersion',
            'https://schema.org/legislationDateVersion'
        ),
        serialization_alias='https://schema.org/legislationDateVersion'
    )
    legislationResponsible: Optional[Union['Person', List['Person'], 'Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'legislationResponsible',
            'https://schema.org/legislationResponsible'
        ),
        serialization_alias='https://schema.org/legislationResponsible'
    )
