from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Buyer(Base):
    __tablename__ = 'buyer'

    buyer_id = Column(
        Integer,
        primary_key=True
    )

    provider_id = Column(
        Integer,
        ForeignKey('provider.provider_id')
    )

    provider = relationship(
        'Provider',
        primaryjoin='Buyer.provider_id == Providmaner.provider_id',
        back_populates='buyer'
    )

    def __repr__(self):
        return "<Buyer(" \
               "provider_id='%s'" \
               ")>" % (
                   self.provider_id
                )


class HealthCareProvider(Base):
    __tablename__ = 'health_care_provider'

    health_care_provider_id = Column(
        Integer,
        primary_key=True
    )

    provider_id = Column(
        Integer,
        ForeignKey('provider.provider_id')
    )

    provider = relationship(
        'Provider',
        primaryjoin='HealthCareProvider.provider_id == Provider.provider_id',
        back_populates='health_care_provider'
    )

    def __repr__(self):
        return "<HealthCareProvider(" \
               "provider_id='%s', " \
               ")>" % (
                   self.provider_id
                )


class ThirdPartyAdministrator(Base):
    __tablename__ = 'third_party_administrator'

    third_party_administrator_id = Column(
        Integer,
        primary_key=True
    )

    provider_id = Column(
        Integer,
        ForeignKey('provider.provider_id')
    )

    provider = relationship(
        'Provider',
        primaryjoin='ThirdPartyAdministrator.provider_id == Provider.provider_id',
        back_populates='third_party_administrator'
    )

    def __repr__(self):
        return "<ThirdPartyAdministrator(" \
               "provider_id='%s'" \
               ")>" % (
                   self.provider_id
                )


class MutualFundProvider(Base):
    __tablename__ = 'mutual_fund_provider'

    mutual_fund_provider_id = Column(
        Integer,
        primary_key=True
    )

    provider_id = Column(
        Integer,
        ForeignKey('provider.provider_id')
    )

    provider = relationship(
        'Provider',
        primaryjoin='MutualFundProvider.provider_id == Provider.provider_id',
        back_populates='mutual_fund_provider'
    )

    def __repr__(self):
        return "<MutualFundProvider(" \
               "provider_id='%s'" \
               ")>" % (
                   self.provider_id
                )


class LegalAdviser(Base):
    __tablename__ = 'legal_adviser'

    legal_adviser_id = Column(
        Integer,
        primary_key=True
    )

    provider_id = Column(
        Integer,
        ForeignKey('provider.provider_id')
    )

    provider = relationship(
        'Provider',
        primaryjoin='LegalAdviser.provider_id == Provider.provider_id',
        back_populates='legal_adviser'
    )

    def __repr__(self):
        return "<LegalAdviser(" \
               "provider_id='%s'" \
               ")>" % (
                   self.provider_id
                )


class Contractor(Base):
    __tablename__ = 'contractor'

    contractor_id = Column(
        Integer,
        primary_key=True
    )

    provider_id = Column(
        Integer,
        ForeignKey('provider.provider_id')
    )

    provider = relationship(
        'Provider',
        primaryjoin='Contractor.provider_id == Provider.provider_id',
        back_populates='contractor'
    )

    subcontractor = relationship(
        'Subcontractor',
        primaryjoin='Contractor.contractor_id == Subcontractor.contractor_id',
        back_populates='contractor'
    )

    def __repr__(self):
        return "<Contractor(" \
               "provider_id='%s'" \
               ")>" % (
                   self.provider_id
                )


class Subcontractor(Base):
    __tablename__ = 'subcontractor'

    subcontractor_id = Column(
        Integer,
        primary_key=True
    )

    contractor_id = Column(
        Integer,
        ForeignKey('contractor.contractor_id')
    )

    contractor = relationship(
        'Contractor',
        primaryjoin='Subcontractor.contractor_id == Contractor.contractor_id',
        back_populates='subcontractor'
    )

    def __repr__(self):
        return "<Subcontractor(" \
               "contractor_id='%s'" \
               ")>" % (
                   self.contractor_id
                )


