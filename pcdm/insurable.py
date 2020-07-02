from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Vehicle(Base):
    __tablename__ = 'vehicle'

    vehicle_id = Column(
        Integer,
        primary_key=True
    )

    insurable_object_id = Column(
        Integer,
        ForeignKey('insurable_object.insurable_object_id')
    )

    vehicle_model_year = Column(Integer)

    vehicle_model_name = Column(String)

    vehicle_driving_wheel_quantity = Column(Integer)

    vehicle_make_name = Column(String)

    vehicle_identification_number = Column(String)

    insurable_object = relationship(
        'InsurableObject',
        primaryjoin='Vehicle.insurable_object_id == InsurableObject.insurable_object_id',
        back_populates='vehicle'
    )

    automobile = relationship(
        'Automobile',
        primaryjoin='Vehicle.vehicle_id == Automobile.vehicle_id',
        back_populates='vehicle'
    )

    van = relationship(
        'Van',
        primaryjoin='Vehicle.vehicle_id == Van.vehicle_id',
        back_populates='vehicle'
    )

    motorcycle = relationship(
        'Motorcycle',
        primaryjoin='Vehicle.vehicle_id == Motorcycle.vehicle_id',
        back_populates='vehicle'
    )

    recreational_vehicle = relationship(
        'RecreationalVehicle',
        primaryjoin='Vehicle.vehicle_id == RecreationalVehicle.vehicle_id',
        back_populates='vehicle'
    )

    construction_vehicle = relationship(
        'ConstructionVehicle',
        primaryjoin='Vehicle.vehicle_id == ConstructionVehicle.vehicle_id',
        back_populates='vehicle'
    )

    watercraft = relationship(
        'Watercraft',
        primaryjoin='Vehicle.vehicle_id == Watercraft.vehicle_id',
        back_populates='vehicle'
    )

    boat = relationship(
        'Boat',
        primaryjoin='Vehicle.vehicle_id == Boat.vehicle_id',
        back_populates='vehicle'
    )

    truck = relationship(
        'Truck',
        primaryjoin='Vehicle.vehicle_id == Truck.vehicle_id',
        back_populates='vehicle'
    )

    bus = relationship(
        'Bus',
        primaryjoin='Vehicle.vehicle_id == Bus.vehicle_id',
        back_populates='vehicle'
    )

    trailer = relationship(
        'Trailer',
        primaryjoin='Vehicle.vehicle_id == Trailer.vehicle_id',
        back_populates='vehicle'
    )

    def __repr__(self):
        return "<Vehicle(" \
               "insurable_object_id='%s', " \
               "vehicle_model_year='%s', " \
               "vehicle_model_name='%s', " \
               "vehicle_driving_wheel_quantity='%s', "\
               "vehicle_make_name='%s', " \
               "vehicle_identification_number='%s', " \
               ")>" % (
                   self.insurable_object_id,
                   self.vehicle_model_year,
                   self.vehicle_model_name,
                   self.vehicle_driving_wheel_quantity,
                   self.vehicle_make_name,
                   self.vehicle_identification_number
                )


class Automobile(Base):
    __tablename__ = 'automobile'

    automobile_id = Column(
        Integer,
        primary_key=True
    )

    vehicle_id = Column(
        Integer,
        ForeignKey('vehicle.vehicle_id')
    )

    vehicle = relationship(
        'Vehicle',
        primaryjoin='Automobile.vehicle_id == Vehicle.vehicle_id',
        back_populates='automobile'
    )

    def __repr__(self):
        return "<Automobile(" \
               "vehicle_id='%s'" \
               ")>" % (
                   self.vehicle_id
                )


class Van(Base):
    __tablename__ = 'van'

    van_id = Column(
        Integer,
        primary_key=True
    )

    vehicle_id = Column(
        Integer,
        ForeignKey('vehicle.vehicle_id')
    )

    vehicle = relationship(
        'Vehicle',
        primaryjoin='Van.vehicle_id == Vehicle.vehicle_id',
        back_populates='van'
    )

    def __repr__(self):
        return "<Van(" \
               "vehicle_id='%s'" \
               ")>" % (
                   self.vehicle_id
               )


class Motorcycle(Base):
    __tablename__ = 'motorcycle'

    motorcycle_id = Column(
        Integer,
        primary_key=True
    )

    vehicle_id = Column(
        Integer,
        ForeignKey('vehicle.vehicle_id')
    )

    vehicle = relationship(
        'Vehicle',
        primaryjoin='Motorcycle.vehicle_id == Vehicle.vehicle_id',
        back_populates='motorcycle'
    )

    def __repr__(self):
        return "<Motorcycle(" \
               "vehicle_id='%s'" \
               ")>" % (
                   self.vehicle_id
               )


