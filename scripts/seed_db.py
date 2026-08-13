"""
scripts/seed_db.py - populates the Personal Assistant tables from the hand-authored, deterministic
rows in src/db/seed_data.py.
"""

from src.db.database import SessionLocal
from src.db.models import Task, ScheduleEvent, Contact, Expense, PersonalNote
from src.db.seed_data import TASKS, SCHEDULE_EVENTS, CONTACTS, EXPENSES, PERSONAL_NOTES


def main():
    session = SessionLocal()
    try:
        # Children first - Expense has FK into contacts
        session.query(Expense).delete()
        session.query(Task).delete()
        session.query(ScheduleEvent).delete()
        session.query(Contact).delete()
        session.query(PersonalNote).delete()
        session.flush()

        contacts_by_name = {}
        for row in CONTACTS:
            c = Contact(**row)
            session.add(c)
            contacts_by_name[row["name"]] = c

        session.flush()  # assigns .id to contacts before Expense FK references

        for row in TASKS:
            session.add(Task(**row))

        for row in SCHEDULE_EVENTS:
            session.add(ScheduleEvent(**row))

        for row in EXPENSES:
            c_name = row.get("contact_name")
            contact_id = contacts_by_name[c_name].id if c_name and c_name in contacts_by_name else None
            session.add(Expense(
                contact_id=contact_id,
                expense_date=row["expense_date"],
                category=row["category"],
                amount_usd=row["amount_usd"],
                description=row["description"],
            ))

        for row in PERSONAL_NOTES:
            session.add(PersonalNote(**row))

        session.commit()
        print(f"Seeded {len(TASKS)} tasks, {len(SCHEDULE_EVENTS)} schedule events, "
              f"{len(CONTACTS)} contacts, {len(EXPENSES)} expenses, and "
              f"{len(PERSONAL_NOTES)} personal notes.")
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


if __name__ == "__main__":
    main()

