from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Attorney(Base):
    __tablename__ = 'attorney'

    attorney_id = Column(
        Integer,
        primary_key=True
    )

    provider_id = Column(
        Integer,
        ForeignKey('provider.provider_id')
    )

    provider = relationship(
        'Provider',
        primaryjoin='Attorney.provider_id == Provider.provider_Id',
        back_populates='attorney'
    )

    def __repr__(self):
        return "<Attorney(" \
               "provider_id='%s'" \
               ")>" % (
                   self.provider_id
                )


class ClaimRole(Base):
    __tablename__ = 'claim_role'

    claim_role_id = Column(
        Integer,
        primary_key=True
    )

    party_role_code = Column(
        String,
        ForeignKey('party_role.party_role_code')
    )

    party_role = relationship(
        'PartyRole',
        primaryjoin='ClaimRole.party_role_code == PartyRole.party_role_code',
        back_populates='claim_role'
    )

    claimant = relationship(
        'Claimant',
        primaryjoin='ClaimRole.claim_role_id == Claimant.claim_role_id',
        back_populates='claim_role'
    )

    claim_representative = relationship(
        'ClaimRepresentative',
        primaryjoin='ClaimRole.claim_role_id == ClaimRepresentative.claim_role_id',
        back_populates='claim_role'
    )

    claim_examiner = relationship(
        'ClaimExaminer',
        primaryjoin='ClaimRole.claim_role_id == ClaimExaminer.claim_role_id',
        back_populates='claim_role'
    )

    victim = relationship(
        'Victim',
        primaryjoin='ClaimRole.claim_role_id == Victim.claim_role_id',
        back_populates='claim_role'
    )

    claim_witness = relationship(
        'ClaimWitness',
        primaryjoin='ClaimRole.claim_role_id == ClaimWitness.claim_role_id',
        back_populates='claim_role'
    )

    claim_administrator = relationship(
        'ClaimAdministrator',
        primaryjoin='ClaimRole.claim_role_id == ClaimAdministrator.claim_role_id',
        back_populates='claim_role'
    )

    claimee = relationship(
        'Claimee',
        primaryjoin='ClaimRole.claim_role_id == Claimee.claim_role_id',
        back_populates='claim_role'
    )

    claim_legal_expert = relationship(
        'ClaimLegalExpert',
        primaryjoin='ClaimRole.claim_role_id == ClaimLegalExpert.claim_role_id',
        back_populates='claim_role'
    )

    loss_payee = relationship(
        'LossPayee',
        primaryjoin='ClaimRole.claim_role_id == LossPayee.claim_role_id',
        back_populates='claim_role'
    )

    claim_expert = relationship(
        'ClaimExpert',
        primaryjoin='ClaimRole.claim_role_id == ClaimExpert.claim_role_id',
        back_populates='claim_role'
    )

    claim_fraud_examiner = relationship(
        'ClaimFraudExaminer',
        primaryjoin='ClaimRole.claim_role_id == ClaimFraudExaminer.claim_role_id',
        back_populates='claim_role'
    )

    driver = relationship(
        'Driver',
        primaryjoin='ClaimRole.claim_role_id == Driver.claim_role_id',
        back_populates='claim_role'
    )

    patient = relationship(
        'Patient',
        primaryjoin='ClaimRole.claim_role_id == Patient.claim_role_id',
        back_populates='claim_role'
    )

    def __repr__(self):
        return "<ClaimRole(" \
               "party_role_code='%s'" \
               ")>" % (
                   self.party_role_code
                )


class Claimant(Base):
    __tablename__ = 'claimant'

    claimant_id = Column(
        Integer,
        primary_key=True
    )

    claim_role_id = Column(
        Integer,
        ForeignKey('claim_role.claim_role_id')
    )

    claim_role = relationship(
        'ClaimRole',
        primaryjoin='Claimant.claim_role_id == ClaimRole.claim_role_id',
        back_populates='claimant'
    )

    def __repr__(self):
        return "<Claimant(" \
               "claim_role_id='%s'" \
               ")>" % (
                   self.claim_role_id
                )


