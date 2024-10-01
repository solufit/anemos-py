from datetime import datetime

from anemos.weather import AnemosObjectTypes, get, get_daily, get_weekly


def test_get():
    assert get("100-0005", datetime(2021, 1, 1), datetime(2021, 1, 2)) == []

def test_get_with_object_type():
    assert get("100-0005", datetime(2021, 1, 1), datetime(2021, 1, 2), AnemosObjectTypes.WeatherWarning) == []

def test_get_daily():
    assert get_daily("100-0005") == []

def test_get_weekly():
    assert get_weekly("100-0005") == []

