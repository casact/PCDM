from sqlalchemy import Column, Date, Float, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Product(Base):
    __tablename__ = 'product'

    product_id = Column(
        Integer,
        primary_key=True
    )
    line_of_business_id = Column(
        Integer
    )

    licensed_product_name = Column(String)

    product_description = Column(String)

    agreement = relationship(
        'Agreement',
        primaryjoin='Product.product_id == Agreement.product_id',
        back_populates='product'
    )

    def __repr__(self):
        return "<Product(" \
               "line_of_business_id='%s', " \
               "licensed_product_name='%s', " \
               "product_description='%s'" \
               ")>" % (
                   self.line_of_business_id,
                   self.licensed_product_name,
                   self.product_description
                )


class PolicyRelationship(Base):
    __tablename__ = 'policy_relationship'

    policy_relationship_id = Column(
        Integer,
        primary_key=True
    )

    relationship_code = Column(Integer)

    effective_date = Column(Date)

    policy_id = Column(
        Integer,
        ForeignKey('policy.policy_id')
    )

    related_policy_id = Column(
        Integer,
        ForeignKey('policy.policy_id')
    )

    expiration_date = Column(Date)

    policy = relationship(
        'Policy',
        primaryjoin='PolicyRelationship.policy_id == Policy.policy_id',
        back_populates='policy_relationship'
    )

    related_policy = relationship(
        'Policy',
        primaryjoin='PolicyRelationship.related_policy_id == Policy.policy_id',
        back_populates='policy_relationship'
    )

    def __repr__(self):
        return "<PolicyRelationship(" \
               "relationship_code='%s', " \
               "effective_date='%s', " \
               "policy_id='%s', " \
               "related_policy_id='%s', " \
               "expiration_date='%s'" \
               ")>" % (
                   self.relationship_code,
                   self.effective_date,
                   self.policy_id,
                   self.related_policy_id,
                   self.expiration_date
                )


class Event(Base):
    __tablename__ = 'event'

    event_id = Column(
        Integer,
        primary_key=True
    )

    policy_event = relationship(
        'PolicyEvent',
        primaryjoin='Event.event_id == PolicyEvent.event_id',
        back_populates='event'
    )


class PolicyEvent(Base):
    __tablename__ = 'policy_event'

    policy_event_id = Column(
        Integer,
        primary_key=True
    )

    event_id = Column(
        Integer,
        ForeignKey('event.event_id')
    )

    event_date = Column(Date)

    effective_date = Column(Date)

    event_type_code = Column(Integer)

    event_sub_type_code = Column(Integer)

    policy_id = Column(
        Integer,
        ForeignKey('policy.policy_id')
    )

    event = relationship(
        'Event',
        primaryjoin='PolicyEvent.event_id == Event.event_id',
        back_populates='policy_event'
    )

    policy = relationship(
        'Policy',
        primaryjoin='PolicyEvent.policy_id == Policy.policy_id',
        back_populates='policy_event'
    )

    def __repr__(self):
        return "<PolicyEvent(" \
               "event_id='%s', " \
               "event_date='%s', " \
               "event_type_code='%s', " \
               "event_sub_type_code='%s', " \
               "policy_id='%s'" \
               ")>" % (
                   self.event_id,
                   self.event_date,
                   self.event_type_code,
                   self.event_sub_type_code,
                   self.policy_id
                )


class PolicyCoveragePart(Base):
    __tablename__ = 'policy_coverage_part'

    policy_coverage_part_id = Column(
        Integer,
        primary_key=True
    )

    coverage_part_code = Column(
        Integer,
        ForeignKey('coverage_part.coverage_part_code')
    )

    policy_id = Column(
        Integer,
        ForeignKey('policy.policy_id')
    )

    coverage_part = relationship(
        'CoveragePart',
        primaryjoin='PolicyCoveragePart.coverage_part_code == CoveragePart.coverage_part_code',
        back_populates='policy_coverage_part'
    )

    policy = relationship(
        'Policy',
        primaryjoin='PolicyCoveragePart.policy_id == Policy.policy_id',
        back_populates='policy_coverage_part'
    )

    def __repr__(self):
        return "<PolicyCoveragePart(" \
               "coverage_part_code='%s', " \
               "policy_id='%s'" \
               ")>" % (
                   self.coverage_part_code,
                   self.policy_id
                )