class ClaimRepresentative(Base):
    __tablename__ = 'claim_representative'

    claim_representative_id = Column(
        Integer,
        primary_key=True
    )

    claim_role_id = Column(
        Integer,
        ForeignKey('claim_role.claim_role_id')
    )

    claim_role = relationship(
        'ClaimRole',
        primaryjoin='ClaimRepresentative.claim_role_id == ClaimRole.claim_role_id',
        back_populates='claim_representative'
    )

    def __repr__(self):
        return "<ClaimRepresentative(" \
               "claim_role_id='%s'" \
               ")>" % (
                   self.claim_role_id
               )


class ClaimExaminer(Base):
    __tablename__ = 'claim_examiner'

    claim_examiner_id = Column(
        Integer,
        primary_key=True
    )

    claim_role_id = Column(
        Integer,
        ForeignKey('claim_role.claim_role_id')
    )

    claim_role = relationship(
        'ClaimRole',
        primaryjoin='ClaimExaminer.claim_role_id == ClaimRole.claim_role_id',
        back_populates='claim_examiner'
    )

    def __repr__(self):
        return "<ClaimExaminer(" \
               "claim_role_id='%s'" \
               ")>" % (
                   self.claim_role_id
               )


class Victim(Base):
    __tablename__ = 'victim'

    victim_id = Column(
        Integer,
        primary_key=True
    )

    claim_role_id = Column(
        Integer,
        ForeignKey('claim_role.claim_role_id')
    )

    claim_role = relationship(
        'ClaimRole',
        primaryjoin='Victim.claim_role_id == ClaimRole.claim_role_id',
        back_populates='victim'
    )

    def __repr__(self):
        return "<Victim(" \
               "claim_role_id='%s'" \
               ")>" % (
                   self.claim_role_id
               )


class ClaimWitness(Base):
    __tablename__ = 'claim_witness'

    claim_witness_id = Column(
        Integer,
        primary_key=True
    )

    claim_role_id = Column(
        Integer,
        ForeignKey('claim_role.claim_role_id')
    )

    claim_role = relationship(
        'ClaimRole',
        primaryjoin='ClaimWitness.claim_role_id == ClaimRole.claim_role_id',
        back_populates='claim_witness'
    )

    def __repr__(self):
        return "<ClaimWitness(" \
               "claim_role_id='%s'" \
               ")>" % (
                   self.claim_role_id
               )


class ClaimAdministrator(Base):
    __tablename__ = 'claim_administrator'

    claim_administrator_id = Column(
        Integer,
        primary_key=True
    )

    claim_role_id = Column(
        Integer,
        ForeignKey('claim_role.claim_role_id')
    )

    claim_role = relationship(
        'ClaimRole',
        primaryjoin='ClaimAdministrator.claim_role_id == ClaimRole.claim_role_id',
        back_populates='claim_administrator'
    )

    def __repr__(self):
        return "<ClaimAdministrator(" \
               "claim_role_id='%s'" \
               ")>" % (
                   self.claim_role_id
               )


class Claimee(Base):
    __tablename__ = 'claimee'

    claimee_id = Column(
        Integer,
        primary_key=True
    )

    claim_role_id = Column(
        Integer,
        ForeignKey('claim_role.claim_role_id')
    )

    claim_role = relationship(
        'ClaimRole',
        primaryjoin='Claimee.claim_role_id == ClaimRole.claim_role_id',
        back_populates='claimee'
    )

    def __repr__(self):
        return "<Claimee(" \
               "claim_role_id='%s'" \
               ")>" % (
                   self.claim_role_id
               )


