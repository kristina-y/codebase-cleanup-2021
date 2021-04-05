
# import function

from app.shopping import format_usd

# test the function

def test_format_usd():
    assert format_usd(9.5) == "$9.50"
    assert format_usd(2.2222) == "$2.22"


# once we have some tests...

