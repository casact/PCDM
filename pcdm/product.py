from sqlalchemy import Column, Date, Float, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from pcdm.base import Base


class LineOfBusiness(Base):
    __tablename__ = 'line_of_business'

    line_of_business_id = Column(
        Integer,
        primary_key=True
    )

    line_of_business_name = Column(String)

    line_of_business_description = Column(String)

    line_of_business_code = Column(Integer)

    line_of_business_group_id = Column(
        Integer,
        ForeignKey('line_of_business_group.line_of_business_group_id')
    )

    insurance_class_id = Column(
        Integer,
        ForeignKey('insurance_class.insurance_class_id')
    )

    product = relationship(
        'Product',
        primaryjoin='LineOfBusiness.line_of_business_id == Product.line_of_business_id',
        back_populates='line_of_business'
    )

    line_of_business_group = relationship(
        'LineOfBusinessGroup',
        primaryjoin='LineOfBusiness.line_of_business_group_id == LineOfBusinessGroup.line_of_business_group_id',
        back_populates='line_of_business'
    )

    insurance_class = relationship(
        'InsuranceClass',
        primaryjoin='LineOfBusiness.insurance_class_id == InsuranceClass.insurance_class_id',
        back_populates='line_of_business'
    )

    def __repr__(self):
        return "<LineOfBusiness(" \
               "line_of_business_name='%s', " \
               "line_of_business_description='%s', "\
               "line_of_business_code='%s', " \
               "line_of_business_group_id='%s', " \
               "insurance_class_id='%s'" \
               ")>" % (
                   self.line_of_business_name,
                   self.line_of_business_description,
                   self.line_of_business_code,
                   self.line_of_business_group_id,
                   self.insurance_class_id
               )


class LineOfBusinessGroup(Base):
    __tablename__ = 'line_of_business_group'

    line_of_business_group_id = Column(
        Integer,
        primary_key=True
    )

    line_of_business_group_name = Column(String)

    line_of_business_group_description = Column(String)

    line_of_business = relationship(
        'LineOfBusiness',
        primaryjoin='LineOfBusinessGroup.line_of_business_group_id == LineOfBusiness.line_of_business_group_id',
        back_populates='line_of_business_group'
    )

    def __repr__(self):
        return "<LineOfBusinessGroup(" \
               "line_of_business_group_name='%s', " \
               "line_of_business_group_description='%s'"\
               ")>" % (
                   self.line_of_business_group_name,
                   self.line_of_business_group_description
               )


class InsuranceClass(Base):
    __tablename__ = 'insurance_class'

    insurance_class_id = Column(
        Integer,
        primary_key=True
    )

    insurance_class_name = Column(String)

    insurance_class_description = Column(String)

    line_of_business = relationship(
        'LineOfBusiness',
        primaryjoin='InsuranceClass.insurance_class_id == LineOfBusiness.insurance_class_id',
        back_populates='insurance_class'
    )

    def __repr__(self):
        return "<InsuranceClass(" \
               "insurance_class_name='%s', " \
               "insurance_class_description='%s'" \
               ")>" % (
                   self.insurance_class_name,
                   self.insurance_class_description
               )


class CoverageType(Base):
    __tablename__ = 'coverage_type'

    coverage_type_id = Column(
        Integer,
        primary_key=True
    )

    coverage_type_name = Column(String)

    coverage_type_description = Column(String)

    coverage = relationship(
        'Coverage',
        primaryjoin='CoverageType.coverage_type_id == Coverage.coverage_type_id',
        back_populates='coverage_type'
    )

    def __repr__(self):
        return "<CoverageType(" \
               "coverage_type_name='%s', " \
               "coverage_type_description='%s'" \
               ")>" % (
                   self.coverage_type_name,
                   self.coverage_type_description
               )


class CoverageGroup(Base):
    __tablename__ = 'coverage_group'

    coverage_group_id = Column(
        Integer,
        primary_key=True
    )

    coverage_group_name = Column(String)

    coverage_group_description = Column(String)

    coverage = relationship(
        'Coverage',
        primaryjoin='CoverageGroup.coverage_group_id == Coverage.coverage_group_id',
        back_populates='coverage_group'
    )

    def __repr__(self):
        return "<CoverageGroup(" \
               "coverage_group_name='%s', " \
               "coverage_group_description='%s'" \
               ")>" % (
                   self.coverage_group_name,
                   self.coverage_group_description
               )


