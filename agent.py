def get_valid_input(input_string, valid_options):
    input_string += " ({}) ".format(", ".join(valid_options))

    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Property:
    """Class which represents Property"""

    def __init__(self, square_feet='', beds='',
                 baths='', **kwargs):
        """Initialized the object"""
        # super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """Print all information about the object"""
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        """
        Gathers all the necessary information about the object
        """
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)


class Apartment:
    """Class which represents Apartment"""
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        """Initialized the object"""
        self.property = Property(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """Print all information about the object"""
        self.property.display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    def prompt_init():
        """
        Gathers all the necessary information about the object
        """

        parent_init = Property.prompt_init()
        laundry = ''
        while laundry.lower() not in \
                Apartment.valid_laundries:
            laundry = input("What laundry facilities does "
                            "the property have? ({})".format(
                ", ".join(Apartment.valid_laundries)))

        balcony = ''
        while balcony.lower() not in \
                Apartment.valid_balconies:
            balcony = input(
                "Does the property have a balcony? "
                "({})".format(", ".join(Apartment.valid_balconies)))
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class House:
    """Class which represents House"""
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='',
                 garage='', fenced='', **kwargs):
        """Initialized the object"""
        self.property = Property(**kwargs)

        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """Print all information about the object"""
        self.property.display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        """
        Gathers all the necessary information about the object
        """
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
                                 House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
                                 House.valid_garage)
        num_stories = input("How many stories? ")
        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Purchase:
    """Class which represents Purchase"""

    def __init__(self, price='', taxes='', **kwargs):
        """Initialized the object"""
        # super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        """Print all information about the object"""
        # super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        """
        Gathers all the necessary information about the object
        """
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are the estimated taxes? "))

    prompt_init = staticmethod(prompt_init)


class Rental:
    """Class which represents Rental"""

    def __init__(self, furnished='', utilities='',
                 rent='', **kwargs):
        """Initialized the object"""
        # super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """Print all information about the object"""
        # super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(
            self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        """
        Gathers all the necessary information about the object
        """
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input(
                "What are the estimated utilities? "),
            furnished=get_valid_input(
                "Is the property furnished? ",
                ("yes", "no")))

    prompt_init = staticmethod(prompt_init)


class ApartmentRental():
    """
    Represents information about an apartment which be rented
    """

    def __init__(self, **kwargs):
        """Initialized an object"""
        self.rental = Rental(**kwargs)
        self.apartment = Apartment(**kwargs)

    def display(self):
        """
        Print all information
        """
        self.apartment.display()
        self.rental.display()

    def prompt_init():
        """
        Gathers all the necessary information about the object
        """
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class HouseRental():
    """
    Represents information about a house which be rented
    """

    def __init__(self, **kwargs):
        """Initialized an object"""
        self.rental = Rental(**kwargs)
        self.house = House(**kwargs)

    def display(self):
        """
        Print all information
        """
        self.house.display()
        self.rental.display()

    def prompt_init():
        """
        Gathers all the necessary information about the object
        """
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase():
    """
    Represents information about an apartment which be purchased
    """

    def __init__(self, **kwargs):
        """Initialized an object"""
        self.purchase = Purchase(**kwargs)
        self.apartment = Apartment(**kwargs)

    def display(self):
        """
        Print all information
        """
        self.apartment.display()
        self.purchase.display()

    def prompt_init():
        """
        Gathers all the necessary information about the object
        """
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class HousePurchase:
    """
    Represents information about an house which be purchased
    """

    def __init__(self, **kwargs):
        """Initialized an object"""
        self.purchase = Purchase(**kwargs)
        self.house = House(**kwargs)

    def display(self):
        """
        Print all information
        """
        self.house.display()
        self.purchase.display()

    def prompt_init():
        """
        Gathers all the necessary information about the object
        """
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class Agent:
    """
    Class for Agent representation
    """
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def __init__(self):
        self.property_list = []
        self.client_dict = {("house", "rental"): [],
                            ("house", "purchase"): [],
                            ("apartment", "rental"): [],
                            ("apartment", "purchase"): []}

    def display_properties(self):
        """
        Print all information about properties
        """
        for property in self.property_list:
            property.display()

    def add_property(self):
        """
        Add properties to property list
        """
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")).lower()

        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")).lower()
        property_class = self.type_map[
            (property_type, payment_type)]
        init_args = property_class.prompt_init()
        self.property_list.append(property_class(**init_args))
        self.inform_clients((property_type, payment_type))

    def find_interested_property(self):
        """
        Find better property for client
        """
        property_type = get_valid_input(
            "What type of property you want to find? ",
            ("house", "apartment")).lower()

        payment_type = get_valid_input(
            "What payment type you want to find? ",
            ("purchase", "rental")).lower()
        property_class = self.type_map[
            (property_type, payment_type)]

        for property in self.property_list:
            if isinstance(property, property_class):
                property.display()

        answer = get_valid_input(
            "Do you want to leave your contact information" +
            "and we called you when we find the property,\n" +
            "which can be interested for you?", ("yes", "no"))
        if answer == "yes":
            contacts = input("Write them down, please: ")
            self.client_dict[(property_type, payment_type)].append(
                contacts)
        else:
            print("Thank you, goodbye")

    def inform_clients(self, type_clients):
        print()
        if len(self.client_dict[type_clients]) != 0:
            print("If it were a real system,",
                  " it would notify a person with these contact details:")
            for i in self.client_dict[type_clients]:
                print("notify ", i)
            print("That's all")
