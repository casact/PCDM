from sqlalchemy import Column, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Premium(Base):
    __tablename__ = 'premium'

    premium_id = Column(
        Integer,
        primary_key=True
    )

    policy_amount_id = Column(
        Integer,
        ForeignKey('policy_amount.policy_amount_id')
    )

    policy_amount = relationship(
        'PolicyAmount',
        primaryjoin='Premium.policy_amount_id == PolicyAmount.policy_amount_id',
        back_populates='premium'
    )

    def __repr__(self):
        return "<Premium(" \
               "policy_amount_id='%s'" \
               ")>" % (
                   self.policy_amount_id
                )


class Tax(Base):
    __tablename__ = 'tax'

    tax_id = Column(
        Integer,
        primary_key=True
    )

    policy_amount_id = Column(
        Integer,
        ForeignKey('policy_amount.policy_amount_id')
    )

    policy_amount = relationship(
        'PolicyAmount',
        primaryjoin='Tax.policy_amount_id == PolicyAmount.policy_amount_id',
        back_populates='tax'
    )

    def __repr__(self):
        return "<Tax(" \
               "policy_amount_id='%s'" \
               ")>" % (
                   self.policy_amount_id
                )


class Surcharge(Base):
    __tablename__ = 'surcharge'

    surcharge_id = Column(
        Integer,
        primary_key=True
    )

    policy_amount_id = Column(
        Integer,
        ForeignKey('policy_amount.policy_amount_id')
    )

    policy_amount = relationship(
        'PolicyAmount',
        primaryjoin='Surcharge.policy_amount_id == PolicyAmount.policy_amount_id',
        back_populates='surcharge'
    )

    def __repr__(self):
        return "<Surcharge(" \
               "policy_amount_id='%s'" \
               ")>" % (
                   self.policy_amount_id
                )


class Fee(Base):
    __tablename__ = 'fee'

    fee_id = Column(
        Integer,
        primary_key=True
    )

    policy_amount_id = Column(
        Integer,
        ForeignKey('policy_amount.policy_amount_id')
    )

    policy_amount = relationship(
        'PolicyAmount',
        primaryjoin='Fee.policy_amount_id == PolicyAmount.policy_amount_id',
        back_populates='fee'
    )

    def __repr__(self):
        return "<Fee(" \
               "policy_amount_id='%s'" \
               ")>" % (
                   self.policy_amount_id
                )


class DirectPolicyAmount(Base):
    __tablename__ = 'direct_policy_amount'

    direct_policy_amount_id = Column(
        Integer,
        primary_key=True
    )

    policy_amount_id = Column(
        Integer,
        ForeignKey('policy_amount.policy_amount_id')
    )

    policy_amount = relationship(
        'PolicyAmount',
        primaryjoin='DirectPolicyAmount.policy_amount_id == PolicyAmount.policy_amount_id',
        back_populates='direct_policy_amount'
    )

    def __repr__(self):
        return "<DirectPolicyAmount(" \
               "policy_amount_id='%s'" \
               ")>" % (
                   self.policy_amount_id
                )


class AssumedPolicyAmount(Base):
    __tablename__ = 'assumed_policy_amount'

    assumed_policy_amount_id = Column(
        Integer,
        primary_key=True
    )

    policy_amount_id = Column(
        Integer,
        ForeignKey('policy_amount.policy_amount_id')
    )

    policy_amount = relationship(
        'PolicyAmount',
        primaryjoin='AssumedPolicyAmount.policy_amount_id == PolicyAmount.policy_amount_id',
        back_populates='assumed_policy_amount'
    )

    def __repr__(self):
        return "<AssumedPolicyAmount(" \
               "policy_amount_id='%s'" \
               ")>" % (
                   self.policy_amount_id
                )


class CededPolicyAmount(Base):
    __tablename__ = 'ceded_policy_amount'

    ceded_policy_amount_id = Column(
        Integer,
        primary_key=True
    )

    policy_amount_id = Column(
        Integer,
        ForeignKey('policy_amount.policy_amount_id')
    )

    policy_amount = relationship(
        'PolicyAmount',
        primaryjoin='CededPolicyAmount.policy_amount_id == PolicyAmount.policy_amount_id',
        back_populates='ceded_policy_amount'
    )

    def __repr__(self):
        return "<CededPolicyAmount(" \
               "policy_amount_id='%s'" \
               ")>" % (
                   self.policy_amount_id
                )


