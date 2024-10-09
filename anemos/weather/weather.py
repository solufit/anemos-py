from .schemas import AnemosWeather, AnemosObjectTypes
from typing import List
from typing_extensions import deprecated
from datetime import datetime
from typing import Union
import requests

@deprecated("この関数はv1以降で正式に実装される予定です。")
def get(postcode: str, object_type: Union[AnemosObjectTypes, None] = None) -> List[AnemosWeather]:
    return []

@deprecated("この関数はv1以降で正式に実装される予定です。")
def get_weekly(postcode: str) -> List[AnemosWeather]:
    return []

@deprecated("この関数はv1以降で正式に実装される予定です。")
def get_daily() -> List[AnemosWeather]:
    return []
