"""Sample test module to ensure at least one test present"""

import pytest


def test_sanity():
    """Check if at least a single unit test will work"""
    with pytest.raises(ValueError):
        raise ValueError()