class RecreationalVehicle(Base):
    __tablename__ = 'recreational_vehicle'

    recreational_vehicle_id = Column(
        Integer,
        primary_key=True
    )

    vehicle_id = Column(
        Integer,
        ForeignKey('vehicle.vehicle_id')
    )

    vehicle = relationship(
        'Vehicle',
        primaryjoin='RecreationalVehicle.vehicle_id == Vehicle.vehicle_id',
        back_populates='recreational_vehicle'
    )

    def __repr__(self):
        return "<RecreationalVehicle(" \
               "vehicle_id='%s'" \
               ")>" % (
                   self.vehicle_id
               )


class ConstructionVehicle(Base):
    __tablename__ = 'construction_vehicle'

    construction_vehicle_id = Column(
        Integer,
        primary_key=True
    )

    vehicle_id = Column(
        Integer,
        ForeignKey('vehicle.vehicle_id')
    )

    vehicle = relationship(
        'Vehicle',
        primaryjoin='ConstructionVehicle.vehicle_id == Vehicle.vehicle_id',
        back_populates='construction_vehicle'
    )

    def __repr__(self):
        return "<ConstructionVehicle(" \
               "vehicle_id='%s'" \
               ")>" % (
                   self.vehicle_id
               )


class Watercraft(Base):
    __tablename__ = 'watercraft'

    watercraft_id = Column(
        Integer,
        primary_key=True
    )

    vehicle_id = Column(
        Integer,
        ForeignKey('vehicle.vehicle_id')
    )

    vehicle = relationship(
        'Vehicle',
        primaryjoin='Watercraft.vehicle_id == Vehicle.vehicle_id',
        back_populates='watercraft'
    )

    def __repr__(self):
        return "<Watercraft(" \
               "vehicle_id='%s'" \
               ")>" % (
                   self.vehicle_id
               )


class Boat(Base):
    __tablename__ = 'boat'

    boat_id = Column(
        Integer,
        primary_key=True
    )

    vehicle_id = Column(
        Integer,
        ForeignKey('vehicle.vehicle_id')
    )

    vehicle = relationship(
        'Vehicle',
        primaryjoin='Boat.vehicle_id == Vehicle.vehicle_id',
        back_populates='boat'
    )

    def __repr__(self):
        return "<Boat(" \
               "vehicle_id='%s'" \
               ")>" % (
                   self.vehicle_id
               )


class Truck(Base):
    __tablename__ = 'truck'

    truck_id = Column(
        Integer,
        primary_key=True
    )

    vehicle_id = Column(
        Integer,
        ForeignKey('vehicle.vehicle_id')
    )

    vehicle = relationship(
        'Vehicle',
        primaryjoin='Truck.vehicle_id == Vehicle.vehicle_id',
        back_populates='truck'
    )

    def __repr__(self):
        return "<Truck(" \
               "vehicle_id='%s'" \
               ")>" % (
                   self.vehicle_id
               )


class Bus(Base):
    __tablename__ = 'bus'

    bus_id = Column(
        Integer,
        primary_key=True
    )

    vehicle_id = Column(
        Integer,
        ForeignKey('vehicle.vehicle_id')
    )

    vehicle = relationship(
        'Vehicle',
        primaryjoin='Bus.vehicle_id == Vehicle.vehicle_id',
        back_populates='bus'
    )

    def __repr__(self):
        return "<Bus(" \
               "vehicle_id='%s'" \
               ")>" % (
                   self.vehicle_id
               )


class Trailer(Base):
    __tablename__ = 'trailer'

    trailer_id = Column(
        Integer,
        primary_key=True
    )

    vehicle_id = Column(
        Integer,
        ForeignKey('vehicle.vehicle_id')
    )

    vehicle = relationship(
        'Vehicle',
        primaryjoin='Trailer.vehicle_id == Vehicle.vehicle_id',
        back_populates='trailer'
    )

    def __repr__(self):
        return "<Trailer(" \
               "vehicle_id='%s'" \
               ")>" % (
                   self.vehicle_id
               )


class ManufacturedObject(Base):
    __tablename__ = 'manufactured_object'

    manufactured_object_id = Column(
        Integer,
        primary_key=True
    )

    insurable_object_id = Column(
        Integer,
        ForeignKey('insurable_object.insurable_object_id')
    )

    insurable_object = relationship(
        'InsurableObject',
        primaryjoin='ManufacturedObject.insurable_object_id == InsurableObject.insurable_object_id',
        back_populates='manufactured_object'
    )

    def __repr__(self):
        return "<ManufacturedObject(" \
               "insurable_object_id='%s'" \
               ")>" % (
                   self.insurable_object_id
               )


