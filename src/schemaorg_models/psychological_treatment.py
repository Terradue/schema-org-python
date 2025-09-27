from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.therapeutic_procedure import TherapeuticProcedure


class PsychologicalTreatment(TherapeuticProcedure):
    """
A process of care relying upon counseling, dialogue and communication  aimed at improving a mental health condition without use of drugs.
    """
    type_: Literal['https://schema.org/PsychologicalTreatment'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/PsychologicalTreatment'),serialization_alias='class') # type: ignore