class Auditor(Base):
    __tablename__ = 'auditor'

    auditor_id = Column(
        Integer,
        primary_key=True
    )

    provider_id = Column(
        Integer,
        ForeignKey('provider.provider_id')
    )

    provider = relationship(
        'Provider',
        primaryjoin='Auditor.provider_id == Provider.provider_id',
        back_populates='auditor'
    )

    premium_auditor = relationship(
        'PremiumAuditor',
        primaryjoin='Auditor.auditor_id == PremiumAuditor.auditor_id',
        back_populates='auditor'
    )

    def __repr__(self):
        return "<Auditor(" \
               "provider_id='%s'" \
               ")>" % (
                   self.provider_id
                )


class PremiumAuditor(Base):
    __tablename__ = 'premium_auditor'

    premium_auditor_id = Column(
        Integer,
        primary_key=True
    )

    auditor_id = Column(
        Integer,
        ForeignKey('auditor.auditor_id')
    )

    auditor = relationship(
        'Auditor',
        primaryjoin='PremiumAuditor.auditor_id == Auditor.auditor_id',
        back_populates='premium_auditor'
    )

    def __repr__(self):
        return "<PremiumAuditor(" \
               "auditor_id='%s'" \
               ")>" % (
                   self.auditor_id
                )


class StaffRole(Base):
    __tablename__ = 'staff_role'

    staff_role_id = Column(
        Integer,
        primary_key=True
    )

    party_role_code = Column(
        String,
        ForeignKey('party_role.party_role_code')
    )

    party_role = relationship(
        'PartyRole',
        primaryjoin='StaffRole.party_role_code == PartyRole.party_role_code',
        back_populates='staff_role'
    )

    accountability = relationship(
        'Accountability',
        primaryjoin='StaffRole.staff_role_id == Accountability.staff_role_id',
        back_populates='staff_role'
    )

    manager = relationship(
        'Manager',
        primaryjoin='StaffRole.staff_role_id == Manager.staff_role_id',
        back_populates='staff_role'
    )

    team_leader = relationship(
        'TeamLeader',
        primaryjoin='StaffRole.staff_role_id == TeamLeader.staff_role_id',
        back_populates='staff_role'
    )

    team_member = relationship(
        'TeamMember',
        primaryjoin='StaffRole.staff_role_id == TeamMember.staff_role_id',
        back_populates='staff_role'
    )

    def __repr__(self):
        return "<StaffRole(" \
               "party_role_code='%s'" \
               ")>" % (
                   self.party_role_code
                )


class Accountability(Base):
    __tablename__ = 'accountability'

    accountability_id = Column(
        Integer,
        primary_key=True
    )

    staff_role_id = Column(
        Integer,
        ForeignKey('staff_role.staff_role_id')
    )

    staff_role = relationship(
        'StaffRole',
        primaryjoin='Accountability.staff_role_id == StaffRole.staff_role_id',
        back_populates='accountability'
    )

    def __repr__(self):
        return "<Accountability(" \
               "staff_role_id='%s'" \
               ")>" % (
                   self.staff_role_id
                )


class Manager(Base):
    __tablename__ = 'manager'

    manager_id = Column(
        Integer,
        primary_key=True
    )

    staff_role_id = Column(
        Integer,
        ForeignKey('staff_role.staff_role_id')
    )

    staff_role = relationship(
        'StaffRole',
        primaryjoin='Manager.staff_role_id == StaffRole.staff_role_id',
        back_populates='manager'
    )

    def __repr__(self):
        return "<Manager(" \
               "staff_role_id='%s'" \
               ")>" % (
                   self.staff_role_id
               )


class TeamLeader(Base):
    __tablename__ = 'team_leader'

    team_leader_id = Column(
        Integer,
        primary_key=True
    )

    staff_role_id = Column(
        Integer,
        ForeignKey('staff_role.staff_role_id')
    )

    staff_role = relationship(
        'StaffRole',
        primaryjoin='TeamLeader.staff_role_id == StaffRole.staff_role_id',
        back_populates='team_leader'
    )

    def __repr__(self):
        return "<TeamLeader(" \
               "staff_role_id='%s'" \
               ")>" % (
                   self.staff_role_id
               )