class CreditPolicyAmount(Base):
    __tablename__ = 'credit_policy_amount'

    credit_policy_amount_id = Column(
        Integer,
        primary_key=True
    )

    policy_amount_id = Column(
        Integer,
        ForeignKey('policy_amount.policy_amount_id')
    )

    policy_amount = relationship(
        'PolicyAmount',
        primaryjoin='CreditPolicyAmount.policy_amount_id == PolicyAmount.policy_amount_id',
        back_populates='credit_policy_amount'
    )

    def __repr__(self):
        return "<CreditPolicyAmount(" \
               "policy_amount_id='%s'" \
               ")>" % (
                   self.policy_amount_id
                )


class DebitPolicyAmount(Base):
    __tablename__ = 'debit_policy_amount'

    debit_policy_amount_id = Column(
        Integer,
        primary_key=True
    )

    policy_amount_id = Column(
        Integer,
        ForeignKey('policy_amount.policy_amount_id')
    )

    policy_amount = relationship(
        'PolicyAmount',
        primaryjoin='DebitPolicyAmount.policy_amount_id == PolicyAmount.policy_amount_id',
        back_populates='debit_policy_amount'
    )

    def __repr__(self):
        return "<DebitPolicyAmount(" \
               "policy_amount_id='%s'" \
               ")>" % (
                   self.policy_amount_id
                )


class CreditClaimAmount(Base):
    __tablename__ = 'credit_claim_amount'

    credit_claim_amount_id = Column(
        Integer,
        primary_key=True
    )

    claim_amount_id = Column(
        Integer,
        ForeignKey('claim_amount.claim_amount_id')
    )

    claim_amount = relationship(
        'ClaimAmount',
        primaryjoin='CreditClaimAmount.claim_amount_id == ClaimAmount.claim_amount_id',
        back_populates='credit_claim_amount'
    )

    def __repr__(self):
        return "<CreditClaimAmount(" \
               "claim_amount_id='%s'" \
               ")>" % (
                   self.claim_amount_id
                )


class DebitClaimAmount(Base):
    __tablename__ = 'debit_claim_amount'

    debit_claim_amount_id = Column(
        Integer,
        primary_key=True
    )

    claim_amount_id = Column(
        Integer,
        ForeignKey('claim_amount.claim_amount_id')
    )

    claim_amount = relationship(
        'ClaimAmount',
        primaryjoin='DebitClaimAmount.claim_amount_id == ClaimAmount.claim_amount_id',
        back_populates='debit_claim_amount'
    )

    def __repr__(self):
        return "<DebitClaimAmount(" \
               "claim_amount_id='%s'" \
               ")>" % (
                   self.claim_amount_id
                )


class DirectClaimAmount(Base):
    __tablename__ = 'direct_claim_amount'

    direct_claim_amount_id = Column(
        Integer,
        primary_key=True
    )

    claim_amount_id = Column(
        Integer,
        ForeignKey('claim_amount.claim_amount_id')
    )

    claim_amount = relationship(
        'ClaimAmount',
        primaryjoin='DirectClaimAmount.claim_amount_id == ClaimAmount.claim_amount_id',
        back_populates='direct_claim_amount'
    )

    def __repr__(self):
        return "<DirectClaimAmount(" \
               "claim_amount_id='%s'" \
               ")>" % (
                   self.claim_amount_id
                )


class AssumedClaimAmount(Base):
    __tablename__ = 'assumed_claim_amount'

    assumed_claim_amount_id = Column(
        Integer,
        primary_key=True
    )

    claim_amount_id = Column(
        Integer,
        ForeignKey('claim_amount.claim_amount_id')
    )

    claim_amount = relationship(
        'ClaimAmount',
        primaryjoin='AssumedClaimAmount.claim_amount_id == ClaimAmount.claim_amount_id',
        back_populates='assumed_claim_amount'
    )

    def __repr__(self):
        return "<AssumedClaimAmount(" \
               "claim_amount_id='%s'" \
               ")>" % (
                   self.claim_amount_id
                )


class CededClaimAmount(Base):
    __tablename__ = 'ceded_claim_amount'

    ceded_claim_amount_id = Column(
        Integer,
        primary_key=True
    )

    claim_amount_id = Column(
        Integer,
        ForeignKey('claim_amount.claim_amount_id')
    )

    claim_amount = relationship(
        'ClaimAmount',
        primaryjoin='CededClaimAmount.claim_amount_id == ClaimAmount.claim_amount_id',
        back_populates='ceded_claim_amount'
    )

    def __repr__(self):
        return "<CededClaimAmount(" \
               "claim_amount_id='%s'" \
               ")>" % (
                   self.claim_amount_id
                )


