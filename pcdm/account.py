from sqlalchemy import Column, Integer, Date, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class AccountPartyRole(Base):
    __tablename__ = 'account_party_role'

    account_party_role_id = Column(
        Integer,
        primary_key=True
    )

    account_id = Column(
        Integer,
        ForeignKey('account.account_id')
    )

    party_role_code = Column(
        String,
        ForeignKey('party_role.party_role_code')
    )

    party_id = Column(
        Integer,
        ForeignKey('party.party_id')
    )

    account = relationship(
        'Account',
        primaryjoin='AccountPartyRole.account_id == Account.account_id',
        back_populates='account_party_role'
    )

    party = relationship(
        'Party',
        primaryjoin='AccountPartyRole.party_id == Party.party_id',
        back_populates='account_party_role'
    )

    party_role = relationship(
        'PartyRole',
        primaryjoin='AccountPartyRole.party_role_code == PartyRole.party_role_code',
        back_populates='account_party_role'
    )

    def __repr__(self):
        return "<AccountPartyRole(" \
               "account_id='%s', " \
               "party_id='%s', " \
               "party_role_code='%s'"\
               ")>" % (
                   self.account_id,
                   self.party_id,
                   self.party_role_code
                )


class Account(Base):
    __tablename__ = 'account'

    account_id = Column(
        Integer,
        primary_key=True
    )

    account_type_code = Column(Integer)

    account_name = Column(String)

    account_party_role = relationship(
        'AccountPartyRole',
        primaryjoin='Account.account_id == AccountPartyRole.account_id',
        back_populates='account'
    )

    account_agreement = relationship(
        'AccountAgreement',
        primaryjoin='Account.account_id == AccountAgreement.account_id',
        back_populates='account'
    )

    insured_account = relationship(
        'InsuredAccount',
        primaryjoin='Account.account_id == InsuredAccount.account_id',
        back_populates='account'
    )

    def __repr__(self):
        return "<Account(" \
               "account_type_code='%s', " \
               "account_name='%s'" \
               ")>" % (
                   self.account_type_code,
                   self.account_name,
                )


class AccountAgreement(Base):
    __tablename__ = 'account_agreement'

    account_agreement_id = Column(
        Integer,
        primary_key=True
    )

    account_id = Column(
        Integer,
        ForeignKey('account.account_id')
    )

    agreement_id = Column(
        Integer,
        ForeignKey('agreement.agreement_id')
    )

    account = relationship(
        'Account',
        primaryjoin='AccountAgreement.account_id == Account.account_id',
        back_populates='account_agreement'
    )

    agreement = relationship(
        'Agreement',
        primaryjoin='AccountAgreement.agreement_id == Agreement.agreement_id',
        back_populates='account_agreement'
    )

    def __repr__(self):
        return "<AccountAgreement(" \
               "account_id='%s', " \
               "agreement_id='%s' " \
               ")>" % (
                   self.account_id,
                   self.agreement_id
                )


class InsuredAccount(Base):
    __tablename__ = 'insured_account'

    insured_account_id = Column(
        Integer,
        primary_key=True
    )

    account_id = Column(
        Integer,
        ForeignKey('account.account_id')
    )

    account = relationship(
        'Account',
        primaryjoin='InsuredAccount.account_id == Account.account_id',
        back_populates='insured_account'
    )

    def __repr__(self):
        return "<InsuredAccount(" \
               "account_id='%s'" \
               ")>" % (
                   self.account_id
                )


class Provider(Base):
    __tablename__ = 'provider'

    provider_id = Column(
        Integer,
        primary_key=True
    )

    party_role_code = Column(
        String,
        ForeignKey('party_role.party_role_code')
    )

    party_role = relationship(
        'PartyRole',
        primaryjoin='Provider.party_role_code == PartyRole.party_role_code',
        back_populates='provider'
    )

    financial_service = relationship(
        'FinancialService',
        primaryjoin='Provider.party_role_code == FinancialService.party_role_code',
        back_populates='provider'
    )

    def __repr__(self):
        return "<Provider(" \
               "party_role_code='%s'" \
               ")>" % (
                   self.party_role_code
                )


