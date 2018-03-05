from unittest import TestCase
import agent


class TestAgent(TestCase):

    def test_Property__init__(self):
        p = agent.Property(square_feet='100', beds='1',
                           baths='2')
        self.assertEqual(p.square_feet, "100")
        self.assertEqual(p.num_bedrooms, "1")
        self.assertEqual(p.num_baths, "2")

    def test_Apartment__init__(self):
        p = agent.Apartment(balcony='yes', laundry='none')

        self.assertEqual(p.balcony, "yes")
        self.assertEqual(p.laundry, "none")

    def test_House__init__(self):
        p = agent.House(num_stories='1',
                        garage='detached', fenced='yes', square_feet='100',
                        beds='1',
                        baths='2')
        self.assertEqual(p.property.square_feet, "100")
        self.assertEqual(p.property.num_bedrooms, "1")
        self.assertEqual(p.property.num_baths, "2")
        self.assertEqual(p.num_stories, '1')
        self.assertEqual(p.garage, 'detached')
        self.assertEqual(p.fenced, 'yes')

    def test_Purchase__init__(self):
        p = agent.Purchase(price='1000', taxes='1')
        self.assertEqual(p.price, "1000")
        self.assertEqual(p.taxes, '1')

    def test_Rental__init__(self):
        t = agent.Rental(furnished='no', utilities='none',
                         rent='100')
        self.assertEqual(t.furnished, 'no')
        self.assertEqual(t.utilities, 'none')
        self.assertEqual(t.rent, '100')

    def test_ApartmentRental__init__(self):
        t = agent.ApartmentRental(furnished='no', utilities='none',
                                  rent='100', balcony='yes', laundry='none')

        self.assertEqual(t.rental.furnished, 'no')
        self.assertEqual(t.rental.utilities, 'none')
        self.assertEqual(t.rental.rent, '100')

        self.assertEqual(t.apartment.balcony, "yes")
        self.assertEqual(t.apartment.laundry, "none")

    def test_HouseRental__init__(self):
        t = agent.HouseRental(num_stories='1',
                              garage='detached',
                              fenced='yes',
                              square_feet='100',
                              beds='1',
                              baths='2',
                              furnished='no',
                              utilities='none',
                              rent='100')
        self.assertEqual(t.house.property.square_feet, "100")
        self.assertEqual(t.house.property.num_bedrooms, "1")
        self.assertEqual(t.house.property.num_baths, "2")
        self.assertEqual(t.house.num_stories, '1')
        self.assertEqual(t.house.garage, 'detached')
        self.assertEqual(t.house.fenced, 'yes')

        self.assertEqual(t.rental.furnished, 'no')
        self.assertEqual(t.rental.utilities, 'none')
        self.assertEqual(t.rental.rent, '100')

    def test_ApartmentPurchase__init__(self):
        p = agent.ApartmentPurchase(balcony='yes', laundry='none',
                                    price='1000',
                                    taxes='1')
        self.assertEqual(p.apartment.balcony, "yes")
        self.assertEqual(p.apartment.laundry, "none")
        self.assertEqual(p.purchase.price, "1000")
        self.assertEqual(p.purchase.taxes, '1')

    def test_HousePurchase__init__(self):
        t = agent.HousePurchase(num_stories='1',
                                garage='detached', fenced='yes',
                                square_feet='100',
                                beds='1',
                                baths='2', price='1000', taxes='1')
        self.assertEqual(t.house.property.square_feet, "100")
        self.assertEqual(t.house.property.num_bedrooms, "1")
        self.assertEqual(t.house.property.num_baths, "2")
        self.assertEqual(t.house.num_stories, '1')
        self.assertEqual(t.house.garage, 'detached')
        self.assertEqual(t.house.fenced, 'yes')
        self.assertEqual(t.purchase.price, "1000")
        self.assertEqual(t.purchase.taxes, '1')

    def test_Agent__init__(self):
        a = agent.Agent()
        self.assertEqual(a.property_list, [])
