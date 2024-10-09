from .schemas import AnemosWeather, AnemosObjectTypes
from typing import List
# from typing_extensions import deprecated
from typing import Union
import requests

def v2get(postcode: str, object_type: Union[AnemosObjectTypes, None] = None) -> List[AnemosWeather]:
    """
    Get weather information by postcode.

    Args:
        postcode (str): The postcode of the location.
        object_type (AnemosObjectTypes, optional): The type of weather information to get. Defaults to None.

    Returns:
        List[AnemosWeather]: A list of weather information.
    """
    url = f"https://anemos-intra.solufit.net/v2/weather?postcode={postcode}"
    if object_type:
        url += f"&object_type={object_type.value}"
    response = requests.get(url)
    response.raise_for_status()
    return [AnemosWeather(**weather) for weather in response.json()[0]]
