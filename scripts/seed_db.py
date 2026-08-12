"""
scripts/seed_db.py - populates the operations tables from the hand-authored, deterministic
rows in src/db/seed_data.py.
"""

from src.db.database import SessionLocal
from src.db.models import MaintenanceEvent, Operation, Equipment, TeamMember, IntelReport
from src.db.seed_data import MAINTENANCE_EVENTS, OPERATIONS, EQUIPMENT as EQUIPMENT_DATA, TEAM_MEMBERS, INTEL_REPORTS


def main():
    session = SessionLocal()
    try:
        # Children first - both have FKs into equipment/team_members.
        session.query(MaintenanceEvent).delete()
        session.query(Operation).delete()
        session.query(IntelReport).delete()
        session.query(Equipment).delete()
        session.query(TeamMember).delete()
        session.flush()

        equipment_by_name = {}
        for row in EQUIPMENT_DATA:
            eq = Equipment(**row)
            session.add(eq)
            equipment_by_name[row["mark_name"]] = eq

        team_members_by_name = {}
        for row in TEAM_MEMBERS:
            tm = TeamMember(**row)
            session.add(tm)
            team_members_by_name[row["name"]] = tm

        session.flush()  # assigns .id to every equipment/team_member before reference

        for row in MAINTENANCE_EVENTS:
            session.add(MaintenanceEvent(
                equipment_id=equipment_by_name[row["equipment"]].id,
                team_member_id=team_members_by_name[row["team_member"]].id,
                event_date=row["event_date"],
                component=row["component"],
                issue=row["issue"],
                resolution=row["resolution"],
                resolution_hours=row["resolution_hours"],
                cost_usd=row["cost_usd"],
            ))

        for row in OPERATIONS:
            session.add(Operation(
                equipment_id=equipment_by_name[row["equipment"]].id,
                operation_date=row["operation_date"],
                location=row["location"],
                threat_level=row["threat_level"],
                duration_min=row["duration_min"],
                outcome=row["outcome"],
            ))

        for row in INTEL_REPORTS:
            session.add(IntelReport(**row))

        session.commit()
        print(f"Seeded {len(EQUIPMENT_DATA)} equipment items, {len(TEAM_MEMBERS)} team members, "
              f"{len(MAINTENANCE_EVENTS)} maintenance events, {len(OPERATIONS)} operations, "
              f"{len(INTEL_REPORTS)} intel reports.")
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


if __name__ == "__main__":
    main()
