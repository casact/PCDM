from sqlalchemy import Column, Float, Integer, Date, String, Time
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Occurrence(Base):
    __tablename__ = 'occurrence'

    occurrence_id = Column(
        Integer,
        primary_key=True
    )

    catastrophic_event_indicator = Column(Integer)

    geographic_location_id = Column(
        Integer,
        ForeignKey('geographic_location.geographic_location_id')
    )

    occurrence_begin_date = Column(Date)

    occurrence_begin_time = Column(Time)

    occurrence_end_date = Column(Date)

    occurrence_end_time = Column(Time)

    occurrence_name = String

    geographic_location = relationship(
        'GeographicLocation',
        primaryjoin='Occurrence.geographic_location_id == GeographicLocation.geographic_location_id',
        back_populates='occurrence'
    )

    claim = relationship(
        'Claim',
        primaryjoin='Occurrence.occurrence_id == Claim.occurrence_id',
        back_populates='occurrence'
    )

    def __repr__(self):
        return "<Occurrence(" \
               "catastrophic_event_indicator='%s', " \
               "geographic_location_id='%s', " \
               "occurrence_begin_date='%s', "\
               "occurrence_begin_time='%s', " \
               "occurrence_end_date='%s', " \
               "occurrence_end_time='%s', " \
               "occurrence_name='%s'" \
               ")>" % (
                   self.catastrophic_event_indicator,
                   self.geographic_location_id,
                   self.occurrence_begin_date,
                   self.occurrence_begin_time,
                   self.occurrence_end_date,
                   self.occurrence_end_time,
                   self.occurrence_name
                )


class Catastrophe(Base):
    __tablename__ = 'catastrophe'

    catastrophe_id = Column(
        Integer,
        primary_key=True
    )

    catastrophe_type_code = Column(Integer)

    catastrophe_name = Column(String)

    industry_catastrophe_code = Column(Integer)

    company_catastrophe_code = Column(Integer)

    claim = relationship(
        'Claim',
        primaryjoin='Catastrophe.catastrophe_id == Claim.catastrophe_id',
        back_populates='catastrophe'
    )

    def __repr__(self):
        return "<Catastrophe(" \
               "catastrophe_type_code='%s', " \
               "catastrophe_name='%s', " \
               "industry_catastrophe_code='%s', "\
               "company_catastrophe_code='%s'" \
               ")>" % (
                   self.catastrophe_type_code,
                   self.catastrophe_name,
                   self.industry_catastrophe_code,
                   self.company_catastrophe_code
                )


class ClaimCoverage(Base):
    __tablename__ = 'claim_coverage'

    claim_coverage_id = Column(
        Integer,
        primary_key=True
    )

    claim_id = Column(
        Integer,
        ForeignKey('claim.claim_id')
    )

    policy_coverage_detail_id = Column(
        Integer,
        ForeignKey('policy_coverage_detail.policy_coverage_detail_id')
    )

    # remove effective date since can be found in policy coverage detail

    claim = relationship(
        'Claim',
        primaryjoin='ClaimCoverage.claim_id == Claim.claim_id',
        back_populates='claim_coverage'
    )

    policy_coverage_detail = relationship(
        'PolicyCoverageDetail',
        primaryjoin='ClaimCoverage.policy_coverage_detail_id == PolicyCoverageDetail.policy_coverage_detail_id',
        back_populates='claim_coverage'
    )

    def __repr__(self):
        return "<ClaimCoverage(" \
               "claim_id='%s', " \
               "policy_coverage_detail_id='%s'" \
               ")>" % (
                   self.claim_id,
                   self.policy_coverage_detail_id
                )


class ClaimAmount(Base):
    __tablename__ = 'claim_amount'

    claim_amount_id = Column(
        Integer,
        primary_key=True
    )

    claim_id = Column(
        Integer,
        ForeignKey('claim.claim_id')
    )

    claim_offer_id = Column(
        Integer,
        ForeignKey('claim_offer.claim_offer_id')
    )

    event_date = Column(Date)

    insurance_type_code = Column(Integer)

    amount_type_code = Column(Integer)

    claim_amount = Column(Float)

    claim = relationship(
        'Claim',
        primaryjoin='ClaimAmount.claim_id == Claim.claim_id',
        back_populates='claim_amount'
    )

    claim_offer = relationship(
        'ClaimOffer',
        primaryjoin='ClaimAmount.claim_offer_id == ClaimOffer.claim_offer_id',
        back_populates='claim_amount'
    )

    def __repr__(self):
        return "<ClaimAmount(" \
               "claim_id='%s', " \
               "claim_offer_id='%s', " \
               "event_date='%s', "\
               "insurance_type_code='%s', " \
               "amount_type_code='%s', " \
               "claim_amount='%s'" \
               ")>" % (
                   self.claim_id,
                   self.claim_offer_id,
                   self.event_date,
                   self.insurance_type_code,
                   self.amount_type_code,
                   self.claim_amount
                )