class ClaimReserve(Base):
    __tablename__ = 'claim_reserve'

    claim_reserve_id = Column(
        Integer,
        primary_key=True
    )

    claim_amount_id = Column(
        Integer,
        ForeignKey('claim_amount.claim_amount_id')
    )

    claim_amount = relationship(
        'ClaimAmount',
        primaryjoin='ClaimReserve.claim_amount_id == ClaimAmount.claim_amount_id',
        back_populates='claim_reserve'
    )

    loss_reserve = relationship(
        'LossReserve',
        primaryjoin='ClaimReserve.claim_reserve_id == LossReserve.claim_reserve_id',
        back_populates='claim_reserve'
    )

    expense_reserve = relationship(
        'ExpenseReserve',
        primaryjoin='ClaimReserve.claim_reserve_id == ExpenseReserve.claim_reserve_id',
        back_populates='claim_reserve'
    )

    def __repr__(self):
        return "<ClaimReserve(" \
               "claim_amount_id='%s'" \
               ")>" % (
                   self.claim_amount_id
                )


class LossReserve(Base):
    __tablename__ = 'loss_reserve'

    loss_reserve_id = Column(
        Integer,
        primary_key=True
    )

    claim_reserve_id = Column(
        Integer,
        ForeignKey('claim_reserve.claim_reserve_id')
    )

    claim_reserve = relationship(
        'ClaimReserve',
        primaryjoin='LossReserve.claim_reserve_id == ClaimReserve.claim_reserve_id',
        back_populates='loss_reserve'
    )

    def __repr__(self):
        return "<LossReserve(" \
               "claim_reserve_id='%s'" \
               ")>" % (
                   self.claim_reserve_id
                )


class ExpenseReserve(Base):
    __tablename__ = 'expense_reserve'

    expense_reserve_id = Column(
        Integer,
        primary_key=True
    )

    claim_reserve_id = Column(
        Integer,
        ForeignKey('claim_reserve.claim_reserve_id')
    )

    claim_reserve = relationship(
        'ClaimReserve',
        primaryjoin='ExpenseReserve.claim_reserve_id == ClaimReserve.claim_reserve_id',
        back_populates='expense_reserve'
    )

    def __repr__(self):
        return "<ExpenseReserve(" \
               "claim_reserve_id='%s'" \
               ")>" % (
                   self.claim_reserve_id
               )


class ClaimPayment(Base):
    __tablename__ = 'claim_payment'

    claim_payment_id = Column(
        Integer,
        primary_key=True
    )

    claim_amount_id = Column(
        Integer,
        ForeignKey('claim_amount.claim_amount_id')
    )

    claim_amount = relationship(
        'ClaimAmount',
        primaryjoin='ClaimPayment.claim_amount_id == ClaimAmount.claim_amount_id',
        back_populates='claim_payment'
    )

    loss_payment = relationship(
        'LossPayment',
        primaryjoin='ClaimPayment.claim_payment_id == LossPayment.claim_payment_id',
        back_populates='claim_payment'
    )

    expense_payment = relationship(
        'ExpensePayment',
        primaryjoin='ClaimPayment.claim_payment_id == ExpensePayment.claim_payment_id',
        back_populates='claim_payment'
    )

    def __repr__(self):
        return "<ClaimPayment(" \
               "claim_amount_id='%s'" \
               ")>" % (
                   self.claim_amount_id
                )


class LossPayment(Base):
    __tablename__ = 'loss_payment'

    loss_payment_id = Column(
        Integer,
        primary_key=True
    )

    claim_payment_id = Column(
        Integer,
        ForeignKey('claim_payment.claim_payment_id')
    )

    claim_payment = relationship(
        'ClaimPayment',
        primaryjoin='LossPayment.claim_payment_id == ClaimPayment.claim_payment_id',
        back_populates='loss_payment'
    )

    def __repr__(self):
        return "<LossPayment(" \
               "claim_payment_id='%s'" \
               ")>" % (
                   self.claim_payment_id
                )


class ExpensePayment(Base):
    __tablename__ = 'expense_payment'

    expense_payment_id = Column(
        Integer,
        primary_key=True
    )

    claim_payment_id = Column(
        Integer,
        ForeignKey('claim_payment.claim_payment_id')
    )

    claim_payment = relationship(
        'ClaimPayment',
        primaryjoin='ExpensePayment.claim_payment_id == ClaimPayment.claim_payment_id',
        back_populates='expense_payment'
    )

    def __repr__(self):
        return "<ExpensePayment(" \
               "claim_payment_id='%s'" \
               ")>" % (
                   self.claim_payment_id
               )


