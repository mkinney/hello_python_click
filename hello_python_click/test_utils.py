import hello_python_click.utils


def test_lower():
    assert hello_python_click.utils.lower("Mike") == "mike"