class AccountRole(Base):
    __tablename__ = 'account_role'

    account_role_id = Column(
        Integer,
        primary_key=True
    )

    party_role_code = Column(
        String,
        ForeignKey('party_role.party_role_code')
    )

    party_role = relationship(
        'PartyRole',
        primaryjoin='AccountRole.party_role_code == PartyRole.party_role_code',
        back_populates='account_role'
    )

    prospect = relationship(
        'Prospect',
        primaryjoin='AccountRole.party_role_code == Prospect.party_role_code',
        back_populates='account_role'
    )

    customer = relationship(
        'Customer',
        primaryjoin='AccountRole.party_role_code == Customer.party_role_code',
        back_populates='account_role'
    )

    def __repr__(self):
        return "<AccountRole(" \
               "party_role_code='%s'" \
               ")>" % (
                   self.party_role_code
                )


class AgreementRole(Base):
    __tablename__ = 'agreement_role'

    agreement_role_id = Column(
        Integer,
        primary_key=True
    )

    party_role_code = Column(
        String,
        ForeignKey('party_role.party_role_code')
    )

    party_role = relationship(
        'PartyRole',
        primaryjoin='AgreementRole.party_role_code == PartyRole.party_role_code',
        back_populates='agreement_role'
    )

    def __repr__(self):
        return "<AgreementRole(" \
               "party_role_code='%s'" \
               ")>" % (
                   self.party_role_code
                )


class FinancialService(Base):
    __tablename__ = 'financial_service'

    financial_service_id = Column(
        Integer,
        primary_key=True
    )

    party_role_code = Column(
        String,
        ForeignKey('provider.party_role_code')
    )

    provider = relationship(
        'Provider',
        primaryjoin='FinancialService.party_role_code == Provider.party_role_code',
        back_populates='financial_service'
    )

    financial_adviser = relationship(
        'FinancialAdviser',
        primaryjoin='FinancialService.party_role_code == FinancialAdviser.party_role_code',
        back_populates='financial_service'
    )

    financial_analyst = relationship(
        'FinancialAnalyst',
        primaryjoin='FinancialService.party_role_code == FinancialAnalyst.party_role_code',
        back_populates='financial_service'
    )

    account_provider = relationship(
        'AccountProvider',
        primaryjoin='FinancialService.party_role_code == AccountProvider.party_role_code',
        back_populates='financial_service'
    )

    def __repr__(self):
        return "<FinancialService(" \
               "party_role_code='%s'" \
               ")>" % (
                   self.party_role_code
                )


class FinancialAdviser(Base):
    __tablename__ = 'financial_adviser'

    financial_service_id = Column(
        Integer,
        primary_key=True
    )

    party_role_code = Column(
        String,
        ForeignKey('financial_service.party_role_code')
    )

    financial_service = relationship(
        'Provider',
        primaryjoin='FinancialAdviser.party_role_code == FinancialService.party_role_code',
        back_populates='financial_adviser'
    )

    def __repr__(self):
        return "<FinancialAdviser(" \
               "party_role_code='%s'" \
               ")>" % (
                   self.party_role_code
                )


class FinancialAnalyst(Base):
    __tablename__ = 'financial_analyst'

    financial_analyst_id = Column(
        Integer,
        primary_key=True
    )

    party_role_code = Column(
        String,
        ForeignKey('financial_service.party_role_code')
    )

    financial_service = relationship(
        'Provider',
        primaryjoin='FinancialAnalyst.party_role_code == FinancialService.party_role_code',
        back_populates='financial_analyst'
    )

    def __repr__(self):
        return "<FinancialAnalyst(" \
               "party_role_code='%s'" \
               ")>" % (
                   self.party_role_code
                )


