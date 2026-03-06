# WiFi Temp Sensor ds18b20

Parameter | Implementation
-- | --
Description | Отправляет в топик `current_temp/pepeunit` значения датчика температуры `ds18b20`
Lang | `Micropython`
Hardware | `esp8266`, `esp32`, `esp32c3`, `esp32s3`, `ds18b20`, `резистор 4.7кОм`, `wires`
Firmware | [RELEASE-1.1.1](https://git.pepemoss.com/pepe/pepeunit/libs/pepeunit_micropython_client/-/releases/1.1.1)
Stack | `pepeunit_micropython_client`
Version | 1.1.1
License | AGPL v3 License
Authors | Ivan Serebrennikov <admin@silberworks.com>

## Schema

<div align="center"><img align="center" src="https://minio.pepemoss.com/public-data/image/wifi_temp_sensor.png"></div>

## Physical IO

- `client.settings.PIN_DS18B20` - Цифровое значение температуры от датчика `ds18b20`

## Env variable assignment

1. `PIN_DS18B20` - Номер пина для датчика `ds18b20`
2. `PUBLISH_SEND_INTERVAL` - Частота публикации данных в `current_temp/pepeunit` в миллисекундах
3. `PUC_WIFI_SSID` - Имя сети `WiFi`
4. `PUC_WIFI_PASS` - Пароль от сети `WiFi`

## Assignment of Device Topics

- `current_temp/pepeunit` - Текущая температура в текстовом формате (например, `27.5`)

## Work algorithm

1. Подключение к `WiFi`
2. Подключение к `MQTT` Брокеру
3. Инициализация датчика `ds18b20`
4. Каждые `PUBLISH_SEND_INTERVAL` миллисекунд публикуется значение температуры в `current_temp/pepeunit`

## Installation

1. Установите образ `Micropython` указанный в `firmware` на `esp8266`, как это сделано в [руководстве](https://micropython.org/download/ESP8266_GENERIC/)
2. Создайте `Unit` в `Pepeunit`
3. Установите переменные окружения в `Pepeunit`
4. Скачайте архив c программой из `Pepeunit`
5. Распакуйте архив в директорию
6. Загрузите файлы из директории на физическое устройство, например командой: `ampy -p /dev/ttyUSB0 -b 115200 put ./ .`
7. Запустить устройство нажатием кнопки `reset`
