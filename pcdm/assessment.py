from sqlalchemy import Column, Date, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Assessment(Base):
    __tablename__ = 'assessment'

    assessment_id = Column(
        Integer,
        primary_key=True
    )

    begin_date = Column(Date)

    end_date = Column(Date)

    assessment_description = Column(String)

    assessment_reason_description = Column(String)

    assessment_party_role = relationship(
        'AssessmentPartyRole',
        primaryjoin='Assessment.assessment_id == AssessmentPartyRole.assessment_id',
        back_populates='assessment'
    )

    party_assessment = relationship(
        'PartyAssessment',
        primaryjoin='Assessment.assessment_id == PartyAssessment.assessment_id',
        back_populates='assessment'
    )

    agreement_assessment = relationship(
        'AgreementAssessment',
        primaryjoin='Assessment.assessment_id == AgreementAssessment.assessment_id',
        back_populates='assessment'
    )

    object_assessment = relationship(
        'ObjectAssessment',
        primaryjoin='Assessment.assessment_id == ObjectAssessment.assessment_id',
        back_populates='assessment'
    )

    claim_assessment = relationship(
        'ClaimAssessment',
        primaryjoin='Assessment.assessment_id == ClaimAssessment.assessment_id',
        back_populates='assessment'
    )

    assessment_result = relationship(
        'AssessmentResult',
        primaryjoin='Assessment.assessment_id == AssessmentResult.assessment_id',
        back_populates='assessment'
    )

    def __repr__(self):
        return "<Assessment(" \
               "begin_date='%s', " \
               "end_date='%s', " \
               "assessment_description='%s', " \
               "assessment_reason_description='%s'" \
               ")>" % (
                   self.begin_date,
                   self.end_date,
                   self.assessment_description,
                   self.assessment_reason_description
                )


class AssessmentPartyRole(Base):
    __tablename__ = 'assessment_party_role'

    assessment_party_role_id = Column(
        Integer,
        primary_key=True
    )

    party_id = Column(
        Integer,
        ForeignKey('party.party_id')
    )

    party_role_code = Column(
        String,
        ForeignKey('party_role.party_role_code')
    )

    assessment_id = Column(
        Integer,
        ForeignKey('assessment.assessment_id')
    )

    begin_date = Column(Date)

    end_date = Column(Date)

    party = relationship(
        'Party',
        primaryjoin='AssessmentPartyRole.party_id == Party.party_id',
        back_populates='assessment_party_role'
    )

    party_role = relationship(
        'PartyRole',
        primaryjoin='AssessmentPartyRole.party_role_code == PartyRole.party_role_code',
        back_populates='assessment_party_role'
    )

    assessment = relationship(
        'Assessment',
        primaryjoin='AssessmentPartyRole.assessment_id == Assessment.assessment_id',
        back_populates='assessment_party_role'
    )

    def __repr__(self):
        return "<AssessmentPartyRole(" \
               "party_id='%s', " \
               "party_role_code='%s', " \
               "assessment_id='%s', " \
               "begin_date='%s', " \
               "end_date='%s'" \
               ")>" % (
                   self.party_role_code,
                   self.party_id,
                   self.assessment_id,
                   self.begin_date,
                   self.end_date
                )


class PartyAssessment(Base):
    __tablename__ = 'party_assessment'

    party_assessment_id = Column(
        Integer,
        primary_key=True
    )

    person_id = Column(
        Integer,
        ForeignKey('person.person_id')
    )

    assessment_id = Column(
        Integer,
        ForeignKey('assessment.assessment_id')
    )

    party_id = Column(
        Integer,
        ForeignKey('party.party_id')
    )

    person = relationship(
        'Person',
        primaryjoin='PartyAssessment.person_id == Person.person_id',
        back_populates='party_assessment'
    )

    assessment = relationship(
        'Assessment',
        primaryjoin='PartyAssessment.assessment_id == Assessment.assessment_id',
        back_populates='party_assessment'
    )

    party = relationship(
        'Party',
        primaryjoin='PartyAssessment.party_id == Party.party_id',
        back_populates='party_assessment'
    )

    def __repr__(self):
        return "<PartyAssessment(" \
               "person_id='%s', " \
               "assessment_id='%s', " \
               "party_id='%s'" \
               ")>" % (
                   self.person_id,
                   self.assessment_id,
                   self.party_id
                )