class FarmEquipment(Base):
    __tablename__ = 'farm_equipment'

    farm_equipment_id = Column(
        Integer,
        primary_key=True
    )

    insurable_object_id = Column(
        Integer,
        ForeignKey('insurable_object.insurable_object_id')
    )

    insurable_object = relationship(
        'InsurableObject',
        primaryjoin='FarmEquipment.insurable_object_id == InsurableObject.insurable_object_id',
        back_populates='farm_equipment'
    )

    tractor = relationship(
        'Tractor',
        primaryjoin='FarmEquipment.farm_equipment_id == Tractor.farm_equipment_id',
        back_populates='farm_equipment'
    )

    combine = relationship(
        'Combine',
        primaryjoin='FarmEquipment.farm_equipment_id == Combine.farm_equipment_id',
        back_populates='farm_equipment'
    )

    milking_machine = relationship(
        'MilkingMachine',
        primaryjoin='FarmEquipment.farm_equipment_id == MilkingMachine.farm_equipment_id',
        back_populates='farm_equipment'
    )

    def __repr__(self):
        return "<FarmEquipment(" \
               "insurable_object_id='%s'" \
               ")>" % (
                   self.insurable_object_id
               )


class Tractor(Base):
    __tablename__ = 'tractor'

    tractor_id = Column(
        Integer,
        primary_key=True
    )

    farm_equipment_id = Column(
        Integer,
        ForeignKey('farm_equipment.farm_equipment_id')
    )

    farm_equipment = relationship(
        'FarmEquipment',
        primaryjoin='Tractor.farm_equipment_id == FarmEquipment.farm_equipment_id',
        back_populates='tractor'
    )

    def __repr__(self):
        return "<Tractor(" \
               "farm_equipment_id='%s'" \
               ")>" % (
                   self.farm_equipment_id
               )


class Combine(Base):
    __tablename__ = 'combine'

    combine_id = Column(
        Integer,
        primary_key=True
    )

    farm_equipment_id = Column(
        Integer,
        ForeignKey('farm_equipment.farm_equipment_id')
    )

    farm_equipment = relationship(
        'FarmEquipment',
        primaryjoin='Combine.farm_equipment_id == FarmEquipment.farm_equipment_id',
        back_populates='combine'
    )

    def __repr__(self):
        return "<Combine(" \
               "farm_equipment_id='%s'" \
               ")>" % (
                   self.farm_equipment_id
               )


class MilkingMachine(Base):
    __tablename__ = 'milking_machine'

    milking_machine_id = Column(
        Integer,
        primary_key=True
    )

    farm_equipment_id = Column(
        Integer,
        ForeignKey('farm_equipment.farm_equipment_id')
    )

    farm_equipment = relationship(
        'FarmEquipment',
        primaryjoin='MilkingMachine.farm_equipment_id == FarmEquipment.farm_equipment_id',
        back_populates='milking_machine'
    )

    def __repr__(self):
        return "<MilkingMachine(" \
               "farm_equipment_id='%s'" \
               ")>" % (
                   self.farm_equipment_id
               )


class BodyObject(Base):
    __tablename__ = 'body_object'

    body_object_id = Column(
        Integer,
        primary_key=True
    )

    insurable_object_id = Column(
        Integer,
        ForeignKey('insurable_object.insurable_object_id')
    )

    insurable_object = relationship(
        'InsurableObject',
        primaryjoin='BodyObject.insurable_object_id == InsurableObject.insurable_object_id',
        back_populates='body_object'
    )

    animal = relationship(
        'Animal',
        primaryjoin='BodyObject.body_object_id == Animal.body_object_id',
        back_populates='body_object'
    )

    def __repr__(self):
        return "<BodyObject(" \
               "insurable_object_id='%s'" \
               ")>" % (
                   self.insurable_object_id
               )


class Animal(Base):
    __tablename__ = 'animal'

    animal_id = Column(
        Integer,
        primary_key=True
    )

    body_object_id = Column(
        Integer,
        ForeignKey('body_object.body_object_id')
    )

    body_object = relationship(
        'BodyObject',
        primaryjoin='Animal.body_object_id == BodyObject.body_object_id',
        back_populates='animal'
    )

    def __repr__(self):
        return "<Animal(" \
               "body_object_id='%s'" \
               ")>" % (
                   self.body_object_id
               )