class CoveragePart(Base):
    __tablename__ = 'coverage_part'

    coverage_part_code = Column(
        Integer,
        primary_key=True
    )

    coverage_part_name = Column(String)

    policy_coverage_part = relationship(
        'PolicyCoveragePart',
        primaryjoin='CoveragePart.coverage_part_code == PolicyCoveragePart.coverage_part_code',
        back_populates='coverage_part'
    )

    coverage = relationship(
        'Coverage',
        primaryjoin='CoveragePart.coverage_part_code == Coverage.coverage_part_code',
        back_populates='coverage'
    )

    policy_coverage_detail = relationship(
        'PolicyCoverageDetail',
        primaryjoin='PolicyCoveragePart.coverage_part_code == PolicyCoverageDetail.coverage_part_code',
        back_populates='coverage'
    )

    def __repr__(self):
        return "<CoveragePart(" \
               "coverage_part_name='%s'" \
               ")>" % (
                   self.coverage_part_name
                )


class Coverage(Base):
    __tablename__ = 'coverage'

    coverage_id = Column(
        Integer,
        primary_key=True
    )

    coverage_part_code = Column(
        Integer,
        ForeignKey('coverage_part.coverage_part_code')
    )

    coverage_type_id = Column(Integer)

    coverage_name = Column(String)

    coverage_description = Column(String)

    coverage_group_id = Column(Integer)

    coverage_part = relationship(
        'CoveragePart',
        primaryjoin='Coverage.coverage_part_code == CoveragePart.coverage_part_code',
        back_populates='coverage'
    )

    policy_coverage_detail_part_code = relationship(
        'PolicyCoverageDetail',
        primaryjoin='Coverage.coverage_part_code == PolicyCoverageDetail.coverage_part_code',
        back_populates='coverage_coverage_part'
    )

    policy_coverage_detail = relationship(
        'PolicyCoverageDetail',
        primaryjoin='Coverage.coverage_id == PolicyCoverageDetail.coverage_id',
        back_populates='coverage'
    )

    def __repr__(self):
        return "<Coverage(" \
               "coverage_part_code='%s', " \
               "coverage_type_id='%s', " \
               "coverage_name='%s', " \
               "coverage_description='%s', " \
               "coverage_group_id='%s'" \
               ")>" % (
                   self.coverage_part_code,
                   self.coverage_type_id,
                   self.coverage_name,
                   self.coverage_description,
                   self.coverage_group_id
                )


class PolicyCoverageDetail(Base):
    __tablename__ = 'policy_coverage_detail'

    policy_coverage_detail_id = Column(
        Integer,
        primary_key=True
    )

    effective_date = Column(Date)  # removed from primary key - does not add to uniqueness

    policy_id = Column(
        Integer,
        ForeignKey('policy.policy_id')
    )

    coverage_part_code = Column(
        Integer,
        ForeignKey('policy_coverage_part.coverage_part_code')
    )

    coverage_id = Column(
        Integer,
        ForeignKey('coverage.coverage_id')
    )

    insurable_object_id = Column(
        Integer,
        ForeignKey('insurable_object.insurable_object_id')
    )

    expiration_date = Column(Date)

    coverage_inclusion_exclusion_code = Column(Integer)

    coverage_description = Column(String)

    policy = relationship(
        'Policy',
        primaryjoin='PolicyCoverageDetail.policy_id == Policy.policy_id',
        back_populates='policy_coverage_detail'
    )

    policy_coverage_part = relationship(
        'PolicyCoveragePart',
        primaryjoin='PolicyCoverageDetail.coverage_part_code == PolicyCoveragePart.coverage_part_code',
        back_populates='policy_coverage_detail'
    )

    coverage_coverage_part = relationship(
        'Coverage',
        primaryjoin='PolicyCoverageDetail.coverage_part_code == Coverage.coverage_part_code',
        back_populates='policy_coverage_detail_part_code'
    )

    coverage = relationship(
        'Coverage',
        primaryjoin='PolicyCoverageDetail.coverage_id == Coverage.coverage_id',
        back_populates='policy_coverage_detail'
    )

    insurable_object = relationship(
        'InsurableObject',
        primaryjoin='PolicyCoverageDetail.insurable_object_id == InsurableObject.insurable_object_id',
        back_populates='policy_coverage_detail'
    )

    policy_limit = relationship(
        'PolicyLimit',
        primaryjoin='PolicyCoverageDetail.policy_coverage_detail_id == PolicyLimit.policy_coverage_detail_id',
        back_populates='policy_coverage_detail'
    )

    policy_deductible = relationship(
        'PolicyDeductible',
        primaryjoin='PolicyCoverageDetail.policy_coverage_detail_id == PolicyDeductible.policy_coverage_detail_id',
        back_populates='policy_coverage_detail'
    )

    policy_amount = relationship(
        'PolicyAmount',
        primaryjoin='PolicyCoverageDetail.policy_coverage_detail_id == PolicyAmount.policy_coverage_detail_id',
        back_populates='policy_coverage_detail'
    )

    def __repr__(self):
        return "<PolicyCoverageDetail(" \
               "effective_date='%s', " \
               "policy_id='%s', " \
               "coverage_part_code='%s', " \
               "coverage_id='%s', " \
               "insurable_object_id='%s', " \
               "expiration_date='%s', " \
               "coverage_inclusion_exclusion_code='%s', " \
               "coverage_description='%s'" \
               ")>" % (
                   self.effective_date,
                   self.policy_id,
                   self.coverage_part_code,
                   self.coverage_id,
                   self.insurable_object_id,
                   self.expiration_date,
                   self.coverage_inclusion_exclusion_code,
                   self.coverage_description
                )