class AgreementAssessment(Base):
    __tablename__ = 'agreement_assessment'

    agreement_assessment_id = Column(
        Integer,
        primary_key=True
    )

    agreement_id = Column(
        Integer,
        ForeignKey('agreement.agreement_id')
    )

    assessment_id = Column(
        Integer,
        ForeignKey('assessment.assessment_id')
    )

    agreement = relationship(
        'Agreement',
        primaryjoin='AgreementAssessment.agreement_id == Agreement.agreement_id',
        back_populates='agreement_assessment'
    )

    assessment = relationship(
        'Assessment',
        primaryjoin='AgreementAssessment.assessment_id == Assessment.assessment_id',
        back_populates='agreement_assessment'
    )

    def __repr__(self):
        return "<AgreementAssessment(" \
               "agreement_id='%s', " \
               "assessment_id='%s'" \
               ")>" % (
                   self.agreement_id,
                   self.assessment_id
                )


class ObjectAssessment(Base):
    __tablename__ = 'object_assessment'

    object_assessment_id = Column(
        Integer,
        primary_key=True
    )

    insurable_object_id = Column(
        Integer,
        ForeignKey('insurable_object.insurable_object_id')
    )

    assessment_id = Column(
        Integer,
        ForeignKey('assessment.assessment_id')
    )

    insurable_object = relationship(
        'InsurableObject',
        primaryjoin='ObjectAssessment.insurable_object_id == InsurableObject.insurable_object_id',
        back_populates='object_assessment'
    )

    assessment = relationship(
        'Assessment',
        primaryjoin='ObjectAssessment.assessment_id == Assessment.assessment_id',
        back_populates='object_assessment'
    )

    def __repr__(self):
        return "<ObjectAssessment(" \
               "insurable_object_id='%s', " \
               "assessment_id='%s'" \
               ")>" % (
                   self.insurable_object_id,
                   self.assessment_id
                )


class ClaimAssessment(Base):
    __tablename__ = 'claim_assessment'

    claim_assessment_id = Column(
        Integer,
        primary_key=True
    )

    claim_id = Column(
        Integer,
        ForeignKey('claim.claim_id')
    )

    assessment_id = Column(
        Integer,
        ForeignKey('assessment.assessment_id')
    )

    claim = relationship(
        'Claim',
        primaryjoin='ClaimAssessment.claim_id == Claim.claim_id',
        back_populates='claim_assessment'
    )

    assessment = relationship(
        'Assessment',
        primaryjoin='ClaimAssessment.assessment_id == Assessment.assessment_id',
        back_populates='claim_assessment'
    )

    def __repr__(self):
        return "<ClaimAssessment(" \
               "claim_id='%s', " \
               "assessment_id='%s'" \
               ")>" % (
                   self.claim_id,
                   self.assessment_id
                )