class ClaimOffer(Base):
    __tablename__ = 'claim_offer'

    claim_offer_id = Column(
        Integer,
        primary_key=True
    )

    claim_folder_id = Column(
        Integer,
        ForeignKey('claim_folder.claim_folder_id')
    )

    # remove claim id since can be linked via claim folder

    arbitration_id = Column(
        Integer,
        ForeignKey('arbitration.arbitration_id')
    )

    litigation_id = Column(
        Integer,
        ForeignKey('litigation.litigation_id')
    )

    settlement_offer_amount = Column(Float)

    settlement_offer_provision_description = Column(String)

    claim_amount = relationship(
        'ClaimAmount',
        primaryjoin='ClaimOffer.claim_offer_id == ClaimAmount.claim_offer_id',
        back_populates='claim_offer'
    )

    claim_folder = relationship(
        'ClaimFolder',
        primaryjoin='ClaimOffer.claim_folder_id == ClaimFolder.claim_folder_id',
        back_populates='claim_offer'
    )

    arbitration = relationship(
        'Arbitration',
        primaryjoin='ClaimOffer.arbitration_id == Arbitration.arbitration_id',
        back_populates='claim_offer'
    )

    litigation = relationship(
        'Litigation',
        primaryjoin='ClaimOffer.litigation_id == Litigation.litigation_id',
        back_populates='claim_offer'
    )

    def __repr__(self):
        return "<ClaimOffer(" \
               "claim_folder_id='%s', " \
               "arbitration_id='%s', " \
               "litigation_id='%s', "\
               "settlement_offer_amount='%s', " \
               "settlement_offer_provision_description='%s'" \
               ")>" % (
                   self.claim_folder_id,
                   self.arbitration_id,
                   self.litigation_id,
                   self.settlement_offer_amount,
                   self.settlement_offer_provision_description
                )


class ClaimFolder(Base):
    __tablename__ = 'claim_folder'

    claim_folder_id = Column(
        Integer,
        primary_key=True
    )

    claim_id = Column(
        Integer,
        ForeignKey('claim.claim_id')
    )

    claim_folder_label_name = Column(String)

    claim = relationship(
        'Claim',
        primaryjoin='ClaimFolder.claim_id == Claim.claim_id',
        back_populates='claim_folder'
    )

    claim_folder_document = relationship(
        'ClaimFolderDocument',
        primaryjoin='ClaimFolder.claim_folder_id == ClaimFolderDocument.claim_folder_id',
        back_populates='claim_folder'
    )

    claim_offer = relationship(
        'ClaimOffer',
        primaryjoin='ClaimFolder.claim_folder_id == ClaimOffer.claim_folder_id',
        back_populates='claim_offer'
    )

    def __repr__(self):
        return "<ClaimFolder(" \
               "claim_id='%s', " \
               "claim_folder_label_name='%s', " \
               ")>" % (
                   self.claim_id,
                   self.claim_folder_label_name
                )


class ClaimFolderDocument(Base):
    __tablename__ = 'claim_folder_document'

    claim_folder_document_id = Column(
        Integer,
        primary_key=True
    )

    # remove claim_id as can be found via claim folder

    claim_folder_id = Column(
        Integer,
        ForeignKey('claim_folder.claim_folder_id')
    )

    document_sequence_number = Column(Integer)

    document_link_value = Column(Integer)

    claim_folder = relationship(
        'ClaimFolder',
        primaryjoin='ClaimFolderDocument.claim_folder_id == ClaimFolder.claim_folder_id',
        back_populates='claim_folder_document'
    )

    def __repr__(self):
        return "<ClaimFolderDocument(" \
               "claim_folder_id='%s', " \
               "document_sequence_number='%s', " \
               "document_link_value='%s'" \
               ")>" % (
                   self.claim_folder_id,
                   self.document_sequence_number,
                   self.document_link_value
                )