class ProductCoverage(Base):
    __tablename__ = 'product_coverage'

    product_coverage_id = Column(
        Integer,
        primary_key=True
    )

    product_id = Column(
        Integer,
        ForeignKey('product.product_id')
    )

    coverage_id = Column(
        Integer,
        ForeignKey('coverage.coverage_id')
    )

    product = relationship(
        'Product',
        primaryjoin='ProductCoverage.product_id == Product.product_id',
        back_populates='product_coverage'
    )

    coverage = relationship(
        'Coverage',
        primaryjoin='ProductCoverage.coverage_id == Coverage.coverage_id',
        back_populates='product_coverage'
    )

    def __repr__(self):
        return "<ProductCoverage(" \
               "product_id='%s', " \
               "coverage_id='%s'" \
               ")>" % (
                   self.product_id,
                   self.coverage_id
               )


class CoverageLevel(Base):
    __tablename__ = 'coverage_level'

    coverage_level_id = Column(
        Integer,
        primary_key=True
    )

    coverage_id = Column(
        Integer,
        ForeignKey('coverage.coverage_id')
    )

    coverage_limit_type_id = Column(
        Integer,
        ForeignKey('coverage_limit_type.coverage_limit_type_id')
    )

    maximum_per_person_amount = Column(Float)

    aggregate_limit_amount = Column(Float)

    maximum_per_claim_amount = Column(Float)

    deductible_rate = Column(Float)

    coverage_label_name = Column(String)

    coverage = relationship(
        'Coverage',
        primaryjoin='CoverageLevel.coverage_id == Coverage.coverage_id',
        back_populates='coverage_level'
    )

    coverage_limit_type = relationship(
        'CoverageLimitType',
        primaryjoin='CoverageLevel.coverage_limit_type_id == CoverageLimitType.coverage_limit_type_id',
        back_populates='coverage_level'
    )

    def __repr__(self):
        return "<CoverageLevel(" \
               "coverage_id='%s', " \
               "coverage_limit_type_id='%s', " \
               "maximum_per_person_amount='%s', " \
               "aggregate_limit_amount='%s', " \
               "maximum_per_claim_amount='%s', "\
               "deductible_rate='%s', " \
               "coverage_label_name='%s'" \
               ")>" % (
                   self.coverage_id,
                   self.coverage_limit_type_id,
                   self.maximum_per_person_amount,
                   self.aggregate_limit_amount,
                   self.maximum_per_claim_amount,
                   self.deductible_rate,
                   self.coverage_label_name
                )


class CoverageLimitType(Base):
    __tablename__ = 'coverage_limit_type'

    coverage_limit_type_id = Column(
        Integer,
        primary_key=True
    )

    coverage_limit_name = Column(String)

    coverage_limit_description = Column(String)

    coverage_level = relationship(
        'CoverageLevel',
        primaryjoin='CoverageLimitType.coverage_limit_type_id == CoverageLevel.coverage_limit_type_id',
        back_populates='coverage_limit_type'
    )

    def __repr__(self):
        return "<CoverageLimitType(" \
               "coverage_limit_name='%s', " \
               "coverage_limit_description='%s'" \
               ")>" % (
                   self.coverage_limit_name,
                   self.coverage_limit_description
               )


class RatingTerritoryGeographicLocation(Base):
    __tablename__ = 'rating_territory_geographic_location'

    rating_territory_geographic_location_id = Column(
        Integer,
        primary_key=True
    )

    geographic_location_id = Column(
        Integer,
        ForeignKey('geographic_location.geographic_location_id')
    )

    rating_territory_id = Column(
        Integer,
        ForeignKey('rating_territory.rating_territory_id')
    )

    geographic_location = relationship(
        'GeographicLocation',
        primaryjoin='RatingTerritoryGeographicLocation.geographic_location_id == '
                    'Geographic_location.geographic_location_id',
        back_populates='rating_territory_geographic_location'
    )

    rating_territory = relationship(
        'RatingTerritory',
        primaryjoin='RatingTerritoryGeographicLocation.rating_territory_id == RatingTerritory.rating_territory_id',
        back_populates='rating_territory_geographic_location'
    )

    def __repr__(self):
        return "<RatingTerritoryGeographicLocation(" \
               "geographic_location_id='%s', " \
               "rating_territory_id='%s'" \
               ")>" % (
                   self.geographic_location_id,
                   self.rating_territory_id
               )