class ClaimLegalExpert(Base):
    __tablename__ = 'claim_legal_expert'

    claim_legal_expert_id = Column(
        Integer,
        primary_key=True
    )

    claim_role_id = Column(
        Integer,
        ForeignKey('claim_role.claim_role_id')
    )

    claim_role = relationship(
        'ClaimRole',
        primaryjoin='ClaimLegalExpert.claim_role_id == ClaimRole.claim_role_id',
        back_populates='claim_legal_expert'
    )

    def __repr__(self):
        return "<ClaimLegalExpert(" \
               "claim_role_id='%s'" \
               ")>" % (
                   self.claim_role_id
               )


class LossPayee(Base):
    __tablename__ = 'loss_payee'

    loss_payee_id = Column(
        Integer,
        primary_key=True
    )

    claim_role_id = Column(
        Integer,
        ForeignKey('claim_role.claim_role_id')
    )

    claim_role = relationship(
        'ClaimRole',
        primaryjoin='LossPayee.claim_role_id == ClaimRole.claim_role_id',
        back_populates='loss_payee'
    )

    def __repr__(self):
        return "<LossPayee(" \
               "claim_role_id='%s'" \
               ")>" % (
                   self.claim_role_id
               )


class ClaimExpert(Base):
    __tablename__ = 'claim_expert'

    claim_expert_id = Column(
        Integer,
        primary_key=True
    )

    claim_role_id = Column(
        Integer,
        ForeignKey('claim_role.claim_role_id')
    )

    claim_role = relationship(
        'ClaimRole',
        primaryjoin='ClaimExpert.claim_role_id == ClaimRole.claim_role_id',
        back_populates='claim_expert'
    )

    def __repr__(self):
        return "<ClaimExpert(" \
               "claim_role_id='%s'" \
               ")>" % (
                   self.claim_role_id
               )


class ClaimFraudExaminer(Base):
    __tablename__ = 'claim_fraud_examiner'

    claim_fraud_examiner_id = Column(
        Integer,
        primary_key=True
    )

    claim_role_id = Column(
        Integer,
        ForeignKey('claim_role.claim_role_id')
    )

    claim_role = relationship(
        'ClaimRole',
        primaryjoin='ClaimFraudExaminer.claim_role_id == ClaimRole.claim_role_id',
        back_populates='claim_fraud_examiner'
    )

    def __repr__(self):
        return "<ClaimFraudExaminer(" \
               "claim_role_id='%s'" \
               ")>" % (
                   self.claim_role_id
               )


class Driver(Base):
    __tablename__ = 'driver'

    driver_id = Column(
        Integer,
        primary_key=True
    )

    claim_role_id = Column(
        Integer,
        ForeignKey('claim_role.claim_role_id')
    )

    claim_role = relationship(
        'ClaimRole',
        primaryjoin='Driver.claim_role_id == ClaimRole.claim_role_id',
        back_populates='driver'
    )

    def __repr__(self):
        return "<Driver(" \
               "claim_role_id='%s'" \
               ")>" % (
                   self.claim_role_id
               )


class Patient(Base):
    __tablename__ = 'patient'

    patient_id = Column(
        Integer,
        primary_key=True
    )

    claim_role_id = Column(
        Integer,
        ForeignKey('claim_role.claim_role_id')
    )

    claim_role = relationship(
        'ClaimRole',
        primaryjoin='Patient.claim_role_id == ClaimRole.claim_role_id',
        back_populates='patient'
    )

    inpatient = relationship(
        'Inpatient',
        primaryjoin='Patient.patient_id == Inpatient.patient_id',
        back_populates='patient'
    )

    outpatient = relationship(
        'Outpatient',
        primaryjoin='Patient.patient_id == Outpatient.patient_id',
        back_populates='inpatient'
    )

    def __repr__(self):
        return "<Patient(" \
               "claim_role_id='%s'" \
               ")>" % (
                   self.claim_role_id
               )


