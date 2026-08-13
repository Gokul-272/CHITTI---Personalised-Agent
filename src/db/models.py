"""
src/db/models.py - the structured Personal Assistant schema: tasks, schedule events,
contacts, expenses, and personal notes. This is the "structured data" counterpart to
data/documents/ for precise metrics (exact counts, priority filtering, sum of expenses,
and date ranges) via the NL2SQL pipeline. See src/nl2sql/ for details.
"""

from sqlalchemy import Column, Integer, String, Text, Numeric, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    category = Column(String, nullable=False)  # work | learning | personal | health | project
    priority = Column(Integer, nullable=False)  # 1 (low) - 5 (critical)
    status = Column(String, nullable=False)    # pending | in_progress | completed | cancelled
    due_date = Column(Date, nullable=False)
    estimated_hours = Column(Numeric, nullable=False)


class ScheduleEvent(Base):
    __tablename__ = "schedule_events"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    category = Column(String, nullable=False)  # work | personal | health | meeting
    event_date = Column(Date, nullable=False)
    duration_min = Column(Integer, nullable=False)
    location = Column(String, nullable=False)
    status = Column(String, nullable=False)    # scheduled | completed | cancelled


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    relationship_type = Column(String, nullable=False)  # colleague | mentor | family | friend | doctor
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    notes = Column(Text, nullable=True)

    expenses = relationship("Expense", back_populates="contact")


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    contact_id = Column(Integer, ForeignKey("contacts.id"), nullable=True)
    expense_date = Column(Date, nullable=False)
    category = Column(String, nullable=False)  # tech | food | travel | learning | utilities
    amount_usd = Column(Numeric, nullable=False)
    description = Column(Text, nullable=False)

    contact = relationship("Contact", back_populates="expenses")


class PersonalNote(Base):
    __tablename__ = "personal_notes"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, nullable=False)
    category = Column(String, nullable=False)  # idea | goal | reminder | reference
    priority = Column(Integer, nullable=False)
    summary = Column(Text, nullable=False)
    created_date = Column(Date, nullable=False)

