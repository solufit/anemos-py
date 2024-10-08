"""
Anemos Weather Schemas
"""
from enum import Enum  # noqa: E0611


class AnemosObjectTypes(Enum):
    WeatherWarning = "Anemos.WeatherWarning"
    WeatherForecast = "Anemos.WeatherForecast"
    Earthquake = "Anemos.Earthquake"

class AnemosWeather:
    object_type: str
    areacode: str
    title: str
    status: str
    detail: str
    reported_at: str
    info_domain: str
    info_object_id: str