class AssessmentResult(Base):
    __tablename__ = 'assessment_result'

    assessment_result_id = Column(
        Integer,
        primary_key=True
    )

    assessment_id = Column(
        Integer,
        ForeignKey('assessment.assessment_id')
    )

    assessment_result_type_code = Column(Integer)

    assessment = relationship(
        'Assessment',
        primaryjoin='AssessmentResult.assessment_id == Assessment.assessment_id',
        back_populates='assessment_result'
    )

    approval = relationship(
        'Approval',
        primaryjoin='AssessmentResult.assessment_result_id == Approval.assessment_result_id',
        back_populates='assessment_result'
    )

    channel_score = relationship(
        'ChannelScore',
        primaryjoin='AssessmentResult.assessment_result_id == ChannelScore.assessment_result_id',
        back_populates='assessment_result'
    )

    customer_score = relationship(
        'CustomerScore',
        primaryjoin='AssessmentResult.assessment_result_id == CustomerScore.assessment_result_id',
        back_populates='assessment_result'
    )

    risk_factor_score = relationship(
        'RiskFactorScore',
        primaryjoin='AssessmentResult.assessment_result_id == RiskFactorScore.assessment_result_id',
        back_populates='assessment_result'
    )

    demographic_score = relationship(
        'DemographicScore',
        primaryjoin='AssessmentResult.assessment_result_id == DemographicScore.assessment_result_id',
        back_populates='assessment_result'
    )

    underwriting_assignment = relationship(
        'UnderwritingAssignment',
        primaryjoin='AssessmentResult.assessment_result_id == UnderwritingAssignment.assessment_result_id',
        back_populates='assessment_result'
    )

    credit_rating = relationship(
        'CreditRating',
        primaryjoin='AssessmentResult.assessment_result_id == CreditRating.assessment_result_id',
        back_populates='assessment_result'
    )

    financial_valuation = relationship(
        'FinancialValuation',
        primaryjoin='AssessmentResult.assessment_result_id == FinancialValuation.assessment_result_id',
        back_populates='assessment_result'
    )

    medical_condition = relationship(
        'MedicalCondition',
        primaryjoin='AssessmentResult.assessment_result_id == MedicalCondition.assessment_result_id',
        back_populates='assessment_result'
    )

    financial_services_assessment = relationship(
        'FinancialServicesAssessment',
        primaryjoin='AssessmentResult.assessment_result_id == FinancialServicesAssessment.assessment_result_id',
        back_populates='assessment_result'
    )

    fraud_assessment = relationship(
        'FraudAssessment',
        primaryjoin='AssessmentResult.assessment_result_id == FraudAssessment.assessment_result_id',
        back_populates='assessment_result'
    )

    physical_object_assessment = relationship(
        'PhysicalObjectAssessment',
        primaryjoin='AssessmentResult.assessment_result_id == PhysicalObjectAssessment.assessment_result_id',
        back_populates='assessment_result'
    )

    place_assessment = relationship(
        'PlaceAssessment',
        primaryjoin='AssessmentResult.assessment_result_id == PlaceAssessment.assessment_result_id',
        back_populates='assessment_result'
    )

    claim_evaluation_result = relationship(
        'ClaimEvaluationResult',
        primaryjoin='AssessmentResult.assessment_result_id == ClaimEvaluationResult.assessment_result_id',
        back_populates='assessment_result'
    )

    other_assessment_result = relationship(
        'OtherAssessmentResult',
        primaryjoin='AssessmentResult.assessment_result_id == OtherAssessmentResult.assessment_result_id',
        back_populates='assessment_result'
    )

    def __repr__(self):
        return "<AssessmentResult(" \
               "assessment_id='%s', " \
               "assessment_result_type_code='%s'" \
               ")>" % (
                   self.assessment_id,
                   self.assessment_result_type_code
                )


class Approval(Base):
    __tablename__ = 'approval'

    approval_id = Column(
        Integer,
        primary_key=True
    )

    assessment_result_id = Column(
        Integer,
        ForeignKey('assessment_result.assessment_result_id')
    )

    assessment_result = relationship(
        'AssessmentResult',
        primaryjoin='Approval.assessment_result_id == AssessmentResult.assessment_result_id',
        back_populates='approval'
    )

    def __repr__(self):
        return "<Approval(" \
               "assessment_result_id='%s'" \
               ")>" % (
                   self.assessment_result_id
                )


class ChannelScore(Base):
    __tablename__ = 'channel_score'

    channel_score_id = Column(
        Integer,
        primary_key=True
    )

    assessment_result_id = Column(
        Integer,
        ForeignKey('assessment_result.assessment_result_id')
    )

    assessment_result = relationship(
        'AssessmentResult',
        primaryjoin='ChannelScore.assessment_result_id == AssessmentResult.assessment_result_id',
        back_populates='channel_score'
    )

    def __repr__(self):
        return "<ChannelScore(" \
               "assessment_result_id='%s'" \
               ")>" % (
                   self.assessment_result_id
                )


