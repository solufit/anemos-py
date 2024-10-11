"""
Anemos Weather Schemas
"""
from enum import Enum  # noqa: E0611
from pydantic import BaseModel  # noqa: E0611


class AnemosObjectTypes(Enum):
    WeatherWarning = "Anemos.WeatherWarning"
    WeatherForecast = "Anemos.WeatherForecast"
    Earthquake = "Anemos.Earthquake"

class AnemosWeather(BaseModel):
    object_type: str
    areacode: str | None
    title: str
    status: str
    detail: dict
    reported_at: str
    info_domain: str
    info_object_id: str
