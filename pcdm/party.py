from sqlalchemy import Column, Integer, Date, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Person(Base):
    __tablename__ = 'person'

    person_id = Column(
        Integer,
        primary_key=True
    )

    party_id = Column(
        Integer,
        ForeignKey('party.party_id')
    )

    prefix_name = Column(String)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    suffix_name = Column(String)
    full_legal_name = Column(String)
    nickname = Column(String)
    birth_date = Column(Date)
    birth_place_name = Column(String)
    gender_code = Column(String)

    person_profession = relationship(
        'PersonProfession',
        primaryjoin='Person.person_id == PersonProfession.person_id',
        back_populates='person'
    )

    staff_work_assignment = relationship(
        'Person',
        primaryjoin='Person.person_id == StaffWorkAssignment.person_id',
        back_populates='person'
    )

    household_person = relationship(
        'Person',
        primaryjoin='Person.person_id == HouseholdPerson.person_id',
        back_populates='person'
    )

    party = relationship(
        'Person',
        primaryjoin='Person.party_id == Party.party_id',
        back_populates='person'
    )

    household_person_role = relationship(
        'HouseholdPersonRole',
        primaryjoin='Person.person_id == HouseholdPersonRole.person_id',
        back_populates='person'
    )

    def __repr__(self):
        return "<Person(" \
               "prefix_name='%s', " \
               "first_name='%s', " \
               "middle_name='%s', "\
               "last_name='%s', " \
               "suffix_name='%s', " \
               "full_legal_name='%s', " \
               "nickname='%s', " \
               "birth_date='%s', " \
               "birth_place_name='%s', " \
               "gender_code='%s', "\
               ")>" % (
                   self.prefix_name,
                   self.first_name,
                   self.middle_name,
                   self.last_name,
                   self.suffix_name,
                   self.full_legal_name,
                   self.nickname,
                   self.birth_date,
                   self.birth_place_name,
                   self.gender_code
                )


class PersonProfession(Base):
    __tablename__ = 'person_profession'

    person_profession_id = Column(
        Integer,
        primary_key=True
    )

    person_id = Column(
        Integer,
        ForeignKey('person.person_id')
    )

    profession_name = Column(String)

    person = relationship(
        'Person',
        primaryjoin='PersonProfession.person_id == Person.person_id',
        back_populates='person_profession'
    )

    def __repr__(self):
        return "<PersonProfession(" \
            "person_id='%s', " \
            "profession_name='%s', " \
            ")>" % (
                self.person_id,
                self.profession_name
            )


class Organization(Base):
    __tablename__ = 'organization'

    organization_id = Column(
        Integer,
        primary_key=True
    )

    party_id = Column(
        Integer,
        ForeignKey('party.party_id')
    )

    organization_type_code = Column(Integer)

    organization_name = Column(String)

    alternate_name = Column(String)

    acronym_name = Column(String)

    industry_type_code = Column(String)

    industry_code = Column(String)

    dun_and_bradstreet_id = Column(String)

    organization_description = Column(String)

    staff_work_assignment = relationship(
        'StaffWorkAssignment',
        primaryjoin='Organization.organization_id == StaffWorkAssignment.organization_id',
        back_populates='organization'
    )

    party = relationship(
        'Party',
        primaryjoin='Organization.party_id == Party.party_id',
        back_populates='organization'
    )

    def __repr__(self):
        return "<Organization(" \
               "party_id='%s', " \
               "organization_type_code='%s', " \
               "organization_name='%s', " \
               "alternate_name='%s', "\
               "acronym_name='%s', " \
               "industry_type_code='%s', " \
               "industry_code='%s', " \
               "dun_and_bradstreet_id='%s', " \
               "organization_description='%s', " \
               ")>" % (
                   self.party_id,
                   self.organization_type_code,
                   self.organization_name,
                   self.alternate_name,
                   self.acronym_name,
                   self.industry_type_code,
                   self.industry_code,
                   self.dun_and_bradstreet_id,
                   self.organization_description
                )


class HouseholdPerson(Base):
    __tablename__ = 'household_person' \
                    ''
    household_person_id = Column(
        Integer,
        primary_key=True
    )

    household_id = Column(
        Integer,
        ForeignKey('household.household_id')
    )

    person_id = Column(
        Integer,
        ForeignKey('person.person_id')
    )

    household = relationship(
        'Household',
        primaryjoin='HouseholdPerson.household_id == Household.household_id',
        back_populates='household_person'
    )

    person = relationship(
        'Household',
        primaryjoin='HouseholdPerson.person_id == Person.person_id',
        back_populates='household_person'
    )

    def __repr__(self):
        return "<HouseholdPerson(" \
               "household_id='%s', " \
               "person_id='%s', " \
               ")>" % (
                   self.household_id,
                   self.person_id,
                )


