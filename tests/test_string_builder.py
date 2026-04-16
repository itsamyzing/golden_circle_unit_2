from lib.string_builder import *

def test_string_builder_starts_empty():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

def test_string_builder_starts_with_hello():
    builder = StringBuilder()
    builder.add("hello")
    result = builder.output()
    assert result == "hello"

def test_adding_a_string_sets_size_to_that_strings_size():
    string_builder = StringBuilder()
    string_builder.add("hello")
    assert string_builder.size() == 5

def test_adding_multiple_strings():
    string_builder = StringBuilder()
    string_builder.add("hello")
    string_builder.add(" ")
    string_builder.add("world")
    assert string_builder.output() == "hello world"

