"""
src/db/seed_data.py - deterministic, hand-authored seed rows for the operations DB.
"""

EQUIPMENT = [
    {"mark_name": "Mark 42", "status": "needs_maintenance", "power_core_pct": 84, "last_diagnostic_date": "2024-03-11"},
    {"mark_name": "Mark 45", "status": "combat_ready", "power_core_pct": 97, "last_diagnostic_date": "2024-03-19"},
    {"mark_name": "Mark 50", "status": "combat_ready", "power_core_pct": 99, "last_diagnostic_date": "2024-03-20"},
    {"mark_name": "War Machine", "status": "combat_ready", "power_core_pct": 91, "last_diagnostic_date": "2024-03-18"},
    {"mark_name": "Rescue", "status": "in_storage", "power_core_pct": 88, "last_diagnostic_date": "2024-02-01"},
    {"mark_name": "Mark 7", "status": "decommissioned", "power_core_pct": 0, "last_diagnostic_date": "2012-05-04"},
]

TEAM_MEMBERS = [
    {"name": "Gokul", "specialty": "Robotics & AI", "years_experience": 5},
    {"name": "CHITTI Automated Diagnostics", "specialty": "Software & Diagnostics", "years_experience": 1},
    {"name": "Happy Hogan", "specialty": "Structural", "years_experience": 8},
    {"name": "Tony Stark", "specialty": "Propulsion", "years_experience": 20},
    {"name": "Priya Anand", "specialty": "Avionics", "years_experience": 6},
    {"name": "Dmitri Kovalenko", "specialty": "Power Systems", "years_experience": 11},
    {"name": "Sam Wilkins", "specialty": "Structural", "years_experience": 4},
    {"name": "Sanjay", "specialty": "Intelligence", "years_experience": 8},
]

