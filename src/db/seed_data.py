"""
src/db/seed_data.py - deterministic, personalized seed rows for Gokul & CHITTI operations DB.
"""

EQUIPMENT = [
    {"mark_name": "CHITTI Mark 1", "status": "combat_ready", "power_core_pct": 98, "last_diagnostic_date": "2024-03-28"},
    {"mark_name": "CHITTI Mark 2", "status": "needs_maintenance", "power_core_pct": 84, "last_diagnostic_date": "2024-03-25"},
    {"mark_name": "Autonomous Mobile Robot AMR-1", "status": "combat_ready", "power_core_pct": 94, "last_diagnostic_date": "2024-03-20"},
    {"mark_name": "Drone Inspector Unit 2", "status": "combat_ready", "power_core_pct": 91, "last_diagnostic_date": "2024-03-22"},
    {"mark_name": "CNC Sensor-Fusion Array 1", "status": "combat_ready", "power_core_pct": 99, "last_diagnostic_date": "2024-03-29"},
    {"mark_name": "Perimeter Shield Alpha", "status": "in_storage", "power_core_pct": 90, "last_diagnostic_date": "2024-02-15"},
    {"mark_name": "CHITTI Prototype 0", "status": "decommissioned", "power_core_pct": 0, "last_diagnostic_date": "2023-08-10"},
]

TEAM_MEMBERS = [
    {"name": "Gokul", "specialty": "Robotics & AI Lead", "years_experience": 5},
    {"name": "CHITTI Automated Diagnostics", "specialty": "Neural Diagnostics & Self-Healing", "years_experience": 1},
    {"name": "Priya Anand", "specialty": "Avionics & Sensor Fusion", "years_experience": 6},
    {"name": "Karthik Raja", "specialty": "Embedded Firmware & Motor Control", "years_experience": 4},
    {"name": "Ananya Ramesh", "specialty": "Computer Vision & SLAM Navigation", "years_experience": 5},
    {"name": "Deepak V", "specialty": "Power Systems & Battery Management", "years_experience": 7},
    {"name": "Kavitha S", "specialty": "Cloud Infrastructure & Vector DB", "years_experience": 6},
    {"name": "Sanjay", "specialty": "Tactical Intelligence & Operations", "years_experience": 8},
]

