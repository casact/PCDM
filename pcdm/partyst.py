from sqlalchemy import Column, Date, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class OrganizationUnit(Base):
    __tablename__ = 'organization_unit'

    organization_unit_id = Column(
        Integer,
        primary_key=True
    )

    organization_id = Column(
        Integer,
        ForeignKey('organization.organization_id')
    )

    organization_unit_name = Column(String)

    organization_unit_description = Column(String)

    industry_code = Column(Integer)

    accounting_code = Column(Integer)

    work_site_type_code = Column(Integer)

    organization = relationship(
        'Organization',
        primaryjoin='OrganizationUnit.organization_id == Organization.organization_id',
        back_populates='organization_unit'
    )

    field_organization_unit = relationship(
        'FieldOrganizationUnit',
        primaryjoin='OrganizationUnit.organization_unit_id == FieldOrganizationUnit.organization_unit_id',
        back_populates='organization_unit'
    )

    administrative_organization_unit = relationship(
        'AdministrativeOrganizationUnit',
        primaryjoin='OrganizationUnit.organization_unit_id == AdministrativeOrganizationUnit.organization_unit_id',
        back_populates='organization_unit'
    )

    def __repr__(self):
        return "<OrganizationUnit(" \
               "organization_id='%s', " \
               "organization_unit_name='%s', " \
               "organization_unit_description='%s', "\
               "industry_code='%s', " \
               "accounting_code='%s', " \
               "work_site_type_code='%s'" \
               ")>" % (
                   self.organization_id,
                   self.organization_unit_name,
                   self.organization_unit_description,
                   self.industry_code ,
                   self.accounting_code,
                   self.work_site_type_code
                )


class FieldOrganizationUnit(Base):
    __tablename__ = 'field_organization_unit'

    field_organization_unit_id = Column(
        Integer,
        primary_key=True
    )

    organization_unit_id = Column(
        Integer,
        ForeignKey('organization_unit.organization_unit_id')
    )

    organization_unit = relationship(
        'OrganizationUnit',
        primaryjoin='FieldOrganizationUnit.organization_unit_id == OrganizationUnit.organization_unit_id',
        back_populates='field_organization_unit'
    )

    territory = relationship(
        'Territory',
        primaryjoin='FieldOrganizationUnit.field_organization_unit_id == Territory.field_organization_unit_id',
        back_populates='field_organization_unit'
    )

    def __repr__(self):
        return "<FieldOrganizationUnit(" \
               "organization_unit_id='%s'" \
               ")>" % (
                   self.organization_unit_id
                )


class Territory(Base):
    __tablename__ = 'territory'

    territory_id = Column(
        Integer,
        primary_key=True
    )

    field_organization_unit_id = Column(
        Integer,
        ForeignKey('field_organization_unit.field_organization_unit_id')
    )

    field_organization_unit = relationship(
        'FieldOrganizationUnit',
        primaryjoin='Territory.field_organization_unit_id == FieldOrganizationUnit.field_organization_unit_id',
        back_populates='territory'
    )

    regional_office = relationship(
        'RegionalOffice',
        primaryjoin='Territory.territory_id == RegionalOffice.territory_id',
        back_populates='territory'
    )

    def __repr__(self):
        return "<Territory(" \
               "field_organization_unit_id='%s'" \
               ")>" % (
                   self.field_organization_unit_id
               )


class RegionalOffice(Base):
    __tablename__ = 'regional_office'

    regional_office_id = Column(
        Integer,
        primary_key=True
    )

    territory_id = Column(
        Integer,
        ForeignKey('territory.territory_id')
    )

    territory = relationship(
        'Territory',
        primaryjoin='RegionalOffice.territory_id == Territory.territory_id',
        back_populates='regional_office'
    )

    branch_office = relationship(
        'BranchOffice',
        primaryjoin='RegionalOffice.regional_office_id == BranchOffice.regional_office_id',
        back_populates='regional_office'
    )

    def __repr__(self):
        return "<RegionalOffice(" \
               "territory_id='%s'" \
               ")>" % (
                   self.territory_id
               )


class BranchOffice(Base):
    __tablename__ = 'branch_office'

    branch_office_id = Column(
        Integer,
        primary_key=True
    )

    regional_office_id = Column(
        Integer,
        ForeignKey('regional_office.regional_office_id')
    )

    regional_office = relationship(
        'RegionalOffice',
        primaryjoin='BranchOffice.regional_office_id == RegionalOffice.regional_office_id',
        back_populates='branch_office'
    )

    def __repr__(self):
        return "<BranchOffice(" \
               "regional_office_id='%s'" \
               ")>" % (
                   self.regional_office_id
               )