class WorkersCompClass(Base):
    __tablename__ = 'workers_comp_class'

    workers_comp_class_id = Column(
        Integer,
        primary_key=True
    )

    insurable_object_id = Column(
        Integer,
        ForeignKey('insurable_object.insurable_object_id')
    )

    insurable_object = relationship(
        'InsurableObject',
        primaryjoin='WorkersCompClass.insurable_object_id == InsurableObject.insurable_object_id',
        back_populates='workers_comp_class'
    )

    def __repr__(self):
        return "<WorkersCompClass(" \
               "insurable_object_id='%s'" \
               ")>" % (
                   self.insurable_object_id
               )


class Structure(Base):
    __tablename__ = 'structure'

    structure_id = Column(
        Integer,
        primary_key=True
    )

    insurable_object_id = Column(
        Integer,
        ForeignKey('insurable_object.insurable_object_id')
    )

    insurable_object = relationship(
        'InsurableObject',
        primaryjoin='Structure.insurable_object_id == InsurableObject.insurable_object_id',
        back_populates='structure'
    )

    commercial_structure = relationship(
        'CommercialStructure',
        primaryjoin='Structure.structure_id == CommercialStructure.structure_id',
        back_populates='structure'
    )

    combination_structure = relationship(
        'CombinationStructure',
        primaryjoin='Structure.structure_id == CombinationStructure.structure_id',
        back_populates='structure'
    )

    residential_structure = relationship(
        'ResidentialStructure',
        primaryjoin='Structure.structure_id == ResidentialStructure.structure_id',
        back_populates='structure'
    )

    def __repr__(self):
        return "<Structure(" \
               "insurable_object_id='%s'" \
               ")>" % (
                   self.insurable_object_id
               )


class CommercialStructure(Base):
    __tablename__ = 'commercial_structure'

    commercial_structure_id = Column(
        Integer,
        primary_key=True
    )

    structure_id = Column(
        Integer,
        ForeignKey('structure.structure_id')
    )

    structure = relationship(
        'Structure',
        primaryjoin='CommercialStructure.structure_id == Structure.structure_id',
        back_populates='commercial_structure'
    )

    def __repr__(self):
        return "<CommercialStructure(" \
               "structure_id='%s'" \
               ")>" % (
                   self.structure_id
               )


class CombinationStructure(Base):
    __tablename__ = 'combination_structure'

    combination_structure_id = Column(
        Integer,
        primary_key=True
    )

    structure_id = Column(
        Integer,
        ForeignKey('structure.structure_id')
    )

    structure = relationship(
        'Structure',
        primaryjoin='CombinationStructure.structure_id == Structure.structure_id',
        back_populates='combination_structure'
    )

    def __repr__(self):
        return "<CombinationStructure(" \
               "structure_id='%s'" \
               ")>" % (
                   self.structure_id
               )


class ResidentialStructure(Base):
    __tablename__ = 'residential_structure'

    residential_structure_id = Column(
        Integer,
        primary_key=True
    )

    structure_id = Column(
        Integer,
        ForeignKey('structure.structure_id')
    )

    structure = relationship(
        'Structure',
        primaryjoin='ResidentialStructure.structure_id == Structure.structure_id',
        back_populates='residential_structure'
    )

    dwelling = relationship(
        'Dwelling',
        primaryjoin='ResidentialStructure.residential_structure_id == Dwelling.residential_structure_id',
        back_populates='residential_structure'
    )

    mobile_home = relationship(
        'MobileHome',
        primaryjoin='ResidentialStructure.residential_structure_id == MobileHome.residential_structure_id',
        back_populates='residential_structure'
    )

    def __repr__(self):
        return "<ResidentialStructure(" \
               "structure_id='%s'" \
               ")>" % (
                   self.structure_id
               )


class Dwelling(Base):
    __tablename__ = 'dwelling'

    dwelling_id = Column(
        Integer,
        primary_key=True
    )

    residential_structure_id = Column(
        Integer,
        ForeignKey('residential_structure.residential_structure_id')
    )

    residential_structure = relationship(
        'ResidentialStructure',
        primaryjoin='Dwelling.residential_structure_id == ResidentialStructure.residential_structure_id',
        back_populates='dwelling'
    )

    def __repr__(self):
        return "<Dwelling(" \
               "residential_structure_id='%s'" \
               ")>" % (
                   self.residential_structure_id
               )