class AccountProvider(Base):
    __tablename__ = 'account_provider'

    account_provider_id = Column(
        Integer,
        primary_key=True
    )

    party_role_code = Column(
        String,
        ForeignKey('financial_service.party_role_code')
    )

    financial_service = relationship(
        'Provider',
        primaryjoin='AccountProvider.party_role_code == FinancialService.party_role_code',
        back_populates='account_provider'
    )

    def __repr__(self):
        return "<AccountProvider(" \
               "party_role_code='%s'" \
               ")>" % (
                   self.party_role_code
                )


class Prospect(Base):
    __tablename__ = 'prospect'

    prospect_id = Column(
        Integer,
        primary_key=True
    )

    party_role_code = Column(
        String,
        ForeignKey('account_role.party_role_code')
    )

    account_role = relationship(
        'AccountRole',
        primaryjoin='Prospect.party_role_code == AccountRole.party_role_code',
        back_populates='prospect'
    )

    def __repr__(self):
        return "<Prospect(" \
               "party_role_code='%s'" \
               ")>" % (
                   self.party_role_code
                )


class Customer(Base):
    __tablename__ = 'customer'

    prospect_id = Column(
        Integer,
        primary_key=True
    )

    party_role_code = Column(
        String,
        ForeignKey('account_role.party_role_code')
    )

    account_role = relationship(
        'AccountRole',
        primaryjoin='Customer.party_role_code == AccountRole.party_role_code',
        back_populates='customer'
    )

    def __repr__(self):
        return "<Customer(" \
               "party_role_code='%s'" \
               ")>" % (
                   self.party_role_code
                )


class Policy(Base):
    __tablename__ = 'policy'

    policy_id = Column(
        Integer,
        primary_key=True
    )

    agreement_id = Column(
        Integer,
        ForeignKey('agreement.agreement_id'),
        ForeignKey('reinsurance_agreement.agreement_id')
    )

    policy_number = Column(Integer)

    effective_date = Column(Date)

    expiration_date = Column(Date)

    status_code = Column(String)

    geographic_location_id = Column(
        Integer,
        ForeignKey('geographic_location.geographic_location_id')
    )

    agreement = relationship(
        'Agreement',
        primaryjoin='Policy.agreement_id == Agreement.agreement_id',
        back_populates='policy'
    )

    geographic_location = relationship(
        'GeographicLocation',
        primaryjoin='Policy.geographic_location_id == GeographicLocation.geographic_location_id',
        back_populates='policy'
    )

    reinsurance_agreement = relationship(
        'ReinsuranceAgreement',
        primaryjoin='Policy.agreement_id == ReinsuranceAgreement.agreement_id',
        back_populates='policy'
    )

    policy_relationship = relationship(
        'PolicyRelationship',
        primaryjoin='Policy.policy_id == PolicyRelationship.policy_id',
        back_populates='policy'
    )

    related_policy_relationship = relationship(
        'PolicyRelationship',
        primaryjoin='Policy.policy_id == PolicyRelationship.related_policy_id',
        back_populates='policy'
    )

    policy_event = relationship(
        'PolicyEvent',
        primaryjoin='Policy.policy_id == PolicyEvent.policy_id',
        back_populates='policy'
    )

    policy_coverage_part = relationship(
        'PolicyCoveragePart',
        primaryjoin='Policy.policy_id == PolicyCoveragePart.policy_id',
        back_populates='policy'
    )

    policy_coverage_detail = relationship(
        'PolicyCoverageDetail',
        primaryjoin='Policy.policy_id == PolicyCoverageDetail.policy_id',
        back_populates='policy'
    )

    policy_form = relationship(
        'PolicyForm',
        primaryjoin='Policy.policy_id == PolicyForm.policy_id',
        back_populates='policy'
    )

    policy_amount = relationship(
        'PolicyAmount',
        primaryjoin='Policy.policy_id == PolicyAmount.policy_id',
        back_populates='policy'
    )

    def __repr__(self):
        return "<Policy(" \
               "agreement_id='%s', " \
               "policy_number='%s', " \
               "effective_date='%s', "\
               "expiration_date='%s', " \
               "status_code='%s', " \
               "geographic_location_id='%s'" \
               ")>" % (
                   self.agreement_id,
                   self.policy_number,
                   self.effective_date,
                   self.expiration_date,
                   self.status_code,
                   self.geographic_location_id
                )


