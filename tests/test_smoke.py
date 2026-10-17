from assistant.rules import reply


def test_greeting():
    assert "Hello" in reply("hi")


def test_office_lookup():
    assert "I.101" in reply("Where is the Training Office?")


def test_partial_training_office_name():
    assert "I.101" in reply("Where is training?")


def test_partial_student_affairs_name():
    assert "I.102" in reply("Where is student?")


def test_generic_office_word_is_not_a_partial_match():
    assert "don't know" in reply("Where is the office?")


def test_help():
    answer = reply("help")
    assert "where" in answer
    assert "when" in answer


def test_unknown():
    assert "don't know" in reply("what is the meaning of life")


def test_empty():
    assert reply("   ") == "Please type a question."


def test_math_lookup():
    assert "I.603" in reply("Where is the Faculty of Math & Computer Science?")


def test_student_lookup():
    assert "I.604" in reply("Where is the Faculty of Information Technology?")