class PolicyForm(Base):
    __tablename__ = 'policy_form'

    policy_form_id = Column(
        Integer,
        primary_key=True
    )

    policy_id = Column(
        Integer,
        ForeignKey('policy.policy_id')
    )

    policy_form_number = Column(String)

    form_value = Column(String)

    policy = relationship(
        'Policy',
        primaryjoin='PolicyForm.policy_id == Policy.policy_id',
        back_populates='policy_form'
    )

    def __repr__(self):
        return "<PolicyForm(" \
               "policy_id='%s', " \
               "policy_form_number='%s', " \
               "form_value='%s'" \
               ")>" % (
                   self.policy_id,
                   self.policy_form_number,
                   self.form_value
                )


class PolicyLimit(Base):
    __tablename__ = 'policy_limit'

    policy_limit_id = Column(
        Integer,
        primary_key=True
    )

    policy_coverage_detail_id = Column(
        Integer,
        ForeignKey('policy_coverage_detail.policy_coverage_detail_id')
    )

    # effective date removed, can be looked up in coverage detail

    limit_type_code = Column(Integer)

    limit_basis_code = Column(Integer)

    limit_value = Column(Float)

    policy_coverage_detail = relationship(
        'PolicyCoverageDetail',
        primaryjoin='PolicyLimit.policy_coverage_detail_id == PolicyCoverageDetail.policy_coverage_detail_id',
        back_populates='policy_limit'
    )

    def __repr__(self):
        return "<PolicyLimit(" \
               "policy_coverage_detail_id='%s', " \
               "limit_type_code='%s', " \
               "limit_basis_code='%s', " \
               "limit_value='%s', " \
               ")>" % (
                   self.policy_coverage_detail_id,
                   self.limit_type_code,
                   self.limit_basis_code,
                   self.limit_value
                )


class PolicyDeductible(Base):
    __tablename__ = 'policy_deductible'

    policy_deductible_identifier = Column(
        Integer,
        primary_key=True
    )

    policy_coverage_detail_id = Column(
        Integer,
        ForeignKey('policy_coverage_detail.policy_coverage_detail_id')
    )

    # effective date removed - can be looked up from policy coverage detail

    deductible_type_code = Column(Integer)

    deductible_basis_code = Column(Integer)

    deductible_value = Column(Float)

    policy_coverage_detail = relationship(
        'PolicyCoverageDetail',
        primaryjoin='PolicyDeductible.policy_coverage_detail_id == PolicyCoverageDetail.policy_coverage_detail_id',
        back_populates='policy_deductible'
    )

    def __repr__(self):
        return "<PolicyDeductible(" \
               "policy_coverage_detail_id='%s', " \
               "deductible_type_code='%s', " \
               "deductible_basis_code='%s', " \
               "deductible_value='%s', " \
               ")>" % (
                   self.policy_coverage_detail_id,
                   self.deductible_type_code,
                   self.deductible_basis_code,
                   self.deductible_value
                )


