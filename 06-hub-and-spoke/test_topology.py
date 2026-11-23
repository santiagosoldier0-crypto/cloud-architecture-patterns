import pytest

from topology import route


def test_spoke_traffic_passes_through_hub():
    assert route("spoke-a", "spoke-b") == ["spoke-a", "hub", "spoke-b"]


def test_unknown_spoke_is_rejected():
    with pytest.raises(ValueError):
        route("internet", "spoke-a")
