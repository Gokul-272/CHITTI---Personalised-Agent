"""
src/db/seed_data.py - deterministic, personalized seed rows for Gokul & CHITTI Personal Assistant DB.
"""

TASKS = [
    {"title": "Prepare presentation for GenAI RAG project", "category": "work", "priority": 5, "status": "in_progress", "due_date": "2024-04-05", "estimated_hours": 4.5},
    {"title": "Complete PyTest suite for NL2SQL pipeline", "category": "work", "priority": 4, "status": "completed", "due_date": "2024-03-30", "estimated_hours": 3.0},
    {"title": "Review Qdrant vector index performance metrics", "category": "work", "priority": 3, "status": "pending", "due_date": "2024-04-10", "estimated_hours": 2.0},
    {"title": "Study Deep Learning for SLAM Navigation", "category": "learning", "priority": 4, "status": "in_progress", "due_date": "2024-04-15", "estimated_hours": 10.0},
    {"title": "Renew AWS cloud infrastructure subscription", "category": "work", "priority": 5, "status": "completed", "due_date": "2024-03-25", "estimated_hours": 1.0},
    {"title": "Schedule annual health checkup", "category": "health", "priority": 3, "status": "pending", "due_date": "2024-04-20", "estimated_hours": 1.5},
    {"title": "Order replacement USB-C debug adapters", "category": "personal", "priority": 2, "status": "completed", "due_date": "2024-03-22", "estimated_hours": 0.5},
    {"title": "Build Streamlit multi-agent dashboard", "category": "project", "priority": 4, "status": "in_progress", "due_date": "2024-04-08", "estimated_hours": 6.0},
    {"title": "Calibrate robotics vision sensor lens", "category": "project", "priority": 2, "status": "pending", "due_date": "2024-04-18", "estimated_hours": 2.5},
]

SCHEDULE_EVENTS = [
    {"title": "Agentic AI Architecture Sync", "category": "meeting", "event_date": "2024-04-01", "duration_min": 60, "location": "Google Meet", "status": "scheduled"},
    {"title": "Coimbatore Tech Park Onsite Demo", "category": "work", "event_date": "2024-04-03", "duration_min": 180, "location": "Coimbatore Tech Park", "status": "scheduled"},
    {"title": "Deep Work - NL2SQL Engine Tuning", "category": "work", "event_date": "2024-03-28", "duration_min": 240, "location": "Home Office", "status": "completed"},
    {"title": "Robotics & Vision Research Standup", "category": "meeting", "event_date": "2024-03-29", "duration_min": 45, "location": "Chennai Innovation Hub", "status": "completed"},
    {"title": "Weekly Gym & Cardio Session", "category": "health", "event_date": "2024-03-31", "duration_min": 90, "location": "Fitness Center", "status": "scheduled"},
    {"title": "Dinner with Tech Mentors", "category": "personal", "event_date": "2024-04-06", "duration_min": 120, "location": "Coimbatore City Center", "status": "scheduled"},
]

CONTACTS = [
    {"name": "Priya Anand", "relationship_type": "colleague", "email": "priya.a@techlab.io", "phone": "+91-98765-43210", "notes": "Avionics & Sensor Fusion specialist; key collaborator on drone projects."},
    {"name": "Karthik Raja", "relationship_type": "colleague", "email": "karthik.r@techlab.io", "phone": "+91-98765-43211", "notes": "Embedded firmware engineer; handles motor control and microcontroller code."},
    {"name": "Dr. Sharma", "relationship_type": "mentor", "email": "sharma@ai-research.edu", "phone": "+91-98765-43212", "notes": "Robotics mentor and thesis advisor at university."},
    {"name": "Ananya Ramesh", "relationship_type": "colleague", "email": "ananya.r@techlab.io", "phone": "+91-98765-43213", "notes": "Computer vision & SLAM navigation engineer."},
    {"name": "Deepak V", "relationship_type": "friend", "email": "deepak.v@gmail.com", "phone": "+91-98765-43214", "notes": "Close friend from college; power systems enthusiast."},
]

EXPENSES = [
    {"contact_name": "Priya Anand", "expense_date": "2024-03-15", "category": "tech", "amount_usd": 250.00, "description": "High-precision IMU sensor module for SLAM robot prototype"},
    {"contact_name": "Karthik Raja", "expense_date": "2024-03-20", "category": "tech", "amount_usd": 120.00, "description": "STM32 microcontroller dev boards & CAN bus transceivers"},
    {"contact_name": None, "expense_date": "2024-03-22", "category": "learning", "amount_usd": 49.00, "description": "Generative AI Agentic Architecture online certification course"},
    {"contact_name": None, "expense_date": "2024-03-25", "category": "tech", "amount_usd": 85.00, "description": "Groq API cloud tokens & inference credit refill"},
    {"contact_name": "Deepak V", "expense_date": "2024-03-27", "category": "food", "amount_usd": 45.00, "description": "Team lunch meeting after successful RAG milestone deployment"},
    {"contact_name": None, "expense_date": "2024-03-29", "category": "travel", "amount_usd": 110.00, "description": "Travel expenses for Chennai Innovation Hub research presentation"},
]

PERSONAL_NOTES = [
    {"title": "Agentic Tool Calling Strategy", "category": "idea", "priority": 5, "summary": "Keep tool scopes narrow and deterministic. Use ReAct pattern with explicit thought steps before tool execution.", "created_date": "2024-03-20"},
    {"title": "Qdrant Vector Indexing Tip", "category": "reference", "priority": 4, "summary": "Use HNSW indexing with cosine similarity for fast MiniLM embedding lookups. Header-aware chunking preserves document context.", "created_date": "2024-03-24"},
    {"title": "Personal Assistant Goal 2024", "category": "goal", "priority": 5, "summary": "Build CHITTI into an indispensable daily assistant for task management, automated query resolution, and deep focus protection.", "created_date": "2024-03-26"},
    {"title": "PostgreSQL NL2SQL Safety Guard", "category": "reference", "priority": 4, "summary": "Enforce strict single-SELECT keyword filtering in guard.py and run queries under least-privilege chitti_readonly role.", "created_date": "2024-03-28"},
]

