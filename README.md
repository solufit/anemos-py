# Hello Projects Anemos

This library for Anemos API develop by Solufit.

Anemos API provides Weather Information, Earthquake Information and more.

Visit [Project Anemos Website](https://anemos.solufit.net)!

## Install

Install using `pip install -U anemos-py`.

## A Simple Example

### Using Anemos v2 API

#### Get Weather Information with postnumber

```python
from anemos.weather import AnemosObjectType, v2get

weather_informations = v2get("5320011")
```

Warning: Some **Ordinance designated city is not supported.** ( For example, Minato Ward, Tokyo)

Return Value Example

```python
[
    {
      "prefcode": null,
      "object_type": "Anemos.WeatherForecast",
      "regioncode": "270000",
      "title": "天気予報",
      "detail": {
        "weather_today": "101",
        "weather_tomorrow": "101",
        "max_temp": 28,
        "min_temp": 28,
        "rain_percent_now": 0,
        "rain_percent_6h": 10,
        "rain_percent_12h": 10,
        "rain_percent_18h": 10,
        "rain_percent_24h": 10,
        "rain_percent_30h": 0,
        "publishing_office": "大阪管区気象台",
        "reported_time": "2024-10-10T05:00:00+09:00"
      },
      "info_objectId": "5593591d-0de6-4d4a-a997-532c9eed1899",
      "areacode": null,
      "id": 178228,
      "status": "発表",
      "info_domain": "jma.go.jp",
      "reported_at": "2024-10-10T05:15:00"
    },
    {
      "prefcode": null,
      "object_type": "Anemos.WeatherWarning",
      "regioncode": null,
      "title": "大雨注意報",
      "detail": {
        "entryid": "20241007072516",
        "editorial_office": "大阪管区気象台",
        "publishing_office": "大阪管区気象台",
        "category": "大雨注意報",
        "datetime": "2024-10-07T07:25:15Z",
        "headline": "大阪府では、８日明け方まで急な強い雨や落雷に注意してください。",
        "pref": "大阪市"
      },
      "info_objectId": "51db0184-97b2-4040-9fe5-3aad9304c849",
      "areacode": "2710000",
      "id": 172614,
      "status": "解除",
      "info_domain": "jma.go.jp",
      "reported_at": "2024-10-07T16:30:00"
    },
    ・・・
]
```

#### Get Weather Information with postcode and objectType

```python
from anemos.weather import AnemosObjectType, v2get

weather_informations = v2get("5320011", AnemosObjectTypes.WeatherWarning)
```

## If you contact us

Repository developer is [Anemos Develop Team](mailto:kengo.handa@solufit.net) on Email.
