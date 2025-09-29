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
from .product import Product
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .car_usage_type import CarUsageType
    from .quantitative_value import QuantitativeValue
    from .qualitative_value import QualitativeValue
    from .engine_specification import EngineSpecification
    from .steering_position_value import SteeringPositionValue
    from .drive_wheel_configuration_value import DriveWheelConfigurationValue

class Vehicle(Product):
    '''
    A vehicle is a device that is designed or used to transport people or cargo over land, water, air, or through space.

    Attributes:
        vehicleIdentificationNumber: The Vehicle Identification Number (VIN) is a unique serial number used by the automotive industry to identify individual motor vehicles.
        dateVehicleFirstRegistered: The date of the first registration of the vehicle with the respective public authorities.
        callSign: A [callsign](https://en.wikipedia.org/wiki/Call_sign), as used in broadcasting and radio communications to identify people, radio and TV stations, or vehicles.
        fuelCapacity: The capacity of the fuel tank or in the case of electric cars, the battery. If there are multiple components for storage, this should indicate the total of all storage of the same type.\
\
Typical unit code(s): LTR for liters, GLL of US gallons, GLI for UK / imperial gallons, AMH for ampere-hours (for electrical vehicles).
        bodyType: Indicates the design and body style of the vehicle (e.g. station wagon, hatchback, etc.).
        driveWheelConfiguration: The drive wheel configuration, i.e. which roadwheels will receive torque from the vehicle's engine via the drivetrain.
        fuelType: The type of fuel suitable for the engine or engines of the vehicle. If the vehicle has only one engine, this property can be attached directly to the vehicle.
        trailerWeight: The permitted weight of a trailer attached to the vehicle.\
\
Typical unit code(s): KGM for kilogram, LBR for pound\
* Note 1: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.\
* Note 2: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]].\
* Note 3: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges.
        numberOfPreviousOwners: The number of owners of the vehicle, including the current one.\
\
Typical unit code(s): C62.
        numberOfAirbags: The number or type of airbags in the vehicle.
        vehicleTransmission: The type of component used for transmitting the power from a rotating power source to the wheels or other relevant component(s) ("gearbox" for cars).
        payload: The permitted weight of passengers and cargo, EXCLUDING the weight of the empty vehicle.\
\
Typical unit code(s): KGM for kilogram, LBR for pound\
\
* Note 1: Many databases specify the permitted TOTAL weight instead, which is the sum of [[weight]] and [[payload]]\
* Note 2: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.\
* Note 3: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]].\
* Note 4: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges.
        numberOfAxles: The number of axles.\
\
Typical unit code(s): C62.
        tongueWeight: The permitted vertical load (TWR) of a trailer attached to the vehicle. Also referred to as Tongue Load Rating (TLR) or Vertical Load Rating (VLR).\
\
Typical unit code(s): KGM for kilogram, LBR for pound\
\
* Note 1: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.\
* Note 2: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]].\
* Note 3: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges.
        stupidProperty: This is a StupidProperty! - for testing only.
        productionDate: The date of production of the item, e.g. vehicle.
        steeringPosition: The position of the steering wheel or similar device (mostly for cars).
        vehicleSeatingCapacity: The number of passengers that can be seated in the vehicle, both in terms of the physical space available, and in terms of limitations set by law.\
\
Typical unit code(s): C62 for persons.
        fuelEfficiency: The distance traveled per unit of fuel used; most commonly miles per gallon (mpg) or kilometers per liter (km/L).\
\
* Note 1: There are unfortunately no standard unit codes for miles per gallon or kilometers per liter. Use [[unitText]] to indicate the unit of measurement, e.g. mpg or km/L.\
* Note 2: There are two ways of indicating the fuel consumption, [[fuelConsumption]] (e.g. 8 liters per 100 km) and [[fuelEfficiency]] (e.g. 30 miles per gallon). They are reciprocal.\
* Note 3: Often, the absolute value is useful only when related to driving speed ("at 80 km/h") or usage pattern ("city traffic"). You can use [[valueReference]] to link the value for the fuel economy to another value.
        numberOfDoors: The number of doors.\
\
Typical unit code(s): C62.
        vehicleSpecialUsage: Indicates whether the vehicle has been used for special purposes, like commercial rental, driving school, or as a taxi. The legislation in many countries requires this information to be revealed when offering a car for sale.
        seatingCapacity: The number of persons that can be seated (e.g. in a vehicle), both in terms of the physical space available, and in terms of limitations set by law.\
\
Typical unit code(s): C62 for persons.
        speed: The speed range of the vehicle. If the vehicle is powered by an engine, the upper limit of the speed range (indicated by [[maxValue]]) should be the maximum speed achievable under regular conditions.\
\
Typical unit code(s): KMH for km/h, HM for mile per hour (0.447 04 m/s), KNT for knot\
\
*Note 1: Use [[minValue]] and [[maxValue]] to indicate the range. Typically, the minimal value is zero.\
* Note 2: There are many different ways of measuring the speed range. You can link to information about how the given value has been determined using the [[valueReference]] property.
        vehicleInteriorType: The type or material of the interior of the vehicle (e.g. synthetic fabric, leather, wood, etc.). While most interior types are characterized by the material used, an interior type can also be based on vehicle usage or target audience.
        vehicleInteriorColor: The color or color combination of the interior of the vehicle.
        vehicleModelDate: The release date of a vehicle model (often used to differentiate versions of the same make and model).
        vehicleConfiguration: A short text indicating the configuration of the vehicle, e.g. '5dr hatchback ST 2.5 MT 225 hp' or 'limited edition'.
        knownVehicleDamages: A textual description of known damages, both repaired and unrepaired.
        meetsEmissionStandard: Indicates that the vehicle meets the respective emission standard.
        weightTotal: The permitted total weight of the loaded vehicle, including passengers and cargo and the weight of the empty vehicle.\
\
Typical unit code(s): KGM for kilogram, LBR for pound\
\
* Note 1: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.\
* Note 2: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]].\
* Note 3: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges.
        numberOfForwardGears: The total number of forward gears available for the transmission system of the vehicle.\
\
Typical unit code(s): C62.
        modelDate: The release date of a vehicle model (often used to differentiate versions of the same make and model).
        purchaseDate: The date the item, e.g. vehicle, was purchased by the current owner.
        vehicleEngine: Information about the engine or engines of the vehicle.
        emissionsCO2: The CO2 emissions in g/km. When used in combination with a QuantitativeValue, put "g/km" into the unitText property of that value, since there is no UN/CEFACT Common Code for "g/km".
        wheelbase: The distance between the centers of the front and rear wheels.\
\
Typical unit code(s): CMT for centimeters, MTR for meters, INH for inches, FOT for foot/feet.
        mileageFromOdometer: The total distance travelled by the particular vehicle since its initial production, as read from its odometer.\
\
Typical unit code(s): KMT for kilometers, SMI for statute miles.
        cargoVolume: The available volume for cargo or luggage. For automobiles, this is usually the trunk volume.\
\
Typical unit code(s): LTR for liters, FTQ for cubic foot/feet\
\
Note: You can use [[minValue]] and [[maxValue]] to indicate ranges.
        fuelConsumption: The amount of fuel consumed for traveling a particular distance or temporal duration with the given vehicle (e.g. liters per 100 km).\
\
* Note 1: There are unfortunately no standard unit codes for liters per 100 km.  Use [[unitText]] to indicate the unit of measurement, e.g. L/100 km.\
* Note 2: There are two ways of indicating the fuel consumption, [[fuelConsumption]] (e.g. 8 liters per 100 km) and [[fuelEfficiency]] (e.g. 30 miles per gallon). They are reciprocal.\
* Note 3: Often, the absolute value is useful only when related to driving speed ("at 80 km/h") or usage pattern ("city traffic"). You can use [[valueReference]] to link the value for the fuel consumption to another value.
        accelerationTime: The time needed to accelerate the vehicle from a given start velocity to a given target velocity.\
\
Typical unit code(s): SEC for seconds\
\
* Note: There are unfortunately no standard unit codes for seconds/0..100 km/h or seconds/0..60 mph. Simply use "SEC" for seconds and indicate the velocities in the [[name]] of the [[QuantitativeValue]], or use [[valueReference]] with a [[QuantitativeValue]] of 0..60 mph or 0..100 km/h to specify the reference speeds.
    '''
    class_: Literal['https://schema.org/Vehicle'] = Field( # type: ignore
        default='https://schema.org/Vehicle',
        alias='@type',
        serialization_alias='@type'
    )
    vehicleIdentificationNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'vehicleIdentificationNumber',
            'https://schema.org/vehicleIdentificationNumber'
        ),
        serialization_alias='https://schema.org/vehicleIdentificationNumber'
    )
    dateVehicleFirstRegistered: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'dateVehicleFirstRegistered',
            'https://schema.org/dateVehicleFirstRegistered'
        ),
        serialization_alias='https://schema.org/dateVehicleFirstRegistered'
    )
    callSign: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'callSign',
            'https://schema.org/callSign'
        ),
        serialization_alias='https://schema.org/callSign'
    )
    fuelCapacity: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'fuelCapacity',
            'https://schema.org/fuelCapacity'
        ),
        serialization_alias='https://schema.org/fuelCapacity'
    )
    bodyType: Optional[Union[str, List[str], 'QualitativeValue', List['QualitativeValue'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'bodyType',
            'https://schema.org/bodyType'
        ),
        serialization_alias='https://schema.org/bodyType'
    )
    driveWheelConfiguration: Optional[Union[str, List[str], 'DriveWheelConfigurationValue', List['DriveWheelConfigurationValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'driveWheelConfiguration',
            'https://schema.org/driveWheelConfiguration'
        ),
        serialization_alias='https://schema.org/driveWheelConfiguration'
    )
    fuelType: Optional[Union[str, List[str], 'QualitativeValue', List['QualitativeValue'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'fuelType',
            'https://schema.org/fuelType'
        ),
        serialization_alias='https://schema.org/fuelType'
    )
    trailerWeight: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'trailerWeight',
            'https://schema.org/trailerWeight'
        ),
        serialization_alias='https://schema.org/trailerWeight'
    )
    numberOfPreviousOwners: Optional[Union[float, List[float], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfPreviousOwners',
            'https://schema.org/numberOfPreviousOwners'
        ),
        serialization_alias='https://schema.org/numberOfPreviousOwners'
    )
    numberOfAirbags: Optional[Union[float, List[float], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfAirbags',
            'https://schema.org/numberOfAirbags'
        ),
        serialization_alias='https://schema.org/numberOfAirbags'
    )
    vehicleTransmission: Optional[Union[str, List[str], 'QualitativeValue', List['QualitativeValue'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'vehicleTransmission',
            'https://schema.org/vehicleTransmission'
        ),
        serialization_alias='https://schema.org/vehicleTransmission'
    )
    payload: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'payload',
            'https://schema.org/payload'
        ),
        serialization_alias='https://schema.org/payload'
    )
    numberOfAxles: Optional[Union[float, List[float], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfAxles',
            'https://schema.org/numberOfAxles'
        ),
        serialization_alias='https://schema.org/numberOfAxles'
    )
    tongueWeight: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'tongueWeight',
            'https://schema.org/tongueWeight'
        ),
        serialization_alias='https://schema.org/tongueWeight'
    )
    stupidProperty: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'stupidProperty',
            'https://schema.org/stupidProperty'
        ),
        serialization_alias='https://schema.org/stupidProperty'
    )
    productionDate: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'productionDate',
            'https://schema.org/productionDate'
        ),
        serialization_alias='https://schema.org/productionDate'
    )
    steeringPosition: Optional[Union['SteeringPositionValue', List['SteeringPositionValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'steeringPosition',
            'https://schema.org/steeringPosition'
        ),
        serialization_alias='https://schema.org/steeringPosition'
    )
    vehicleSeatingCapacity: Optional[Union[float, List[float], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'vehicleSeatingCapacity',
            'https://schema.org/vehicleSeatingCapacity'
        ),
        serialization_alias='https://schema.org/vehicleSeatingCapacity'
    )
    fuelEfficiency: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'fuelEfficiency',
            'https://schema.org/fuelEfficiency'
        ),
        serialization_alias='https://schema.org/fuelEfficiency'
    )
    numberOfDoors: Optional[Union[float, List[float], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfDoors',
            'https://schema.org/numberOfDoors'
        ),
        serialization_alias='https://schema.org/numberOfDoors'
    )
    vehicleSpecialUsage: Optional[Union['CarUsageType', List['CarUsageType'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'vehicleSpecialUsage',
            'https://schema.org/vehicleSpecialUsage'
        ),
        serialization_alias='https://schema.org/vehicleSpecialUsage'
    )
    seatingCapacity: Optional[Union['QuantitativeValue', List['QuantitativeValue'], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'seatingCapacity',
            'https://schema.org/seatingCapacity'
        ),
        serialization_alias='https://schema.org/seatingCapacity'
    )
    speed: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'speed',
            'https://schema.org/speed'
        ),
        serialization_alias='https://schema.org/speed'
    )
    vehicleInteriorType: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'vehicleInteriorType',
            'https://schema.org/vehicleInteriorType'
        ),
        serialization_alias='https://schema.org/vehicleInteriorType'
    )
    vehicleInteriorColor: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'vehicleInteriorColor',
            'https://schema.org/vehicleInteriorColor'
        ),
        serialization_alias='https://schema.org/vehicleInteriorColor'
    )
    vehicleModelDate: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'vehicleModelDate',
            'https://schema.org/vehicleModelDate'
        ),
        serialization_alias='https://schema.org/vehicleModelDate'
    )
    vehicleConfiguration: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'vehicleConfiguration',
            'https://schema.org/vehicleConfiguration'
        ),
        serialization_alias='https://schema.org/vehicleConfiguration'
    )
    knownVehicleDamages: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'knownVehicleDamages',
            'https://schema.org/knownVehicleDamages'
        ),
        serialization_alias='https://schema.org/knownVehicleDamages'
    )
    meetsEmissionStandard: Optional[Union[str, List[str], 'QualitativeValue', List['QualitativeValue'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'meetsEmissionStandard',
            'https://schema.org/meetsEmissionStandard'
        ),
        serialization_alias='https://schema.org/meetsEmissionStandard'
    )
    weightTotal: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'weightTotal',
            'https://schema.org/weightTotal'
        ),
        serialization_alias='https://schema.org/weightTotal'
    )
    numberOfForwardGears: Optional[Union[float, List[float], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'numberOfForwardGears',
            'https://schema.org/numberOfForwardGears'
        ),
        serialization_alias='https://schema.org/numberOfForwardGears'
    )
    modelDate: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'modelDate',
            'https://schema.org/modelDate'
        ),
        serialization_alias='https://schema.org/modelDate'
    )
    purchaseDate: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'purchaseDate',
            'https://schema.org/purchaseDate'
        ),
        serialization_alias='https://schema.org/purchaseDate'
    )
    vehicleEngine: Optional[Union['EngineSpecification', List['EngineSpecification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'vehicleEngine',
            'https://schema.org/vehicleEngine'
        ),
        serialization_alias='https://schema.org/vehicleEngine'
    )
    emissionsCO2: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'emissionsCO2',
            'https://schema.org/emissionsCO2'
        ),
        serialization_alias='https://schema.org/emissionsCO2'
    )
    wheelbase: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'wheelbase',
            'https://schema.org/wheelbase'
        ),
        serialization_alias='https://schema.org/wheelbase'
    )
    mileageFromOdometer: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'mileageFromOdometer',
            'https://schema.org/mileageFromOdometer'
        ),
        serialization_alias='https://schema.org/mileageFromOdometer'
    )
    cargoVolume: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'cargoVolume',
            'https://schema.org/cargoVolume'
        ),
        serialization_alias='https://schema.org/cargoVolume'
    )
    fuelConsumption: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'fuelConsumption',
            'https://schema.org/fuelConsumption'
        ),
        serialization_alias='https://schema.org/fuelConsumption'
    )
    accelerationTime: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'accelerationTime',
            'https://schema.org/accelerationTime'
        ),
        serialization_alias='https://schema.org/accelerationTime'
    )
