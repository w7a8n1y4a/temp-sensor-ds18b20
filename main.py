import machine
import onewire
import ds18x20

from pepeunit_micropython_client.client import PepeunitClient


last_output_send_time = 0
ds_sensor = None
rom = None


def init_sensor(client):
    global ds_sensor, rom
    ds_sensor = ds18x20.DS18X20(onewire.OneWire(machine.Pin(int(client.settings.DS18B20_PIN_NUM))))
    roms = ds_sensor.scan()
    if not roms:
        client.logger.critical('DS18B20 not found on the bus')
        raise RuntimeError('DS18B20 not found on the bus')
    rom = roms[0]


def output_handler(client: PepeunitClient):
    global last_output_send_time
    current_time = client.time_manager.get_epoch_ms()

    if (current_time - last_output_send_time) / 1000 >= client.settings.PUBLISH_SEND_INTERVAL:
        try:
            ds_sensor.convert_temp()
            current_temp = ds_sensor.read_temp(rom)
            client.publish_to_topics('current_temp/pepeunit', str(current_temp))
            client.logger.debug('current_temp: ' + str(current_temp), file_only=True)
        except Exception as e:
            client.logger.error('Temp read error: ' + str(e))
        finally:
            last_output_send_time = current_time


def input_handler(client: PepeunitClient, msg):
    return


def main():
    client = PepeunitClient(
        env_file_path='/env.json',
        schema_file_path='/schema.json',
        log_file_path='/log.json',
        sta=sta
    )
    client.set_mqtt_input_handler(input_handler)
    client.mqtt_client.connect()
    client.subscribe_all_schema_topics()
    client.set_output_handler(output_handler)

    init_sensor(client)

    client.run_main_cycle()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        try:
            print('Error:', str(e))
        except Exception:
            pass
