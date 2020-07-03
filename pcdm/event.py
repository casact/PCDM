from sqlalchemy import Column, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class BusinessEvent(Base):
    __tablename__ = 'business_event'

    business_event_id = Column(
        Integer,
        primary_key=True
    )

    event_id = Column(
        Integer,
        ForeignKey('event.event_id')
    )

    event = relationship(
        'Event',
        primaryjoin='BusinessEvent.event_id == Event.event_id',
        back_populates='business_event'
    )

    def __repr__(self):
        return "<BusinessEvent(" \
               "event_id='%s'" \
               ")>" % (
                   self.event_id
                )


class LifeEvent(Base):
    __tablename__ = 'life_event'

    life_event_id = Column(
        Integer,
        primary_key=True
    )

    event_id = Column(
        Integer,
        ForeignKey('event.event_id')
    )

    event = relationship(
        'Event',
        primaryjoin='LifeEvent.event_id == Event.event_id',
        back_populates='life_event'
    )

    def __repr__(self):
        return "<LifeEvent(" \
               "event_id='%s'" \
               ")>" % (
                   self.event_id
                )


class ClaimEvent(Base):
    __tablename__ = 'claim_event'

    claim_event_id = Column(
        Integer,
        primary_key=True
    )

    event_id = Column(
        Integer,
        ForeignKey('event.event_id')
    )

    event = relationship(
        'Event',
        primaryjoin='ClaimEvent.event_id == Event.event_id',
        back_populates='claim_event'
    )

    def __repr__(self):
        return "<ClaimEvent(" \
               "event_id='%s'" \
               ")>" % (
                   self.event_id
                )


class PreQualification(Base):
    __tablename__ = 'pre_qualification'

    pre_qualification_id = Column(
        Integer,
        primary_key=True
    )

    policy_event_id = Column(
        Integer,
        ForeignKey('policy_event.policy_event_id')
    )

    policy_event = relationship(
        'PolicyEvent',
        primaryjoin='PreQualification.policy_event_id == PolicyEvent.policy_event_id',
        back_populates='pre_qualification'
    )

    def __repr__(self):
        return "<PreQualification(" \
               "policy_event_id='%s'" \
               ")>" % (
                   self.policy_event_id
                )


class Quote(Base):
    __tablename__ = 'quote'

    quote_id = Column(
        Integer,
        primary_key=True
    )

    policy_event_id = Column(
        Integer,
        ForeignKey('policy_event.policy_event_id')
    )

    policy_event = relationship(
        'PolicyEvent',
        primaryjoin='Quote.policy_event_id == PolicyEvent.policy_event_id',
        back_populates='quote_id'
    )

    def __repr__(self):
        return "<Quote(" \
               "policy_event_id='%s'" \
               ")>" % (
                   self.policy_event_id
               )


class Binding(Base):
    __tablename__ = 'binding'

    binding_id = Column(
        Integer,
        primary_key=True
    )

    policy_event_id = Column(
        Integer,
        ForeignKey('policy_event.policy_event_id')
    )

    policy_event = relationship(
        'PolicyEvent',
        primaryjoin='Binding.policy_event_id == PolicyEvent.policy_event_id',
        back_populates='binding'
    )

    def __repr__(self):
        return "<Binding(" \
               "policy_event_id='%s'" \
               ")>" % (
                   self.policy_event_id
               )


class NewBusiness(Base):
    __tablename__ = 'new_business'

    new_business_id = Column(
        Integer,
        primary_key=True
    )

    policy_event_id = Column(
        Integer,
        ForeignKey('policy_event.policy_event_id')
    )

    policy_event = relationship(
        'PolicyEvent',
        primaryjoin='NewBusiness.policy_event_id == PolicyEvent.policy_event_id',
        back_populates='new_business'
    )

    def __repr__(self):
        return "<NewBusiness(" \
               "policy_event_id='%s'" \
               ")>" % (
                   self.policy_event_id
               )


class Endorsement(Base):
    __tablename__ = 'endorsement'

    endorsement_id = Column(
        Integer,
        primary_key=True
    )

    policy_event_id = Column(
        Integer,
        ForeignKey('policy_event.policy_event_id')
    )

    policy_event = relationship(
        'PolicyEvent',
        primaryjoin='Endorsement.policy_event_id == PolicyEvent.policy_event_id',
        back_populates='endorsement'
    )

    full_term = relationship(
        'FullTerm',
        primaryjoin='Endorsement.endorsement_id == FullTerm.endorsement_id',
        back_populates='endorsement'
    )

    mid_term = relationship(
        'MidTerm',
        primaryjoin='Endorsement.endorsement_id == MidTerm.endorsement_id',
        back_populates='endorsement'
    )

    audit = relationship(
        'Audit',
        primaryjoin='Endorsement.endorsement_id == Audit.endorsement_id',
        back_populates='endorsement'
    )

    def __repr__(self):
        return "<Endorsement(" \
               "policy_event_id='%s'" \
               ")>" % (
                   self.policy_event_id
               )