class HouseholdPersonRole(Base):
    __tablename__ = 'household_person_role'

    household_person_role_id = Column(
        Integer,
        primary_key=True
    )

    household_id = Column(
        Integer,
        ForeignKey('household.household_id')
    )

    party_role_code = Column(
        String,
        ForeignKey('party_role.party_role_code')
    )

    begin_date = Column(Date)

    person_id = Column(
        Integer,
        ForeignKey('person.person_id')
    )

    end_date = Column(Date)

    household = relationship(
        'Household',
        primaryjoin='HouseholdPersonRole.household_id == Household.household_id',
        back_populates='household_person_role'
    )

    party_role = relationship(
        'PartyRole',
        primaryjoin='HouseholdPersonRole.party_role_code == PartyRole.party_role_code',
        back_populates='household_person_role'
    )

    person = relationship(
        'Person',
        primaryjoin='HouseholdPersonRole.person_id == Person.person_id',
        back_populates='household_person_role'
    )

    def __repr__(self):
        return "<HouseholdPersonRole(" \
               "household_id='%s', " \
               "party_role_code='%s', " \
               "begin_date='%s', "\
               "person_id='%s', " \
               "end_date='%s', " \
               ")>" % (
                   self.household_id,
                   self.party_role_code,
                   self.begin_date,
                   self.person_id,
                   self.end_date
                )


class Household(Base):
    __tablename__ = 'household'

    household_id = Column(
        Integer,
        primary_key=True
    )

    grouping_id = Column(
        Integer,
        ForeignKey('grouping.grouping_id')
    )

    household_person = relationship(
        'HouseholdPerson',
        primaryjoin='Household.household_id == HouseholdPerson.household_id',
        back_populates='household'
    )

    grouping = relationship(
        'Grouping',
        primaryjoin='Household.grouping_id == Grouping.grouping_id',
        back_populates='household'
    )

    household_person_role = relationship(
        'HouseholdPersonRole',
        primaryjoin='Household.household_id == HouseholdPersonRole.household_id',
        back_populates='household'
    )

    def __repr__(self):
        return "<Household(" \
               "grouping_id='%s', " \
               ")>" % (
                   self.grouping_id
                )