class ReinsuranceAgreement(Base):
    __tablename__ = 'reinsurance_agreement'

    reinsurance_agreement_id = Column(
        Integer,
        primary_key=True
    )

    agreement_id = Column(
        Integer,
        ForeignKey('policy.policy_id'),
        ForeignKey('agreement.agreement_id')
    )

    policy = relationship(
        'Policy',
        primaryjoin='ReinsuranceAgreement.agreement_id == Policy.agreement_id',
        back_populates='reinsurance_agreement'
    )

    agreement = relationship(
        'Agreement',
        primaryjoin='ReinsuranceAgreement.agreement_id == Agreement.agreement_id',
        back_populates='reinsurance_agreement'
    )

    def __repr__(self):
        return "<ReinsuranceAgreement(" \
               "agreement_id='%s', " \
               ")>" % (
                   self.agreement_id
                )


class AgencyContract(Base):
    __tablename__ = 'agency_contract'

    agency_contract_id = Column(
        Integer,
        primary_key=True
    )

    agreement_id = Column(
        Integer,
        ForeignKey('agreement.agreement_id')
    )

    agreement = relationship(
        'Agreement',
        primaryjoin='AgencyContract.agreement_id == Agreement.agreement_id',
        back_populates='agency_contract'
    )

    def __repr__(self):
        return "<AgencyContact(" \
               "agreement_id='%s', " \
               ")>" % (
                   self.agreement_id
               )


class CommercialAgreement(Base):
    __tablename__ = 'commercial_agreement'

    commercial_agreement_id = Column(
        Integer,
        primary_key=True
    )

    agreement_id = Column(
        Integer,
        ForeignKey('agreement.agreement_id')
    )

    agreement = relationship(
        'Agreement',
        primaryjoin='CommercialAgreement.agreement_id == Agreement.agreement_id',
        back_populates='commercial_agreement'
    )

    def __repr__(self):
        return "<CommercialAgreement(" \
               "agreement_id='%s', " \
               ")>" % (
                   self.agreement_id
               )


class BrokerageContract(Base):
    __tablename__ = 'brokerage_contract'

    brokerage_contract_id = Column(
        Integer,
        primary_key=True
    )

    agreement_id = Column(
        Integer,
        ForeignKey('agreement.agreement_id')
    )

    agreement = relationship(
        'Agreement',
        primaryjoin='BrokerageContract.agreement_id == Agreement.agreement_id',
        back_populates='brokerage_contract'
    )

    def __repr__(self):
        return "<BrokerageContract(" \
               "agreement_id='%s', " \
               ")>" % (
                   self.agreement_id
               )


class FinancialAccountAgreement(Base):
    __tablename__ = 'financial_account_agreement'

    financial_account_agreement_id = Column(
        Integer,
        primary_key=True
    )

    agreement_id = Column(
        Integer,
        ForeignKey('agreement.agreement_id')
    )

    agreement = relationship(
        'Agreement',
        primaryjoin='FinancialAccountAgreement.agreement_id == Agreement.agreement_id',
        back_populates='financial_account_agreement'
    )

    def __repr__(self):
        return "<FinancialAccountAgreement(" \
               "agreement_id='%s', " \
               ")>" % (
                   self.agreement_id
               )


class DerivativeContract(Base):
    __tablename__ = 'derivative_contract'

    derivative_contract_id = Column(
        Integer,
        primary_key=True
    )

    agreement_id = Column(
        Integer,
        ForeignKey('agreement.agreement_id')
    )

    agreement = relationship(
        'Agreement',
        primaryjoin='DerivativeContract.agreement_id == Agreement.agreement_id',
        back_populates='derivative_contract'
    )

    def __repr__(self):
        return "<DerivativeContract(" \
               "agreement_id='%s', " \
               ")>" % (
                   self.agreement_id
               )