class MobileHome(Base):
    __tablename__ = 'mobile_home'

    mobile_home_id = Column(
        Integer,
        primary_key=True
    )

    residential_structure_id = Column(
        Integer,
        ForeignKey('residential_structure.residential_structure_id')
    )

    residential_structure = relationship(
        'ResidentialStructure',
        primaryjoin='MobileHome.residential_structure_id == ResidentialStructure.residential_structure_id',
        back_populates='mobile_home'
    )

    def __repr__(self):
        return "<MobileHome(" \
               "residential_structure_id='%s'" \
               ")>" % (
                   self.residential_structure_id
               )


class TransportationClass(Base):
    __tablename__ = 'transportation_class'

    transportation_class_id = Column(
        Integer,
        primary_key=True
    )

    insurable_object_id = Column(
        Integer,
        ForeignKey('insurable_object.insurable_object_id')
    )

    insurable_object = relationship(
        'InsurableObject',
        primaryjoin='TransportationClass.insurable_object_id == InsurableObject.insurable_object_id',
        back_populates='transportation_class'
    )

    scheduled_item = relationship(
        'ScheduledItem',
        primaryjoin='TransportationClass.transportation_class_id == ScheduledItem.transportation_class_id',
        back_populates='transportation_class'
    )

    property_in_transit = relationship(
        'PropertyInTransit',
        primaryjoin='TransportationClass.transportation_class_id == PropertyInTransit.transportation_class_id',
        back_populates='transportation_class'
    )

    freight_group = relationship(
        'FreightGroup',
        primaryjoin='TransportationClass.transportation_class_id == FreightGroup.transportation_class_id',
        back_populates='transportation_class'
    )

    household_content = relationship(
        'HouseholdContent',
        primaryjoin='TransportationClass.transportation_class_id == HouseholdContent.transportation_class_id',
        back_populates='transportation_class'
    )

    def __repr__(self):
        return "<TransportationClass(" \
               "insurable_object_id='%s'" \
               ")>" % (
                   self.insurable_object_id
               )


class ScheduledItem(Base):
    __tablename__ = 'scheduled_item'

    scheduled_item_id = Column(
        Integer,
        primary_key=True
    )

    transportation_class_id = Column(
        Integer,
        ForeignKey('transportation_class.transportation_class_id')
    )

    transportation_class = relationship(
        'TransportationClass',
        primaryjoin='ScheduledItem.transportation_class_id == TransportationClass.transportation_class_id',
        back_populates='scheduled_item'
    )

    def __repr__(self):
        return "<ScheduledItem(" \
               "transportation_class_id='%s'" \
               ")>" % (
                   self.transportation_class_id
               )


class PropertyInTransit(Base):
    __tablename__ = 'property_in_transit'

    property_in_transit_id = Column(
        Integer,
        primary_key=True
    )

    transportation_class_id = Column(
        Integer,
        ForeignKey('transportation_class.transportation_class_id')
    )

    transportation_class = relationship(
        'TransportationClass',
        primaryjoin='PropertyInTransit.transportation_class_id == TransportationClass.transportation_class_id',
        back_populates='property_in_transit'
    )

    def __repr__(self):
        return "<PropertyInTransit(" \
               "transportation_class_id='%s'" \
               ")>" % (
                   self.transportation_class_id
               )


class FreightGroup(Base):
    __tablename__ = 'freight_group'

    freight_group_id = Column(
        Integer,
        primary_key=True
    )

    transportation_class_id = Column(
        Integer,
        ForeignKey('transportation_class.transportation_class_id')
    )

    transportation_class = relationship(
        'TransportationClass',
        primaryjoin='FreightGroup.transportation_class_id == TransportationClass.transportation_class_id',
        back_populates='freight_group'
    )

    def __repr__(self):
        return "<FreightGroup(" \
               "transportation_class_id='%s'" \
               ")>" % (
                   self.transportation_class_id
               )


class HouseholdContent(Base):
    __tablename__ = 'household_content'

    household_content_id = Column(
        Integer,
        primary_key=True
    )

    transportation_class_id = Column(
        Integer,
        ForeignKey('transportation_class.transportation_class_id')
    )

    household_id = Column(
        Integer,
        ForeignKey('household.household_id')
    )

    transportation_class = relationship(
        'TransportationClass',
        primaryjoin='HouseholdContent.transportation_class_id == TransportationClass.transportation_class_id',
        back_populates='household_content'
    )

    household = relationship(
        'Household',
        primaryjoin='HouseholdContent.household_id == Household.household_id',
        back_populates='household_content'
    )

    def __repr__(self):
        return "<HouseholdContent(" \
               "transportation_class_id='%s', " \
               "household_id='%s'" \
               ")>" % (
                   self.transportation_class_id,
                   self.household_id
               )
