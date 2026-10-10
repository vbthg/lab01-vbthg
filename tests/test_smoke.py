import pytest

from assistant.rules import reply


def test_greeting():
    assert "Hello" in reply("hi")


@pytest.mark.parametrize(
    "message", ["good morning", "GOOD MORNING", "  Good morning!  ", "Good morning?"]
)
def test_good_morning_greeting(message):
    assert reply(message) == "Hello! Ask me where an office is, or when it opens."


def test_office_lookup():
    assert "I.101" in reply("Where is the Training Office?")


def test_unknown():
    assert "don't know" in reply("what is the meaning of life")


def test_empty():
    assert reply("   ") == "Please type a question."