class IntermediaryAgreement(Base):
    __tablename__ = 'intermediary_agreement'

    intermediary_agreement_id = Column(
        Integer,
        primary_key=True
    )

    agreement_id = Column(
        Integer,
        ForeignKey('agreement.agreement_id')
    )

    agreement = relationship(
        'Agreement',
        primaryjoin='IntermediaryAgreement.agreement_id == Agreement.agreement_id',
        back_populates='intermediary_agreement'
    )

    def __repr__(self):
        return "<IntermediaryAgreement(" \
               "agreement_id='%s', " \
               ")>" % (
                   self.agreement_id
               )


class GroupAgreement(Base):
    __tablename__ = 'group_agreement'

    group_agreement_id = Column(
        Integer,
        primary_key=True
    )

    agreement_id = Column(
        Integer,
        ForeignKey('agreement.agreement_id')
    )

    agreement = relationship(
        'Agreement',
        primaryjoin='GroupAgreement.agreement_id == Agreement.agreement_id',
        back_populates='group_agreement'
    )

    def __repr__(self):
        return "<GroupAgreement(" \
               "agreement_id='%s', " \
               ")>" % (
                   self.agreement_id
               )


class CommutationAgreement(Base):
    __tablename__ = 'commutation_agreement'

    commutation_agreement_id = Column(
        Integer,
        primary_key=True
    )

    agreement_id = Column(
        Integer,
        ForeignKey('agreement.agreement_id')
    )

    agreement = relationship(
        'Agreement',
        primaryjoin='CommutationAgreement.agreement_id == Agreement.agreement_id',
        back_populates='commutation_agreement'
    )

    def __repr__(self):
        return "<CommutationAgreement(" \
               "agreement_id='%s', " \
               ")>" % (
                   self.agreement_id
               )


class ProviderAgreement(Base):
    __tablename__ = 'provider_agreement'

    provider_agreement_id = Column(
        Integer,
        primary_key=True
    )

    agreement_id = Column(
        Integer,
        ForeignKey('agreement.agreement_id')
    )

    agreement = relationship(
        'Agreement',
        primaryjoin='ProviderAgreement.agreement_id == Agreement.agreement_id',
        back_populates='provider_agreement'
    )

    def __repr__(self):
        return "<ProviderAgreement(" \
               "agreement_id='%s', " \
               ")>" % (
                   self.agreement_id
               )


class IndividualAgreement(Base):
    __tablename__ = 'individual_agreement'

    individual_agreement_id = Column(
        Integer,
        primary_key=True
    )

    agreement_id = Column(
        Integer,
        ForeignKey('agreement.agreement_id')
    )

    agreement = relationship(
        'Agreement',
        primaryjoin='IndividualAgreement.agreement_id == Agreement.agreement_id',
        back_populates='individual_agreement'
    )

    def __repr__(self):
        return "<IndividualAgreement(" \
               "agreement_id='%s', " \
               ")>" % (
                   self.agreement_id
               )


class AutoRepairShopContract(Base):
    __tablename__ = 'auto_repair_shop_contract'

    auto_repair_shop_contract_id = Column(
        Integer,
        primary_key=True
    )

    agreement_id = Column(
        Integer,
        ForeignKey('agreement.agreement_id')
    )

    agreement = relationship(
        'Agreement',
        primaryjoin='AutoRepairShopContract.agreement_id == Agreement.agreement_id',
        back_populates='auto_repair_shop_contract'
    )

    def __repr__(self):
        return "<AutoRepairShopContract(" \
               "agreement_id='%s', " \
               ")>" % (
                   self.agreement_id
               )


class StaffingAgreement(Base):
    __tablename__ = 'staffing_agreement'

    staffing_agreement_id = Column(
        Integer,
        primary_key=True
    )

    agreement_id = Column(
        Integer,
        ForeignKey('agreement.agreement_id')
    )

    agreement = relationship(
        'Agreement',
        primaryjoin='StaffingAgreement.agreement_id == Agreement.agreement_id',
        back_populates='staffing_agreement'
    )

    def __repr__(self):
        return "<StaffingAgreement(" \
               "agreement_id='%s', " \
               ")>" % (
                   self.agreement_id
               )
