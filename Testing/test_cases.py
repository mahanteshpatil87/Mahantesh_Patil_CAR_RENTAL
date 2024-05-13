import unittest

from Exception.myexceptions import CarNotFoundException, LeaseNotFoundException
from dao.ICarLeaseRepositoryImpl  import CarManagementImplementation,LeaseManagementImplementation
from Entity.entity import Car


class MyTestCases(unittest.TestCase):
    def setUp(self):
        self.car = CarManagementImplementation()
        self.lease_manage = LeaseManagementImplementation()

    def test_car_create(self):
        result = self.car.addCar(Car(0, make="Tata", model="Sumo", Year="2014", dailyRate="35", status="1", passenger_capacity="12", engine_capacity="2400"))

        self.assertEqual(result, "Successfully Added the Car")

    def test_lease_creation(self):
        result = self.lease_manage.createLease(customerID=1,  startDate = "2024-05-01", endDate="2024-06-01", type="1",carID=3)
        self.assertEqual(result,"Lease created successfully")

    def test_lease_retrive(self):
        result = self.lease_manage.listLeaseHistory()
        self.assertNotEqual(len(result),0)

    def test_find_car(self):
        with self.assertRaises(CarNotFoundException):
            self.car.findCarsById(110)