class AdministrativeOrganizationUnit(Base):
    __tablename__ = 'administrative_organization_unit'

    administrative_organization_unit_id = Column(
        Integer,
        primary_key=True
    )

    organization_unit_id = Column(
        Integer,
        ForeignKey('organization_unit.organization_unit_id')
    )

    organization_unit = relationship(
        'OrganizationUnit',
        primaryjoin='AdministrativeOrganizationUnit.organization_unit_id == OrganizationUnit.organization_unit_id',
        back_populates='administrative_organization_unit'
    )

    department = relationship(
        'Department',
        primaryjoin='AdministrativeOrganizationUnit.administrative_organization_unit_id == '
                    'Department.administrative_organization_unit_id',
        back_populates='administrative_organization_unit'
    )

    def __repr__(self):
        return "<AdministrativeOrganizationUnit(" \
               "organization_unit_id='%s'" \
               ")>" % (
                   self.organization_unit_id
               )


class Department(Base):
    __tablename__ = 'department'

    department_id = Column(
        Integer,
        primary_key=True
    )

    administrative_organization_unit_id = Column(
        Integer,
        ForeignKey('administrative_organization_unit.administrative_organization_unit_id')
    )

    administrative_organization_unit = relationship(
        'AdministrativeOrganizationUnit',
        primaryjoin='Department.administrative_organization_unit_id == '
        'AdministrativeOrganizationUnit.administrative_organization_unit_id',
        back_populates='department'
    )

    def __repr__(self):
        return "<Department(" \
               "administrative_organization_unit_id='%s'" \
               ")>" % (
                   self.administrative_organization_unit_id
               )


class ForProfitOrganization(Base):
    __tablename__ = 'for_profit_organization'

    for_profit_organization_id = Column(
        Integer,
        primary_key=True
    )

    organization_id = Column(
        Integer,
        ForeignKey('organization.organization_id')
    )

    organization = relationship(
        'Organization',
        primaryjoin='ForProfitOrganization.organization_id == Organization.organization_id',
        back_populates='for_profit_organization'
    )

    def __repr__(self):
        return "<ForProfitOrganization(" \
               "organization_id='%s'" \
               ")>" % (
                   self.organization_id
               )


class GovernmentOrganization(Base):
    __tablename__ = 'government_organization'

    government_organization_id = Column(
        Integer,
        primary_key=True
    )

    organization_id = Column(
        Integer,
        ForeignKey('organization.organization_id')
    )

    organization = relationship(
        'Organization',
        primaryjoin='GovernmentOrganization.organization_id == Organization.organization_id',
        back_populates='government_organization'
    )

    def __repr__(self):
        return "<GovernmentOrganization(" \
               "organization_id='%s'" \
               ")>" % (
                   self.organization_id
               )


class NotForProfitOrganization(Base):
    __tablename__ = 'not_for_profit_organization'

    not_for_profit_organization_id = Column(
        Integer,
        primary_key=True
    )

    organization_id = Column(
        Integer,
        ForeignKey('organization.organization_id')
    )

    organization = relationship(
        'Organization',
        primaryjoin='NotForProfitOrganization.organization_id == Organization.organization_id',
        back_populates='not_for_profit_organization'
    )

    def __repr__(self):
        return "<NotForProfitOrganization(" \
               "organization_id='%s'" \
               ")>" % (
                   self.organization_id
               )


class ProfessionalGroup(Base):
    __tablename__ = 'professional_group'

    professional_group_id = Column(
        Integer,
        primary_key=True
    )

    grouping_id = Column(
        Integer,
        ForeignKey('grouping.grouping_id')
    )

    grouping = relationship(
        'Grouping',
        primaryjoin='ProfessionalGroup.grouping_id == Grouping.grouping_id',
        back_populates='professional_group'
    )

    def __repr__(self):
        return "<ProfessionalGroup(" \
               "grouping_id='%s'" \
               ")>" % (
                   self.grouping_id
               )


class Project(Base):
    __tablename__ = 'project'

    project_id = Column(
        Integer,
        primary_key=True
    )

    grouping_id = Column(
        Integer,
        ForeignKey('grouping.grouping_id')
    )

    grouping = relationship(
        'Grouping',
        primaryjoin='Project.grouping_id == Grouping.grouping_id',
        back_populates='project'
    )

    def __repr__(self):
        return "<Project(" \
               "grouping_id='%s'" \
               ")>" % (
                   self.grouping_id
               )


class Team(Base):
    __tablename__ = 'team'

    team_id = Column(
        Integer,
        primary_key=True
    )

    grouping_id = Column(
        Integer,
        ForeignKey('grouping.grouping_id')
    )

    grouping = relationship(
        'Grouping',
        primaryjoin='Team.grouping_id == Grouping.grouping_id',
        back_populates='team'
    )

    def __repr__(self):
        return "<Team(" \
               "grouping_id='%s'" \
               ")>" % (
                   self.grouping_id
               )