MAINTENANCE_EVENTS = [
    # CHITTI Mark 2 maintenance
    {"equipment": "CHITTI Mark 2", "team_member": "Karthik Raja", "event_date": "2023-12-01", "component": "Servo joint 4", "issue": "Minor thermal drift after 4-hour continuous sorting run", "resolution": "Applied heat sink pad and updated thermal throttling firmware", "resolution_hours": 3.5, "cost_usd": 1200},
    {"equipment": "CHITTI Mark 2", "team_member": "Deepak V", "event_date": "2024-01-14", "component": "Power core regulator", "issue": "Voltage spike under peak motor acceleration", "resolution": "Replaced power regulation circuit and recalibrated fuse", "resolution_hours": 5.0, "cost_usd": 2800},
    {"equipment": "CHITTI Mark 2", "team_member": "Karthik Raja", "event_date": "2024-03-02", "component": "Left arm actuator", "issue": "Repulsor phase synchronization delay during heavy load test", "resolution": "Replaced actuator coil assembly with cold-rated unit", "resolution_hours": 6.0, "cost_usd": 3500},
    {"equipment": "CHITTI Mark 2", "team_member": "Priya Anand", "event_date": "2024-02-10", "component": "HUD display & Vision Unit", "issue": "Optical reflection artifact under direct sunlight", "resolution": "Recalibrated polarized camera filter and updated shader firmware", "resolution_hours": 1.5, "cost_usd": 300},
    {"equipment": "CHITTI Mark 2", "team_member": "Deepak V", "event_date": "2024-01-22", "component": "Battery management matrix", "issue": "Cell charge imbalance flagged during routine diagnostic", "resolution": "Rebalanced cell array and updated BMS balancing algorithm", "resolution_hours": 2.0, "cost_usd": 600},
    {"equipment": "CHITTI Mark 2", "team_member": "Karthik Raja", "event_date": "2024-03-25", "component": "Right boot thruster", "issue": "Vibration harmonic detected during flight hover test", "resolution": "Replaced thruster intake coupling and rebalanced rotor", "resolution_hours": 4.0, "cost_usd": 2100},

    # CHITTI Mark 1 maintenance
    {"equipment": "CHITTI Mark 1", "team_member": "Gokul", "event_date": "2024-02-03", "component": "Neural voice processor", "issue": "Audio buffer overrun during high-speed speech synthesis", "resolution": "Optimized memory allocation buffer in C++ backend", "resolution_hours": 1.0, "cost_usd": 0},
    {"equipment": "CHITTI Mark 1", "team_member": "Deepak V", "event_date": "2024-03-19", "component": "Arc power core", "issue": "Output fluctuation of ±1.5% under sustained combat load", "resolution": "Replaced primary plasma dampeners", "resolution_hours": 3.0, "cost_usd": 2400},
    {"equipment": "CHITTI Mark 1", "team_member": "Ananya Ramesh", "event_date": "2023-12-15", "component": "LIDAR vision sensor", "issue": "Minor lens abrasion after dusty field trial", "resolution": "Replaced protective sapphire glass lens", "resolution_hours": 2.0, "cost_usd": 500},
    {"equipment": "CHITTI Mark 1", "team_member": "CHITTI Automated Diagnostics", "event_date": "2024-03-28", "component": "Qdrant vector memory link", "issue": "Search latency spike of 3ms during dense retrieval", "resolution": "Re-indexed HNSW payload storage and optimized payload filter", "resolution_hours": 0.5, "cost_usd": 0},

    # Autonomous Mobile Robot AMR-1 maintenance
    {"equipment": "Autonomous Mobile Robot AMR-1", "team_member": "Gokul", "event_date": "2024-01-14", "component": "Left drive motor", "issue": "Intermittent slip under heavy industrial load", "resolution": "Replaced optical encoder and recalibrated motor controller", "resolution_hours": 4.0, "cost_usd": 1100},
    {"equipment": "Autonomous Mobile Robot AMR-1", "team_member": "Ananya Ramesh", "event_date": "2024-02-20", "component": "ROS2 SLAM navigation unit", "issue": "Drift in map localization during heavy warehouse interference", "resolution": "Updated ROS2 EKF node parameters and re-mapped facility", "resolution_hours": 2.5, "cost_usd": 400},

    # Drone Inspector Unit 2 maintenance
    {"equipment": "Drone Inspector Unit 2", "team_member": "Gokul", "event_date": "2024-03-02", "component": "LIDAR sensor array", "issue": "Optical noise flagged during night scan exercise", "resolution": "Cleaned lens housing and updated firmware noise filter", "resolution_hours": 1.5, "cost_usd": 250},
    {"equipment": "Drone Inspector Unit 2", "team_member": "Priya Anand", "event_date": "2024-03-22", "component": "Telemetry transmitter", "issue": "Packet drop observed during Operation Thunderstrike deployment", "resolution": "Re-aligned directional antenna array and updated RF modulation", "resolution_hours": 2.0, "cost_usd": 450},

    # CNC Sensor-Fusion Array 1 maintenance
    {"equipment": "CNC Sensor-Fusion Array 1", "team_member": "Kavitha S", "event_date": "2024-02-15", "component": "Vibration sensor node 4", "issue": "Calibration drift on high-speed CNC spindle sensor", "resolution": "Recalibrated piezo sensor node and validated fast FFT analysis", "resolution_hours": 1.0, "cost_usd": 200},

    # Perimeter Shield Alpha maintenance
    {"equipment": "Perimeter Shield Alpha", "team_member": "Gokul", "event_date": "2024-03-28", "component": "Protocol 17 force field transducer", "issue": "Acoustic dampener frequency drift of 0.2 kHz during Protocol 17 test", "resolution": "Re-aligned transducer nodes and verified emergency lockdown speed", "resolution_hours": 3.0, "cost_usd": 1500},

    # CHITTI Prototype 0 maintenance
    {"equipment": "CHITTI Prototype 0", "team_member": "Gokul", "event_date": "2023-08-10", "component": "Full frame & chassis", "issue": "Retired prototype frame replaced by CHITTI Mark 1", "resolution": "Unit decommissioned and transferred to research archive", "resolution_hours": 0.0, "cost_usd": 0},
]

