# WiFi Temp Sensor ds18b20

Parameter | Implementation
-- | --
Description | Отправляет в топик current_temp/pepeunit значения датчика температуры ds18b20
Lang | `Micropython`
Hardware | `esp8266`, `ds18b20`, `резистор 4.7кОм`, `wires`
Firmware | [ESP8266_GENERIC-v1.26.1-PEPEUNIT-v1.0.0.bin](https://git.pepemoss.com/pepe/pepeunit/libs/pepeunit_micropython_client/-/package_files/51/download)
Stack | `pepeunit_micropython_client`
Version | 0.0.0
License | AGPL v3 License
Authors | Ivan Serebrennikov <admin@silberworks.com>

## Schema

<div align="center"><img align="center" src="https://i.ibb.co/PcjGvXQ/wifi-temp-sensor.png"></div>

## Physical IO

- `client.settings.DS18B20_PIN_NUM` - Цифровое значение температуры от датчика `ds18b20`

## Env variable assignment

1. `WIFI_SSID` - Имя сети WiFi
2. `WIFI_PASS` - Пароль от сети WiFi
3. `PUBLISH_SEND_INTERVAL` - Частота публикации данных в `current_temp/pepeunit` в секундах
4. `DS18B20_PIN_NUM` - Номер пина для датчика `ds18b20`

## Assignment of Device Topics

- `current_temp/pepeunit` - Текущая температура в текстовом формате (например, `27.5`)

## Work algorithm

1. Подключение к WiFi
2. Инициализация датчика ds18b20
3. Подключение к MQTT Брокеру
4. Каждые PUBLISH_SEND_INTERVAL секунд публикуются сообщения в current_temp/pepeunit

## Installation

1. Установите образ `Micropython` указанный в `firmware` на `esp8266`, как это сделано в [руководстве](https://micropython.org/download/ESP8266_GENERIC/)
2. Создайте `Unit` в `Pepeunit`
3. Установите переменные окружения в `Pepeunit`
4. Скачайте архив c программой из `Pepeunit`
5. Распакуйте архив в директорию
6. Загрузите файлы из директории на физическое устройство, например командой: `ampy -p /dev/ttyUSB0 -b 115200 put ./ .`
7. Запустить устройство нажатием кнопки `reset`
