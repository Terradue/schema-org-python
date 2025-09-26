from schemaorg_models.enumeration import Enumeration


class PaymentMethodType(Enumeration):
    """
The type of payment method, only for generic payment types, specific forms of payments, like card payment should be expressed using subclasses of PaymentMethod.
    """