class CustomerScore(Base):
    __tablename__ = 'customer_score'

    customer_score_id = Column(
        Integer,
        primary_key=True
    )

    assessment_result_id = Column(
        Integer,
        ForeignKey('assessment_result.assessment_result_id')
    )

    assessment_result = relationship(
        'AssessmentResult',
        primaryjoin='CustomerScore.assessment_result_id == AssessmentResult.assessment_result_id',
        back_populates='customer_score'
    )

    def __repr__(self):
        return "<CustomerScore(" \
               "assessment_result_id='%s'" \
               ")>" % (
                   self.assessment_result_id
                )


class RiskFactorScore(Base):
    __tablename__ = 'risk_factor_score'

    risk_factor_score_id = Column(
        Integer,
        primary_key=True
    )

    assessment_result_id = Column(
        Integer,
        ForeignKey('assessment_result.assessment_result_id')
    )

    assessment_result = relationship(
        'AssessmentResult',
        primaryjoin='RiskFactorScore.assessment_result_id == AssessmentResult.assessment_result_id',
        back_populates='risk_factor_score'
    )

    def __repr__(self):
        return "<RiskFactorScore(" \
               "assessment_result_id='%s'" \
               ")>" % (
                   self.assessment_result_id
                )


class DemographicScore(Base):
    __tablename__ = 'demographic_score'

    demographic_score_id = Column(
        Integer,
        primary_key=True
    )

    assessment_result_id = Column(
        Integer,
        ForeignKey('assessment_result.assessment_result_id')
    )

    assessment_result = relationship(
        'AssessmentResult',
        primaryjoin='DemographicScore.assessment_result_id == AssessmentResult.assessment_result_id',
        back_populates='demographic_score'
    )

    def __repr__(self):
        return "<DemographicScore(" \
               "assessment_result_id='%s'" \
               ")>" % (
                   self.assessment_result_id
                )


class UnderwritingAssignment(Base):
    __tablename__ = 'underwriting_assignment'

    underwriting_assignment_id = Column(
        Integer,
        primary_key=True
    )

    assessment_result_id = Column(
        Integer,
        ForeignKey('assessment_result.assessment_result_id')
    )

    assessment_result = relationship(
        'AssessmentResult',
        primaryjoin='UnderwritingAssignment.assessment_result_id == AssessmentResult.assessment_result_id',
        back_populates='underwriting_assignment'
    )

    def __repr__(self):
        return "<UnderwritingAssignment(" \
               "assessment_result_id='%s'" \
               ")>" % (
                   self.assessment_result_id
                )


class CreditRating(Base):
    __tablename__ = 'credit_rating'

    credit_rating_id = Column(
        Integer,
        primary_key=True
    )

    assessment_result_id = Column(
        Integer,
        ForeignKey('assessment_result.assessment_result_id')
    )

    assessment_result = relationship(
        'AssessmentResult',
        primaryjoin='CreditRating.assessment_result_id == AssessmentResult.assessment_result_id',
        back_populates='credit_rating'
    )

    def __repr__(self):
        return "<CreditRating(" \
               "assessment_result_id='%s'" \
               ")>" % (
                   self.assessment_result_id
                )


class FinancialValuation(Base):
    __tablename__ = 'financial_valuation'

    financial_valuation_id = Column(
        Integer,
        primary_key=True
    )

    assessment_result_id = Column(
        Integer,
        ForeignKey('assessment_result.assessment_result_id')
    )

    assessment_result = relationship(
        'AssessmentResult',
        primaryjoin='FinancialValuation.assessment_result_id == AssessmentResult.assessment_result_id',
        back_populates='financial_valuation'
    )

    def __repr__(self):
        return "<FinancialValuation(" \
               "assessment_result_id='%s'" \
               ")>" % (
                   self.assessment_result_id
                )


class MedicalCondition(Base):
    __tablename__ = 'medical_condition'

    medical_condition_id = Column(
        Integer,
        primary_key=True
    )

    assessment_result_id = Column(
        Integer,
        ForeignKey('assessment_result.assessment_result_id')
    )

    assessment_result = relationship(
        'AssessmentResult',
        primaryjoin='MedicalCondition.assessment_result_id == AssessmentResult.assessment_result_id',
        back_populates='medical_condition'
    )

    def __repr__(self):
        return "<MedicalCondition(" \
               "assessment_result_id='%s'" \
               ")>" % (
                   self.assessment_result_id
                )


