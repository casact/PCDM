from sqlalchemy import Column, Date, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class StaffPositionAssignment(Base):
    __tablename__ = 'staff_position_assignment'

    staff_position_assignment_id = Column(
        Integer,
        primary_key=True
    )

    person_id = Column(
        Integer,
        ForeignKey('person.person_id')
    )

    organization_id = Column(
        Integer,
        ForeignKey('organization.organization_id')
    )

    staff_position_id = Column(
        Integer,
        ForeignKey('staff_position.staff_position_id')
    )

    begin_date = Column(Date)

    end_date = Column(Date)

    person = relationship(
        'Person',
        primaryjoin='StaffPositionAssignment.person_id == Person.person_id',
        back_populates='staff_position_assignment'
    )

    organization = relationship(
        'Organization',
        primaryjoin='StaffPositionAssignment.organization_id == Organization.organization_id',
        back_populates='staff_position_assignment'
    )

    staff_position = relationship(
        'StaffPosition',
        primaryjoin='StaffPositionAssignment.staff_position_id == StaffPosition.staff_position_id',
        back_populates='staff_position_assignment'
    )

    def __repr__(self):
        return "<StaffPositionAssignment(" \
               "person_id='%s', " \
               "organization_id='%s', " \
               "staff_position_id='%s', "\
               "begin_date='%s', " \
               "end_date='%s'" \
               ")>" % (
                   self.person_id,
                   self.organization_id,
                   self.staff_position_id,
                   self.begin_date,
                   self.end_date
                )


class StaffPosition(Base):
    __tablename__ = 'staff_position'

    staff_position_id = Column(
        Integer,
        primary_key=True
    )

    staff_position_name = Column(String)

    staff_position_description = Column(String)

    staff_classification_code = Column(
        Integer,
        ForeignKey('staff_classification.staff_classification_code')
    )

    staff_position_assignment = relationship(
        'StaffPositionAssignment',
        primaryjoin='StaffPosition.staff_position_id == StaffPositionAssignment.staff_position_id',
        back_populates='staff_position'
    )

    staff_classification = relationship(
        'StaffClassification',
        primaryjoin='StaffPosition.staff_classification_code == StaffClassification.staff_classification_code',
        back_populates='staff_position'
    )

    def __repr__(self):
        return "<StaffPosition(" \
               "staff_position_name='%s', " \
               "staff_position_description='%s', " \
               "staff_classification_code='%s'" \
               ")>" % (
                   self.staff_position_name,
                   self.staff_position_description,
                   self.staff_classification_code
                )


class StaffClassification(Base):
    __tablename__ = 'staff_classification'

    staff_classification_code = Column(
        Integer,
        primary_key=True
    )

    staff_classification_name = Column(String)

    staff_classification_description = Column(String)

    staff_position = relationship(
        'StaffPosition',
        primaryjoin='StaffClassification.staff_classification_code == StaffPosition.staff_classification_code',
        back_populates='staff_classification'
    )

    def __repr__(self):
        return "<StaffClassification(" \
               "staff_classification_name='%s', " \
               "staff_classification_description='%s'" \
               ")>" % (
                   self.staff_classification_name,
                   self.staff_classification_description
                )


class StaffingOrganization(Base):
    __tablename__ = 'staffing_organization'

    staffing_organization_id = Column(
        Integer,
        primary_key=True
    )

    party_role_code = Column(
        String,
        ForeignKey('party_role.party_role_code')
    )

    party_role = relationship(
        'PartyRole',
        primaryjoin='StaffingOrganization.party_role_code == PartyRole.party_role_code',
        back_populates='staffing_organization'
    )

    def __repr__(self):
        return "<StaffingOrganization(" \
               "party_role_code='%s'" \
               ")>" % (
                   self.party_role_code
                )


class Staff(Base):
    __tablename__ = 'staff'

    staff_id = Column(
        Integer,
        primary_key=True
    )

    party_role_code = Column(
        String,
        ForeignKey('party_role.party_role_code')
    )

    party_role = relationship(
        'PartyRole',
        primaryjoin='Staff.party_role_code == PartyRole.party_role_code',
        back_populates='staff'
    )

    def __repr__(self):
        return "<Staff(" \
               "party_role_code='%s'" \
               ")>" % (
                   self.party_role_code
               )


class EmploymentAgreement(Base):
    __tablename__ = 'employment_agreement'

    employment_agreement_id = Column(
        Integer,
        primary_key=True
    )

    staffing_agreement_id = Column(
        Integer,
        ForeignKey('staffing_agreement.staffing_agreement_id')
    )

    staffing_agreement = relationship(
        'StaffingAgreement',
        primaryjoin='EmploymentAgreement.staffing_agreement_id == StaffingAgreement.staffing_agreement_id',
        back_populates='employment_agreement'
    )

    def __repr__(self):
        return "<EmploymentAgreement(" \
               "staffing_agreement_id='%s'" \
               ")>" % (
                   self.staffing_agreement_id
               )


class ConsultantContract(Base):
    __tablename__ = 'consultant_contract'

    consultant_contract_id = Column(
        Integer,
        primary_key=True
    )

    staffing_agreement_id = Column(
        Integer,
        ForeignKey('staffing_agreement.staffing_agreement_id')
    )

    staffing_agreement = relationship(
        'StaffingAgreement',
        primaryjoin='ConsultantContract.staffing_agreement_id == StaffingAgreement.staffing_agreement_id',
        back_populates='consultant_contract'
    )

    def __repr__(self):
        return "<ConsultantContract(" \
               "staffing_agreement_id='%s'" \
               ")>" % (
                   self.staffing_agreement_id
               )


class ThirdPartyStaffingAgreement(Base):
    __tablename__ = 'third_party_staffing_agreement'

    third_party_staffing_agreement_id = Column(
        Integer,
        primary_key=True
    )

    staffing_agreement_id = Column(
        Integer,
        ForeignKey('staffing_agreement.staffing_agreement_id')
    )

    staffing_agreement = relationship(
        'StaffingAgreement',
        primaryjoin='ThirdPartyStaffingAgreement.staffing_agreement_id == StaffingAgreement.staffing_agreement_id',
        back_populates='third_party_staffing_agreement'
    )

    def __repr__(self):
        return "<ThirdPartyStaffingAgreement(" \
               "staffing_agreement_id='%s'" \
               ")>" % (
                   self.staffing_agreement_id
               )