MAINTENANCE_EVENTS = [
    {"equipment": "Mark 42", "team_member": "Happy Hogan", "event_date": "2023-12-01", "component": "Left boot thruster", "issue": "Intermittent fault under cold conditions", "resolution": "Replaced thruster coil and resealed housing", "resolution_hours": 4.5, "cost_usd": 2200},
    {"equipment": "Mark 42", "team_member": "Happy Hogan", "event_date": "2024-01-14", "component": "Left boot thruster", "issue": "Repeat intermittent fault after coil replacement", "resolution": "Escalated to full thruster housing replacement", "resolution_hours": 9, "cost_usd": 6800},
    {"equipment": "Mark 42", "team_member": "Happy Hogan", "event_date": "2024-03-02", "component": "Left boot thruster", "issue": "Fault flagged a third time under sustained cold exposure", "resolution": "Replaced with redesigned cold-rated coil assembly", "resolution_hours": 6, "cost_usd": 4100},
    {"equipment": "Mark 42", "team_member": "Priya Anand", "event_date": "2024-02-10", "component": "HUD display", "issue": "Minor glare artifact in direct sunlight", "resolution": "Recalibrated display polarization filter", "resolution_hours": 1.5, "cost_usd": 300},
    {"equipment": "Mark 42", "team_member": "Dmitri Kovalenko", "event_date": "2024-01-22", "component": "Power core regulator", "issue": "Output dipped 4% below nominal for under a minute", "resolution": "Replaced regulator fuse, retested to spec", "resolution_hours": 2, "cost_usd": 900},
    {"equipment": "Mark 42", "team_member": "Happy Hogan", "event_date": "2024-03-11", "component": "Right boot thruster", "issue": "New fault reported on right side for the first time", "resolution": "Replaced right thruster coil preemptively", "resolution_hours": 4, "cost_usd": 2100},
    {"equipment": "Mark 42", "team_member": "Happy Hogan", "event_date": "2024-02-07", "component": "Left gauntlet plating", "issue": "Minor wear from training exercise", "resolution": "Buffed and resealed plating", "resolution_hours": 1, "cost_usd": 150},
    {"equipment": "Mark 42", "team_member": "Tony Stark", "event_date": "2024-01-20", "component": "Repulsor coil", "issue": "Output 3% below spec on diagnostic sweep", "resolution": "Recalibrated repulsor coil alignment", "resolution_hours": 2, "cost_usd": 500},
    {"equipment": "Mark 45", "team_member": "Tony Stark", "event_date": "2024-02-03", "component": "Chestplate servo", "issue": "Minor calibration drift after a high-G maneuver", "resolution": "Recalibrated via the diagnostic dock", "resolution_hours": 1, "cost_usd": 150},
    {"equipment": "Mark 45", "team_member": "Tony Stark", "event_date": "2024-03-19", "component": "Power regulation circuit", "issue": "Output fluctuation of plus or minus 2 percent under sustained load", "resolution": "Replaced the regulation circuit board", "resolution_hours": 3, "cost_usd": 2400},
    {"equipment": "Mark 45", "team_member": "Sam Wilkins", "event_date": "2023-12-15", "component": "Left gauntlet plating", "issue": "Hairline stress fracture after impact", "resolution": "Replaced plating section", "resolution_hours": 2.5, "cost_usd": 700},
    {"equipment": "Mark 45", "team_member": "Happy Hogan", "event_date": "2024-03-05", "component": "Chestplate servo", "issue": "Servo grinding noise reported by pilot", "resolution": "Lubricated and retested servo assembly", "resolution_hours": 1, "cost_usd": 180},
    {"equipment": "Mark 45", "team_member": "Sam Wilkins", "event_date": "2024-01-16", "component": "Chestplate integrity", "issue": "Minor scoring from debris impact", "resolution": "Buffed and resealed chestplate coating", "resolution_hours": 1.5, "cost_usd": 300},
    {"equipment": "Mark 45", "team_member": "Dmitri Kovalenko", "event_date": "2024-03-15", "component": "Power core regulator", "issue": "Preventive inspection ahead of scheduled mission", "resolution": "No repair needed - logged as passed diagnostic", "resolution_hours": 1, "cost_usd": 0},
    {"equipment": "Mark 50", "team_member": "CHITTI Automated Diagnostics", "event_date": "2024-02-20", "component": "Nanotech reassembly matrix", "issue": "Reassembly lag of 0.4 seconds above spec", "resolution": "Applied firmware patch; lag reduced to 0.1 seconds", "resolution_hours": 0.5, "cost_usd": 0},
    {"equipment": "Mark 50", "team_member": "Dmitri Kovalenko", "event_date": "2024-01-05", "component": "Repulsor coil", "issue": "Thermal throttling triggered below spec threshold", "resolution": "Replaced coolant line, retested under load", "resolution_hours": 3, "cost_usd": 1800},
    {"equipment": "Mark 50", "team_member": "Priya Anand", "event_date": "2023-12-28", "component": "Targeting HUD", "issue": "Lock time drift of 0.1 seconds above spec", "resolution": "Recalibrated sensor array", "resolution_hours": 1, "cost_usd": 200},
    {"equipment": "Mark 50", "team_member": "Sam Wilkins", "event_date": "2024-02-14", "component": "Left boot thruster", "issue": "Minor efficiency loss reported", "resolution": "Cleaned thruster intake, retested to spec", "resolution_hours": 2, "cost_usd": 400},
    {"equipment": "Mark 50", "team_member": "Tony Stark", "event_date": "2024-02-28", "component": "Nanotech reassembly matrix", "issue": "Routine firmware audit", "resolution": "Updated firmware to latest validated build", "resolution_hours": 1, "cost_usd": 0},
    {"equipment": "Mark 50", "team_member": "Priya Anand", "event_date": "2024-03-20", "component": "Power core regulator", "issue": "Routine post-mission inspection", "resolution": "No repair needed - logged as passed diagnostic", "resolution_hours": 0.5, "cost_usd": 0},
    {"equipment": "War Machine", "team_member": "Happy Hogan", "event_date": "2024-01-30", "component": "Minigun mount", "issue": "Mount vibration exceeding tolerance during sustained fire", "resolution": "Reinforced mount bracket", "resolution_hours": 5, "cost_usd": 3100},
    {"equipment": "War Machine", "team_member": "Sam Wilkins", "event_date": "2023-11-18", "component": "Left leg actuator", "issue": "Actuator response delay under heavy load", "resolution": "Replaced actuator servo", "resolution_hours": 4, "cost_usd": 2600},
    {"equipment": "War Machine", "team_member": "Tony Stark", "event_date": "2024-02-25", "component": "Power core regulator", "issue": "Output spike during weapons discharge", "resolution": "Installed surge dampener", "resolution_hours": 3.5, "cost_usd": 2900},
    {"equipment": "War Machine", "team_member": "Priya Anand", "event_date": "2024-01-27", "component": "Comms array", "issue": "Static interference on priority channel", "resolution": "Replaced comms antenna array", "resolution_hours": 2.5, "cost_usd": 1200},
    {"equipment": "War Machine", "team_member": "Priya Anand", "event_date": "2023-11-30", "component": "HUD display", "issue": "Refresh rate below spec under G-load", "resolution": "Replaced HUD driver board", "resolution_hours": 2, "cost_usd": 950},
    {"equipment": "War Machine", "team_member": "Sam Wilkins", "event_date": "2023-12-08", "component": "Flight stabilizer", "issue": "Drift during high-speed maneuvering", "resolution": "Recalibrated stabilizer gyroscope", "resolution_hours": 1.5, "cost_usd": 300},
    {"equipment": "Rescue", "team_member": "Priya Anand", "event_date": "2023-11-05", "component": "Flight stabilizer", "issue": "Minor drift during hover mode", "resolution": "Recalibrated stabilizer gyroscope", "resolution_hours": 1, "cost_usd": 250},
    {"equipment": "Rescue", "team_member": "Dmitri Kovalenko", "event_date": "2024-01-08", "component": "Power core", "issue": "Routine capacity check, no fault found", "resolution": "No repair needed - logged as passed diagnostic", "resolution_hours": 0.5, "cost_usd": 0},
    {"equipment": "Rescue", "team_member": "Dmitri Kovalenko", "event_date": "2023-12-20", "component": "Arc Reactor (chest unit, current)", "issue": "Output ceiling test", "resolution": "No repair needed - logged as passed diagnostic", "resolution_hours": 0.5, "cost_usd": 0},
    {"equipment": "Mark 7", "team_member": "Tony Stark", "event_date": "2012-05-04", "component": "Full frame", "issue": "Total structural failure during the Battle of New York", "resolution": "Suit decommissioned, not repaired", "resolution_hours": 0, "cost_usd": 0},
]

