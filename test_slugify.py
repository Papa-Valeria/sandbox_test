from slugify import slugify


def test_basic_words():
    assert slugify("Hello World") == "hello-world"


def test_multiple_spaces():
    assert slugify("Hello    World") == "hello-world"


def test_leading_and_trailing_spaces():
    assert slugify("  Hello World  ") == "hello-world"


def test_underscores_are_separators():
    assert slugify("hello_world") == "hello-world"


def test_mixed_separators_are_collapsed():
    assert slugify("hello _   world") == "hello-world"


def test_punctuation_is_removed():
    assert slugify("Hello, World!") == "hello-world"


def test_repeated_hyphens_are_collapsed():
    assert slugify("hello---world") == "hello-world"


def test_leading_and_trailing_hyphens_are_removed():
    assert slugify("---hello-world---") == "hello-world"


def test_numbers_are_preserved():
    assert slugify("Release 2026 Version 2") == "release-2026-version-2"


def test_empty_string():
    assert slugify("") == ""


def test_only_separators():
    assert slugify(" _ --- _ ") == ""