class Arbitration(Base):
    __tablename__ = 'arbitration'

    arbitration_id = Column(
        Integer,
        primary_key=True
    )

    arbitration_description = Column(String)

    claim_offer = relationship(
        'ClaimOffer',
        primaryjoin='Arbitration.arbitration_id == ClaimOffer.arbitration_id',
        back_populates='arbitration'
    )

    arbitration_party_role = relationship(
        'ArbitrationPartyRole',
        primaryjoin='Arbitration.arbitration_id == ArbitrationPartyRole.arbitration_id',
        back_populates='arbitration'
    )

    claim_arbitration = relationship(
        'ClaimArbitration',
        primaryjoin='Arbitration.arbitration_id == ClaimArbitration.arbitration_id',
        back_populates='arbitration'
    )

    def __repr__(self):
        return "<Arbitration(" \
               "arbitration_description='%s'" \
               ")>" % (
                   self.arbitration_description
                )


class Litigation(Base):
    __tablename__ = 'litigation'

    litigation_id = Column(
        Integer,
        primary_key=True
    )

    # remove court id, can be found via court jurisdiction table

    # remove jurisdiction id, can be found via court jurisdiction table

    court_jurisdiction_id = Column(
        Integer,
        ForeignKey('court_jurisdiction.court_jurisdiction_id')
    )

    litigation_description = Column(String)

    claim_offer = relationship(
        'ClaimOffer',
        primaryjoin='Litigation.litigation_id == ClaimOffer.litigation_id',
        back_populates='litigation'
    )

    claim_litigation = relationship(
        'ClaimLitigation',
        primaryjoin='Litigation.litigation_id == ClaimLitigation.litigation_id == ',
        back_populates='litigation'
    )

    court_jurisdiction = relationship(
        'CourtJurisdiction',
        primaryjoin='Litigation.court_jurisdiction_id == CourtJurisdiction.court_jurisdiction_id',
        back_populates='litigation'
    )

    litigation_party_role = relationship(
        'LitigationPartyRole',
        primaryjoin='Litigation.litigation_id == LitigationPartyRole.litigation_id',
        back_populates='litigation'
    )

    def __repr__(self):
        return "<Litigation(" \
               "court_id='%s', " \
               "jurisdiction_id='%s', " \
               "litigation_description='%s'" \
               ")>" % (
                   self.court_id,
                   self.jurisdiction_id,
                   self.litigation_description
                )


class ArbitrationPartyRole(Base):
    __tablename__ = 'arbitration_party_role'

    arbitration_party_id = Column(
        Integer,
        primary_key=True
    )

    arbitration_id = Column(
        Integer,
        ForeignKey('arbitration.arbitration_id')
    )

    party_id = Column(
        Integer,
        ForeignKey('party.party_id')
    )

    party_role_code = Column(
        String,
        ForeignKey('party_role.party_role_code')
    )

    begin_date = Column(Date)

    claim_id = Column(
        Integer,
        ForeignKey('claim.claim_id')
    )

    end_date = Column(Date)

    arbitration = relationship(
        'Arbitration',
        primaryjoin='ArbitrationPartyRole.arbitration_id == Arbitration.arbitration_id',
        back_populates='arbitration_party_role'
    )

    party = relationship(
        'Party',
        primaryjoin='ArbitrationPartyRole.party_id == Party.party_id',
        back_populates='arbitration_party_role'
    )

    party_role = relationship(
        'PartyRole',
        primaryjoin='ArbitrationPartyRole.party_role_code == PartyRole.party_role_code',
        back_populates='arbitration_party_role'
    )

    claim = relationship(
        'Claim',
        primaryjoin='ArbitrationPartyRole.claim_id == Claim.claim_id',
        back_populates='arbitration_party_role'
    )

    def __repr__(self):
        return "<ArbitrationPartyRole(" \
               "arbitration_id='%s', " \
               "party_id='%s', " \
               "party_role_code='%s', "\
               "begin_date='%s', " \
               "claim_id='%s, '" \
               "end_date='%s'" \
               ")>" % (
                   self.arbitration_id,
                   self.party_id,
                   self.party_role_code,
                   self.begin_date,
                   self.claim_id,
                   self.end_date
                )


