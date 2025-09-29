from __future__ import annotations
import importlib
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .pronounceable_text import PronounceableText
    from .css_selector_type import CssSelectorType
    from .thing import Thing
    from .person import Person
    from .place import Place
    from .event import Event
    from .intangible import Intangible
    from .creative_work import CreativeWork
    from .action import Action
    from .product import Product
    from .medical_entity import MedicalEntity
    from .stupid_type import StupidType
    from .taxon import Taxon
    from .organization import Organization
    from .bio_chem_entity import BioChemEntity
    from .residence import Residence
    from .tourist_destination import TouristDestination
    from .administrative_area import AdministrativeArea
    from .landform import Landform
    from .local_business import LocalBusiness
    from .civic_structure import CivicStructure
    from .tourist_attraction import TouristAttraction
    from .accommodation import Accommodation
    from .landmarks_or_historical_buildings import LandmarksOrHistoricalBuildings
    from .theater_event import TheaterEvent
    from .food_event import FoodEvent
    from .education_event import EducationEvent
    from .festival import Festival
    from .social_event import SocialEvent
    from .music_event import MusicEvent
    from .screening_event import ScreeningEvent
    from .visual_arts_event import VisualArtsEvent
    from .literary_event import LiteraryEvent
    from .user_interaction import UserInteraction
    from .delivery_event import DeliveryEvent
    from .sports_event import SportsEvent
    from .publication_event import PublicationEvent
    from .comedy_event import ComedyEvent
    from .course_instance import CourseInstance
    from .childrens_event import ChildrensEvent
    from .dance_event import DanceEvent
    from .business_event import BusinessEvent
    from .hackathon import Hackathon
    from .sale_event import SaleEvent
    from .exhibition_event import ExhibitionEvent
    from .media_subscription import MediaSubscription
    from .virtual_location import VirtualLocation
    from .ticket import Ticket
    from .data_feed_item import DataFeedItem
    from .series import Series
    from .role import Role
    from .floor_plan import FloorPlan
    from .permit import Permit
    from .member_program_tier import MemberProgramTier
    from .educational_occupational_program import EducationalOccupationalProgram
    from .geospatial_geometry import GeospatialGeometry
    from .audience import Audience
    from .brand import Brand
    from .occupation import Occupation
    from .program_membership import ProgramMembership
    from .service import Service
    from .health_plan_cost_sharing_specification import HealthPlanCostSharingSpecification
    from .invoice import Invoice
    from .health_insurance_plan import HealthInsurancePlan
    from .property import Property
    from .alignment_object import AlignmentObject
    from .merchant_return_policy_seasonal_override import MerchantReturnPolicySeasonalOverride
    from .energy_consumption_details import EnergyConsumptionDetails
    from .schedule import Schedule
    from .enumeration import Enumeration
    from .speakable_specification import SpeakableSpecification
    from .health_plan_formulary import HealthPlanFormulary
    from .language import Language
    from .structured_value import StructuredValue
    from .member_program import MemberProgram
    from .property_value_specification import PropertyValueSpecification
    from .rating import Rating
    from .digital_document_permission import DigitalDocumentPermission
    from .computer_language import ComputerLanguage
    from .product_return_policy import ProductReturnPolicy
    from .payment_method import PaymentMethod
    from .parcel_delivery import ParcelDelivery
    from .merchant_return_policy import MerchantReturnPolicy
    from .reservation import Reservation
    from .job_posting import JobPosting
    from .broadcast_frequency_specification import BroadcastFrequencySpecification
    from .occupational_experience_requirements import OccupationalExperienceRequirements
    from .bed_details import BedDetails
    from .game_server import GameServer
    from .service_channel import ServiceChannel
    from .demand import Demand
    from .defined_term import DefinedTerm
    from .action_access_specification import ActionAccessSpecification
    from .financial_incentive import FinancialIncentive
    from .menu_item import MenuItem
    from .list_item import ListItem
    from .order_item import OrderItem
    from .item_list import ItemList
    from .health_plan_network import HealthPlanNetwork
    from .grant import Grant
    from .statistical_population import StatisticalPopulation
    from .order import Order
    from .constraint_node import ConstraintNode
    from .offer import Offer
    from .trip import Trip
    from .observation import Observation
    from .entry_point import EntryPoint
    from .quantity import Quantity
    from .seat import Seat
    from .broadcast_channel import BroadcastChannel
    from .__class import _Class
    from .chapter import Chapter
    from .tv_series import TVSeries
    from .web_site import WebSite
    from .comic_story import ComicStory
    from .how_to import HowTo
    from .web_content import WebContent
    from .game import Game
    from .guide import Guide
    from .media_object import MediaObject
    from .data_catalog import DataCatalog
    from .clip import Clip
    from .review import Review
    from .certification import Certification
    from .play import Play
    from .special_announcement import SpecialAnnouncement
    from .short_story import ShortStory
    from .photograph import Photograph
    from .claim import Claim
    from .blog import Blog
    from .quotation import Quotation
    from .digital_document import DigitalDocument
    from .dataset import Dataset
    from .creative_work_season import CreativeWorkSeason
    from .learning_resource import LearningResource
    from .music_playlist import MusicPlaylist
    from .menu import Menu
    from .sculpture import Sculpture
    from .painting import Painting
    from .web_page_element import WebPageElement
    from .code import Code
    from .movie import Movie
    from .poster import Poster
    from .how_to_tip import HowToTip
    from .how_to_section import HowToSection
    from .media_review_item import MediaReviewItem
    from .book import Book
    from .statement import Statement
    from .season import Season
    from .article import Article
    from .atlas import Atlas
    from .how_to_direction import HowToDirection
    from .publication_issue import PublicationIssue
    from .thesis import Thesis
    from .software_application import SoftwareApplication
    from .publication_volume import PublicationVolume
    from .comment import Comment
    from .music_composition import MusicComposition
    from .exercise_plan import ExercisePlan
    from .message import Message
    from .conversation import Conversation
    from .drawing import Drawing
    from .map import Map
    from .music_recording import MusicRecording
    from .legislation import Legislation
    from .defined_term_set import DefinedTermSet
    from .software_source_code import SoftwareSourceCode
    from .hyper_toc_entry import HyperTocEntry
    from .visual_artwork import VisualArtwork
    from .sheet_music import SheetMusic
    from .collection import Collection
    from .educational_occupational_credential import EducationalOccupationalCredential
    from .web_page import WebPage
    from .menu_section import MenuSection
    from .episode import Episode
    from .manuscript import Manuscript
    from .creative_work_series import CreativeWorkSeries
    from .math_solver import MathSolver
    from .hyper_toc import HyperToc
    from .archive_component import ArchiveComponent
    from .control_action import ControlAction
    from .trade_action import TradeAction
    from .assess_action import AssessAction
    from .move_action import MoveAction
    from .achieve_action import AchieveAction
    from .find_action import FindAction
    from .transfer_action import TransferAction
    from .organize_action import OrganizeAction
    from .update_action import UpdateAction
    from .create_action import CreateAction
    from .play_action import PlayAction
    from .seek_to_action import SeekToAction
    from .solve_math_action import SolveMathAction
    from .consume_action import ConsumeAction
    from .interact_action import InteractAction
    from .search_action import SearchAction
    from .product_model import ProductModel
    from .some_products import SomeProducts
    from .product_group import ProductGroup
    from .product_collection import ProductCollection
    from .vehicle import Vehicle
    from .individual_product import IndividualProduct
    from .medical_procedure import MedicalProcedure
    from .medical_risk_factor import MedicalRiskFactor
    from .medical_indication import MedicalIndication
    from .medical_test import MedicalTest
    from .medical_risk_estimator import MedicalRiskEstimator
    from .lifestyle_modification import LifestyleModification
    from .substance import Substance
    from .medical_contraindication import MedicalContraindication
    from .medical_study import MedicalStudy
    from .medical_condition import MedicalCondition
    from .medical_guideline import MedicalGuideline
    from .medical_cause import MedicalCause
    from .drug_class import DrugClass
    from .medical_device import MedicalDevice
    from .superficial_anatomy import SuperficialAnatomy
    from .drug_cost import DrugCost
    from .anatomical_structure import AnatomicalStructure
    from .anatomical_system import AnatomicalSystem
    from .medical_intangible import MedicalIntangible
    from .news_media_organization import NewsMediaOrganization
    from .ngo import NGO
    from .cooperative import Cooperative
    from .sports_organization import SportsOrganization
    from .performing_group import PerformingGroup
    from .funding_scheme import FundingScheme
    from .search_rescue_organization import SearchRescueOrganization
    from .library_system import LibrarySystem
    from .medical_organization import MedicalOrganization
    from .online_business import OnlineBusiness
    from .consortium import Consortium
    from .workers_union import WorkersUnion
    from .government_organization import GovernmentOrganization
    from .project import Project
    from .research_organization import ResearchOrganization
    from .airline import Airline
    from .corporation import Corporation
    from .political_party import PoliticalParty
    from .protein import Protein
    from .gene import Gene
    from .molecular_entity import MolecularEntity
    from .chemical_substance import ChemicalSubstance
    from .gated_residence_community import GatedResidenceCommunity
    from .apartment_complex import ApartmentComplex
    from .country import Country
    from .city import City
    from .state import State
    from .school_district import SchoolDistrict
    from .continent import Continent
    from .body_of_water import BodyOfWater
    from .mountain import Mountain
    from .volcano import Volcano
    from .radio_station import RadioStation
    from .internet_cafe import InternetCafe
    from .medical_business import MedicalBusiness
    from .employment_agency import EmploymentAgency
    from .food_establishment import FoodEstablishment
    from .entertainment_business import EntertainmentBusiness
    from .sports_activity_location import SportsActivityLocation
    from .shopping_center import ShoppingCenter
    from .financial_service import FinancialService
    from .child_care import ChildCare
    from .home_and_construction_business import HomeAndConstructionBusiness
    from .automotive_business import AutomotiveBusiness
    from .lodging_business import LodgingBusiness
    from .store import Store
    from .legal_service import LegalService
    from .animal_shelter import AnimalShelter
    from .television_station import TelevisionStation
    from .emergency_service import EmergencyService
    from .dry_cleaning_or_laundry import DryCleaningOrLaundry
    from .archive_organization import ArchiveOrganization
    from .real_estate_agent import RealEstateAgent
    from .library import Library
    from .recycling_center import RecyclingCenter
    from .government_office import GovernmentOffice
    from .travel_agency import TravelAgency
    from .tourist_information_center import TouristInformationCenter
    from .health_and_beauty_business import HealthAndBeautyBusiness
    from .professional_service import ProfessionalService
    from .self_storage import SelfStorage
    from .playground import Playground
    from .music_venue import MusicVenue
    from .crematorium import Crematorium
    from .police_station import PoliceStation
    from .place_of_worship import PlaceOfWorship
    from .public_toilet import PublicToilet
    from .taxi_stand import TaxiStand
    from .train_station import TrainStation
    from .subway_station import SubwayStation
    from .bridge import Bridge
    from .event_venue import EventVenue
    from .bus_stop import BusStop
    from .educational_organization import EducationalOrganization
    from .bus_station import BusStation
    from .cemetery import Cemetery
    from .government_building import GovernmentBuilding
    from .airport import Airport
    from .stadium_or_arena import StadiumOrArena
    from .beach import Beach
    from .park import Park
    from .rv_park import RVPark
    from .performing_arts_theater import PerformingArtsTheater
    from .boat_terminal import BoatTerminal
    from .hospital import Hospital
    from .aquarium import Aquarium
    from .zoo import Zoo
    from .parking_facility import ParkingFacility
    from .museum import Museum
    from .movie_theater import MovieTheater
    from .fire_station import FireStation
    from .apartment import Apartment
    from .room import Room
    from .suite import Suite
    from .house import House
    from .camping_pitch import CampingPitch
    from .user_checkins import UserCheckins
    from .user_blocks import UserBlocks
    from .user_comments import UserComments
    from .user_tweets import UserTweets
    from .user_likes import UserLikes
    from .user_plays import UserPlays
    from .user_page_visits import UserPageVisits
    from .user_plus_ones import UserPlusOnes
    from .user_downloads import UserDownloads
    from .on_demand_event import OnDemandEvent
    from .broadcast_event import BroadcastEvent
    from .event_series import EventSeries
    from .link_role import LinkRole
    from .performance_role import PerformanceRole
    from .organization_role import OrganizationRole
    from .government_permit import GovernmentPermit
    from .work_based_program import WorkBasedProgram
    from .researcher import Researcher
    from .business_audience import BusinessAudience
    from .educational_audience import EducationalAudience
    from .people_audience import PeopleAudience
    from .medical_audience import MedicalAudience
    from .cable_or_satellite_service import CableOrSatelliteService
    from .web_api import WebAPI
    from .financial_product import FinancialProduct
    from .taxi import Taxi
    from .food_service import FoodService
    from .broadcast_service import BroadcastService
    from .government_service import GovernmentService
    from .taxi_service import TaxiService
    from .size_group_enumeration import SizeGroupEnumeration
    from .return_label_source_enumeration import ReturnLabelSourceEnumeration
    from .physical_activity_category import PhysicalActivityCategory
    from .contact_point_option import ContactPointOption
    from .price_component_type_enumeration import PriceComponentTypeEnumeration
    from .map_category_type import MapCategoryType
    from .restricted_diet import RestrictedDiet
    from .digital_platform_enumeration import DigitalPlatformEnumeration
    from .payment_method_type import PaymentMethodType
    from .incentive_qualified_expense_type import IncentiveQualifiedExpenseType
    from .certification_status_enumeration import CertificationStatusEnumeration
    from .government_benefits_type import GovernmentBenefitsType
    from .status_enumeration import StatusEnumeration
    from .car_usage_type import CarUsageType
    from .fulfillment_type_enumeration import FulfillmentTypeEnumeration
    from .size_system_enumeration import SizeSystemEnumeration
    from .specialty import Specialty
    from .gender_type import GenderType
    from .health_aspect_enumeration import HealthAspectEnumeration
    from .media_manipulation_rating_enumeration import MediaManipulationRatingEnumeration
    from .media_enumeration import MediaEnumeration
    from .warranty_scope import WarrantyScope
    from .music_album_release_type import MusicAlbumReleaseType
    from .medical_enumeration import MedicalEnumeration
    from .digital_document_permission_type import DigitalDocumentPermissionType
    from .offer_item_condition import OfferItemCondition
    from .measurement_method_enum import MeasurementMethodEnum
    from .legal_value_level import LegalValueLevel
    from .energy_efficiency_enumeration import EnergyEfficiencyEnumeration
    from .book_format_type import BookFormatType
    from .business_entity_type import BusinessEntityType
    from .product_return_enumeration import ProductReturnEnumeration
    from .price_type_enumeration import PriceTypeEnumeration
    from .item_availability import ItemAvailability
    from .item_list_order_type import ItemListOrderType
    from .refund_type_enumeration import RefundTypeEnumeration
    from .tier_benefit_enumeration import TierBenefitEnumeration
    from .game_availability_enumeration import GameAvailabilityEnumeration
    from .boarding_policy_type import BoardingPolicyType
    from .business_function import BusinessFunction
    from .delivery_method import DeliveryMethod
    from .incentive_status import IncentiveStatus
    from .purchase_type import PurchaseType
    from .qualitative_value import QualitativeValue
    from .return_fees_enumeration import ReturnFeesEnumeration
    from .incentive_type import IncentiveType
    from .adult_oriented_enumeration import AdultOrientedEnumeration
    from .nonprofit_type import NonprofitType
    from .rsvp_response_type import RsvpResponseType
    from .return_method_enumeration import ReturnMethodEnumeration
    from .merchant_return_enumeration import MerchantReturnEnumeration
    from .day_of_week import DayOfWeek
    from .measurement_type_enumeration import MeasurementTypeEnumeration
    from .music_release_format_type import MusicReleaseFormatType
    from .event_attendance_mode_enumeration import EventAttendanceModeEnumeration
    from .music_album_production_type import MusicAlbumProductionType
    from .game_play_mode import GamePlayMode
    from .defined_region import DefinedRegion
    from .engine_specification import EngineSpecification
    from .shipping_service import ShippingService
    from .quantitative_value import QuantitativeValue
    from .repayment_specification import RepaymentSpecification
    from .service_period import ServicePeriod
    from .warranty_promise import WarrantyPromise
    from .delivery_time_settings import DeliveryTimeSettings
    from .shipping_rate_settings import ShippingRateSettings
    from .price_specification import PriceSpecification
    from .quantitative_value_distribution import QuantitativeValueDistribution
    from .shipping_delivery_time import ShippingDeliveryTime
    from .postal_code_range_specification import PostalCodeRangeSpecification
    from .monetary_amount import MonetaryAmount
    from .shipping_conditions import ShippingConditions
    from .property_value import PropertyValue
    from .ownership_info import OwnershipInfo
    from .interaction_counter import InteractionCounter
    from .exchange_rate_specification import ExchangeRateSpecification
    from .geo_shape import GeoShape
    from .cdcpmd_record import CDCPMDRecord
    from .type_and_quantity_node import TypeAndQuantityNode
    from .offer_shipping_details import OfferShippingDetails
    from .dated_money_specification import DatedMoneySpecification
    from .contact_point import ContactPoint
    from .nutrition_information import NutritionInformation
    from .geo_coordinates import GeoCoordinates
    from .opening_hours_specification import OpeningHoursSpecification
    from .endorsement_rating import EndorsementRating
    from .aggregate_rating import AggregateRating
    from .rental_car_reservation import RentalCarReservation
    from .lodging_reservation import LodgingReservation
    from .train_reservation import TrainReservation
    from .boat_reservation import BoatReservation
    from .event_reservation import EventReservation
    from .flight_reservation import FlightReservation
    from .bus_reservation import BusReservation
    from .taxi_reservation import TaxiReservation
    from .reservation_package import ReservationPackage
    from .food_establishment_reservation import FoodEstablishmentReservation
    from .category_code import CategoryCode
    from .how_to_item import HowToItem
    from .breadcrumb_list import BreadcrumbList
    from .how_to_step import HowToStep
    from .offer_catalog import OfferCatalog
    from .monetary_grant import MonetaryGrant
    from .statistical_variable import StatisticalVariable
    from .aggregate_offer import AggregateOffer
    from .offer_for_purchase import OfferForPurchase
    from .offer_for_lease import OfferForLease
    from .train_trip import TrainTrip
    from .bus_trip import BusTrip
    from .tourist_trip import TouristTrip
    from .flight import Flight
    from .boat_trip import BoatTrip
    from .energy import Energy
    from .distance import Distance
    from .mass import Mass
    from .duration import Duration
    from .radio_channel import RadioChannel
    from .television_channel import TelevisionChannel
    from .comic_cover_art import ComicCoverArt
    from .recipe import Recipe
    from .health_topic_content import HealthTopicContent
    from .video_game import VideoGame
    from .video_object import VideoObject
    from .audio_object import AudioObject
    from .music_video_object import MusicVideoObject
    from .amp_story import AmpStory
    from .data_download import DataDownload
    from .text_object import TextObject
    from .image_object import ImageObject
    from ._3_d_model import _3DModel
    from .radio_clip import RadioClip
    from .tv_clip import TVClip
    from .movie_clip import MovieClip
    from .video_game_clip import VideoGameClip
    from .claim_review import ClaimReview
    from .media_review import MediaReview
    from .user_review import UserReview
    from .employer_review import EmployerReview
    from .recommendation import Recommendation
    from .critic_review import CriticReview
    from .note_digital_document import NoteDigitalDocument
    from .spreadsheet_digital_document import SpreadsheetDigitalDocument
    from .text_digital_document import TextDigitalDocument
    from .presentation_digital_document import PresentationDigitalDocument
    from .data_feed import DataFeed
    from .tv_season import TVSeason
    from .radio_season import RadioSeason
    from .podcast_season import PodcastSeason
    from .quiz import Quiz
    from .course import Course
    from .syllabus import Syllabus
    from .music_album import MusicAlbum
    from .music_release import MusicRelease
    from .table import Table
    from .wp_footer import WPFooter
    from .wp_side_bar import WPSideBar
    from .wp_ad_block import WPAdBlock
    from .wp_header import WPHeader
    from .site_navigation_element import SiteNavigationElement
    from .news_article import NewsArticle
    from .satirical_article import SatiricalArticle
    from .advertiser_content_article import AdvertiserContentArticle
    from .social_media_posting import SocialMediaPosting
    from .report import Report
    from .scholarly_article import ScholarlyArticle
    from .tech_article import TechArticle
    from .comic_issue import ComicIssue
    from .web_application import WebApplication
    from .mobile_application import MobileApplication
    from .correction_comment import CorrectionComment
    from .question import Question
    from .answer import Answer
    from .email_message import EmailMessage
    from .legislation_object import LegislationObject
    from .category_code_set import CategoryCodeSet
    from .cover_art import CoverArt
    from .real_estate_listing import RealEstateListing
    from .profile_page import ProfilePage
    from .medical_web_page import MedicalWebPage
    from .search_results_page import SearchResultsPage
    from .checkout_page import CheckoutPage
    from .contact_page import ContactPage
    from .item_page import ItemPage
    from .collection_page import CollectionPage
    from .about_page import AboutPage
    from .qa_page import QAPage
    from .faq_page import FAQPage
    from .radio_episode import RadioEpisode
    from .podcast_episode import PodcastEpisode
    from .tv_episode import TVEpisode
    from .radio_series import RadioSeries
    from .periodical import Periodical
    from .podcast_series import PodcastSeries
    from .book_series import BookSeries
    from .movie_series import MovieSeries
    from .video_game_series import VideoGameSeries
    from .resume_action import ResumeAction
    from .suspend_action import SuspendAction
    from .activate_action import ActivateAction
    from .deactivate_action import DeactivateAction
    from .rent_action import RentAction
    from .order_action import OrderAction
    from .pre_order_action import PreOrderAction
    from .buy_action import BuyAction
    from .tip_action import TipAction
    from .sell_action import SellAction
    from .pay_action import PayAction
    from .quote_action import QuoteAction
    from .ignore_action import IgnoreAction
    from .review_action import ReviewAction
    from .react_action import ReactAction
    from .choose_action import ChooseAction
    from .travel_action import TravelAction
    from .depart_action import DepartAction
    from .arrive_action import ArriveAction
    from .tie_action import TieAction
    from .lose_action import LoseAction
    from .win_action import WinAction
    from .track_action import TrackAction
    from .discover_action import DiscoverAction
    from .check_action import CheckAction
    from .lend_action import LendAction
    from .send_action import SendAction
    from .money_transfer import MoneyTransfer
    from .return_action import ReturnAction
    from .take_action import TakeAction
    from .give_action import GiveAction
    from .borrow_action import BorrowAction
    from .donate_action import DonateAction
    from .receive_action import ReceiveAction
    from .download_action import DownloadAction
    from .bookmark_action import BookmarkAction
    from .plan_action import PlanAction
    from .allocate_action import AllocateAction
    from .apply_action import ApplyAction
    from .delete_action import DeleteAction
    from .add_action import AddAction
    from .replace_action import ReplaceAction
    from .draw_action import DrawAction
    from .photograph_action import PhotographAction
    from .cook_action import CookAction
    from .paint_action import PaintAction
    from .film_action import FilmAction
    from .write_action import WriteAction
    from .perform_action import PerformAction
    from .exercise_action import ExerciseAction
    from .install_action import InstallAction
    from .read_action import ReadAction
    from .view_action import ViewAction
    from .drink_action import DrinkAction
    from .use_action import UseAction
    from .eat_action import EatAction
    from .listen_action import ListenAction
    from .play_game_action import PlayGameAction
    from .watch_action import WatchAction
    from .marry_action import MarryAction
    from .follow_action import FollowAction
    from .join_action import JoinAction
    from .leave_action import LeaveAction
    from .subscribe_action import SubscribeAction
    from .register_action import RegisterAction
    from .communicate_action import CommunicateAction
    from .un_register_action import UnRegisterAction
    from .befriend_action import BefriendAction
    from .car import Car
    from .motorcycle import Motorcycle
    from .bus_or_coach import BusOrCoach
    from .motorized_bicycle import MotorizedBicycle
    from .diagnostic_procedure import DiagnosticProcedure
    from .surgical_procedure import SurgicalProcedure
    from .therapeutic_procedure import TherapeuticProcedure
    from .treatment_indication import TreatmentIndication
    from .approved_indication import ApprovedIndication
    from .prevention_indication import PreventionIndication
    from .pathology_test import PathologyTest
    from .blood_test import BloodTest
    from .imaging_test import ImagingTest
    from .medical_test_panel import MedicalTestPanel
    from .medical_risk_calculator import MedicalRiskCalculator
    from .medical_risk_score import MedicalRiskScore
    from .physical_activity import PhysicalActivity
    from .diet import Diet
    from .drug import Drug
    from .dietary_supplement import DietarySupplement
    from .medical_trial import MedicalTrial
    from .medical_observational_study import MedicalObservationalStudy
    from .infectious_disease import InfectiousDisease
    from .medical_sign_or_symptom import MedicalSignOrSymptom
    from .medical_guideline_recommendation import MedicalGuidelineRecommendation
    from .medical_guideline_contraindication import MedicalGuidelineContraindication
    from .vessel import Vessel
    from .ligament import Ligament
    from .bone import Bone
    from .brain_structure import BrainStructure
    from .joint import Joint
    from .muscle import Muscle
    from .nerve import Nerve
    from .dose_schedule import DoseSchedule
    from .medical_condition_stage import MedicalConditionStage
    from .drug_strength import DrugStrength
    from .d_dx_element import DDxElement
    from .medical_code import MedicalCode
    from .drug_legal_status import DrugLegalStatus
    from .sports_team import SportsTeam
    from .dance_group import DanceGroup
    from .music_group import MusicGroup
    from .theater_group import TheaterGroup
    from .veterinary_care import VeterinaryCare
    from .diagnostic_lab import DiagnosticLab
    from .medical_clinic import MedicalClinic
    from .pharmacy import Pharmacy
    from .online_store import OnlineStore
    from .funding_agency import FundingAgency
    from .research_project import ResearchProject
    from .lake_body_of_water import LakeBodyOfWater
    from .reservoir import Reservoir
    from .pond import Pond
    from .river_body_of_water import RiverBodyOfWater
    from .sea_body_of_water import SeaBodyOfWater
    from .ocean_body_of_water import OceanBodyOfWater
    from .waterfall import Waterfall
    from .canal import Canal
    from .dentist import Dentist
    from .physician import Physician
    from .optician import Optician
    from .winery import Winery
    from .ice_cream_shop import IceCreamShop
    from .bar_or_pub import BarOrPub
    from .restaurant import Restaurant
    from .bakery import Bakery
    from .cafe_or_coffee_shop import CafeOrCoffeeShop
    from .fast_food_restaurant import FastFoodRestaurant
    from .distillery import Distillery
    from .brewery import Brewery
    from .comedy_club import ComedyClub
    from .amusement_park import AmusementPark
    from .casino import Casino
    from .art_gallery import ArtGallery
    from .adult_entertainment import AdultEntertainment
    from .night_club import NightClub
    from .public_swimming_pool import PublicSwimmingPool
    from .bowling_alley import BowlingAlley
    from .tennis_complex import TennisComplex
    from .golf_course import GolfCourse
    from .exercise_gym import ExerciseGym
    from .sports_club import SportsClub
    from .insurance_agency import InsuranceAgency
    from .bank_or_credit_union import BankOrCreditUnion
    from .automated_teller import AutomatedTeller
    from .accounting_service import AccountingService
    from .moving_company import MovingCompany
    from .locksmith import Locksmith
    from .general_contractor import GeneralContractor
    from .plumber import Plumber
    from .roofing_contractor import RoofingContractor
    from .hvac_business import HVACBusiness
    from .electrician import Electrician
    from .house_painter import HousePainter
    from .auto_dealer import AutoDealer
    from .auto_body_shop import AutoBodyShop
    from .gas_station import GasStation
    from .motorcycle_dealer import MotorcycleDealer
    from .auto_rental import AutoRental
    from .auto_repair import AutoRepair
    from .auto_wash import AutoWash
    from .motorcycle_repair import MotorcycleRepair
    from .bed_and_breakfast import BedAndBreakfast
    from .vacation_rental import VacationRental
    from .campground import Campground
    from .resort import Resort
    from .hotel import Hotel
    from .motel import Motel
    from .hostel import Hostel
    from .hobby_shop import HobbyShop
    from .liquor_store import LiquorStore
    from .pawn_shop import PawnShop
    from .electronics_store import ElectronicsStore
    from .book_store import BookStore
    from .florist import Florist
    from .jewelry_store import JewelryStore
    from .hardware_store import HardwareStore
    from .computer_store import ComputerStore
    from .pet_store import PetStore
    from .garden_store import GardenStore
    from .outlet_store import OutletStore
    from .home_goods_store import HomeGoodsStore
    from .department_store import DepartmentStore
    from .office_equipment_store import OfficeEquipmentStore
    from .shoe_store import ShoeStore
    from .mobile_phone_store import MobilePhoneStore
    from .music_store import MusicStore
    from .bike_store import BikeStore
    from .auto_parts_store import AutoPartsStore
    from .furniture_store import FurnitureStore
    from .grocery_store import GroceryStore
    from .mens_clothing_store import MensClothingStore
    from .convenience_store import ConvenienceStore
    from .tire_shop import TireShop
    from .movie_rental_store import MovieRentalStore
    from .sporting_goods_store import SportingGoodsStore
    from .wholesale_store import WholesaleStore
    from .clothing_store import ClothingStore
    from .toy_store import ToyStore
    from .attorney import Attorney
    from .notary import Notary
    from .post_office import PostOffice
    from .day_spa import DaySpa
    from .beauty_salon import BeautySalon
    from .health_club import HealthClub
    from .hair_salon import HairSalon
    from .nail_salon import NailSalon
    from .tattoo_parlor import TattooParlor
    from .hindu_temple import HinduTemple
    from .buddhist_temple import BuddhistTemple
    from .mosque import Mosque
    from .church import Church
    from .synagogue import Synagogue
    from .college_or_university import CollegeOrUniversity
    from .elementary_school import ElementarySchool
    from .school import School
    from .middle_school import MiddleSchool
    from .high_school import HighSchool
    from .preschool import Preschool
    from .embassy import Embassy
    from .courthouse import Courthouse
    from .defence_establishment import DefenceEstablishment
    from .legislative_building import LegislativeBuilding
    from .city_hall import CityHall
    from .meeting_room import MeetingRoom
    from .hotel_room import HotelRoom
    from .single_family_residence import SingleFamilyResidence
    from .employee_role import EmployeeRole
    from .parent_audience import ParentAudience
    from .patient import Patient
    from .investment_or_deposit import InvestmentOrDeposit
    from .payment_service import PaymentService
    from .loan_or_credit import LoanOrCredit
    from .bank_account import BankAccount
    from .currency_conversion_service import CurrencyConversionService
    from .payment_card import PaymentCard
    from .radio_broadcast_service import RadioBroadcastService
    from .wearable_size_group_enumeration import WearableSizeGroupEnumeration
    from .payment_status_type import PaymentStatusType
    from .reservation_status_type import ReservationStatusType
    from .game_server_status import GameServerStatus
    from .event_status_type import EventStatusType
    from .action_status_type import ActionStatusType
    from .order_status import OrderStatus
    from .legal_force_status import LegalForceStatus
    from .wearable_size_system_enumeration import WearableSizeSystemEnumeration
    from .medical_specialty import MedicalSpecialty
    from .iptc_digital_source_enumeration import IPTCDigitalSourceEnumeration
    from .drug_prescription_status import DrugPrescriptionStatus
    from .medical_device_purpose import MedicalDevicePurpose
    from .medical_trial_design import MedicalTrialDesign
    from .drug_cost_category import DrugCostCategory
    from .medical_procedure_type import MedicalProcedureType
    from .drug_pregnancy_category import DrugPregnancyCategory
    from .physical_exam import PhysicalExam
    from .medical_observational_study_design import MedicalObservationalStudyDesign
    from .medical_evidence_level import MedicalEvidenceLevel
    from .medical_study_status import MedicalStudyStatus
    from .medical_imaging_technique import MedicalImagingTechnique
    from .medicine_system import MedicineSystem
    from .infectious_agent_class import InfectiousAgentClass
    from .medical_audience_type import MedicalAudienceType
    from .eu_energy_efficiency_enumeration import EUEnergyEfficiencyEnumeration
    from .energy_star_energy_efficiency_enumeration import EnergyStarEnergyEfficiencyEnumeration
    from .bed_type import BedType
    from .steering_position_value import SteeringPositionValue
    from .size_specification import SizeSpecification
    from .drive_wheel_configuration_value import DriveWheelConfigurationValue
    from .us_nonprofit_type import USNonprofitType
    from .nl_nonprofit_type import NLNonprofitType
    from .uk_nonprofit_type import UKNonprofitType
    from .wearable_measurement_type_enumeration import WearableMeasurementTypeEnumeration
    from .body_measurement_type_enumeration import BodyMeasurementTypeEnumeration
    from .compound_price_specification import CompoundPriceSpecification
    from .unit_price_specification import UnitPriceSpecification
    from .payment_charge_specification import PaymentChargeSpecification
    from .delivery_charge_specification import DeliveryChargeSpecification
    from .monetary_amount_distribution import MonetaryAmountDistribution
    from .location_feature_specification import LocationFeatureSpecification
    from .geo_circle import GeoCircle
    from .postal_address import PostalAddress
    from .employer_aggregate_rating import EmployerAggregateRating
    from .how_to_supply import HowToSupply
    from .how_to_tool import HowToTool
    from .am_radio_channel import AMRadioChannel
    from .fm_radio_channel import FMRadioChannel
    from .video_object_snapshot import VideoObjectSnapshot
    from .audio_object_snapshot import AudioObjectSnapshot
    from .audiobook import Audiobook
    from .image_object_snapshot import ImageObjectSnapshot
    from .barcode import Barcode
    from .complete_data_feed import CompleteDataFeed
    from .opinion_news_article import OpinionNewsArticle
    from .review_news_article import ReviewNewsArticle
    from .reportage_news_article import ReportageNewsArticle
    from .background_news_article import BackgroundNewsArticle
    from .analysis_news_article import AnalysisNewsArticle
    from .ask_public_news_article import AskPublicNewsArticle
    from .discussion_forum_posting import DiscussionForumPosting
    from .blog_posting import BlogPosting
    from .medical_scholarly_article import MedicalScholarlyArticle
    from .api_reference import APIReference
    from .media_gallery import MediaGallery
    from .newspaper import Newspaper
    from .comic_series import ComicSeries
    from .disagree_action import DisagreeAction
    from .dislike_action import DislikeAction
    from .want_action import WantAction
    from .endorse_action import EndorseAction
    from .like_action import LikeAction
    from .agree_action import AgreeAction
    from .vote_action import VoteAction
    from .schedule_action import ScheduleAction
    from .cancel_action import CancelAction
    from .reserve_action import ReserveAction
    from .reject_action import RejectAction
    from .authorize_action import AuthorizeAction
    from .accept_action import AcceptAction
    from .assign_action import AssignAction
    from .insert_action import InsertAction
    from .wear_action import WearAction
    from .comment_action import CommentAction
    from .reply_action import ReplyAction
    from .check_out_action import CheckOutAction
    from .invite_action import InviteAction
    from .check_in_action import CheckInAction
    from .ask_action import AskAction
    from .inform_action import InformAction
    from .share_action import ShareAction
    from .psychological_treatment import PsychologicalTreatment
    from .medical_therapy import MedicalTherapy
    from .medical_symptom import MedicalSymptom
    from .medical_sign import MedicalSign
    from .vein import Vein
    from .lymphatic_vessel import LymphaticVessel
    from .artery import Artery
    from .maximum_dose_schedule import MaximumDoseSchedule
    from .reported_dose_schedule import ReportedDoseSchedule
    from .recommended_dose_schedule import RecommendedDoseSchedule
    from .covid_testing_facility import CovidTestingFacility
    from .online_marketplace import OnlineMarketplace
    from .physicians_office import PhysiciansOffice
    from .individual_physician import IndividualPhysician
    from .ski_resort import SkiResort
    from .catholic_church import CatholicChurch
    from .brokerage_account import BrokerageAccount
    from .deposit_account import DepositAccount
    from .investment_fund import InvestmentFund
    from .mortgage_loan import MortgageLoan
    from .credit_card import CreditCard
    from .live_blog_posting import LiveBlogPosting
    from .video_gallery import VideoGallery
    from .image_gallery import ImageGallery
    from .append_action import AppendAction
    from .prepend_action import PrependAction
    from .confirm_action import ConfirmAction
    from .rsvp_action import RsvpAction
    from .occupational_therapy import OccupationalTherapy
    from .palliative_procedure import PalliativeProcedure
    from .physical_therapy import PhysicalTherapy
    from .radiation_therapy import RadiationTherapy
    from .vital_sign import VitalSign

