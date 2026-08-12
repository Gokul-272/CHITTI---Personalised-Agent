"""
src/db/models.py - the structured fleet-ops schema: suits, technicians, maintenance
events, and missions. This is the "structured data" counterpart to data/documents/ - the
same real-world facts (suit maintenance, in maintenance_log.csv) sometimes belong in a
proper relational DB instead of a document, because a question like "how many times has
the Mark 42 needed thruster repairs" needs an exact COUNT, not an LLM eyeballing a handful
of retrieved chunks. See src/nl2sql/ for how natural language reaches these tables.
"""

from sqlalchemy import Column, Integer, String, Text, Numeric, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Equipment(Base):
    __tablename__ = "equipment"

    id = Column(Integer, primary_key=True)
    mark_name = Column(String, unique=True, nullable=False)
    status = Column(String, nullable=False)  # combat_ready | needs_maintenance | in_storage | decommissioned
    power_core_pct = Column(Numeric, nullable=False)
    last_diagnostic_date = Column(Date, nullable=False)

    maintenance_events = relationship("MaintenanceEvent", back_populates="equipment")
    operations = relationship("Operation", back_populates="equipment")


class TeamMember(Base):
    __tablename__ = "team_members"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    specialty = Column(String, nullable=False)
    years_experience = Column(Integer, nullable=False)

    maintenance_events = relationship("MaintenanceEvent", back_populates="team_member")


class MaintenanceEvent(Base):
    __tablename__ = "maintenance_events"

    id = Column(Integer, primary_key=True)
    equipment_id = Column(Integer, ForeignKey("equipment.id"), nullable=False)
    team_member_id = Column(Integer, ForeignKey("team_members.id"), nullable=False)
    event_date = Column(Date, nullable=False)
    component = Column(String, nullable=False)
    issue = Column(Text, nullable=False)
    resolution = Column(Text, nullable=False)
    resolution_hours = Column(Numeric, nullable=False)
    cost_usd = Column(Numeric, nullable=False)

    equipment = relationship("Equipment", back_populates="maintenance_events")
    team_member = relationship("TeamMember", back_populates="maintenance_events")


class Operation(Base):
    __tablename__ = "operations"

    id = Column(Integer, primary_key=True)
    equipment_id = Column(Integer, ForeignKey("equipment.id"), nullable=False)
    operation_date = Column(Date, nullable=False)
    location = Column(String, nullable=False)
    threat_level = Column(Integer, nullable=False)  # 1 (routine) - 5 (extinction-level)
    duration_min = Column(Integer, nullable=False)
    outcome = Column(String, nullable=False)  # success | partial | aborted

    equipment = relationship("Equipment", back_populates="operations")


class IntelReport(Base):
    __tablename__ = "intel_reports"

    id = Column(Integer, primary_key=True)
    codename = Column(String, unique=True, nullable=False)
    status = Column(String, nullable=False)  # active | completed | classified
    threat_level = Column(Integer, nullable=False)
    summary = Column(Text, nullable=False)
    report_date = Column(Date, nullable=False)