class PolicyAmount(Base):
    __tablename__ = 'policy_amount'

    policy_amount_id = Column(
        Integer,
        primary_key=True
    )

    policy_id = Column(
        Integer,
        ForeignKey('policy.policy_id')
    )

    policy_coverage_detail_id = Column(
        Integer,
        ForeignKey('policy_coverage_detail.policy_coverage_detail_id')
    )

    insurable_object_id = Column(
        Integer,
        ForeignKey('insurable_object.insurable_object_id')
    )

    geographic_location_id = Column(
        Integer,
        ForeignKey('geographic_location.geographic_location_id')
    )

    # effective date removed, can be looked up in policy coverage detail

    earning_begin_date = Column(Date)

    earning_end_date = Column(Date)

    insurance_type_code = Column(Integer)

    amount_type_code = Column(Integer)

    policy_amount = Column(Float)

    policy = relationship(
        'Policy',
        primaryjoin='PolicyAmount.policy_id == Policy.policy_id',
        back_populates='policy_amount'
    )

    policy_coverage_detail = relationship(
        'PolicyCoverageDetail',
        primaryjoin='PolicyAmount.policy_coverage_detail_id == PolicyCoverageDetail.policy_coverage_detail_id',
        back_populates='policy_amount'
    )

    insurable_object = relationship(
        'InsurableObject',
        primaryjoin='PolicyAmount.insurable_object_id == InsurableObject.insurable_object_id',
        back_populates='policy_amount'
    )

    geographic_location = relationship(
        'GeographicLocation',
        primaryjoin='PolicyAmount.geographic_location_id == GeographicLocation.geographic_location_id',
        back_populates='policy_amount'
    )

    def __repr__(self):
        return "<PolicyAmount(" \
               "policy_id='%s', " \
               "policy_coverage_detail_id='%s', " \
               "insurable_object_id='%s', " \
               "geographic_location_id='%s', " \
               "earning_begin_date='%s', " \
               "earning_end_date='%s', " \
               "insurance_type_code='%s', " \
               "amount_type_code='%s', " \
               "policy_amount='%s'" \
               ")>" % (
                   self.policy_id,
                   self.policy_coverage_detail_id,
                   self.insurable_object_id,
                   self.geographic_location_id,
                   self.earning_begin_date,
                   self.earning_end_date,
                   self.insurance_type_code,
                   self.amount_type_code,
                   self.policy_amount
                )


class LocationAddress(Base):
    __tablename__ = 'location_address'

    location_address_id = Column(
        Integer,
        primary_key=True
    )

    line_1_address = Column(String)

    line_2_address = Column(String)

    municipality_name = Column(String)

    state_code = Column(String)

    postal_code = Column(String)

    country_code = Column(String)

    begin_date = Column(Date)

    end_date = Column(Date)

    geographic_location = relationship(
        'GeographicLocation',
        primaryjoin='LocationAddress.location_address_id == GeographicLocation.location_address_id',
        back_populates='location_address'
    )

    physical_location = relationship(
        'PhysicalLocation',
        primaryjoin='LocationAddress.location_address_id == PhysicalLocation.location_address_id',
        back_populates='location_address'
    )

    def __repr__(self):
        return "<LocationAddress(" \
               "line_1_address='%s', " \
               "line_2_address='%s', " \
               "municipality_name='%s', " \
               "state_code='%s', " \
               "postal_code='%s', " \
               "country_code='%s', " \
               "begin_date='%s', " \
               "end_date='%s'" \
               ")>" % (
                   self.line_1_address,
                   self.line_2_address,
                   self.municipality_name,
                   self.state_code,
                   self.postal_code,
                   self.country_code,
                   self.begin_date,
                   self.end_date
                )


class PhysicalLocation(Base):
    __tablename__ = 'physical_location'

    physical_location_id = Column(
        Integer,
        primary_key=True
    )

    physical_location_name = Column(String)

    latitude_value = Column(Float)

    longitude_value = Column(Float)

    altitude_value = Column(Float)

    altitude_mean_sea_level_value = Column(Float)

    horizontal_accuracy_value = Column(Float)

    vertical_accuracy_value = Column(Float)

    travel_direction_description = Column(String)

    location_address_id = Column(
        Integer,
        ForeignKey('location_address.location_address_id')
    )

    location_address = relationship(
        'LocationAddress',
        primaryjoin='PhysicalLocation.location_address_id == LocationAddress.location_address_id',
        back_populates='physical_location'
    )

    geographic_location = relationship(
        'GeographicLocation',
        primaryjoin='PhysicalLocation.physical_location_id == GeographicLocation.physical_location_id',
        back_populates='physical_location'
    )

    def __repr__(self):
        return "<PhysicalLocation(" \
               "physical_location_name='%s', " \
               "latitude_value='%s', " \
               "longitude_value='%s', " \
               "altitude_value='%s', " \
               "altitude_mean_sea_level_value='%s', " \
               "horizontal_accuracy_value='%s', " \
               "vertical_accuracy_value='%s', " \
               "travel_direction_description='%s', " \
               "location_address_id='%s'" \
               ")>" % (
                   self.physical_location_name,
                   self.latitude_value,
                   self.longitude_value,
                   self.altitude_value,
                   self.altitude_mean_sea_level_value,
                   self.horizontal_accuracy_value,
                   self.vertical_accuracy_value,
                   self.travel_direction_description,
                   self.location_address_id
                )