__all__ = [
    'PronounceableText',
    'CssSelectorType',
    'Thing',
    'Person',
    'Place',
    'Event',
    'Intangible',
    'CreativeWork',
    'Action',
    'Product',
    'MedicalEntity',
    'StupidType',
    'Taxon',
    'Organization',
    'BioChemEntity',
    'Residence',
    'TouristDestination',
    'AdministrativeArea',
    'Landform',
    'LocalBusiness',
    'CivicStructure',
    'TouristAttraction',
    'Accommodation',
    'LandmarksOrHistoricalBuildings',
    'TheaterEvent',
    'FoodEvent',
    'EducationEvent',
    'Festival',
    'SocialEvent',
    'MusicEvent',
    'ScreeningEvent',
    'VisualArtsEvent',
    'LiteraryEvent',
    'UserInteraction',
    'DeliveryEvent',
    'SportsEvent',
    'PublicationEvent',
    'ComedyEvent',
    'CourseInstance',
    'ChildrensEvent',
    'DanceEvent',
    'BusinessEvent',
    'Hackathon',
    'SaleEvent',
    'ExhibitionEvent',
    'MediaSubscription',
    'VirtualLocation',
    'Ticket',
    'DataFeedItem',
    'Series',
    'Role',
    'FloorPlan',
    'Permit',
    'MemberProgramTier',
    'EducationalOccupationalProgram',
    'GeospatialGeometry',
    'Audience',
    'Brand',
    'Occupation',
    'ProgramMembership',
    'Service',
    'HealthPlanCostSharingSpecification',
    'Invoice',
    'HealthInsurancePlan',
    'Property',
    'AlignmentObject',
    'MerchantReturnPolicySeasonalOverride',
    'EnergyConsumptionDetails',
    'Schedule',
    'Enumeration',
    'SpeakableSpecification',
    'HealthPlanFormulary',
    'Language',
    'StructuredValue',
    'MemberProgram',
    'PropertyValueSpecification',
    'Rating',
    'DigitalDocumentPermission',
    'ComputerLanguage',
    'ProductReturnPolicy',
    'PaymentMethod',
    'ParcelDelivery',
    'MerchantReturnPolicy',
    'Reservation',
    'JobPosting',
    'BroadcastFrequencySpecification',
    'OccupationalExperienceRequirements',
    'BedDetails',
    'GameServer',
    'ServiceChannel',
    'Demand',
    'DefinedTerm',
    'ActionAccessSpecification',
    'FinancialIncentive',
    'MenuItem',
    'ListItem',
    'OrderItem',
    'ItemList',
    'HealthPlanNetwork',
    'Grant',
    'StatisticalPopulation',
    'Order',
    'ConstraintNode',
    'Offer',
    'Trip',
    'Observation',
    'EntryPoint',
    'Quantity',
    'Seat',
    'BroadcastChannel',
    '_Class',
    'Chapter',
    'TVSeries',
    'WebSite',
    'ComicStory',
    'HowTo',
    'WebContent',
    'Game',
    'Guide',
    'MediaObject',
    'DataCatalog',
    'Clip',
    'Review',
    'Certification',
    'Play',
    'SpecialAnnouncement',
    'ShortStory',
    'Photograph',
    'Claim',
    'Blog',
    'Quotation',
    'DigitalDocument',
    'Dataset',
    'CreativeWorkSeason',
    'LearningResource',
    'MusicPlaylist',
    'Menu',
    'Sculpture',
    'Painting',
    'WebPageElement',
    'Code',
    'Movie',
    'Poster',
    'HowToTip',
    'HowToSection',
    'MediaReviewItem',
    'Book',
    'Statement',
    'Season',
    'Article',
    'Atlas',
    'HowToDirection',
    'PublicationIssue',
    'Thesis',
    'SoftwareApplication',
    'PublicationVolume',
    'Comment',
    'MusicComposition',
    'ExercisePlan',
    'Message',
    'Conversation',
    'Drawing',
    'Map',
    'MusicRecording',
    'Legislation',
    'DefinedTermSet',
    'SoftwareSourceCode',
    'HyperTocEntry',
    'VisualArtwork',
    'SheetMusic',
    'Collection',
    'EducationalOccupationalCredential',
    'WebPage',
    'MenuSection',
    'Episode',
    'Manuscript',
    'CreativeWorkSeries',
    'MathSolver',
    'HyperToc',
    'ArchiveComponent',
    'ControlAction',
    'TradeAction',
    'AssessAction',
    'MoveAction',
    'AchieveAction',
    'FindAction',
    'TransferAction',
    'OrganizeAction',
    'UpdateAction',
    'CreateAction',
    'PlayAction',
    'SeekToAction',
    'SolveMathAction',
    'ConsumeAction',
    'InteractAction',
    'SearchAction',
    'ProductModel',
    'SomeProducts',
    'ProductGroup',
    'ProductCollection',
    'Vehicle',
    'IndividualProduct',
    'MedicalProcedure',
    'MedicalRiskFactor',
    'MedicalIndication',
    'MedicalTest',
    'MedicalRiskEstimator',
    'LifestyleModification',
    'Substance',
    'MedicalContraindication',
    'MedicalStudy',
    'MedicalCondition',
    'MedicalGuideline',
    'MedicalCause',
    'DrugClass',
    'MedicalDevice',
    'SuperficialAnatomy',
    'DrugCost',
    'AnatomicalStructure',
    'AnatomicalSystem',
    'MedicalIntangible',
    'NewsMediaOrganization',
    'NGO',
    'Cooperative',
    'SportsOrganization',
    'PerformingGroup',
    'FundingScheme',
    'SearchRescueOrganization',
    'LibrarySystem',
    'MedicalOrganization',
    'OnlineBusiness',
    'Consortium',
    'WorkersUnion',
    'GovernmentOrganization',
    'Project',
    'ResearchOrganization',
    'Airline',
    'Corporation',
    'PoliticalParty',
    'Protein',
    'Gene',
    'MolecularEntity',
    'ChemicalSubstance',
    'GatedResidenceCommunity',
    'ApartmentComplex',
    'Country',
    'City',
    'State',
    'SchoolDistrict',
    'Continent',
    'BodyOfWater',
    'Mountain',
    'Volcano',
    'RadioStation',
    'InternetCafe',
    'MedicalBusiness',
    'EmploymentAgency',
    'FoodEstablishment',
    'EntertainmentBusiness',
    'SportsActivityLocation',
    'ShoppingCenter',
    'FinancialService',
    'ChildCare',
    'HomeAndConstructionBusiness',
    'AutomotiveBusiness',
    'LodgingBusiness',
    'Store',
    'LegalService',
    'AnimalShelter',
    'TelevisionStation',
    'EmergencyService',
    'DryCleaningOrLaundry',
    'ArchiveOrganization',
    'RealEstateAgent',
    'Library',
    'RecyclingCenter',
    'GovernmentOffice',
    'TravelAgency',
    'TouristInformationCenter',
    'HealthAndBeautyBusiness',
    'ProfessionalService',
    'SelfStorage',
    'Playground',
    'MusicVenue',
    'Crematorium',
    'PoliceStation',
    'PlaceOfWorship',
    'PublicToilet',
    'TaxiStand',
    'TrainStation',
    'SubwayStation',
    'Bridge',
    'EventVenue',
    'BusStop',
    'EducationalOrganization',
    'BusStation',
    'Cemetery',
    'GovernmentBuilding',
    'Airport',
    'StadiumOrArena',
    'Beach',
    'Park',
    'RVPark',
    'PerformingArtsTheater',
    'BoatTerminal',
    'Hospital',
    'Aquarium',
    'Zoo',
    'ParkingFacility',
    'Museum',
    'MovieTheater',
    'FireStation',
    'Apartment',
    'Room',
    'Suite',
    'House',
    'CampingPitch',
    'UserCheckins',
    'UserBlocks',
    'UserComments',
    'UserTweets',
    'UserLikes',
    'UserPlays',
    'UserPageVisits',
    'UserPlusOnes',
    'UserDownloads',
    'OnDemandEvent',
    'BroadcastEvent',
    'EventSeries',
    'LinkRole',
    'PerformanceRole',
    'OrganizationRole',
    'GovernmentPermit',
    'WorkBasedProgram',
    'Researcher',
    'BusinessAudience',
    'EducationalAudience',
    'PeopleAudience',
    'MedicalAudience',
    'CableOrSatelliteService',
    'WebAPI',
    'FinancialProduct',
    'Taxi',
    'FoodService',
    'BroadcastService',
    'GovernmentService',
    'TaxiService',
    'SizeGroupEnumeration',
    'ReturnLabelSourceEnumeration',
    'PhysicalActivityCategory',
    'ContactPointOption',
    'PriceComponentTypeEnumeration',
    'MapCategoryType',
    'RestrictedDiet',
    'DigitalPlatformEnumeration',
    'PaymentMethodType',
    'IncentiveQualifiedExpenseType',
    'CertificationStatusEnumeration',
    'GovernmentBenefitsType',
    'StatusEnumeration',
    'CarUsageType',
    'FulfillmentTypeEnumeration',
    'SizeSystemEnumeration',
    'Specialty',
    'GenderType',
    'HealthAspectEnumeration',
    'MediaManipulationRatingEnumeration',
    'MediaEnumeration',
    'WarrantyScope',
    'MusicAlbumReleaseType',
    'MedicalEnumeration',
    'DigitalDocumentPermissionType',
    'OfferItemCondition',
    'MeasurementMethodEnum',
    'LegalValueLevel',
    'EnergyEfficiencyEnumeration',
    'BookFormatType',
    'BusinessEntityType',
    'ProductReturnEnumeration',
    'PriceTypeEnumeration',
    'ItemAvailability',
    'ItemListOrderType',
    'RefundTypeEnumeration',
    'TierBenefitEnumeration',
    'GameAvailabilityEnumeration',
    'BoardingPolicyType',
    'BusinessFunction',
    'DeliveryMethod',
    'IncentiveStatus',
    'PurchaseType',
    'QualitativeValue',
    'ReturnFeesEnumeration',
    'IncentiveType',
    'AdultOrientedEnumeration',
    'NonprofitType',
    'RsvpResponseType',
    'ReturnMethodEnumeration',
    'MerchantReturnEnumeration',
    'DayOfWeek',
    'MeasurementTypeEnumeration',
    'MusicReleaseFormatType',
    'EventAttendanceModeEnumeration',
    'MusicAlbumProductionType',
    'GamePlayMode',
    'DefinedRegion',
    'EngineSpecification',
    'ShippingService',
    'QuantitativeValue',
    'RepaymentSpecification',
    'ServicePeriod',
    'WarrantyPromise',
    'DeliveryTimeSettings',
    'ShippingRateSettings',
    'PriceSpecification',
    'QuantitativeValueDistribution',
    'ShippingDeliveryTime',
    'PostalCodeRangeSpecification',
    'MonetaryAmount',
    'ShippingConditions',
    'PropertyValue',
    'OwnershipInfo',
    'InteractionCounter',
    'ExchangeRateSpecification',
    'GeoShape',
    'CDCPMDRecord',
    'TypeAndQuantityNode',
    'OfferShippingDetails',
    'DatedMoneySpecification',
    'ContactPoint',
    'NutritionInformation',
    'GeoCoordinates',
    'OpeningHoursSpecification',
    'EndorsementRating',
    'AggregateRating',
    'RentalCarReservation',
    'LodgingReservation',
    'TrainReservation',
    'BoatReservation',
    'EventReservation',
    'FlightReservation',
    'BusReservation',
    'TaxiReservation',
    'ReservationPackage',
    'FoodEstablishmentReservation',
    'CategoryCode',
    'HowToItem',
    'BreadcrumbList',
    'HowToStep',
    'OfferCatalog',
    'MonetaryGrant',
    'StatisticalVariable',
    'AggregateOffer',
    'OfferForPurchase',
    'OfferForLease',
    'TrainTrip',
    'BusTrip',
    'TouristTrip',
    'Flight',
    'BoatTrip',
    'Energy',
    'Distance',
    'Mass',
    'Duration',
    'RadioChannel',
    'TelevisionChannel',
    'ComicCoverArt',
    'Recipe',
    'HealthTopicContent',
    'VideoGame',
    'VideoObject',
    'AudioObject',
    'MusicVideoObject',
    'AmpStory',
    'DataDownload',
    'TextObject',
    'ImageObject',
    '_3DModel',
    'RadioClip',
    'TVClip',
    'MovieClip',
    'VideoGameClip',
    'ClaimReview',
    'MediaReview',
    'UserReview',
    'EmployerReview',
    'Recommendation',
    'CriticReview',
    'NoteDigitalDocument',
    'SpreadsheetDigitalDocument',
    'TextDigitalDocument',
    'PresentationDigitalDocument',
    'DataFeed',
    'TVSeason',
    'RadioSeason',
    'PodcastSeason',
    'Quiz',
    'Course',
    'Syllabus',
    'MusicAlbum',
    'MusicRelease',
    'Table',
    'WPFooter',
    'WPSideBar',
    'WPAdBlock',
    'WPHeader',
    'SiteNavigationElement',
    'NewsArticle',
    'SatiricalArticle',
    'AdvertiserContentArticle',
    'SocialMediaPosting',
    'Report',
    'ScholarlyArticle',
    'TechArticle',
    'ComicIssue',
    'WebApplication',
    'MobileApplication',
    'CorrectionComment',
    'Question',
    'Answer',
    'EmailMessage',
    'LegislationObject',
    'CategoryCodeSet',
    'CoverArt',
    'RealEstateListing',
    'ProfilePage',
    'MedicalWebPage',
    'SearchResultsPage',
    'CheckoutPage',
    'ContactPage',
    'ItemPage',
    'CollectionPage',
    'AboutPage',
    'QAPage',
    'FAQPage',
    'RadioEpisode',
    'PodcastEpisode',
    'TVEpisode',
    'RadioSeries',
    'Periodical',
    'PodcastSeries',
    'BookSeries',
    'MovieSeries',
    'VideoGameSeries',
    'ResumeAction',
    'SuspendAction',
    'ActivateAction',
    'DeactivateAction',
    'RentAction',
    'OrderAction',
    'PreOrderAction',
    'BuyAction',
    'TipAction',
    'SellAction',
    'PayAction',
    'QuoteAction',
    'IgnoreAction',
    'ReviewAction',
    'ReactAction',
    'ChooseAction',
    'TravelAction',
    'DepartAction',
    'ArriveAction',
    'TieAction',
    'LoseAction',
    'WinAction',
    'TrackAction',
    'DiscoverAction',
    'CheckAction',
    'LendAction',
    'SendAction',
    'MoneyTransfer',
    'ReturnAction',
    'TakeAction',
    'GiveAction',
    'BorrowAction',
    'DonateAction',
    'ReceiveAction',
    'DownloadAction',
    'BookmarkAction',
    'PlanAction',
    'AllocateAction',
    'ApplyAction',
    'DeleteAction',
    'AddAction',
    'ReplaceAction',
    'DrawAction',
    'PhotographAction',
    'CookAction',
    'PaintAction',
    'FilmAction',
    'WriteAction',
    'PerformAction',
    'ExerciseAction',
    'InstallAction',
    'ReadAction',
    'ViewAction',
    'DrinkAction',
    'UseAction',
    'EatAction',
    'ListenAction',
    'PlayGameAction',
    'WatchAction',
    'MarryAction',
    'FollowAction',
    'JoinAction',
    'LeaveAction',
    'SubscribeAction',
    'RegisterAction',
    'CommunicateAction',
    'UnRegisterAction',
    'BefriendAction',
    'Car',
    'Motorcycle',
    'BusOrCoach',
    'MotorizedBicycle',
    'DiagnosticProcedure',
    'SurgicalProcedure',
    'TherapeuticProcedure',
    'TreatmentIndication',
    'ApprovedIndication',
    'PreventionIndication',
    'PathologyTest',
    'BloodTest',
    'ImagingTest',
    'MedicalTestPanel',
    'MedicalRiskCalculator',
    'MedicalRiskScore',
    'PhysicalActivity',
    'Diet',
    'Drug',
    'DietarySupplement',
    'MedicalTrial',
    'MedicalObservationalStudy',
    'InfectiousDisease',
    'MedicalSignOrSymptom',
    'MedicalGuidelineRecommendation',
    'MedicalGuidelineContraindication',
    'Vessel',
    'Ligament',
    'Bone',
    'BrainStructure',
    'Joint',
    'Muscle',
    'Nerve',
    'DoseSchedule',
    'MedicalConditionStage',
    'DrugStrength',
    'DDxElement',
    'MedicalCode',
    'DrugLegalStatus',
    'SportsTeam',
    'DanceGroup',
    'MusicGroup',
    'TheaterGroup',
    'VeterinaryCare',
    'DiagnosticLab',
    'MedicalClinic',
    'Pharmacy',
    'OnlineStore',
    'FundingAgency',
    'ResearchProject',
    'LakeBodyOfWater',
    'Reservoir',
    'Pond',
    'RiverBodyOfWater',
    'SeaBodyOfWater',
    'OceanBodyOfWater',
    'Waterfall',
    'Canal',
    'Dentist',
    'Physician',
    'Optician',
    'Winery',
    'IceCreamShop',
    'BarOrPub',
    'Restaurant',
    'Bakery',
    'CafeOrCoffeeShop',
    'FastFoodRestaurant',
    'Distillery',
    'Brewery',
    'ComedyClub',
    'AmusementPark',
    'Casino',
    'ArtGallery',
    'AdultEntertainment',
    'NightClub',
    'PublicSwimmingPool',
    'BowlingAlley',
    'TennisComplex',
    'GolfCourse',
    'ExerciseGym',
    'SportsClub',
    'InsuranceAgency',
    'BankOrCreditUnion',
    'AutomatedTeller',
    'AccountingService',
    'MovingCompany',
    'Locksmith',
    'GeneralContractor',
    'Plumber',
    'RoofingContractor',
    'HVACBusiness',
    'Electrician',
    'HousePainter',
    'AutoDealer',
    'AutoBodyShop',
    'GasStation',
    'MotorcycleDealer',
    'AutoRental',
    'AutoRepair',
    'AutoWash',
    'MotorcycleRepair',
    'BedAndBreakfast',
    'VacationRental',
    'Campground',
    'Resort',
    'Hotel',
    'Motel',
    'Hostel',
    'HobbyShop',
    'LiquorStore',
    'PawnShop',
    'ElectronicsStore',
    'BookStore',
    'Florist',
    'JewelryStore',
    'HardwareStore',
    'ComputerStore',
    'PetStore',
    'GardenStore',
    'OutletStore',
    'HomeGoodsStore',
    'DepartmentStore',
    'OfficeEquipmentStore',
    'ShoeStore',
    'MobilePhoneStore',
    'MusicStore',
    'BikeStore',
    'AutoPartsStore',
    'FurnitureStore',
    'GroceryStore',
    'MensClothingStore',
    'ConvenienceStore',
    'TireShop',
    'MovieRentalStore',
    'SportingGoodsStore',
    'WholesaleStore',
    'ClothingStore',
    'ToyStore',
    'Attorney',
    'Notary',
    'PostOffice',
    'DaySpa',
    'BeautySalon',
    'HealthClub',
    'HairSalon',
    'NailSalon',
    'TattooParlor',
    'HinduTemple',
    'BuddhistTemple',
    'Mosque',
    'Church',
    'Synagogue',
    'CollegeOrUniversity',
    'ElementarySchool',
    'School',
    'MiddleSchool',
    'HighSchool',
    'Preschool',
    'Embassy',
    'Courthouse',
    'DefenceEstablishment',
    'LegislativeBuilding',
    'CityHall',
    'MeetingRoom',
    'HotelRoom',
    'SingleFamilyResidence',
    'EmployeeRole',
    'ParentAudience',
    'Patient',
    'InvestmentOrDeposit',
    'PaymentService',
    'LoanOrCredit',
    'BankAccount',
    'CurrencyConversionService',
    'PaymentCard',
    'RadioBroadcastService',
    'WearableSizeGroupEnumeration',
    'PaymentStatusType',
    'ReservationStatusType',
    'GameServerStatus',
    'EventStatusType',
    'ActionStatusType',
    'OrderStatus',
    'LegalForceStatus',
    'WearableSizeSystemEnumeration',
    'MedicalSpecialty',
    'IPTCDigitalSourceEnumeration',
    'DrugPrescriptionStatus',
    'MedicalDevicePurpose',
    'MedicalTrialDesign',
    'DrugCostCategory',
    'MedicalProcedureType',
    'DrugPregnancyCategory',
    'PhysicalExam',
    'MedicalObservationalStudyDesign',
    'MedicalEvidenceLevel',
    'MedicalStudyStatus',
    'MedicalImagingTechnique',
    'MedicineSystem',
    'InfectiousAgentClass',
    'MedicalAudienceType',
    'EUEnergyEfficiencyEnumeration',
    'EnergyStarEnergyEfficiencyEnumeration',
    'BedType',
    'SteeringPositionValue',
    'SizeSpecification',
    'DriveWheelConfigurationValue',
    'USNonprofitType',
    'NLNonprofitType',
    'UKNonprofitType',
    'WearableMeasurementTypeEnumeration',
    'BodyMeasurementTypeEnumeration',
    'CompoundPriceSpecification',
    'UnitPriceSpecification',
    'PaymentChargeSpecification',
    'DeliveryChargeSpecification',
    'MonetaryAmountDistribution',
    'LocationFeatureSpecification',
    'GeoCircle',
    'PostalAddress',
    'EmployerAggregateRating',
    'HowToSupply',
    'HowToTool',
    'AMRadioChannel',
    'FMRadioChannel',
    'VideoObjectSnapshot',
    'AudioObjectSnapshot',
    'Audiobook',
    'ImageObjectSnapshot',
    'Barcode',
    'CompleteDataFeed',
    'OpinionNewsArticle',
    'ReviewNewsArticle',
    'ReportageNewsArticle',
    'BackgroundNewsArticle',
    'AnalysisNewsArticle',
    'AskPublicNewsArticle',
    'DiscussionForumPosting',
    'BlogPosting',
    'MedicalScholarlyArticle',
    'APIReference',
    'MediaGallery',
    'Newspaper',
    'ComicSeries',
    'DisagreeAction',
    'DislikeAction',
    'WantAction',
    'EndorseAction',
    'LikeAction',
    'AgreeAction',
    'VoteAction',
    'ScheduleAction',
    'CancelAction',
    'ReserveAction',
    'RejectAction',
    'AuthorizeAction',
    'AcceptAction',
    'AssignAction',
    'InsertAction',
    'WearAction',
    'CommentAction',
    'ReplyAction',
    'CheckOutAction',
    'InviteAction',
    'CheckInAction',
    'AskAction',
    'InformAction',
    'ShareAction',
    'PsychologicalTreatment',
    'MedicalTherapy',
    'MedicalSymptom',
    'MedicalSign',
    'Vein',
    'LymphaticVessel',
    'Artery',
    'MaximumDoseSchedule',
    'ReportedDoseSchedule',
    'RecommendedDoseSchedule',
    'CovidTestingFacility',
    'OnlineMarketplace',
    'PhysiciansOffice',
    'IndividualPhysician',
    'SkiResort',
    'CatholicChurch',
    'BrokerageAccount',
    'DepositAccount',
    'InvestmentFund',
    'MortgageLoan',
    'CreditCard',
    'LiveBlogPosting',
    'VideoGallery',
    'ImageGallery',
    'AppendAction',
    'PrependAction',
    'ConfirmAction',
    'RsvpAction',
    'OccupationalTherapy',
    'PalliativeProcedure',
    'PhysicalTherapy',
    'RadiationTherapy',
    'VitalSign'
]