class FinancialServicesAssessment(Base):
    __tablename__ = 'financial_services_assessment'

    financial_services_assessment_id = Column(
        Integer,
        primary_key=True
    )

    assessment_result_id = Column(
        Integer,
        ForeignKey('assessment_result.assessment_result_id')
    )

    assessment_result = relationship(
        'AssessmentResult',
        primaryjoin='FinancialServicesAssessment.assessment_result_id == AssessmentResult.assessment_result_id',
        back_populates='financial_services_assessment'
    )

    def __repr__(self):
        return "<FinancialServicesAssessment(" \
               "assessment_result_id='%s'" \
               ")>" % (
                   self.assessment_result_id
                )


class FraudAssessment(Base):
    __tablename__ = 'fraud_assessment'

    fraud_assessment_id = Column(
        Integer,
        primary_key=True
    )

    assessment_result_id = Column(
        Integer,
        ForeignKey('assessment_result.assessment_result_id')
    )

    assessment_result = relationship(
        'AssessmentResult',
        primaryjoin='FraudAssessment.assessment_result_id == AssessmentResult.assessment_result_id',
        back_populates='fraud_assessment'
    )

    def __repr__(self):
        return "<FraudAssessment(" \
               "assessment_result_id='%s'" \
               ")>" % (
                   self.assessment_result_id
                )


class PhysicalObjectAssessment(Base):
    __tablename__ = 'physical_object_assessment'

    physical_object_assessment_id = Column(
        Integer,
        primary_key=True
    )

    assessment_result_id = Column(
        Integer,
        ForeignKey('assessment_result.assessment_result_id')
    )

    assessment_result = relationship(
        'AssessmentResult',
        primaryjoin='PhysicalObjectAssessment.assessment_result_id == AssessmentResult.assessment_result_id',
        back_populates='physical_object_assessment'
    )

    def __repr__(self):
        return "<PhysicalObjectAssessment(" \
               "assessment_result_id='%s'" \
               ")>" % (
                   self.assessment_result_id
                )


class PlaceAssessment(Base):
    __tablename__ = 'place_assessment'

    place_assessment_id = Column(
        Integer,
        primary_key=True
    )

    assessment_result_id = Column(
        Integer,
        ForeignKey('assessment_result.assessment_result_id')
    )

    assessment_result = relationship(
        'AssessmentResult',
        primaryjoin='PlaceAssessment.assessment_result_id == AssessmentResult.assessment_result_id',
        back_populates='place_assessment'
    )

    def __repr__(self):
        return "<PlaceAssessment(" \
               "assessment_result_id='%s'" \
               ")>" % (
                   self.assessment_result_id
                )


class ClaimEvaluationResult(Base):
    __tablename__ = 'claim_evaluation_result'

    claim_evaluation_result_id = Column(
        Integer,
        primary_key=True
    )

    assessment_result_id = Column(
        Integer,
        ForeignKey('assessment_result.assessment_result_id')
    )

    assessment_result = relationship(
        'AssessmentResult',
        primaryjoin='ClaimEvaluationResult.assessment_result_id == AssessmentResult.assessment_result_id',
        back_populates='claim_evaluation_result'
    )

    def __repr__(self):
        return "<ClaimEvaluationResult(" \
               "assessment_result_id='%s'" \
               ")>" % (
                   self.assessment_result_id
                )


class OtherAssessmentResult(Base):
    __tablename__ = 'other_assessment_result'

    other_assessment_result_id = Column(
        Integer,
        primary_key=True
    )

    assessment_result_id = Column(
        Integer,
        ForeignKey('assessment_result.assessment_result_id')
    )

    assessment_result = relationship(
        'AssessmentResult',
        primaryjoin='OtherAssessmentResult.assessment_result_id == AssessmentResult.assessment_result_id',
        back_populates='other_assessment_result'
    )

    def __repr__(self):
        return "<OtherAssessmentResult(" \
               "assessment_result_id='%s'" \
               ")>" % (
                   self.assessment_result_id
                )