class StaffWorkAssignment(Base):
    __tablename__ = 'staff_work_assignment'

    staff_work_assignment_id = Column(
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

    grouping_id = Column(
        Integer,
        ForeignKey('grouping.grouping_id')
    )

    begin_date = Column(Date)
    party_role_code = Column(
        Integer,
        ForeignKey('party_role.party_role_code')
    )
    end_date = Column(Date)

    person = relationship(
        'Person',
        primaryjoin='StaffWorkAssignment.person_id == Person.person_id',
        back_populates='staff_work_assignment'
    )

    organization = relationship(
        'Organization',
        primaryjoin='StaffWorkAssignment.organization_id == Organization.organization_id',
        back_populates='staff_work_assignment'
    )

    grouping = relationship(
        'Grouping',
        primaryjoin='StaffWorkAssignment.grouping_id == Grouping.grouping_id',
        back_populates='staff_work_assignment'
    )

    party_role = relationship(
        'PartyRole',
        primaryjoin='StaffWorkAssignment.party_role_code == PartyRole.party_role_code',
        back_populates='staff_work_assignment'
    )

    def __repr__(self):
        return "<StaffWorkAssignment(" \
               "person_id='%s', " \
               "organization_id='%s', " \
               "grouping_id='%s', "\
               "begin_date='%s', " \
               "party_role_code='%s', " \
               "end_date='%s', " \
               ")>" % (
                   self.person_id,
                   self.organization_id,
                   self.grouping_id,
                   self.begin_date,
                   self.party_role_code,
                   self.end_date
                )


class Grouping(Base):
    __tablename__ = 'grouping'

    grouping_id = Column(
        Integer,
        primary_key=True
    )

    party_id = Column(
        Integer,
        ForeignKey('party.party_id')
    )

    grouping_name = Column(String)

    staff_work_assignment = relationship(
        'StaffWorkAssignment',
        primaryjoin='Grouping.grouping_id == StaffWorkAssignment.grouping_id',
        back_populates='grouping'
    )

    party = relationship(
        'Party',
        primaryjoin='Grouping.party_id == party.party_id',
        back_populates='grouping'
    )

    household = relationship(
        'Household',
        primaryjoin='Grouping.grouping_id == Household.grouping_id',
        back_populates='grouping'
    )

    def __repr__(self):
        return "<Grouping(" \
               "party_id='%s', " \
               "grouping_name='%s', " \
               ")>" % (
                   self.party_id,
                   self.grouping_name
                )


class PartyRole(Base):
    __tablename__ = 'party_role'

    party_role_code = Column(
        String,
        primary_key=True
    )

    party_role_name = Column(String)
    party_role_description = Column(String)

    staff_work_assignment = relationship(
        'StaffWorkAssignment',
        primaryjoin='PartyRole.party_role_code == StaffWorkAssignment.party_role_code',
        back_populates='party_role'
    )

    party_relationship_role = relationship(
        'PartyRelationshipRole',
        primaryjoin='PartyRole.party_role_code == PartyRelationshipRole.party_role_code',
        back_populates='party_role'
    )

    insurable_object_party_role = relationship(
        'InsurableObjectPartyRole',
        primaryjoin='Party.party_role_code == InsurableObjectPartyRole.party_role_code',
        back_populates='party_role'
    )

    claim_party_role = relationship(
        'ClaimPartyRole',
        primaryjoin='PartyRole.party_role_code == ClaimPartyRole.party_role_code',
        back_populates='party_role'
    )

    agreement_party_role = relationship(
        'AgreementPartyRole',
        primaryjoin='PartyRole.party_role_code == AgreementPartyRole.party_role_code',
        back_populates='party_role'
    )

    household_person_role = relationship(
        'HouseholdPersonRole',
        primaryjoin='PartyRole.party_role_code == HouseholdPersonRole.party_role_code',
        back_populates='party_role'
    )

    account_party_role = relationship(
        'AccountPartyRole',
        primaryjoin='PartyRole.party_role_code == AccountPartyRole.party_role_code',
        back_populates='party_role'
    )

    provider = relationship(
        'Provider',
        primaryjoin='PartyRole.party_role_code == Provider.party_role_code',
        back_populates='party_role'
    )

    account_role = relationship(
        'AccountRole',
        primaryjoin='PartyRole.party_role_code == AccountRole.party_role_code',
        back_populates='party_role'
    )

    agreement_role = relationship(
        'AgreementRole',
        primaryjoin='PartyRole.party_role_code == AgreementRole.party_role_code',
        back_populates='party_role'
    )

    def __repr__(self):
        return "<PartyRole(" \
               "party_role_name='%s', " \
               "party_role_description='%s', " \
               ")>" % (
                   self.party_role_name,
                   self.party_role_description
                )


class Party(Base):
    __tablename__ = 'party'

    party_id = Column(
        Integer,
        primary_key=True
    )

    party_name = Column(String)

    party_type_code = Column(String)

    begin_date = Column(Date)

    end_date = Column(Date)

    person = relationship(
        'Person',
        primaryjoin='Party.party_id == Person.party_id',
        back_populates='party'
    )

    grouping = relationship(
        'Grouping',
        primaryjoin='Party.party_id == Grouping.party_id',
        back_populates='party'
    )

    organization = relationship(
        'Organization',
        primaryjoin='Party.party_id == Organization.party_id',
        back_populates='party'
    )

    party_relationship = relationship(
        'PartyRelationship',
        primaryjoin='Party.party_id = PartyRelationship.party_id',
        back_populates='party'
    )

    related_party_relationship = relationship(
        'PartyRelationship',
        primaryjoin='Party.party_id = PartyRelationship.related_party_id',
        back_populates='related_party'
    )

    legal_jurisdiction_party_identity = relationship(
        'LegalJurisdictionPartyIdentity',
        primaryjoin='Party.party_id == LegalJurisdictionPartyIdentity.party_id',
        back_populates='party'
    )

    party_communication = relationship(
        'PartyCommunication',
        primaryjoin='Party.party_id == PartyCommunication.party_id',
        back_populates='party'
    )

    insurable_object_party_role = relationship(
        'InsurableObjectPartyRole',
        primaryjoin='Party.party_id == InsurableObjectPartyRole.party_id',
        back_populates='party'
    )

    party_preference = relationship(
        'PartyPreference',
        primaryjoin='Party.party_id == PartyPreference.party_id',
        back_populates='party'
    )

    agreement_party_role = relationship(
        'AgreementPartyRole',
        primaryjoin='Party.party_id == AgreementPartyRole.party_id',
        back_populates='party'
    )

    account_party_role = relationship(
        'AccountPartyRole',
        primaryjoin='Party.party_id == AccountPartyRole.party_id',
        back_populates='party'
    )

    def __repr__(self):
        return "<Party(" \
               "party_name='%s', " \
               "party_type_code='%s', " \
               "begin_date='%s', " \
               "end_date='%s', " \
               ")>" % (
                   self.party_name,
                   self.party_type_code,
                   self.begin_date,
                   self.end_date
                )


class PartyRelationship(Base):
    __tablename__ = 'party_relationship'

    party_relationship_id = Column(
        Integer,
        primary_key=True
    )

    party_id = Column(
        Integer,
        ForeignKey('party.party_id')
    )

    related_party_id = Column(
        Integer,
        ForeignKey('party.party_id')
    )

    relationship_type_code = Column(String)

    begin_date = Column(Date)

    end_date = Column(Date)

    party = relationship(
        'Party',
        primaryjoin='PartyRelationship.party_id = Party.party_id',
        back_populates='party_relationship'
    )

    related_party = relationship(
        'Party',
        primaryjoin='PartyRelationship.related_party_id = Party.party_id',
        back_populates='related_party_relationship'
    )

    party_relationship_role = relationship(
        'PartyRelationshipRole',
        primaryjoin='PartyRelationship.party_id == PartyRelationshipRole.party_id ',
        back_populates='party_relationship'
    )

    related_party_relationship_role = relationship(
        'PartyRelationshipRole',
        primaryjoin='PartyRelationship.related_party_id == PartyRelationshipRole.related_party_id',
        back_populates='related_party_relationship'
    )

    party_relationship_role_type_code = relationship(
        'PartyRelationshipRole',
        primaryjoin='PartyRelationship.relationship_type_code == PartyRelationshipRole.relationship_type_code',
        back_populates='party_relationship_type_code'
    )

    party_relationship_role_begin_date = relationship(
        'PartyRelationship',
        primaryjoin='PartyRelationship.begin_date == PartyRelationshipRole.relationship_begin_date',
        back_populates='party_relationship_begin_date'
    )

    def __repr__(self):
        return "<PartyRelationship(" \
               "party_id='%s', " \
               "relationship_type_code='%s', " \
               "begin_date='%s', " \
               "end_date='%s', " \
               ")>" % (
                   self.party_id,
                   self.relationship_type_code,
                   self.begin_date,
                   self.end_date
                )


class PartyRelationshipRole(Base):
    __tablename__ = 'party_relationship_role'

    party_relationship_role_id = Column(
        Integer,
        primary_key=True
    )

    party_id = Column(
        Integer,
        ForeignKey('party_relationship.party_id')
    )

    related_party_id = Column(
        Integer,
        ForeignKey('party_relationship.related_party_id')
    )

    relationship_type_code = Column(
        Integer,
        ForeignKey('party_relationship.relationship_type_code')
    )

    relationship_begin_date = Column(
        Date,
        ForeignKey('party_relationship.begin_date')
    )

    party_role_code = Column(
        String,
        ForeignKey('party_role.party_role_code')
    )

    role_begin_date = Column(Date)

    party_relationship = relationship(
        'PartyRelationship',
        primaryjoin='PartyRelationshipRole.party_id == PartyRelationship.party_id',
        back_populates='party_relationship_role'
    )

    related_party_relationship = relationship(
        'PartyRelationship',
        primaryjoin='PartyRelationshipRole.related_party_id == PartyRelationship.related_party_id',
        back_populates='related_party_relationship_role'
    )

    party_relationship_type_code = relationship(
        'PartyRelationship',
        primaryjoin='PartyRelationshipRole.relationship_type_code == PartyRelationship.relationship_type_code',
        back_populates='party_relationship_role_type_code'
    )

    party_relationship_begin_date = relationship(
        'PartyRelationship',
        primaryjoin='PartyRelationshipRole.relationship_begin_date == PartyRelationship.begin_date',
        back_populates='party_relationship_role_begin_date'
    )

    party_role = relationship(
        'PartyRole',
        primaryjoin='PartyRelationshipRole.party_role_code == PartyRole.party_role_code',
        back_populates='party_relationship_role'
    )

    def __repr__(self):
        return "<PartyRelationshipRole(" \
               "party_id='%s', " \
               "related_party_id='%s', " \
               "relationship_type_code='%s', "\
               "relationship_begin_date='%s', " \
               "party_role_code='%s', " \
               "role_begin_date='%s', " \
               ")>" % (
                   self.party_id,
                   self.related_party_id,
                   self.relationship_type_code,
                   self.relationship_begin_date,
                   self.party_role_code,
                   self.role_begin_date
                )


class LegalJurisdictionPartyIdentity(Base):
    __tablename__ = 'legal_jurisdiction_party_identity'

    legal_jurisdiction_party_id = Column(
        Integer,
        primary_key=True
    )

    legal_jurisdiction_id = Column(
        Integer,
        ForeignKey('legal_jurisdiction.legal_jurisdiction_id')
    )

    party_id = Column(
        Integer,
        ForeignKey('party.party_id')
    )

    legal_identity_type_code = Column(String)
    legal_classification_code = Column(String)

    party = relationship(
        'Party',
        primaryjoin='LegalJurisdictionPartyIdentity.party_id == Party.party_id',
        back_populates='legal_jurisdiction_party_identity'
    )

    legal_jurisdiction = relationship(
        'LegalJurisdiction',
        primaryjoin='LegalJurisdictionPartyIdentity.legal_jurisdiction_id == LegalJurisdiction.legal_jurisdiction_id',
        back_populates='legal_jurisdiction_party_identity'
    )

    def __repr__(self):
        return "<LegalJurisdictionPartyIdentity(" \
               "legal_jurisdiction_id='%s', " \
               "party_id='%s', " \
               "legal_identity_type_code='%s', "\
               "legal_classification_code='%s', " \
               ")>" % (
                   self.legal_jurisdiction_id,
                   self.party_id,
                   self.legal_identity_type_code,
                   self.legal_classification_code
                )


class LegalJurisdiction(Base):
    __tablename__ = 'legal_jurisdiction'

    legal_jurisdiction_id = Column(
        Integer,
        primary_key=True
    )

    legal_jurisdiction_name = Column(String)
    legal_jurisdiction_description = Column(String)
    rules_preference_description = Column(String)

    legal_jurisdiction_party_identity = relationship(
        'LegalJurisdictionPartyIdentity',
        primaryjoin='LegalJurisdiction.legal_jurisdiction_id == LegalJurisdictionPartyIdentity.legal_jurisdiction_id',
        back_populates='legal_jurisdiction'
    )

    def __repr__(self):
        return "<LegalJurisdiction(" \
               "legal_jurisdiction_name='%s', " \
               "legal_jurisdiction_description='%s', " \
               "rules_preference_description='%s', "\
               ")>" % (
                   self.legal_jurisdiction_name,
                   self.legal_jurisdiction_description,
                   self.rules_preference_description
                )


class PartyCommunication(Base):
    __tablename__ = 'party_communication'

    party_communication_id = Column(
        Integer,
        primary_key=True
    )

    party_id = Column(
        Integer,
        ForeignKey('party.party_id')
    )

    communication_id = Column(
        Integer,
        ForeignKey('communication_identity.communication_id')
    )

    party_locality_code = Column(Integer)

    begin_date = Column(Date)

    end_date = Column(Date)

    preference_sequence_number = Column(Integer)

    preference_day_and_time_group_code = Column(Integer)

    party_routing_description = Column(String)

    party = relationship(
        'Party',
        primaryjoin='PartyCommunication.party_id == Party.party_id',
        back_populates='party_communication'
    )

    communication = relationship(
        'CommunicationIdentity',
        primaryjoin='PartyCommunication.communication_id == CommunicationIdentity.communication_id',
        back_populates='party_communication'
    )

    def __repr__(self):
        return "<PartyCommunication(" \
               "party_id='%s', " \
               "communication_id='%s', " \
               "party_locality_code='%s', " \
               "begin_date='%s', " \
               "end_date='%s', "\
               "preference_sequence_number='%s', " \
               "preference_day_and_time_group_code='%s', " \
               "party_routing_description='%s', " \
               ")>" % (
                   self.party_id,
                   self.communication_id,
                   self.party_locality_code,
                   self.begin_date,
                   self.end_date,
                   self.preference_sequence_number,
                   self.preference_day_and_time_group_code,
                   self.party_routing_description
                )


class CommunicationIdentity(Base):
    __tablename__ = 'communication_identity'

    communication_id = Column(
        Integer,
        primary_key=True
    )

    communication_type_code = Column(String)
    communication_value = Column(String)
    communication_qualifier_value = Column(String)

    geographic_location_id = Column(
        Integer,
        ForeignKey('geographic_location.geographic_location_id')
    )

    party_communication = relationship(
        'PartyCommunication',
        primaryjoin='CommunicationIdentity.communication_id == PartyCommunication.communication_id',
        back_populates='communication'
    )
    geographic_location = relationship(
        'GeographicLocationIdentifier',
        primaryjoin='CommunicationIdentity.geographic_location_id == '
                    'GeographicLocationIdentifier.geographic_location_id',
        back_populates='communication_identity'
    )

    def __repr__(self):
        return "<CommunicationIdentity(" \
               "communication_type_code='%s', " \
               "communication_value='%s', " \
               "communication_qualifier_value='%s', " \
               "geographic_location_id='%s', " \
               ")>" % (
                   self.communication_type_code,
                   self.communication_value,
                   self.communication_qualifier_value,
                   self.geographic_location_id
                )


class GeographicLocation(Base):
    __tablename__ = 'geographic_location'

    geographic_location_id = Column(
        Integer,
        primary_key=True
    )

    geographic_location_type_code = Column(String)

    location_code = Column(String)

    location_name = Column(String)

    location_number = Column(String)

    state_code = Column(String)

    parent_geographic_location_id = Column(
        Integer,
        ForeignKey('geographic_location.geographic_location_id')
    )

    location_address_identifier = Column(Integer)

    physical_location_identifier = Column(Integer)

    geographic_location_parent = relationship(
        'GeographicLocation',
        primaryjoin='GeographicLocation.parent_geographic_location_id =='
                    ' GeographicLocation.geographic_location_id',
        back_populates='geographic_location_parent_u'
    )

    geographic_location_parent_u = relationship(
        'GeographicLocation',
        primaryjoin='GeographicLocation.geographic_location_id =='
                    ' GeographicLocation.parent_geographic_location_id',
        back_populates='geographic_location_parent'
    )

    communication_identity = relationship(
        'GeographicLocation',
        primaryjoin='CommunicationIdentity.geographic_location_id == '
                    'GeographicLocation.geographic_location_id',
        back_populates='geographic_location'
    )

    insurable_object = relationship(
        'InsurableObject',
        primaryjoin='GeographicLocation.geographic_location_id == InsurableObject.geographic_location_id',
        back_populates='geographic_location'
    )

    policy = relationship(
        'Policy',
        primaryjoin='GeographicLocation.geographic_location_id == Policy.geographic_location_id',
        back_populates='geographic_location'
    )

    def __repr__(self):
        return "<GeographicLocation(" \
               "geographic_location_type_code='%s', " \
               "location_code='%s', " \
               "location_name='%s', "\
               "location_number='%s', " \
               "state_code='%s', " \
               "parent_geographic_location_id='%s', " \
               "location_address_identifier='%s', " \
               "physical_location_identifier='%s', " \
               ")>" % (
                   self.geographic_location_type_code,
                   self.location_code,
                   self.location_name,
                   self.location_number,
                   self.state_code,
                   self.parent_geographic_location_id,
                   self.location_address_identifier,
                   self.physical_location_identifier
                )


class InsurableObject(Base):
    __tablename__ = 'insurable_object'

    insurable_object_id = Column(
        Integer,
        primary_key=True
    )

    insurable_object_type_code = Column(Integer)

    geographic_location_id = Column(
        Integer,
        ForeignKey('geographic_location.geographic_location_id')
    )

    geographic_location = relationship(
        'GeographicLocation',
        primaryjoin='InsurableObject.geographic_location_id == GeographicLocation.geographic_location_id',
        back_populates='insurable_object'
    )

    claim = relationship(
        'Claim',
        primaryjoin='InsurableObject.insurable_object_id == Claim.insurable_object_id',
        back_populates='insurable_object'
    )

    insurable_object_party_role = relationship(
        'InsurableObjectPartyRole',
        primaryjoin='InsurableObject.insurable_object_id == InsurableObjectPartyRole.insurable_object_id',
        back_populates='insurable_object'
    )

    def __repr__(self):
        return "<InsurableObject(" \
               "insurable_object_type_code='%s', " \
               "geographic_location_id='%s', " \
               ")>" % (
                   self.insurable_object_type_code,
                   self.geographic_location_id
                )


class Claim(Base):
    __tablename__ = 'claim'

    claim_id = Column(
        Integer,
        primary_key=True
    )

    occurrence_id = Column(Integer)
    catastrophe_id = Column(Integer)
    insurable_object_id = Column(
        Integer,
        ForeignKey('insurable_object.insurable_object_id')
    )
    company_claim_number = Column(Integer)
    company_subclaim_number = Column(Integer)
    claim_description = Column(String)
    claim_open_date = Column(Date)
    claim_close_date = Column(Date)
    claim_reopen_date = Column(Date)
    claim_status_code = Column(String)
    claim_reported_date = Column(Date)
    claims_made_date = Column(Date)
    entry_in_to_claims_made_program_date = Column(Date)

    insurable_object = relationship(
        'InsurableObject',
        primaryjoin='Claim.insurable_object_id == InsurableObject.insurable_object_id',
        back_populates='claim'
    )

    def __repr__(self):
        return "<Claim(" \
               "occurrence_id='%s', " \
               "catastrophe_id='%s', " \
               "insurable_object_id='%s', "\
               "company_claim_number='%s', " \
               "company_subclaim_number='%s', " \
               "claim_description='%s', " \
               "claim_open_date='%s', " \
               "claim_close_date='%s', " \
               "claim_reopen_date='%s', " \
               "claim_status_code='%s', " \
               "claim_reported_date='%s', "\
               "claims_made_date='%s', "\
               "entry_in_to_claims_made_program_date='%s', "\
               ")>" % (
                   self.occurrence_id,
                   self.catastrophe_id,
                   self.insurable_object_id,
                   self.company_claim_number,
                   self.company_subclaim_number,
                   self.claim_description,
                   self.claim_open_date,
                   self.claim_close_date,
                   self.claim_reopen_date,
                   self.claim_status_code,
                   self.claim_reported_date,
                   self.claims_made_date,
                   self.entry_in_to_claims_made_program_date
                )


class InsurableObjectPartyRole(Base):
    __tablename__ = 'insurable_object_party_role'

    insurable_object_party_role_id = Column(
        Integer,
        primary_key=True
    )

    insurable_object_id = Column(
        Integer,
        ForeignKey('insurable_object.insurable_object_id')
    )

    party_role_code = Column(
        String,
        ForeignKey('party_role.party_role_code')
    )

    effective_date = Column(Date)

    party_id = Column(
        Integer,
        ForeignKey('party.party_id')
    )

    expiration_date = Column(Date)

    insurable_object = relationship(
        'InsurableObject',
        primaryjoin='InsurableObjectPartyRole.insurable_object_id == InsurableObject.insurable_object_id',
        back_populates='insurable_object_party_role'
    )

    party_role = relationship(
        'PartyRole',
        primaryjoin='InsurableObjectPartyRole.party_role_code == PartyRole.party_role_code',
        back_populates='insurable_object_party_role'
    )

    party = relationship(
        'Party',
        primaryjoin='InsurableObjectPartyRole.party_id == Party.party_id',
        back_populates='insurable_object_party_role'
    )

    def __repr__(self):
        return "<InsurableObjectPartyRole(" \
               "insurable_object_id='%s', " \
               "party_role_code='%s', " \
               "effective_date='%s', "\
               "party_id='%s', " \
               "expiration_date='%s', " \
               ")>" % (
                   self.insurable_object_id,
                   self.party_role_code,
                   self.effective_date,
                   self.party_id,
                   self.expiration_date
                )


class ClaimPartyRole(Base):
    __tablename__ = 'claim_party_role'

    claim_party_role_id = Column(
        Integer,
        primary_key=True
    )

    party_role_code = Column(
        String,
        ForeignKey('party_role.party_role_code')
    )

    begin_date = Column(Date)

    party_id = Column(
        Integer,
        ForeignKey('party.party_id')
    )

    end_date = Column(Date)

    party_role = relationship(
        'PartyRole',
        primaryjoin='ClaimPartyRole.party_role_code == PartyRole.party_role_code',
        back_populates='claim_party_role'
    )

    party = relationship(
        'Party',
        primaryjoin='ClaimPartyRole.party_id == Party.party_id',
        back_populates='claim_party_role'
    )

    def __repr__(self):
        return "<ClaimPartyRole(" \
               "party_role_code='%s', " \
               "begin_date='%s', " \
               "party_id='%s', " \
               "end_date='%s', " \
               ")>" % (
                   self.party_role_code,
                   self.begin_date,
                   self.party_id,
                   self.end_date
                )


class PartyPreference(Base):
    __tablename__ = 'party_preference'

    party_id = Column(
        Integer,
        ForeignKey('party.party_id'),
        primary_key=True
    )

    preferred_language_code = Column(Integer)

    party = relationship(
        'Party',
        primaryjoin='PartyPreference.party_id == Party.party_id',
        back_populates='party_preference'
    )

    def __repr__(self):
        return "<PartyPreference(" \
               "preferred_language_code='%s', " \
               ")>" % (
                   self.preferred_language_code
                )


class Agreement(Base):
    __tablename__ = 'agreement'

    agreement_id = Column(
        Integer,
        primary_key=True
    )

    agreement_type_code = Column(Integer)
    agreement_name = Column(String)
    agreement_original_inception_date = Column(Date)
    product_identifier = Column(Integer)

    agreement_party_role = relationship(
        'AgreementPartyRole',
        primaryjoin='Agreement.agreement_id == AgreementPartyRole.agreement_id',
        back_populates='agreement'
    )

    account_agreement = relationship(
        'AccountAgreement',
        primaryjoin='Agreement.agreement_id == AccountAgreement.agreement_id',
        back_populates='agreement'
    )

    policy = relationship(
        'Policy',
        primaryjoin='Agreement.agreement_id == Policy.agreement_id',
        back_populates='agreement'
    )

    agency_contract = relationship(
        'AgencyContract',
        primaryjoin='agreement.agreement_id == AgencyContract.agreement_id',
        back_populates='agreement'
    )

    reinsurance_agreement = relationship(
        'ReinsuranceAgreement',
        primaryjoin='Agreement.agreement_id == ReinsuranceAgreement.agreement_id',
        back_populates='agreement'
    )

    commercial_agreement = relationship(
        'CommercialAgreement',
        primaryjoin='Agreement.agreement_id == CommercialAgreement.agreement_id',
        back_populates='agreement'
    )

    brokerage_contract = relationship(
        'BrokerageContract',
        primaryjoin='Agreement.agreement_id == BrokerageContract.agreement_id',
        back_populates='agreement'
    )

    financial_account_agreement = relationship(
        'FinancialAccountAgreement',
        primaryjoin='Agreement.agreement_id == FinancialAccountAgreement.agreement_id',
        back_populates='agreement'
    )

    derivative_contract = relationship(
        'DerivativeContract',
        primaryjoin='Agreement.agreement_id == DerivativeContract.agreement_id',
        back_populates='agreement'
    )

    intermediary_agreement = relationship(
        'IntermediaryAgreement',
        primaryjoin='Agreement.agreement_id == IntermediaryAgreement.agreement_id',
        back_populates='agreement'
    )

    group_agreement = relationship(
        'GroupAgreement',
        primaryjoin='Agreement.agreement_id == GroupAgreement.agreement_id',
        back_populates='agreement'
    )

    commutation_agreement = relationship(
        'CommutationAgreement',
        primaryjoin='Agreement.agreement_id == CommutationAgreement.agreement_id',
        back_populates='agreement'
    )

    provider_agreement = relationship(
        'ProviderAgreement',
        primaryjoin='Agreement.agreement_id == ProviderAgreement.agreement_id',
        back_populates='agreement'
    )

    individual_agreement = relationship(
        'IndividualAgreement',
        primaryjoin='Agreement.agreement_id == IndividualAgreement.agreement_id',
        back_populates='agreement'
    )

    auto_repair_shop_contract = relationship(
        'AutoRepairShopContract',
        primaryjoin='Agreement.agreement_id == AutoRepairShopContract.agreement_id',
        back_populates='agreement'
    )

    staffing_agreement = relationship(
        'StaffingAgreement',
        primaryjoin='Agreement.agreement_id == StaffingAgreement.agreement_id',
        back_populates='staffing_agreement'
    )

    def __repr__(self):
        return "<Agreement(" \
               "agreement_type_code='%s', " \
               "agreement_name='%s', " \
               "agreement_original_inception_date='%s', " \
               "product_identifier='%s', " \
               ")>" % (
                   self.agreement_type_code,
                   self.agreement_name,
                   self.agreement_original_inception_date,
                   self.product_identifier
                )


class AgreementPartyRole(Base):
    __tablename__ = 'agreement_party_role'

    agreement_party_role_id = Column(
        Integer,
        primary_key=True
    )

    agreement_id = Column(
        Integer,
        ForeignKey('agreement.agreement_id')
    )

    party_role_code = Column(
        String,
        ForeignKey('party_role.party_role_code')
    )

    effective_date = Column(Date)

    party_id = Column(
        Integer,
        ForeignKey('party.party_id')
    )

    expiration_date = Column(Date)

    agreement = relationship(
        'Agreement',
        primaryjoin='AgreementPartyRole.agreement_id == Agreement.agreement_id',
        back_populates='agreement_party_role'
    )

    party_role = relationship(
        'PartyRole',
        primaryjoin='AgreementPartyRole.party_role_code == PartyRole.party_role_code',
        back_populates='agreement_party_role'
    )

    party = relationship(
        'Party',
        primaryjoin='AgreementPartyRole.party_id == Party.party_id',
        back_populates='agreement_party_role'
    )

    def __repr__(self):
        return "<AgreementPartyRole(" \
               "agreement_id='%s', " \
               "party_role_code='%s', " \
               "effective_date='%s', " \
               "party_id='%s', " \
               "expiration_date='%s', " \
               ")>" % (
                   self.agreement_id,
                   self.party_role_code,
                   self.effective_date,
                   self.party_id,
                   self.expiration_date
                )