class TeamMember(Base):
    __tablename__ = 'team_member'

    team_member_id = Column(
        Integer,
        primary_key=True
    )

    staff_role_id = Column(
        Integer,
        ForeignKey('staff_role.staff_role_id')
    )

    staff_role = relationship(
        'StaffRole',
        primaryjoin='TeamMember.staff_role_id == StaffRole.staff_role_id',
        back_populates='team_member'
    )

    def __repr__(self):
        return "<TeamMember(" \
               "staff_role_id='%s'" \
               ")>" % (
                   self.staff_role_id
               )


class Producer(Base):
    __tablename__ = 'producer'

    producer_id = Column(
        Integer,
        primary_key=True
    )

    agreement_role_id = Column(
        Integer,
        ForeignKey('agreement_role.agreement_role_id')
    )

    agreement_role = relationship(
        'AgreementRole',
        primaryjoin='Producer.agreement_role_id == AgreementRole.agreement_role_id',
        back_populates='producer'
    )

    agent = relationship(
        'Agent',
        primaryjoin='Producer.producer_id == Agent.producer_id',
        back_populates='producer'
    )

    broker = relationship(
        'Broker',
        primaryjoin='Producer.producer_id == Broker.producer_id',
        back_populates='producer'
    )

    managing_general_agent = relationship(
        'ManagingGeneralAgent',
        primaryjoin='Producer.producer_id == ManagingGeneralAgent.producer_id',
        back_populates='producer'
    )

    def __repr__(self):
        return "<Producer(" \
               "agreement_role_id='%s'" \
               ")>" % (
                   self.agreement_role_id
               )


class Agent(Base):
    __tablename__ = 'agent'

    agent_id = Column(
        Integer,
        primary_key=True
    )

    producer_id = Column(
        Integer,
        ForeignKey('producer.producer_id')
    )

    producer = relationship(
        'Producer',
        primaryjoin='Agent.producer_id == Producer.producer_id',
        back_populates='agent'
    )

    def __repr__(self):
        return "<Agent(" \
               "producer_id='%s'" \
               ")>" % (
                   self.producer_id
               )


class Broker(Base):
    __tablename__ = 'broker'

    broker_id = Column(
        Integer,
        primary_key=True
    )

    producer_id = Column(
        Integer,
        ForeignKey('producer.producer_id')
    )

    producer = relationship(
        'Producer',
        primaryjoin='Broker.producer_id == Producer.producer_id',
        back_populates='broker'
    )

    def __repr__(self):
        return "<Broker(" \
               "producer_id='%s'" \
               ")>" % (
                   self.producer_id
               )


class ManagingGeneralAgent(Base):
    __tablename__ = 'managing_general_agent'

    managing_general_agent_id = Column(
        Integer,
        primary_key=True
    )

    producer_id = Column(
        Integer,
        ForeignKey('producer.producer_id')
    )

    producer = relationship(
        'Producer',
        primaryjoin='ManagingGeneralAgent.producer_id == Producer.producer_id',
        back_populates='managing_general_agent'
    )

    def __repr__(self):
        return "<ManagingGeneralAgent(" \
               "producer_id='%s'" \
               ")>" % (
                   self.producer_id
               )


class Supplier(Base):
    __tablename__ = 'supplier'

    supplier_id = Column(
        Integer,
        primary_key=True
    )

    agreement_role_id = Column(
        Integer,
        ForeignKey('agreement_role.agreement_role_id')
    )

    agreement_role = relationship(
        'AgreementRole',
        primaryjoin='Supplier.agreement_role_id == AgreementRole.agreement_role_id',
        back_populates='supplier'
    )

    def __repr__(self):
        return "<Supplier(" \
               "agreement_role_id='%s'" \
               ")>" % (
                   self.agreement_role_id
               )


class ChannelRole(Base):
    __tablename__ = 'channel_role'

    channel_role_id = Column(
        Integer,
        primary_key=True
    )

    agreement_role_id = Column(
        Integer,
        ForeignKey('agreement_role.agreement_role_id')
    )

    agreement_role = relationship(
        'AgreementRole',
        primaryjoin='ChannelRole.agreement_role_id == AgreementRole.agreement_role_id',
        back_populates='channel_role'
    )

    def __repr__(self):
        return "<ChannelRole(" \
               "agreement_role_id='%s'" \
               ")>" % (
                   self.agreement_role_id
               )