OPERATIONS = [
    {"equipment": "Mark 42", "operation_date": "2024-01-05", "location": "Malibu Coastline", "threat_level": 4, "duration_min": 38, "outcome": "success"},
    {"equipment": "Mark 42", "operation_date": "2024-02-18", "location": "Downtown LA", "threat_level": 3, "duration_min": 22, "outcome": "success"},
    {"equipment": "Mark 42", "operation_date": "2024-03-01", "location": "Pacific Test Range", "threat_level": 2, "duration_min": 15, "outcome": "success"},
    {"equipment": "Mark 42", "operation_date": "2023-12-12", "location": "Nevada Desert Range", "threat_level": 2, "duration_min": 14, "outcome": "success"},
    {"equipment": "Mark 45", "operation_date": "2024-01-20", "location": "New York City", "threat_level": 5, "duration_min": 54, "outcome": "success"},
    {"equipment": "Mark 45", "operation_date": "2024-02-05", "location": "Extremis Containment Site", "threat_level": 5, "duration_min": 61, "outcome": "partial"},
    {"equipment": "Mark 45", "operation_date": "2024-03-10", "location": "Stark Industries Perimeter", "threat_level": 2, "duration_min": 12, "outcome": "success"},
    {"equipment": "Mark 45", "operation_date": "2024-02-27", "location": "Miami Coastal Patrol", "threat_level": 3, "duration_min": 19, "outcome": "success"},
    {"equipment": "Mark 50", "operation_date": "2024-01-12", "location": "Wakanda Border", "threat_level": 5, "duration_min": 47, "outcome": "success"},
    {"equipment": "Mark 50", "operation_date": "2024-02-22", "location": "Sokovia Airspace", "threat_level": 5, "duration_min": 58, "outcome": "success"},
    {"equipment": "Mark 50", "operation_date": "2024-03-05", "location": "Siberian Facility", "threat_level": 4, "duration_min": 33, "outcome": "success"},
    {"equipment": "Mark 50", "operation_date": "2023-12-30", "location": "Test Flight Corridor", "threat_level": 1, "duration_min": 8, "outcome": "success"},
    {"equipment": "Mark 50", "operation_date": "2024-01-15", "location": "Arctic Research Station", "threat_level": 4, "duration_min": 36, "outcome": "aborted"},
    {"equipment": "War Machine", "operation_date": "2024-01-08", "location": "Wakanda Border", "threat_level": 5, "duration_min": 49, "outcome": "success"},
    {"equipment": "War Machine", "operation_date": "2024-02-14", "location": "Lagos", "threat_level": 4, "duration_min": 30, "outcome": "partial"},
    {"equipment": "War Machine", "operation_date": "2024-03-18", "location": "USAF Joint Exercise", "threat_level": 2, "duration_min": 20, "outcome": "success"},
    {"equipment": "War Machine", "operation_date": "2024-03-22", "location": "Joint NATO Exercise", "threat_level": 3, "duration_min": 28, "outcome": "success"},
    {"equipment": "Rescue", "operation_date": "2023-11-10", "location": "Malibu Cliffside Recovery", "threat_level": 3, "duration_min": 25, "outcome": "success"},
    {"equipment": "Rescue", "operation_date": "2024-01-25", "location": "Stark Expo Backup", "threat_level": 1, "duration_min": 10, "outcome": "success"},
    {"equipment": "Rescue", "operation_date": "2024-02-01", "location": "Stark Tower Perimeter Drill", "threat_level": 1, "duration_min": 9, "outcome": "success"},
]

INTEL_REPORTS = [
    {"codename": "Vaathi Coming", "status": "active", "threat_level": 4, "summary": "Heavy deployment of forces detected at the northern frontier. High tactical vigilance recommended.", "report_date": "2024-03-25"},
    {"codename": "Mastermind", "status": "completed", "threat_level": 5, "summary": "Strategic operation at the port completed successfully. Enemy supply line disabled.", "report_date": "2024-02-15"},
    {"codename": "Leo Rescue", "status": "classified", "threat_level": 3, "summary": "Extraction of key assets completed successfully during high wind conditions.", "report_date": "2024-01-10"},
]
