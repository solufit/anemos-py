from .schemas import AnemosWeather, AnemosObjectTypes
from typing_extensions import deprecated
from datetime import datetime

@deprecated("この関数はv1以降で正式に実装される予定です。")
def get(postcode: str, start_date: datetime, end_date: datetime, object_type: AnemosObjectTypes | None = None) -> list[AnemosWeather]:
    return []

@deprecated("この関数はv1以降で正式に実装される予定です。")
def get_weekly(postcode: str) -> list[AnemosWeather]:
    return []

@deprecated("この関数はv1以降で正式に実装される予定です。")
def get_daily(postcode: str) -> list[AnemosWeather]:
    return []