class ServiceProvider(Base):
    __tablename__ = 'service_provider'

    service_provider_id = Column(
        Integer,
        primary_key=True
    )

    agreement_role_id = Column(
        Integer,
        ForeignKey('agreement_role.agreement_role_id')
    )

    agreement_role = relationship(
        'AgreementRole',
        primaryjoin='ServiceProvider.agreement_role_id == AgreementRole.agreement_role_id',
        back_populates='service_provider'
    )

    def __repr__(self):
        return "<ServiceProvider(" \
               "agreement_role_id='%s'" \
               ")>" % (
                   self.agreement_role_id
               )


class FinancialInterestRole(Base):
    __tablename__ = 'financial_interest_role'

    financial_interest_role_id = Column(
        Integer,
        primary_key=True
    )

    agreement_role_id = Column(
        Integer,
        ForeignKey('agreement_role.agreement_role_id')
    )

    agreement_role = relationship(
        'AgreementRole',
        primaryjoin='FinancialInterestRole.agreement_role_id == AgreementRole.agreement_role_id',
        back_populates='financial_interest_role'
    )

    insured = relationship(
        'Insured',
        primaryjoin='FinancialInterestRole.financial_interest_role_id == Insured.financial_interest_role_id',
        back_populates='financial_interest_role'
    )

    insurer = relationship(
        'Insurer',
        primaryjoin='FinancialInterestRole.financial_interest_role_id == Insurer.financial_interest_role_id',
        back_populates='financial_interest_role'
    )

    additional_interest = relationship(
        'AdditionalInterest',
        primaryjoin='FinancialInterestRole.financial_interest_role_id == AdditionalInterest.financial_interest_role_id',
        back_populates='financial_interest_role'
    )

    def __repr__(self):
        return "<FinancialInterestRole(" \
               "agreement_role_id='%s'" \
               ")>" % (
                   self.agreement_role_id
               )


class Insured(Base):
    __tablename__ = 'insured'

    insured_id = Column(
        Integer,
        primary_key=True
    )

    financial_interest_role_id = Column(
        Integer,
        ForeignKey('financial_interest_role.financial_interest_role_id')
    )

    financial_interest_role = relationship(
        'FinancialInterestRole',
        primaryjoin='Insured.financial_interest_role_id == FinancialInterestRole.financial_interest_role_id',
        back_populates='insured'
    )

    def __repr__(self):
        return "<Insured(" \
               "financial_interest_role_id='%s'" \
               ")>" % (
                   self.financial_interest_role_id
               )


class Insurer(Base):
    __tablename__ = 'insurer'

    insurer_id = Column(
        Integer,
        primary_key=True
    )

    financial_interest_role_id = Column(
        Integer,
        ForeignKey('financial_interest_role.financial_interest_role_id')
    )

    financial_interest_role = relationship(
        'FinancialInterestRole',
        primaryjoin='Insurer.financial_interest_role_id == FinancialInterestRole.financial_interest_role_id',
        back_populates='insurer'
    )

    def __repr__(self):
        return "<Insurer(" \
               "financial_interest_role_id='%s'" \
               ")>" % (
                   self.financial_interest_role_id
               )


class AdditionalInterest(Base):
    __tablename__ = 'additional_interest'

    additional_interest_id = Column(
        Integer,
        primary_key=True
    )

    financial_interest_role_id = Column(
        Integer,
        ForeignKey('financial_interest_role.financial_interest_role_id')
    )

    financial_interest_role = relationship(
        'FinancialInterestRole',
        primaryjoin='AdditionalInterest.financial_interest_role_id == FinancialInterestRole.financial_interest_role_id',
        back_populates='additional_interest'
    )

    def __repr__(self):
        return "<AdditionalInterest(" \
               "financial_interest_role_id='%s'" \
               ")>" % (
                   self.financial_interest_role_id
               )
