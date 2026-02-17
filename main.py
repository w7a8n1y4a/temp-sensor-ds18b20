import machine
import onewire
import ds18x20
import uasyncio as asyncio

from pepeunit_micropython_client.client import PepeunitClient


last_output_send_time = 0
ds_sensor = None
rom = None


def init_sensor(client):
    global ds_sensor, rom
    ds_sensor = ds18x20.DS18X20(onewire.OneWire(machine.Pin(int(client.settings.PIN_DS18B20))))
    roms = ds_sensor.scan()
    if not roms:
        client.logger.critical('DS18B20 not found on the bus')
        raise RuntimeError('DS18B20 not found on the bus')
    rom = roms[0]


async def output_handler(client: PepeunitClient):
    global last_output_send_time
    current_time = client.time_manager.get_epoch_ms()

    if (current_time - last_output_send_time) >= client.settings.PUBLISH_SEND_INTERVAL:
        try:
            ds_sensor.convert_temp()
            await asyncio.sleep_ms(750)
            current_temp = ds_sensor.read_temp(rom)
            await client.publish_to_topics('current_temp/pepeunit', str(current_temp))
            client.logger.debug('current_temp: ' + str(current_temp), file_only=True)
        except Exception as e:
            client.logger.error('Temp read error: ' + str(e))
        finally:
            last_output_send_time = current_time


async def input_handler(client: PepeunitClient, msg):
    return


async def main_async(client: PepeunitClient):
    client.set_mqtt_input_handler(input_handler)
    client.subscribe_all_schema_topics()
    client.set_output_handler(output_handler)

    init_sensor(client)

    await client.run_main_cycle()


if __name__ == '__main__':
    try:
        asyncio.run(main_async(client))
    except KeyboardInterrupt:
        raise
    except Exception as e:
        client.logger.critical(f"Error with reset: {str(e)}", file_only=True)
        client.restart_device()