class RatingTerritory(Base):
    __tablename__ = 'rating_territory'

    rating_territory_id = Column(
        Integer,
        primary_key=True
    )

    rating_territory_assigning_organization_id = Column(Integer)

    rating_territory_code = Column(Integer)

    rating_territory_code_set_identifier = Column(Integer)

    rating_territory_geographic_location = relationship(
        'RatingTerritoryGeographicLocation',
        primaryjoin='RatingTerritory.rating_territory_id == RatingTerritoryGeographicLocation.rating_territory_id',
        back_populates='rating_territory'
    )

    def __repr__(self):
        return "<RatingTerritory(" \
               "rating_territory_assigning_organization_id='%s', " \
               "rating_territory_code='%s', " \
               "rating_territory_code_set_identifier='%s'" \
               ")>" % (
                   self.rating_territory_assigning_organization_id,
                   self.rating_territory_code,
                   self.rating_territory_code_set_identifier
               )


class State(Base):
    __tablename__ = 'state'

    state_code = Column(
        String,
        primary_key=True
    )

    state_name = Column(String)

    geographic_location = relationship(
        'GeographicLocation',
        primaryjoin='State.state_code == GeographicLocation.state_code',
        back_populates='state'
    )

    def __repr__(self):
        return "<State(" \
               "state_name='%s'" \
               ")>" % (
                   self.state_name
               )


class CompanyJurisdiction(Base):
    __tablename__ = 'company_jurisdiction'

    company_jurisdiction_id = Column(
        Integer,
        primary_key=True
    )

    company_id = Column(
        Integer,
        ForeignKey('company.company_id')
    )

    geographic_location_id = Column(
        Integer,
        ForeignKey('geographic_location.geographic_location_id')
    )

    company = relationship(
        'Company',
        primaryjoin='CompanyJurisdiction.company_id == Company.company_id',
        back_populates='company_jurisdiction'
    )

    geographic_location = relationship(
        'GeographicLocation',
        primaryjoin='CompanyJurisdiction.geographic_location_id == GeographicLocation.geographic_location_id',
        back_populates='company_jurisdiction'
    )

    product_license = relationship(
        'ProductLicense',
        primaryjoin='CompanyJurisdiction.company_jurisdiction_id == ProductLicense.company_jurisdiction_id',
        back_populates='company_jurisdiction'
    )

    def __repr__(self):
        return "<CompanyJurisdiction(" \
               "company_id='%s', " \
               "geographic_location_id='%s'" \
               ")>" % (
                   self.company_id,
                   self.geographic_location_id
               )


class Company(Base):
    __tablename__ = 'company'

    company_id = Column(
        Integer,
        primary_key=True
    )

    company_code = Column(Integer)

    company_name = Column(String)

    company_description = Column(String)

    company_jurisdiction = relationship(
        'CompanyJurisdiction',
        primaryjoin='Company.company_id == CompanyJurisdiction.company_id',
        back_populates='company'
    )

    def __repr__(self):
        return "<Company(" \
               "company_code='%s', " \
               "company_name='%s', " \
               "company_description='%s'" \
               ")>" % (
                   self.company_code,
                   self.company_name,
                   self.company_description
               )


class ProductLicense(Base):
    __tablename__ = 'product_license'

    product_license_id = Column(
        Integer,
        primary_key=True
    )

    company_jurisdiction_id = Column(
        Integer,
        ForeignKey('company_jurisdiction.company_jurisdiction_id')
    )

    effective_date = Column(Date)

    expiration_date = Column(Date)

    company_jurisdiction = relationship(
        'CompanyJurisdiction',
        primaryjoin='ProductLicense.company_jurisdiction_id == CompanyJurisdiction.company_jurisdiction_id',
        back_populates='product_license'
    )

    def __repr__(self):
        return "<ProductLicense(" \
               "company_jurisdiction_id='%s', " \
               "effective_date='%s', " \
               "expiration_date='%s'" \
               ")>" % (
                   self.company_jurisdiction_id,
                   self.effective_date,
                   self.expiration_date
               )