class ClaimLitigation(Base):
    __tablename__ = 'claim_litigation'

    claim_litigation_id = Column(
        Integer,
        primary_key=True
    )

    claim_id = Column(
        Integer,
        ForeignKey('claim.claim_id')
    )

    litigation_id = Column(
        Integer,
        ForeignKey('litigation.litigation_id')
    )

    claim = relationship(
        'Claim',
        primaryjoin='ClaimLitigation.claim_id == Claim.claim_id',
        back_populates='claim_litigation'
    )

    litigation = relationship(
        'Litigation',
        primaryjoin='ClaimLitigation.litigation_id == Litigation.litigation_id',
        back_populates='claim_litigation'
    )

    def __repr__(self):
        return "<ClaimLitigation(" \
               "claim_id='%s', " \
               "litigation_id='%s'" \
               ")>" % (
                   self.claim_id,
                   self.litigation_id
                )


class ClaimArbitration(Base):
    __tablename__ = 'claim_arbitration'

    claim_arbitration_id = Column(
        Integer,
        primary_key=True
    )

    claim_id = Column(
        Integer,
        ForeignKey('claim.claim_id')
    )

    arbitration_id = Column(
        Integer,
        ForeignKey('arbitration.arbitration_id')
    )

    claim = relationship(
        'Claim',
        primaryjoin='ClaimArbitration.claim_id == Claim.claim_id',
        back_populates='claim_arbitration'
    )

    arbitration = relationship(
        'Arbitration',
        primaryjoin='ClaimArbitration.arbitration_id == Arbitration.arbitration_id',
        back_populates='claim_arbitration'
    )

    def __repr__(self):
        return "<ClaimArbitration(" \
               "claim_id='%s', " \
               "arbitration_id='%s'" \
               ")>" % (
                   self.claim_id,
                   self.arbitration_id
                )


class CourtJurisdiction(Base):
    __tablename__ = 'court_jurisdiction'

    court_jurisdiction_id = Column(
        Integer,
        primary_key=True
    )

    court_id = Column(Integer)

    jurisdiction_id = Column(Integer)

    litigation = relationship(
        'Litigation',
        primaryjoin='CourtJurisdiction.court_jurisdiction_id == Litigation.court_jurisdiction_id',
        back_populates='litigation'
    )

    def __repr__(self):
        return "<CourtJurisdiction(" \
               "court_id='%s', " \
               "jurisdiction_id='%s'" \
               ")>" % (
                   self.court_id,
                   self.jurisdiction_id
                )


class LitigationPartyRole(Base):
    __tablename__ = 'litigation_party_role'

    litigation_party_id = Column(
        Integer,
        primary_key=True
    )

    litigation_id = Column(
        Integer,
        ForeignKey('litigation.litigation_id')
    )

    party_id = Column(
        Integer,
        ForeignKey('party.party_id')
    )

    party_role_code = Column(
        String,
        ForeignKey('party_role.party_role_code')
    )

    begin_date = Column(Date)

    claim_id = Column(
        Integer,
        ForeignKey('claim.claim_id')
    )

    end_date = Column(Date)

    litigation = relationship(
        'Litigation',
        primaryjoin='LitigationPartyRole.litigation_id == Litigation.litigation_id',
        back_populates='litigation_party_role'
    )

    party = relationship(
        'Party',
        primaryjoin='LitigationPartyRole.party_id == Party.party_id',
        back_populates='litigation_party_role'
    )

    party_role = relationship(
        'PartyRole',
        primaryjoin='LitigationPartyRole.party_role_code == PartyRoleCode.party_role_code',
        back_populates='litigation_party_role'
    )

    claim = relationship(
        'Claim',
        primaryjoin='LitigationPartyRole.claim_id == Claim.claim_id',
        back_populates='litigation_party_role'
    )

    def __repr__(self):
        return "<LitigationPartyRole(" \
               "litigation_id='%s', " \
               "party_id='%s', " \
               "party_role_code='%s', "\
               "begin_date='%s', " \
               "claim_id='%s, '" \
               "end_date='%s'" \
               ")>" % (
                   self.litigation_id,
                   self.party_id,
                   self.party_role_code,
                   self.begin_date,
                   self.claim_id,
                   self.end_date
                )