_lazy_map = {
    'PronounceableText': '.pronounceable_text',
    'CssSelectorType': '.css_selector_type',
    'Thing': '.thing',
    'Person': '.person',
    'Place': '.place',
    'Event': '.event',
    'Intangible': '.intangible',
    'CreativeWork': '.creative_work',
    'Action': '.action',
    'Product': '.product',
    'MedicalEntity': '.medical_entity',
    'StupidType': '.stupid_type',
    'Taxon': '.taxon',
    'Organization': '.organization',
    'BioChemEntity': '.bio_chem_entity',
    'Residence': '.residence',
    'TouristDestination': '.tourist_destination',
    'AdministrativeArea': '.administrative_area',
    'Landform': '.landform',
    'LocalBusiness': '.local_business',
    'CivicStructure': '.civic_structure',
    'TouristAttraction': '.tourist_attraction',
    'Accommodation': '.accommodation',
    'LandmarksOrHistoricalBuildings': '.landmarks_or_historical_buildings',
    'TheaterEvent': '.theater_event',
    'FoodEvent': '.food_event',
    'EducationEvent': '.education_event',
    'Festival': '.festival',
    'SocialEvent': '.social_event',
    'MusicEvent': '.music_event',
    'ScreeningEvent': '.screening_event',
    'VisualArtsEvent': '.visual_arts_event',
    'LiteraryEvent': '.literary_event',
    'UserInteraction': '.user_interaction',
    'DeliveryEvent': '.delivery_event',
    'SportsEvent': '.sports_event',
    'PublicationEvent': '.publication_event',
    'ComedyEvent': '.comedy_event',
    'CourseInstance': '.course_instance',
    'ChildrensEvent': '.childrens_event',
    'DanceEvent': '.dance_event',
    'BusinessEvent': '.business_event',
    'Hackathon': '.hackathon',
    'SaleEvent': '.sale_event',
    'ExhibitionEvent': '.exhibition_event',
    'MediaSubscription': '.media_subscription',
    'VirtualLocation': '.virtual_location',
    'Ticket': '.ticket',
    'DataFeedItem': '.data_feed_item',
    'Series': '.series',
    'Role': '.role',
    'FloorPlan': '.floor_plan',
    'Permit': '.permit',
    'MemberProgramTier': '.member_program_tier',
    'EducationalOccupationalProgram': '.educational_occupational_program',
    'GeospatialGeometry': '.geospatial_geometry',
    'Audience': '.audience',
    'Brand': '.brand',
    'Occupation': '.occupation',
    'ProgramMembership': '.program_membership',
    'Service': '.service',
    'HealthPlanCostSharingSpecification': '.health_plan_cost_sharing_specification',
    'Invoice': '.invoice',
    'HealthInsurancePlan': '.health_insurance_plan',
    'Property': '.property',
    'AlignmentObject': '.alignment_object',
    'MerchantReturnPolicySeasonalOverride': '.merchant_return_policy_seasonal_override',
    'EnergyConsumptionDetails': '.energy_consumption_details',
    'Schedule': '.schedule',
    'Enumeration': '.enumeration',
    'SpeakableSpecification': '.speakable_specification',
    'HealthPlanFormulary': '.health_plan_formulary',
    'Language': '.language',
    'StructuredValue': '.structured_value',
    'MemberProgram': '.member_program',
    'PropertyValueSpecification': '.property_value_specification',
    'Rating': '.rating',
    'DigitalDocumentPermission': '.digital_document_permission',
    'ComputerLanguage': '.computer_language',
    'ProductReturnPolicy': '.product_return_policy',
    'PaymentMethod': '.payment_method',
    'ParcelDelivery': '.parcel_delivery',
    'MerchantReturnPolicy': '.merchant_return_policy',
    'Reservation': '.reservation',
    'JobPosting': '.job_posting',
    'BroadcastFrequencySpecification': '.broadcast_frequency_specification',
    'OccupationalExperienceRequirements': '.occupational_experience_requirements',
    'BedDetails': '.bed_details',
    'GameServer': '.game_server',
    'ServiceChannel': '.service_channel',
    'Demand': '.demand',
    'DefinedTerm': '.defined_term',
    'ActionAccessSpecification': '.action_access_specification',
    'FinancialIncentive': '.financial_incentive',
    'MenuItem': '.menu_item',
    'ListItem': '.list_item',
    'OrderItem': '.order_item',
    'ItemList': '.item_list',
    'HealthPlanNetwork': '.health_plan_network',
    'Grant': '.grant',
    'StatisticalPopulation': '.statistical_population',
    'Order': '.order',
    'ConstraintNode': '.constraint_node',
    'Offer': '.offer',
    'Trip': '.trip',
    'Observation': '.observation',
    'EntryPoint': '.entry_point',
    'Quantity': '.quantity',
    'Seat': '.seat',
    'BroadcastChannel': '.broadcast_channel',
    '_Class': '.__class',
    'Chapter': '.chapter',
    'TVSeries': '.tv_series',
    'WebSite': '.web_site',
    'ComicStory': '.comic_story',
    'HowTo': '.how_to',
    'WebContent': '.web_content',
    'Game': '.game',
    'Guide': '.guide',
    'MediaObject': '.media_object',
    'DataCatalog': '.data_catalog',
    'Clip': '.clip',
    'Review': '.review',
    'Certification': '.certification',
    'Play': '.play',
    'SpecialAnnouncement': '.special_announcement',
    'ShortStory': '.short_story',
    'Photograph': '.photograph',
    'Claim': '.claim',
    'Blog': '.blog',
    'Quotation': '.quotation',
    'DigitalDocument': '.digital_document',
    'Dataset': '.dataset',
    'CreativeWorkSeason': '.creative_work_season',
    'LearningResource': '.learning_resource',
    'MusicPlaylist': '.music_playlist',
    'Menu': '.menu',
    'Sculpture': '.sculpture',
    'Painting': '.painting',
    'WebPageElement': '.web_page_element',
    'Code': '.code',
    'Movie': '.movie',
    'Poster': '.poster',
    'HowToTip': '.how_to_tip',
    'HowToSection': '.how_to_section',
    'MediaReviewItem': '.media_review_item',
    'Book': '.book',
    'Statement': '.statement',
    'Season': '.season',
    'Article': '.article',
    'Atlas': '.atlas',
    'HowToDirection': '.how_to_direction',
    'PublicationIssue': '.publication_issue',
    'Thesis': '.thesis',
    'SoftwareApplication': '.software_application',
    'PublicationVolume': '.publication_volume',
    'Comment': '.comment',
    'MusicComposition': '.music_composition',
    'ExercisePlan': '.exercise_plan',
    'Message': '.message',
    'Conversation': '.conversation',
    'Drawing': '.drawing',
    'Map': '.map',
    'MusicRecording': '.music_recording',
    'Legislation': '.legislation',
    'DefinedTermSet': '.defined_term_set',
    'SoftwareSourceCode': '.software_source_code',
    'HyperTocEntry': '.hyper_toc_entry',
    'VisualArtwork': '.visual_artwork',
    'SheetMusic': '.sheet_music',
    'Collection': '.collection',
    'EducationalOccupationalCredential': '.educational_occupational_credential',
    'WebPage': '.web_page',
    'MenuSection': '.menu_section',
    'Episode': '.episode',
    'Manuscript': '.manuscript',
    'CreativeWorkSeries': '.creative_work_series',
    'MathSolver': '.math_solver',
    'HyperToc': '.hyper_toc',
    'ArchiveComponent': '.archive_component',
    'ControlAction': '.control_action',
    'TradeAction': '.trade_action',
    'AssessAction': '.assess_action',
    'MoveAction': '.move_action',
    'AchieveAction': '.achieve_action',
    'FindAction': '.find_action',
    'TransferAction': '.transfer_action',
    'OrganizeAction': '.organize_action',
    'UpdateAction': '.update_action',
    'CreateAction': '.create_action',
    'PlayAction': '.play_action',
    'SeekToAction': '.seek_to_action',
    'SolveMathAction': '.solve_math_action',
    'ConsumeAction': '.consume_action',
    'InteractAction': '.interact_action',
    'SearchAction': '.search_action',
    'ProductModel': '.product_model',
    'SomeProducts': '.some_products',
    'ProductGroup': '.product_group',
    'ProductCollection': '.product_collection',
    'Vehicle': '.vehicle',
    'IndividualProduct': '.individual_product',
    'MedicalProcedure': '.medical_procedure',
    'MedicalRiskFactor': '.medical_risk_factor',
    'MedicalIndication': '.medical_indication',
    'MedicalTest': '.medical_test',
    'MedicalRiskEstimator': '.medical_risk_estimator',
    'LifestyleModification': '.lifestyle_modification',
    'Substance': '.substance',
    'MedicalContraindication': '.medical_contraindication',
    'MedicalStudy': '.medical_study',
    'MedicalCondition': '.medical_condition',
    'MedicalGuideline': '.medical_guideline',
    'MedicalCause': '.medical_cause',
    'DrugClass': '.drug_class',
    'MedicalDevice': '.medical_device',
    'SuperficialAnatomy': '.superficial_anatomy',
    'DrugCost': '.drug_cost',
    'AnatomicalStructure': '.anatomical_structure',
    'AnatomicalSystem': '.anatomical_system',
    'MedicalIntangible': '.medical_intangible',
    'NewsMediaOrganization': '.news_media_organization',
    'NGO': '.ngo',
    'Cooperative': '.cooperative',
    'SportsOrganization': '.sports_organization',
    'PerformingGroup': '.performing_group',
    'FundingScheme': '.funding_scheme',
    'SearchRescueOrganization': '.search_rescue_organization',
    'LibrarySystem': '.library_system',
    'MedicalOrganization': '.medical_organization',
    'OnlineBusiness': '.online_business',
    'Consortium': '.consortium',
    'WorkersUnion': '.workers_union',
    'GovernmentOrganization': '.government_organization',
    'Project': '.project',
    'ResearchOrganization': '.research_organization',
    'Airline': '.airline',
    'Corporation': '.corporation',
    'PoliticalParty': '.political_party',
    'Protein': '.protein',
    'Gene': '.gene',
    'MolecularEntity': '.molecular_entity',
    'ChemicalSubstance': '.chemical_substance',
    'GatedResidenceCommunity': '.gated_residence_community',
    'ApartmentComplex': '.apartment_complex',
    'Country': '.country',
    'City': '.city',
    'State': '.state',
    'SchoolDistrict': '.school_district',
    'Continent': '.continent',
    'BodyOfWater': '.body_of_water',
    'Mountain': '.mountain',
    'Volcano': '.volcano',
    'RadioStation': '.radio_station',
    'InternetCafe': '.internet_cafe',
    'MedicalBusiness': '.medical_business',
    'EmploymentAgency': '.employment_agency',
    'FoodEstablishment': '.food_establishment',
    'EntertainmentBusiness': '.entertainment_business',
    'SportsActivityLocation': '.sports_activity_location',
    'ShoppingCenter': '.shopping_center',
    'FinancialService': '.financial_service',
    'ChildCare': '.child_care',
    'HomeAndConstructionBusiness': '.home_and_construction_business',
    'AutomotiveBusiness': '.automotive_business',
    'LodgingBusiness': '.lodging_business',
    'Store': '.store',
    'LegalService': '.legal_service',
    'AnimalShelter': '.animal_shelter',
    'TelevisionStation': '.television_station',
    'EmergencyService': '.emergency_service',
    'DryCleaningOrLaundry': '.dry_cleaning_or_laundry',
    'ArchiveOrganization': '.archive_organization',
    'RealEstateAgent': '.real_estate_agent',
    'Library': '.library',
    'RecyclingCenter': '.recycling_center',
    'GovernmentOffice': '.government_office',
    'TravelAgency': '.travel_agency',
    'TouristInformationCenter': '.tourist_information_center',
    'HealthAndBeautyBusiness': '.health_and_beauty_business',
    'ProfessionalService': '.professional_service',
    'SelfStorage': '.self_storage',
    'Playground': '.playground',
    'MusicVenue': '.music_venue',
    'Crematorium': '.crematorium',
    'PoliceStation': '.police_station',
    'PlaceOfWorship': '.place_of_worship',
    'PublicToilet': '.public_toilet',
    'TaxiStand': '.taxi_stand',
    'TrainStation': '.train_station',
    'SubwayStation': '.subway_station',
    'Bridge': '.bridge',
    'EventVenue': '.event_venue',
    'BusStop': '.bus_stop',
    'EducationalOrganization': '.educational_organization',
    'BusStation': '.bus_station',
    'Cemetery': '.cemetery',
    'GovernmentBuilding': '.government_building',
    'Airport': '.airport',
    'StadiumOrArena': '.stadium_or_arena',
    'Beach': '.beach',
    'Park': '.park',
    'RVPark': '.rv_park',
    'PerformingArtsTheater': '.performing_arts_theater',
    'BoatTerminal': '.boat_terminal',
    'Hospital': '.hospital',
    'Aquarium': '.aquarium',
    'Zoo': '.zoo',
    'ParkingFacility': '.parking_facility',
    'Museum': '.museum',
    'MovieTheater': '.movie_theater',
    'FireStation': '.fire_station',
    'Apartment': '.apartment',
    'Room': '.room',
    'Suite': '.suite',
    'House': '.house',
    'CampingPitch': '.camping_pitch',
    'UserCheckins': '.user_checkins',
    'UserBlocks': '.user_blocks',
    'UserComments': '.user_comments',
    'UserTweets': '.user_tweets',
    'UserLikes': '.user_likes',
    'UserPlays': '.user_plays',
    'UserPageVisits': '.user_page_visits',
    'UserPlusOnes': '.user_plus_ones',
    'UserDownloads': '.user_downloads',
    'OnDemandEvent': '.on_demand_event',
    'BroadcastEvent': '.broadcast_event',
    'EventSeries': '.event_series',
    'LinkRole': '.link_role',
    'PerformanceRole': '.performance_role',
    'OrganizationRole': '.organization_role',
    'GovernmentPermit': '.government_permit',
    'WorkBasedProgram': '.work_based_program',
    'Researcher': '.researcher',
    'BusinessAudience': '.business_audience',
    'EducationalAudience': '.educational_audience',
    'PeopleAudience': '.people_audience',
    'MedicalAudience': '.medical_audience',
    'CableOrSatelliteService': '.cable_or_satellite_service',
    'WebAPI': '.web_api',
    'FinancialProduct': '.financial_product',
    'Taxi': '.taxi',
    'FoodService': '.food_service',
    'BroadcastService': '.broadcast_service',
    'GovernmentService': '.government_service',
    'TaxiService': '.taxi_service',
    'SizeGroupEnumeration': '.size_group_enumeration',
    'ReturnLabelSourceEnumeration': '.return_label_source_enumeration',
    'PhysicalActivityCategory': '.physical_activity_category',
    'ContactPointOption': '.contact_point_option',
    'PriceComponentTypeEnumeration': '.price_component_type_enumeration',
    'MapCategoryType': '.map_category_type',
    'RestrictedDiet': '.restricted_diet',
    'DigitalPlatformEnumeration': '.digital_platform_enumeration',
    'PaymentMethodType': '.payment_method_type',
    'IncentiveQualifiedExpenseType': '.incentive_qualified_expense_type',
    'CertificationStatusEnumeration': '.certification_status_enumeration',
    'GovernmentBenefitsType': '.government_benefits_type',
    'StatusEnumeration': '.status_enumeration',
    'CarUsageType': '.car_usage_type',
    'FulfillmentTypeEnumeration': '.fulfillment_type_enumeration',
    'SizeSystemEnumeration': '.size_system_enumeration',
    'Specialty': '.specialty',
    'GenderType': '.gender_type',
    'HealthAspectEnumeration': '.health_aspect_enumeration',
    'MediaManipulationRatingEnumeration': '.media_manipulation_rating_enumeration',
    'MediaEnumeration': '.media_enumeration',
    'WarrantyScope': '.warranty_scope',
    'MusicAlbumReleaseType': '.music_album_release_type',
    'MedicalEnumeration': '.medical_enumeration',
    'DigitalDocumentPermissionType': '.digital_document_permission_type',
    'OfferItemCondition': '.offer_item_condition',
    'MeasurementMethodEnum': '.measurement_method_enum',
    'LegalValueLevel': '.legal_value_level',
    'EnergyEfficiencyEnumeration': '.energy_efficiency_enumeration',
    'BookFormatType': '.book_format_type',
    'BusinessEntityType': '.business_entity_type',
    'ProductReturnEnumeration': '.product_return_enumeration',
    'PriceTypeEnumeration': '.price_type_enumeration',
    'ItemAvailability': '.item_availability',
    'ItemListOrderType': '.item_list_order_type',
    'RefundTypeEnumeration': '.refund_type_enumeration',
    'TierBenefitEnumeration': '.tier_benefit_enumeration',
    'GameAvailabilityEnumeration': '.game_availability_enumeration',
    'BoardingPolicyType': '.boarding_policy_type',
    'BusinessFunction': '.business_function',
    'DeliveryMethod': '.delivery_method',
    'IncentiveStatus': '.incentive_status',
    'PurchaseType': '.purchase_type',
    'QualitativeValue': '.qualitative_value',
    'ReturnFeesEnumeration': '.return_fees_enumeration',
    'IncentiveType': '.incentive_type',
    'AdultOrientedEnumeration': '.adult_oriented_enumeration',
    'NonprofitType': '.nonprofit_type',
    'RsvpResponseType': '.rsvp_response_type',
    'ReturnMethodEnumeration': '.return_method_enumeration',
    'MerchantReturnEnumeration': '.merchant_return_enumeration',
    'DayOfWeek': '.day_of_week',
    'MeasurementTypeEnumeration': '.measurement_type_enumeration',
    'MusicReleaseFormatType': '.music_release_format_type',
    'EventAttendanceModeEnumeration': '.event_attendance_mode_enumeration',
    'MusicAlbumProductionType': '.music_album_production_type',
    'GamePlayMode': '.game_play_mode',
    'DefinedRegion': '.defined_region',
    'EngineSpecification': '.engine_specification',
    'ShippingService': '.shipping_service',
    'QuantitativeValue': '.quantitative_value',
    'RepaymentSpecification': '.repayment_specification',
    'ServicePeriod': '.service_period',
    'WarrantyPromise': '.warranty_promise',
    'DeliveryTimeSettings': '.delivery_time_settings',
    'ShippingRateSettings': '.shipping_rate_settings',
    'PriceSpecification': '.price_specification',
    'QuantitativeValueDistribution': '.quantitative_value_distribution',
    'ShippingDeliveryTime': '.shipping_delivery_time',
    'PostalCodeRangeSpecification': '.postal_code_range_specification',
    'MonetaryAmount': '.monetary_amount',
    'ShippingConditions': '.shipping_conditions',
    'PropertyValue': '.property_value',
    'OwnershipInfo': '.ownership_info',
    'InteractionCounter': '.interaction_counter',
    'ExchangeRateSpecification': '.exchange_rate_specification',
    'GeoShape': '.geo_shape',
    'CDCPMDRecord': '.cdcpmd_record',
    'TypeAndQuantityNode': '.type_and_quantity_node',
    'OfferShippingDetails': '.offer_shipping_details',
    'DatedMoneySpecification': '.dated_money_specification',
    'ContactPoint': '.contact_point',
    'NutritionInformation': '.nutrition_information',
    'GeoCoordinates': '.geo_coordinates',
    'OpeningHoursSpecification': '.opening_hours_specification',
    'EndorsementRating': '.endorsement_rating',
    'AggregateRating': '.aggregate_rating',
    'RentalCarReservation': '.rental_car_reservation',
    'LodgingReservation': '.lodging_reservation',
    'TrainReservation': '.train_reservation',
    'BoatReservation': '.boat_reservation',
    'EventReservation': '.event_reservation',
    'FlightReservation': '.flight_reservation',
    'BusReservation': '.bus_reservation',
    'TaxiReservation': '.taxi_reservation',
    'ReservationPackage': '.reservation_package',
    'FoodEstablishmentReservation': '.food_establishment_reservation',
    'CategoryCode': '.category_code',
    'HowToItem': '.how_to_item',
    'BreadcrumbList': '.breadcrumb_list',
    'HowToStep': '.how_to_step',
    'OfferCatalog': '.offer_catalog',
    'MonetaryGrant': '.monetary_grant',
    'StatisticalVariable': '.statistical_variable',
    'AggregateOffer': '.aggregate_offer',
    'OfferForPurchase': '.offer_for_purchase',
    'OfferForLease': '.offer_for_lease',
    'TrainTrip': '.train_trip',
    'BusTrip': '.bus_trip',
    'TouristTrip': '.tourist_trip',
    'Flight': '.flight',
    'BoatTrip': '.boat_trip',
    'Energy': '.energy',
    'Distance': '.distance',
    'Mass': '.mass',
    'Duration': '.duration',
    'RadioChannel': '.radio_channel',
    'TelevisionChannel': '.television_channel',
    'ComicCoverArt': '.comic_cover_art',
    'Recipe': '.recipe',
    'HealthTopicContent': '.health_topic_content',
    'VideoGame': '.video_game',
    'VideoObject': '.video_object',
    'AudioObject': '.audio_object',
    'MusicVideoObject': '.music_video_object',
    'AmpStory': '.amp_story',
    'DataDownload': '.data_download',
    'TextObject': '.text_object',
    'ImageObject': '.image_object',
    '_3DModel': '._3_d_model',
    'RadioClip': '.radio_clip',
    'TVClip': '.tv_clip',
    'MovieClip': '.movie_clip',
    'VideoGameClip': '.video_game_clip',
    'ClaimReview': '.claim_review',
    'MediaReview': '.media_review',
    'UserReview': '.user_review',
    'EmployerReview': '.employer_review',
    'Recommendation': '.recommendation',
    'CriticReview': '.critic_review',
    'NoteDigitalDocument': '.note_digital_document',
    'SpreadsheetDigitalDocument': '.spreadsheet_digital_document',
    'TextDigitalDocument': '.text_digital_document',
    'PresentationDigitalDocument': '.presentation_digital_document',
    'DataFeed': '.data_feed',
    'TVSeason': '.tv_season',
    'RadioSeason': '.radio_season',
    'PodcastSeason': '.podcast_season',
    'Quiz': '.quiz',
    'Course': '.course',
    'Syllabus': '.syllabus',
    'MusicAlbum': '.music_album',
    'MusicRelease': '.music_release',
    'Table': '.table',
    'WPFooter': '.wp_footer',
    'WPSideBar': '.wp_side_bar',
    'WPAdBlock': '.wp_ad_block',
    'WPHeader': '.wp_header',
    'SiteNavigationElement': '.site_navigation_element',
    'NewsArticle': '.news_article',
    'SatiricalArticle': '.satirical_article',
    'AdvertiserContentArticle': '.advertiser_content_article',
    'SocialMediaPosting': '.social_media_posting',
    'Report': '.report',
    'ScholarlyArticle': '.scholarly_article',
    'TechArticle': '.tech_article',
    'ComicIssue': '.comic_issue',
    'WebApplication': '.web_application',
    'MobileApplication': '.mobile_application',
    'CorrectionComment': '.correction_comment',
    'Question': '.question',
    'Answer': '.answer',
    'EmailMessage': '.email_message',
    'LegislationObject': '.legislation_object',
    'CategoryCodeSet': '.category_code_set',
    'CoverArt': '.cover_art',
    'RealEstateListing': '.real_estate_listing',
    'ProfilePage': '.profile_page',
    'MedicalWebPage': '.medical_web_page',
    'SearchResultsPage': '.search_results_page',
    'CheckoutPage': '.checkout_page',
    'ContactPage': '.contact_page',
    'ItemPage': '.item_page',
    'CollectionPage': '.collection_page',
    'AboutPage': '.about_page',
    'QAPage': '.qa_page',
    'FAQPage': '.faq_page',
    'RadioEpisode': '.radio_episode',
    'PodcastEpisode': '.podcast_episode',
    'TVEpisode': '.tv_episode',
    'RadioSeries': '.radio_series',
    'Periodical': '.periodical',
    'PodcastSeries': '.podcast_series',
    'BookSeries': '.book_series',
    'MovieSeries': '.movie_series',
    'VideoGameSeries': '.video_game_series',
    'ResumeAction': '.resume_action',
    'SuspendAction': '.suspend_action',
    'ActivateAction': '.activate_action',
    'DeactivateAction': '.deactivate_action',
    'RentAction': '.rent_action',
    'OrderAction': '.order_action',
    'PreOrderAction': '.pre_order_action',
    'BuyAction': '.buy_action',
    'TipAction': '.tip_action',
    'SellAction': '.sell_action',
    'PayAction': '.pay_action',
    'QuoteAction': '.quote_action',
    'IgnoreAction': '.ignore_action',
    'ReviewAction': '.review_action',
    'ReactAction': '.react_action',
    'ChooseAction': '.choose_action',
    'TravelAction': '.travel_action',
    'DepartAction': '.depart_action',
    'ArriveAction': '.arrive_action',
    'TieAction': '.tie_action',
    'LoseAction': '.lose_action',
    'WinAction': '.win_action',
    'TrackAction': '.track_action',
    'DiscoverAction': '.discover_action',
    'CheckAction': '.check_action',
    'LendAction': '.lend_action',
    'SendAction': '.send_action',
    'MoneyTransfer': '.money_transfer',
    'ReturnAction': '.return_action',
    'TakeAction': '.take_action',
    'GiveAction': '.give_action',
    'BorrowAction': '.borrow_action',
    'DonateAction': '.donate_action',
    'ReceiveAction': '.receive_action',
    'DownloadAction': '.download_action',
    'BookmarkAction': '.bookmark_action',
    'PlanAction': '.plan_action',
    'AllocateAction': '.allocate_action',
    'ApplyAction': '.apply_action',
    'DeleteAction': '.delete_action',
    'AddAction': '.add_action',
    'ReplaceAction': '.replace_action',
    'DrawAction': '.draw_action',
    'PhotographAction': '.photograph_action',
    'CookAction': '.cook_action',
    'PaintAction': '.paint_action',
    'FilmAction': '.film_action',
    'WriteAction': '.write_action',
    'PerformAction': '.perform_action',
    'ExerciseAction': '.exercise_action',
    'InstallAction': '.install_action',
    'ReadAction': '.read_action',
    'ViewAction': '.view_action',
    'DrinkAction': '.drink_action',
    'UseAction': '.use_action',
    'EatAction': '.eat_action',
    'ListenAction': '.listen_action',
    'PlayGameAction': '.play_game_action',
    'WatchAction': '.watch_action',
    'MarryAction': '.marry_action',
    'FollowAction': '.follow_action',
    'JoinAction': '.join_action',
    'LeaveAction': '.leave_action',
    'SubscribeAction': '.subscribe_action',
    'RegisterAction': '.register_action',
    'CommunicateAction': '.communicate_action',
    'UnRegisterAction': '.un_register_action',
    'BefriendAction': '.befriend_action',
    'Car': '.car',
    'Motorcycle': '.motorcycle',
    'BusOrCoach': '.bus_or_coach',
    'MotorizedBicycle': '.motorized_bicycle',
    'DiagnosticProcedure': '.diagnostic_procedure',
    'SurgicalProcedure': '.surgical_procedure',
    'TherapeuticProcedure': '.therapeutic_procedure',
    'TreatmentIndication': '.treatment_indication',
    'ApprovedIndication': '.approved_indication',
    'PreventionIndication': '.prevention_indication',
    'PathologyTest': '.pathology_test',
    'BloodTest': '.blood_test',
    'ImagingTest': '.imaging_test',
    'MedicalTestPanel': '.medical_test_panel',
    'MedicalRiskCalculator': '.medical_risk_calculator',
    'MedicalRiskScore': '.medical_risk_score',
    'PhysicalActivity': '.physical_activity',
    'Diet': '.diet',
    'Drug': '.drug',
    'DietarySupplement': '.dietary_supplement',
    'MedicalTrial': '.medical_trial',
    'MedicalObservationalStudy': '.medical_observational_study',
    'InfectiousDisease': '.infectious_disease',
    'MedicalSignOrSymptom': '.medical_sign_or_symptom',
    'MedicalGuidelineRecommendation': '.medical_guideline_recommendation',
    'MedicalGuidelineContraindication': '.medical_guideline_contraindication',
    'Vessel': '.vessel',
    'Ligament': '.ligament',
    'Bone': '.bone',
    'BrainStructure': '.brain_structure',
    'Joint': '.joint',
    'Muscle': '.muscle',
    'Nerve': '.nerve',
    'DoseSchedule': '.dose_schedule',
    'MedicalConditionStage': '.medical_condition_stage',
    'DrugStrength': '.drug_strength',
    'DDxElement': '.d_dx_element',
    'MedicalCode': '.medical_code',
    'DrugLegalStatus': '.drug_legal_status',
    'SportsTeam': '.sports_team',
    'DanceGroup': '.dance_group',
    'MusicGroup': '.music_group',
    'TheaterGroup': '.theater_group',
    'VeterinaryCare': '.veterinary_care',
    'DiagnosticLab': '.diagnostic_lab',
    'MedicalClinic': '.medical_clinic',
    'Pharmacy': '.pharmacy',
    'OnlineStore': '.online_store',
    'FundingAgency': '.funding_agency',
    'ResearchProject': '.research_project',
    'LakeBodyOfWater': '.lake_body_of_water',
    'Reservoir': '.reservoir',
    'Pond': '.pond',
    'RiverBodyOfWater': '.river_body_of_water',
    'SeaBodyOfWater': '.sea_body_of_water',
    'OceanBodyOfWater': '.ocean_body_of_water',
    'Waterfall': '.waterfall',
    'Canal': '.canal',
    'Dentist': '.dentist',
    'Physician': '.physician',
    'Optician': '.optician',
    'Winery': '.winery',
    'IceCreamShop': '.ice_cream_shop',
    'BarOrPub': '.bar_or_pub',
    'Restaurant': '.restaurant',
    'Bakery': '.bakery',
    'CafeOrCoffeeShop': '.cafe_or_coffee_shop',
    'FastFoodRestaurant': '.fast_food_restaurant',
    'Distillery': '.distillery',
    'Brewery': '.brewery',
    'ComedyClub': '.comedy_club',
    'AmusementPark': '.amusement_park',
    'Casino': '.casino',
    'ArtGallery': '.art_gallery',
    'AdultEntertainment': '.adult_entertainment',
    'NightClub': '.night_club',
    'PublicSwimmingPool': '.public_swimming_pool',
    'BowlingAlley': '.bowling_alley',
    'TennisComplex': '.tennis_complex',
    'GolfCourse': '.golf_course',
    'ExerciseGym': '.exercise_gym',
    'SportsClub': '.sports_club',
    'InsuranceAgency': '.insurance_agency',
    'BankOrCreditUnion': '.bank_or_credit_union',
    'AutomatedTeller': '.automated_teller',
    'AccountingService': '.accounting_service',
    'MovingCompany': '.moving_company',
    'Locksmith': '.locksmith',
    'GeneralContractor': '.general_contractor',
    'Plumber': '.plumber',
    'RoofingContractor': '.roofing_contractor',
    'HVACBusiness': '.hvac_business',
    'Electrician': '.electrician',
    'HousePainter': '.house_painter',
    'AutoDealer': '.auto_dealer',
    'AutoBodyShop': '.auto_body_shop',
    'GasStation': '.gas_station',
    'MotorcycleDealer': '.motorcycle_dealer',
    'AutoRental': '.auto_rental',
    'AutoRepair': '.auto_repair',
    'AutoWash': '.auto_wash',
    'MotorcycleRepair': '.motorcycle_repair',
    'BedAndBreakfast': '.bed_and_breakfast',
    'VacationRental': '.vacation_rental',
    'Campground': '.campground',
    'Resort': '.resort',
    'Hotel': '.hotel',
    'Motel': '.motel',
    'Hostel': '.hostel',
    'HobbyShop': '.hobby_shop',
    'LiquorStore': '.liquor_store',
    'PawnShop': '.pawn_shop',
    'ElectronicsStore': '.electronics_store',
    'BookStore': '.book_store',
    'Florist': '.florist',
    'JewelryStore': '.jewelry_store',
    'HardwareStore': '.hardware_store',
    'ComputerStore': '.computer_store',
    'PetStore': '.pet_store',
    'GardenStore': '.garden_store',
    'OutletStore': '.outlet_store',
    'HomeGoodsStore': '.home_goods_store',
    'DepartmentStore': '.department_store',
    'OfficeEquipmentStore': '.office_equipment_store',
    'ShoeStore': '.shoe_store',
    'MobilePhoneStore': '.mobile_phone_store',
    'MusicStore': '.music_store',
    'BikeStore': '.bike_store',
    'AutoPartsStore': '.auto_parts_store',
    'FurnitureStore': '.furniture_store',
    'GroceryStore': '.grocery_store',
    'MensClothingStore': '.mens_clothing_store',
    'ConvenienceStore': '.convenience_store',
    'TireShop': '.tire_shop',
    'MovieRentalStore': '.movie_rental_store',
    'SportingGoodsStore': '.sporting_goods_store',
    'WholesaleStore': '.wholesale_store',
    'ClothingStore': '.clothing_store',
    'ToyStore': '.toy_store',
    'Attorney': '.attorney',
    'Notary': '.notary',
    'PostOffice': '.post_office',
    'DaySpa': '.day_spa',
    'BeautySalon': '.beauty_salon',
    'HealthClub': '.health_club',
    'HairSalon': '.hair_salon',
    'NailSalon': '.nail_salon',
    'TattooParlor': '.tattoo_parlor',
    'HinduTemple': '.hindu_temple',
    'BuddhistTemple': '.buddhist_temple',
    'Mosque': '.mosque',
    'Church': '.church',
    'Synagogue': '.synagogue',
    'CollegeOrUniversity': '.college_or_university',
    'ElementarySchool': '.elementary_school',
    'School': '.school',
    'MiddleSchool': '.middle_school',
    'HighSchool': '.high_school',
    'Preschool': '.preschool',
    'Embassy': '.embassy',
    'Courthouse': '.courthouse',
    'DefenceEstablishment': '.defence_establishment',
    'LegislativeBuilding': '.legislative_building',
    'CityHall': '.city_hall',
    'MeetingRoom': '.meeting_room',
    'HotelRoom': '.hotel_room',
    'SingleFamilyResidence': '.single_family_residence',
    'EmployeeRole': '.employee_role',
    'ParentAudience': '.parent_audience',
    'Patient': '.patient',
    'InvestmentOrDeposit': '.investment_or_deposit',
    'PaymentService': '.payment_service',
    'LoanOrCredit': '.loan_or_credit',
    'BankAccount': '.bank_account',
    'CurrencyConversionService': '.currency_conversion_service',
    'PaymentCard': '.payment_card',
    'RadioBroadcastService': '.radio_broadcast_service',
    'WearableSizeGroupEnumeration': '.wearable_size_group_enumeration',
    'PaymentStatusType': '.payment_status_type',
    'ReservationStatusType': '.reservation_status_type',
    'GameServerStatus': '.game_server_status',
    'EventStatusType': '.event_status_type',
    'ActionStatusType': '.action_status_type',
    'OrderStatus': '.order_status',
    'LegalForceStatus': '.legal_force_status',
    'WearableSizeSystemEnumeration': '.wearable_size_system_enumeration',
    'MedicalSpecialty': '.medical_specialty',
    'IPTCDigitalSourceEnumeration': '.iptc_digital_source_enumeration',
    'DrugPrescriptionStatus': '.drug_prescription_status',
    'MedicalDevicePurpose': '.medical_device_purpose',
    'MedicalTrialDesign': '.medical_trial_design',
    'DrugCostCategory': '.drug_cost_category',
    'MedicalProcedureType': '.medical_procedure_type',
    'DrugPregnancyCategory': '.drug_pregnancy_category',
    'PhysicalExam': '.physical_exam',
    'MedicalObservationalStudyDesign': '.medical_observational_study_design',
    'MedicalEvidenceLevel': '.medical_evidence_level',
    'MedicalStudyStatus': '.medical_study_status',
    'MedicalImagingTechnique': '.medical_imaging_technique',
    'MedicineSystem': '.medicine_system',
    'InfectiousAgentClass': '.infectious_agent_class',
    'MedicalAudienceType': '.medical_audience_type',
    'EUEnergyEfficiencyEnumeration': '.eu_energy_efficiency_enumeration',
    'EnergyStarEnergyEfficiencyEnumeration': '.energy_star_energy_efficiency_enumeration',
    'BedType': '.bed_type',
    'SteeringPositionValue': '.steering_position_value',
    'SizeSpecification': '.size_specification',
    'DriveWheelConfigurationValue': '.drive_wheel_configuration_value',
    'USNonprofitType': '.us_nonprofit_type',
    'NLNonprofitType': '.nl_nonprofit_type',
    'UKNonprofitType': '.uk_nonprofit_type',
    'WearableMeasurementTypeEnumeration': '.wearable_measurement_type_enumeration',
    'BodyMeasurementTypeEnumeration': '.body_measurement_type_enumeration',
    'CompoundPriceSpecification': '.compound_price_specification',
    'UnitPriceSpecification': '.unit_price_specification',
    'PaymentChargeSpecification': '.payment_charge_specification',
    'DeliveryChargeSpecification': '.delivery_charge_specification',
    'MonetaryAmountDistribution': '.monetary_amount_distribution',
    'LocationFeatureSpecification': '.location_feature_specification',
    'GeoCircle': '.geo_circle',
    'PostalAddress': '.postal_address',
    'EmployerAggregateRating': '.employer_aggregate_rating',
    'HowToSupply': '.how_to_supply',
    'HowToTool': '.how_to_tool',
    'AMRadioChannel': '.am_radio_channel',
    'FMRadioChannel': '.fm_radio_channel',
    'VideoObjectSnapshot': '.video_object_snapshot',
    'AudioObjectSnapshot': '.audio_object_snapshot',
    'Audiobook': '.audiobook',
    'ImageObjectSnapshot': '.image_object_snapshot',
    'Barcode': '.barcode',
    'CompleteDataFeed': '.complete_data_feed',
    'OpinionNewsArticle': '.opinion_news_article',
    'ReviewNewsArticle': '.review_news_article',
    'ReportageNewsArticle': '.reportage_news_article',
    'BackgroundNewsArticle': '.background_news_article',
    'AnalysisNewsArticle': '.analysis_news_article',
    'AskPublicNewsArticle': '.ask_public_news_article',
    'DiscussionForumPosting': '.discussion_forum_posting',
    'BlogPosting': '.blog_posting',
    'MedicalScholarlyArticle': '.medical_scholarly_article',
    'APIReference': '.api_reference',
    'MediaGallery': '.media_gallery',
    'Newspaper': '.newspaper',
    'ComicSeries': '.comic_series',
    'DisagreeAction': '.disagree_action',
    'DislikeAction': '.dislike_action',
    'WantAction': '.want_action',
    'EndorseAction': '.endorse_action',
    'LikeAction': '.like_action',
    'AgreeAction': '.agree_action',
    'VoteAction': '.vote_action',
    'ScheduleAction': '.schedule_action',
    'CancelAction': '.cancel_action',
    'ReserveAction': '.reserve_action',
    'RejectAction': '.reject_action',
    'AuthorizeAction': '.authorize_action',
    'AcceptAction': '.accept_action',
    'AssignAction': '.assign_action',
    'InsertAction': '.insert_action',
    'WearAction': '.wear_action',
    'CommentAction': '.comment_action',
    'ReplyAction': '.reply_action',
    'CheckOutAction': '.check_out_action',
    'InviteAction': '.invite_action',
    'CheckInAction': '.check_in_action',
    'AskAction': '.ask_action',
    'InformAction': '.inform_action',
    'ShareAction': '.share_action',
    'PsychologicalTreatment': '.psychological_treatment',
    'MedicalTherapy': '.medical_therapy',
    'MedicalSymptom': '.medical_symptom',
    'MedicalSign': '.medical_sign',
    'Vein': '.vein',
    'LymphaticVessel': '.lymphatic_vessel',
    'Artery': '.artery',
    'MaximumDoseSchedule': '.maximum_dose_schedule',
    'ReportedDoseSchedule': '.reported_dose_schedule',
    'RecommendedDoseSchedule': '.recommended_dose_schedule',
    'CovidTestingFacility': '.covid_testing_facility',
    'OnlineMarketplace': '.online_marketplace',
    'PhysiciansOffice': '.physicians_office',
    'IndividualPhysician': '.individual_physician',
    'SkiResort': '.ski_resort',
    'CatholicChurch': '.catholic_church',
    'BrokerageAccount': '.brokerage_account',
    'DepositAccount': '.deposit_account',
    'InvestmentFund': '.investment_fund',
    'MortgageLoan': '.mortgage_loan',
    'CreditCard': '.credit_card',
    'LiveBlogPosting': '.live_blog_posting',
    'VideoGallery': '.video_gallery',
    'ImageGallery': '.image_gallery',
    'AppendAction': '.append_action',
    'PrependAction': '.prepend_action',
    'ConfirmAction': '.confirm_action',
    'RsvpAction': '.rsvp_action',
    'OccupationalTherapy': '.occupational_therapy',
    'PalliativeProcedure': '.palliative_procedure',
    'PhysicalTherapy': '.physical_therapy',
    'RadiationTherapy': '.radiation_therapy',
    'VitalSign': '.vital_sign',
}

def __getattr__(name): 
    mod = importlib.import_module(_lazy_map[name], __name__)
    return getattr(mod, name)

if TYPE_CHECKING:
    for _n, _m in _lazy_map.items():
        globals()[_n] = getattr(importlib.import_module(_m, __name__), _n)
        