class FullTerm(Base):
    __tablename__ = 'full_term'

    full_term_id = Column(
        Integer,
        primary_key=True
    )

    endorsement_id = Column(
        Integer,
        ForeignKey('endorsement.endorsement_id')
    )

    endorsement = relationship(
        'Endorsement',
        primaryjoin='FullTerm.endorsement_id == Endorsement.endorsement_id',
        back_populates='full_term'
    )

    def __repr__(self):
        return "<FullTerm(" \
               "endorsement_id='%s'" \
               ")>" % (
                   self.endorsement_id
               )


class MidTerm(Base):
    __tablename__ = 'mid_term'

    mid_term_id = Column(
        Integer,
        primary_key=True
    )

    endorsement_id = Column(
        Integer,
        ForeignKey('endorsement.endorsement_id')
    )

    endorsement = relationship(
        'Endorsement',
        primaryjoin='MidTerm.endorsement_id == Endorsement.endorsement_id',
        back_populates='mid_term'
    )

    def __repr__(self):
        return "<MidTerm(" \
               "endorsement_id='%s'" \
               ")>" % (
                   self.endorsement_id
               )


class Audit(Base):
    __tablename__ = 'audit'

    audit_id = Column(
        Integer,
        primary_key=True
    )

    endorsement_id = Column(
        Integer,
        ForeignKey('endorsement.endorsement_id')
    )

    endorsement = relationship(
        'Endorsement',
        primaryjoin='Audit.endorsement_id == Endorsement.endorsement_id',
        back_populates='audit'
    )

    def __repr__(self):
        return "<Audit(" \
               "endorsement_id='%s'" \
               ")>" % (
                   self.endorsement_id
               )


class Cancel(Base):
    __tablename__ = 'cancel'

    cancel_id = Column(
        Integer,
        primary_key=True
    )

    policy_event_id = Column(
        Integer,
        ForeignKey('policy_event.policy_event_id')
    )

    policy_event = relationship(
        'PolicyEvent',
        primaryjoin='Cancel.policy_event_id == PolicyEvent.policy_event_id',
        back_populates='cancel'
    )

    pro_rata = relationship(
        'ProRata',
        primaryjoin='Cancel.cancel_id == ProRata.cancel_id',
        back_populates='cancel'
    )

    short_rate = relationship(
        'ShortRate',
        primaryjoin='Cancel.cancel_id == ShortRate.cancel_id',
        back_populates='cancel'
    )

    flat = relationship(
        'Flat',
        primaryjoin='Cancel.cancel_id == Flat.cancel_id',
        back_populates='cancel'
    )

    def __repr__(self):
        return "<Cancel(" \
               "policy_event_id='%s'" \
               ")>" % (
                   self.policy_event_id
               )


class ProRata(Base):
    __tablename__ = 'pro_rata'

    pro_rata_id = Column(
        Integer,
        primary_key=True
    )

    cancel_id = Column(
        Integer,
        ForeignKey('cancel.cancel_id')
    )

    cancel = relationship(
        'Cancel',
        primaryjoin='ProRata.cancel_id == Cancel.cancel_id',
        back_populates='pro_rata'
    )

    def __repr__(self):
        return "<ProRata(" \
               "cancel_id='%s'" \
               ")>" % (
                   self.cancel_id
               )


class ShortRate(Base):
    __tablename__ = 'short_rate'

    short_rate_id = Column(
        Integer,
        primary_key=True
    )

    cancel_id = Column(
        Integer,
        ForeignKey('cancel.cancel_id')
    )

    cancel = relationship(
        'Cancel',
        primaryjoin='ShortRate.cancel_id == Cancel.cancel_id',
        back_populates='short_rate'
    )

    def __repr__(self):
        return "<ShortRate(" \
               "cancel_id='%s'" \
               ")>" % (
                   self.cancel_id
               )


class Flat(Base):
    __tablename__ = 'flat'

    flat_id = Column(
        Integer,
        primary_key=True
    )

    cancel_id = Column(
        Integer,
        ForeignKey('cancel.cancel_id')
    )

    cancel = relationship(
        'Cancel',
        primaryjoin='Flat.cancel_id == Cancel.cancel_id',
        back_populates='flat'
    )

    def __repr__(self):
        return "<Flat(" \
               "cancel_id='%s'" \
               ")>" % (
                   self.cancel_id
               )


class Reinstatement(Base):
    __tablename__ = 'reinstatement'

    reinstatement_id = Column(
        Integer,
        primary_key=True
    )

    policy_event_id = Column(
        Integer,
        ForeignKey('policy_event.policy_event_id')
    )

    policy_event = relationship(
        'PolicyEvent',
        primaryjoin='Reinstatement.policy_event_id == PolicyEvent.policy_event_id',
        back_populates='reinstatement'
    )

    def __repr__(self):
        return "<Reinstatement(" \
               "policy_event_id='%s'" \
               ")>" % (
                   self.policy_event_id
               )


class Renewal(Base):
    __tablename__ = 'renewal'

    renewal_id = Column(
        Integer,
        primary_key=True
    )

    policy_event_id = Column(
        Integer,
        ForeignKey('policy_event.policy_event_id')
    )

    policy_event = relationship(
        'PolicyEvent',
        primaryjoin='Renewal.policy_event_id == PolicyEvent.policy_event_id',
        back_populates='renewal'
    )

    def __repr__(self):
        return "<Renewal(" \
               "policy_event_id='%s'" \
               ")>" % (
                   self.policy_event_id
               )