class Inpatient(Base):
    __tablename__ = 'inpatient'

    inpatient_id = Column(
        Integer,
        primary_key=True
    )

    patient_id = Column(
        Integer,
        ForeignKey('patient.patient_id')
    )

    patient = relationship(
        'Patient',
        primaryjoin='Inpatient.patient_id == Patient.patient_id',
        back_populates='inpatient'
    )

    def __repr__(self):
        return "<Inpatient(" \
               "patient_id='%s'" \
               ")>" % (
                   self.patient_id
               )


class Outpatient(Base):
    __tablename__ = 'outpatient'

    outpatient_id = Column(
        Integer,
        primary_key=True
    )

    patient_id = Column(
        Integer,
        ForeignKey('patient.patient_id')
    )

    patient = relationship(
        'Patient',
        primaryjoin='Outpatient.patient_id == Patient.patient_id',
        back_populates='outpatient'
    )

    def __repr__(self):
        return "<Outpatient(" \
               "patient_id='%s'" \
               ")>" % (
                   self.patient_id
               )


class Adjuster(Base):
    __tablename__ = 'adjuster'

    adjuster_id = Column(
        Integer,
        primary_key=True
    )

    party_role_code = Column(
        String,
        ForeignKey('party_role.party_role_code')
    )

    party_role = relationship(
        'PartyRole',
        primaryjoin='Adjuster.party_role_code == PartyRole.party_role_code',
        back_populates='adjuster'
    )

    inhouse_adjuster = relationship(
        'InhouseAdjuster',
        primaryjoin='Adjuster.adjuster_id == InhouseAdjuster.adjuster_id',
        back_populates='adjuster'
    )

    public_adjuster = relationship(
        'PublicAdjuster',
        primaryjoin='Adjuster.adjuster_id == PublicAdjuster.adjuster_id',
        back_populates='adjuster'
    )

    independent_adjuster = relationship(
        'IndependentAdjuster',
        primaryjoin='Adjuster.adjuster_id == IndependentAdjuster.adjuster_id',
        back_populates='adjuster'
    )

    def __repr__(self):
        return "<Adjuster(" \
               "party_role_code='%s'" \
               ")>" % (
                   self.party_role_code
               )


class InhouseAdjuster(Base):
    __tablename__ = 'inhouse_adjuster'

    inhouse_adjuster_id = Column(
        Integer,
        primary_key=True
    )

    adjuster_id = Column(
        Integer,
        ForeignKey('adjuster.adjuster_id')
    )

    adjuster = relationship(
        'Adjuster',
        primaryjoin='InhouseAdjuster.adjuster_id == Adjuster.adjuster_id',
        back_populates='inhouse_adjuster'
    )

    def __repr__(self):
        return "<InhouseAdjuster(" \
               "adjuster_id='%s'" \
               ")>" % (
                   self.adjuster_id
               )


class PublicAdjuster(Base):
    __tablename__ = 'public_adjuster'

    public_adjuster_id = Column(
        Integer,
        primary_key=True
    )

    adjuster_id = Column(
        Integer,
        ForeignKey('adjuster.adjuster_id')
    )

    adjuster = relationship(
        'Adjuster',
        primaryjoin='PublicAdjuster.adjuster_id == Adjuster.adjuster_id',
        back_populates='public_adjuster'
    )

    def __repr__(self):
        return "<PublicAdjuster(" \
               "adjuster_id='%s'" \
               ")>" % (
                   self.adjuster_id
               )


class IndependentAdjuster(Base):
    __tablename__ = 'independent_adjuster'

    independent_adjuster_id = Column(
        Integer,
        primary_key=True
    )

    adjuster_id = Column(
        Integer,
        ForeignKey('adjuster.adjuster_id')
    )

    adjuster = relationship(
        'Adjuster',
        primaryjoin='IndependentAdjuster.adjuster_id == Adjuster.adjuster_id',
        back_populates='independent_adjuster'
    )

    def __repr__(self):
        return "<IndependentAdjuster(" \
               "adjuster_id='%s'" \
               ")>" % (
                   self.adjuster_id
               )