class Recovery(Base):
    __tablename__ = 'recovery'

    recovery_id = Column(
        Integer,
        primary_key=True
    )

    claim_amount_id = Column(
        Integer,
        ForeignKey('claim_amount.claim_amount_id')
    )

    claim_amount = relationship(
        'ClaimAmount',
        primaryjoin='Recovery.claim_amount_id == ClaimAmount.claim_amount_id',
        back_populates='recovery'
    )

    loss_recovery = relationship(
        'LossRecovery',
        primaryjoin='Recovery.recovery_id == LossRecovery.recovery_id',
        back_populates='recovery'
    )

    salvage = relationship(
        'Salvage',
        primaryjoin='Recovery.recovery_id == Salvage.recovery_id',
        back_populates='recovery'
    )

    reinsurance_recovery = relationship(
        'ResinsuranceRecovery',
        primaryjoin='Recovery.recovery_id == ResinsuranceRecovery.recovery_id',
        back_populates='recovery'
    )

    expense_recovery = relationship(
        'ExpenseRecovery',
        primaryjoin='Recovery.recovery_id == ExpenseRecovery.recovery_id',
        back_populates='recovery'
    )

    deductible_recovery = relationship(
        'DeductibleRecovery',
        primaryjoin='Recovery.recovery_id == DeductibleRecovery.recovery_id',
        back_populates='recovery'
    )

    subrogation = relationship(
        'Subrogation',
        primaryjoin='Recovery.recovery_id == Subrogation.recovery_id',
        back_populates='recovery'
    )

    def __repr__(self):
        return "<Recovery(" \
               "claim_amount_id='%s'" \
               ")>" % (
                   self.claim_amount_id
                )


class LossRecovery(Base):
    __tablename__ = 'loss_recovery'

    loss_recovery_id = Column(
        Integer,
        primary_key=True
    )

    recovery_id = Column(
        Integer,
        ForeignKey('recovery.recovery_id')
    )

    recovery = relationship(
        'Recovery',
        primaryjoin='LossRecovery.recovery_id == Recovery.recovery_id',
        back_populates='loss_recovery'
    )

    def __repr__(self):
        return "<LossRecovery(" \
               "recovery_id='%s'" \
               ")>" % (
                   self.recovery_id
                )


class Salvage(Base):
    __tablename__ = 'salvage'

    salvage_id = Column(
        Integer,
        primary_key=True
    )

    recovery_id = Column(
        Integer,
        ForeignKey('recovery.recovery_id')
    )

    recovery = relationship(
        'Recovery',
        primaryjoin='Salvage.recovery_id == Recovery.recovery_id',
        back_populates='salvage'
    )

    def __repr__(self):
        return "<Salvage(" \
               "recovery_id='%s'" \
               ")>" % (
                   self.recovery_id
               )


class ResinsuranceRecovery(Base):
    __tablename__ = 'reinsurance_recovery'

    reinsurance_recovery_id = Column(
        Integer,
        primary_key=True
    )

    recovery_id = Column(
        Integer,
        ForeignKey('recovery.recovery_id')
    )

    recovery = relationship(
        'Recovery',
        primaryjoin='ResinsuranceRecovery.recovery_id == Recovery.recovery_id',
        back_populates='reinsurance_recovery'
    )

    def __repr__(self):
        return "<ResinsuranceRecovery(" \
               "recovery_id='%s'" \
               ")>" % (
                   self.recovery_id
               )


class ExpenseRecovery(Base):
    __tablename__ = 'expense_recovery'

    expense_recovery_id = Column(
        Integer,
        primary_key=True
    )

    recovery_id = Column(
        Integer,
        ForeignKey('recovery.recovery_id')
    )

    recovery = relationship(
        'Recovery',
        primaryjoin='ExpenseRecovery.recovery_id == Recovery.recovery_id',
        back_populates='expense_recovery'
    )

    def __repr__(self):
        return "<ExpenseRecovery(" \
               "recovery_id='%s'" \
               ")>" % (
                   self.recovery_id
               )


class DeductibleRecovery(Base):
    __tablename__ = 'deductible_recovery'

    deductible_recovery_id = Column(
        Integer,
        primary_key=True
    )

    recovery_id = Column(
        Integer,
        ForeignKey('recovery.recovery_id')
    )

    recovery = relationship(
        'Recovery',
        primaryjoin='DeductibleRecovery.recovery_id == Recovery.recovery_id',
        back_populates='deductible_recovery'
    )

    def __repr__(self):
        return "<DeductibleRecovery(" \
               "recovery_id='%s'" \
               ")>" % (
                   self.recovery_id
               )


class Subrogation(Base):
    __tablename__ = 'subrogation'

    subrogation_id = Column(
        Integer,
        primary_key=True
    )

    recovery_id = Column(
        Integer,
        ForeignKey('recovery.recovery_id')
    )

    recovery = relationship(
        'Recovery',
        primaryjoin='Subrogation.recovery_id == Recovery.recovery_id',
        back_populates='subrogation'
    )

    def __repr__(self):
        return "<Subrogation(" \
               "recovery_id='%s'" \
               ")>" % (
                   self.recovery_id
               )
