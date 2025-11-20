# WiFi Temp Sensor ds18b20

Parameter | Implementation
-- | --
Discription | Отправляет значения датчика температуры
Lang | `Micropython`
Hardware | `esp8266`, `ds18b20`, `1х резистор 4.7кОм`, `wires`
Firmware | [ESP8266_GENERIC-v1.26.1-PEPEUNIT-v0.10.0.bin](https://git.pepemoss.com/pepe/pepeunit/libs/pepeunit_micropython_client/-/package_files/43/download)
Stack | `pepeunit_micropython_client`

## Schematic Diagram
![img](https://i.ibb.co/PcjGvXQ/wifi-temp-sensor.png)

## Physical IO
- `machine.Pin([client.settings.DS18B20_PIN_NUM])` настроен на получение цифрового значения температуры от датчика `ds18b20`
 
## env_example.json

```json
{
    "DS18B20_PIN_NUM": 12,
    "PUBLISH_SEND_INTERVAL": 10,
    "WIFI_SSID": "ssid",
    "WIFI_PASS": "password",
    "PEPEUNIT_URL": "unit.example.com",
    "PEPEUNIT_APP_PREFIX": "/pepeunit",
    "PEPEUNIT_API_ACTUAL_PREFIX": "/api/v1",
    "HTTP_TYPE": "https",
    "MQTT_URL": "emqx.example.com",
    "MQTT_PORT": 1883,
    "PEPEUNIT_TOKEN": "jwt_token",
    "SYNC_ENCRYPT_KEY": "32_bit_encrypt_key",
    "SECRET_KEY": "32_bit_secret_key",
    "PING_INTERVAL": 30,
    "STATE_SEND_INTERVAL": 300,
    "MIN_LOG_LEVEL": "Debug",
    "MAX_LOG_LENGTH": 64
}

```

### Env variable assignment
1. `WIFI_SSID` - имя сети `WiFi` в которой будет работать устройство
1. `WIFI_PASS` - пароль от сети `WiFI` в которой будет работать устройство
1. `PUBLISH_SEND_INTERVAL` - частота публикации данных в `current_temp/pepeunit` указывать нужно в секундах
1. `DS18B20_PIN_NUM` - номер пина на который припаян датчик `ds18b20`

## schema_example.json

```json
{   
    "input_base_topic": [
        "update/pepeunit",
        "env_update/pepeunit",
        "schema_update/pepeunit",
        "log_sync/pepeunit"
    ],
    "output_base_topic": [
        "state/pepeunit",
        "log/pepeunit"
    ],
    "input_topic": [],
    "output_topic": [
        "current_temp/pepeunit"
    ]
}
```

### Assignment of Device Topics
- `output` `current_temp/pepeunit` - текущая температура в текстовом формате - `27.5`

## Work algorithm
Алгоритм работы с момента нажатия кнопки включения:
1. Подключение к `WiFI`
1. Инициализация датчика `DS18B20`
1. Подключение к `MQTT Брокеру`
1. Каждые `PUBLISH_SEND_INTERVAL` секунд публикуются сообщения в `current_temp/pepeunit`
