"""
tests/unit/test_chunking.py - regression tests for src/core/chunking.py.
"""

from src.core.chunking import INGESTION_PLAN, build_all_chunks


def test_build_all_chunks_covers_every_file_with_no_empty_chunks():
    chunks = build_all_chunks()
    assert len(chunks) > 0
    for text, meta in chunks:
        assert text.strip(), f"empty chunk produced for {meta}"
        assert meta["doc_type"]
        assert meta["source"]
        assert meta["strategy"]


def test_every_ingestion_plan_entry_produces_at_least_one_chunk():
    for chunk_fn, filename, doc_type in INGESTION_PLAN:
        chunks = chunk_fn(filename, doc_type)
        assert len(chunks) > 0, f"{filename} via {chunk_fn.__name__} produced zero chunks"


def test_about_me_chunking_keeps_profile_fields_together():
    chunks = [c for c in build_all_chunks() if c[1]["doc_type"] == "about_me"]
    assert len(chunks) == 6
    titles = {meta["title"] for _text, meta in chunks}
    assert titles == {
        "Name / Nickname",
        "Location / Time Zone",
        "Languages",
        "Occupation",
        "General Background",
        "What Matters",
    }
    combined_text = " ".join(text for text, _meta in chunks)
    assert "Gokul" in combined_text
    assert "Coimbatore" in combined_text
    assert "Tamil" in combined_text


def test_coding_profile_chunking_captures_development_preferences():
    chunks = [c for c in build_all_chunks() if c[1]["doc_type"] == "coding_profile"]
    assert len(chunks) == 5
    combined_text = " ".join(text for text, _meta in chunks)
    assert "Python" in combined_text
    assert "FastAPI" in combined_text
    assert "debug" in combined_text.lower()


def test_education_history_chunking_keeps_education_context_together():
    chunks = [c for c in build_all_chunks() if c[1]["doc_type"] == "education_history"]
    assert len(chunks) == 5
    combined_text = " ".join(text for text, _meta in chunks)
    assert "B.E." in combined_text or "Bachelor" in combined_text
    assert "Coimbatore Institute" in combined_text


def test_work_style_and_goals_docs_are_available_for_broader_question_types():
    work_style = [c for c in build_all_chunks() if c[1]["doc_type"] == "work_style"]
    qualities = [c for c in build_all_chunks() if c[1]["doc_type"] == "qualities"]
    goals = [c for c in build_all_chunks() if c[1]["doc_type"] == "goals"]
    learning_style = [c for c in build_all_chunks() if c[1]["doc_type"] == "learning_style"]
    projects = [c for c in build_all_chunks() if c[1]["doc_type"] == "projects_portfolio"]

    assert len(work_style) == 5
    assert len(qualities) == 4
    assert len(goals) == 3
    assert len(learning_style) == 4
    assert len(projects) == 3

    combined = " ".join(text for text, _meta in work_style + qualities + goals + learning_style + projects)
    assert "deep work" in combined.lower()
    assert "discipline" in combined.lower()
    assert "robotics" in combined.lower()
    assert "open-source" in combined.lower() or "open source" in combined.lower()


def test_preferences_chunking_keeps_recommendation_rules_and_tastes_together():
    chunks = [c for c in build_all_chunks() if c[1]["doc_type"] == "preferences"]
    assert len(chunks) == 6
    titles = {meta["title"] for _text, meta in chunks}
    assert titles == {
        "Food Preferences",
        "Music and Movies",
        "Technology Preferences",
        "Recommendation Style",
        "Things I Dislike",
        "Decision-Making Preferences",
    }
    combined_text = " ".join(text for text, _meta in chunks)
    assert "biryani" in combined_text.lower()
    assert "synthwave" in combined_text.lower()
    assert "concise" in combined_text.lower()


def test_relationships_and_memory_ingestion_cover_the_new_personal_schema():
    important_people = [c for c in build_all_chunks() if c[1]["doc_type"] == "important_people"]
    assert len(important_people) == 3
    person_01 = [c for c in build_all_chunks() if c[1]["doc_type"] == "person_01"]
    person_02 = [c for c in build_all_chunks() if c[1]["doc_type"] == "person_02"]
    memories = [c for c in build_all_chunks() if c[1]["doc_type"] == "memories"]

    assert len(person_01) == 2
    assert len(person_02) == 2
    assert len(memories) == 4

    memory_categories = {meta["category"] for _text, meta in memories}
    assert memory_categories == {"communication", "learning", "goals", "decision-making"}

    for text, _meta in memories:
        assert text.strip()
