from typing import List, Literal, Optional, Union
from datetime import date
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.product import Product


class Vehicle(Product):
    """
A vehicle is a device that is designed or used to transport people or cargo over land, water, air, or through space.
    """
    class_: Literal['https://schema.org/Vehicle'] = Field(default='https://schema.org/Vehicle', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    vehicleIdentificationNumber: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('vehicleIdentificationNumber', 'https://schema.org/vehicleIdentificationNumber'), serialization_alias='https://schema.org/vehicleIdentificationNumber')
    dateVehicleFirstRegistered: Optional[Union[date, List[date]]] = Field(default=None, validation_alias=AliasChoices('dateVehicleFirstRegistered', 'https://schema.org/dateVehicleFirstRegistered'), serialization_alias='https://schema.org/dateVehicleFirstRegistered')
    callSign: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('callSign', 'https://schema.org/callSign'), serialization_alias='https://schema.org/callSign')
    fuelCapacity: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('fuelCapacity', 'https://schema.org/fuelCapacity'), serialization_alias='https://schema.org/fuelCapacity')
    bodyType: Optional[Union[str, List[str], "QualitativeValue", List["QualitativeValue"], HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('bodyType', 'https://schema.org/bodyType'), serialization_alias='https://schema.org/bodyType')
    @field_serializer('bodyType')
    def bodyType2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    driveWheelConfiguration: Optional[Union[str, List[str], "DriveWheelConfigurationValue", List["DriveWheelConfigurationValue"]]] = Field(default=None, validation_alias=AliasChoices('driveWheelConfiguration', 'https://schema.org/driveWheelConfiguration'), serialization_alias='https://schema.org/driveWheelConfiguration')
    fuelType: Optional[Union[str, List[str], "QualitativeValue", List["QualitativeValue"], HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('fuelType', 'https://schema.org/fuelType'), serialization_alias='https://schema.org/fuelType')
    @field_serializer('fuelType')
    def fuelType2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    trailerWeight: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('trailerWeight', 'https://schema.org/trailerWeight'), serialization_alias='https://schema.org/trailerWeight')
    numberOfPreviousOwners: Optional[Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('numberOfPreviousOwners', 'https://schema.org/numberOfPreviousOwners'), serialization_alias='https://schema.org/numberOfPreviousOwners')
    numberOfAirbags: Optional[Union[float, List[float], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('numberOfAirbags', 'https://schema.org/numberOfAirbags'), serialization_alias='https://schema.org/numberOfAirbags')
    vehicleTransmission: Optional[Union[str, List[str], "QualitativeValue", List["QualitativeValue"], HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('vehicleTransmission', 'https://schema.org/vehicleTransmission'), serialization_alias='https://schema.org/vehicleTransmission')
    @field_serializer('vehicleTransmission')
    def vehicleTransmission2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    payload: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('payload', 'https://schema.org/payload'), serialization_alias='https://schema.org/payload')
    numberOfAxles: Optional[Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('numberOfAxles', 'https://schema.org/numberOfAxles'), serialization_alias='https://schema.org/numberOfAxles')
    tongueWeight: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('tongueWeight', 'https://schema.org/tongueWeight'), serialization_alias='https://schema.org/tongueWeight')
    stupidProperty: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('stupidProperty', 'https://schema.org/stupidProperty'), serialization_alias='https://schema.org/stupidProperty')
    productionDate: Optional[Union[date, List[date]]] = Field(default=None, validation_alias=AliasChoices('productionDate', 'https://schema.org/productionDate'), serialization_alias='https://schema.org/productionDate')
    steeringPosition: Optional[Union["SteeringPositionValue", List["SteeringPositionValue"]]] = Field(default=None, validation_alias=AliasChoices('steeringPosition', 'https://schema.org/steeringPosition'), serialization_alias='https://schema.org/steeringPosition')
    vehicleSeatingCapacity: Optional[Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('vehicleSeatingCapacity', 'https://schema.org/vehicleSeatingCapacity'), serialization_alias='https://schema.org/vehicleSeatingCapacity')
    fuelEfficiency: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('fuelEfficiency', 'https://schema.org/fuelEfficiency'), serialization_alias='https://schema.org/fuelEfficiency')
    numberOfDoors: Optional[Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('numberOfDoors', 'https://schema.org/numberOfDoors'), serialization_alias='https://schema.org/numberOfDoors')
    vehicleSpecialUsage: Optional[Union["CarUsageType", List["CarUsageType"], str, List[str]]] = Field(default=None, validation_alias=AliasChoices('vehicleSpecialUsage', 'https://schema.org/vehicleSpecialUsage'), serialization_alias='https://schema.org/vehicleSpecialUsage')
    seatingCapacity: Optional[Union["QuantitativeValue", List["QuantitativeValue"], float, List[float]]] = Field(default=None, validation_alias=AliasChoices('seatingCapacity', 'https://schema.org/seatingCapacity'), serialization_alias='https://schema.org/seatingCapacity')
    speed: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('speed', 'https://schema.org/speed'), serialization_alias='https://schema.org/speed')
    vehicleInteriorType: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('vehicleInteriorType', 'https://schema.org/vehicleInteriorType'), serialization_alias='https://schema.org/vehicleInteriorType')
    vehicleInteriorColor: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('vehicleInteriorColor', 'https://schema.org/vehicleInteriorColor'), serialization_alias='https://schema.org/vehicleInteriorColor')
    vehicleModelDate: Optional[Union[date, List[date]]] = Field(default=None, validation_alias=AliasChoices('vehicleModelDate', 'https://schema.org/vehicleModelDate'), serialization_alias='https://schema.org/vehicleModelDate')
    vehicleConfiguration: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('vehicleConfiguration', 'https://schema.org/vehicleConfiguration'), serialization_alias='https://schema.org/vehicleConfiguration')
    knownVehicleDamages: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('knownVehicleDamages', 'https://schema.org/knownVehicleDamages'), serialization_alias='https://schema.org/knownVehicleDamages')
    meetsEmissionStandard: Optional[Union[str, List[str], "QualitativeValue", List["QualitativeValue"], HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('meetsEmissionStandard', 'https://schema.org/meetsEmissionStandard'), serialization_alias='https://schema.org/meetsEmissionStandard')
    @field_serializer('meetsEmissionStandard')
    def meetsEmissionStandard2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    weightTotal: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('weightTotal', 'https://schema.org/weightTotal'), serialization_alias='https://schema.org/weightTotal')
    numberOfForwardGears: Optional[Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('numberOfForwardGears', 'https://schema.org/numberOfForwardGears'), serialization_alias='https://schema.org/numberOfForwardGears')
    modelDate: Optional[Union[date, List[date]]] = Field(default=None, validation_alias=AliasChoices('modelDate', 'https://schema.org/modelDate'), serialization_alias='https://schema.org/modelDate')
    purchaseDate: Optional[Union[date, List[date]]] = Field(default=None, validation_alias=AliasChoices('purchaseDate', 'https://schema.org/purchaseDate'), serialization_alias='https://schema.org/purchaseDate')
    vehicleEngine: Optional[Union["EngineSpecification", List["EngineSpecification"]]] = Field(default=None, validation_alias=AliasChoices('vehicleEngine', 'https://schema.org/vehicleEngine'), serialization_alias='https://schema.org/vehicleEngine')
    emissionsCO2: Optional[Union[float, List[float]]] = Field(default=None, validation_alias=AliasChoices('emissionsCO2', 'https://schema.org/emissionsCO2'), serialization_alias='https://schema.org/emissionsCO2')
    wheelbase: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('wheelbase', 'https://schema.org/wheelbase'), serialization_alias='https://schema.org/wheelbase')
    mileageFromOdometer: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('mileageFromOdometer', 'https://schema.org/mileageFromOdometer'), serialization_alias='https://schema.org/mileageFromOdometer')
    cargoVolume: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('cargoVolume', 'https://schema.org/cargoVolume'), serialization_alias='https://schema.org/cargoVolume')
    fuelConsumption: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('fuelConsumption', 'https://schema.org/fuelConsumption'), serialization_alias='https://schema.org/fuelConsumption')
    accelerationTime: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('accelerationTime', 'https://schema.org/accelerationTime'), serialization_alias='https://schema.org/accelerationTime')