OPERATIONS = [
    # CHITTI Mark 1 Operations
    {"equipment": "CHITTI Mark 1", "operation_date": "2024-01-05", "location": "Coimbatore Research Lab", "threat_level": 2, "duration_min": 45, "outcome": "success"},
    {"equipment": "CHITTI Mark 1", "operation_date": "2024-02-18", "location": "Chennai Innovation Hub", "threat_level": 3, "duration_min": 60, "outcome": "success"},
    {"equipment": "CHITTI Mark 1", "operation_date": "2024-03-22", "location": "Bay of Bengal (Operation Thunderstrike)", "threat_level": 5, "duration_min": 42, "outcome": "success"},
    {"equipment": "CHITTI Mark 1", "operation_date": "2024-03-28", "location": "Coimbatore Stealth AI Facility (Protocol 17 Lockdown)", "threat_level": 4, "duration_min": 30, "outcome": "success"},

    # CHITTI Mark 2 Operations
    {"equipment": "CHITTI Mark 2", "operation_date": "2024-01-20", "location": "Chennai Port Facility", "threat_level": 4, "duration_min": 54, "outcome": "success"},
    {"equipment": "CHITTI Mark 2", "operation_date": "2024-02-05", "location": "Extremis Containment Site (Chennai Port)", "threat_level": 5, "duration_min": 61, "outcome": "partial"},
    {"equipment": "CHITTI Mark 2", "operation_date": "2024-03-10", "location": "Coimbatore Tech Park", "threat_level": 2, "duration_min": 25, "outcome": "success"},

    # Autonomous Mobile Robot AMR-1 Operations
    {"equipment": "Autonomous Mobile Robot AMR-1", "operation_date": "2024-01-14", "location": "Chennai Logistics Warehouse", "threat_level": 1, "duration_min": 480, "outcome": "success"},
    {"equipment": "Autonomous Mobile Robot AMR-1", "operation_date": "2024-02-28", "location": "Salem Industrial Facility", "threat_level": 1, "duration_min": 360, "outcome": "success"},

    # Drone Inspector Unit 2 Operations
    {"equipment": "Drone Inspector Unit 2", "operation_date": "2024-01-08", "location": "Nilgiris Frontier Zone (Leo Rescue)", "threat_level": 3, "duration_min": 40, "outcome": "success"},
    {"equipment": "Drone Inspector Unit 2", "operation_date": "2024-03-02", "location": "Nevada Desert Test Range", "threat_level": 2, "duration_min": 35, "outcome": "success"},
    {"equipment": "Drone Inspector Unit 2", "operation_date": "2024-03-22", "location": "Bay of Bengal (Operation Thunderstrike)", "threat_level": 5, "duration_min": 42, "outcome": "success"},

    # CNC Sensor-Fusion Array 1 Operations
    {"equipment": "CNC Sensor-Fusion Array 1", "operation_date": "2024-02-15", "location": "Coimbatore CNC Manufacturing Facility", "threat_level": 1, "duration_min": 720, "outcome": "success"},

    # Perimeter Shield Alpha Operations
    {"equipment": "Perimeter Shield Alpha", "operation_date": "2024-03-28", "location": "Coimbatore Stealth AI Facility", "threat_level": 4, "duration_min": 15, "outcome": "success"},
]

INTEL_REPORTS = [
    {"codename": "Operation Thunderstrike", "status": "completed", "threat_level": 5, "summary": "Joint tactical drone swarm interception over the Bay of Bengal executed by Gokul, CHITTI Mark 1, and Drone Inspector Unit 2. Intercepted 120 hostile aerial targets in 42 minutes with zero impact to commercial shipping.", "report_date": "2024-03-22"},
    {"codename": "Protocol 17 Security Drill", "status": "active", "threat_level": 4, "summary": "Perimeter force field and emergency containment lockdown verified across all sectors of the Coimbatore Stealth AI Lab. Force field transducer nodes and acoustic dampeners responded within 2.8 seconds.", "report_date": "2024-03-28"},
    {"codename": "Vaathi Coming", "status": "active", "threat_level": 4, "summary": "Heavy deployment of tactical sensor nodes detected at the northern frontier. High vigilance and automated sensor-fusion relays maintained by Gokul's team.", "report_date": "2024-03-25"},
    {"codename": "Mastermind", "status": "completed", "threat_level": 5, "summary": "Strategic logistics & port security audit at Chennai Port completed successfully. Predictive maintenance sensors disabled unauthorized supply disruptions.", "report_date": "2024-02-15"},
    {"codename": "Leo Rescue", "status": "classified", "threat_level": 3, "summary": "Extraction of key research assets in the Nilgiris high-altitude zone completed under severe wind conditions using Drone Inspector Unit 2.", "report_date": "2024-01-10"},
]
