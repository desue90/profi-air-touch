from homeassistant.components.sensor import SensorEntity, SensorDeviceClass, SensorStateClass
from homeassistant.const import UnitOfTemperature
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import DOMAIN, CONF_HOST, DEVICE_ID
from .data_fetcher import ProfiAirTouchData

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    config = hass.data[DOMAIN][entry.entry_id]
    host = config[CONF_HOST]
    session = async_get_clientsession(hass)
    data_handler = ProfiAirTouchData(f"http://{host}/status.xml", session)

    # Update data bevor creating entity
    await data_handler.async_update()

    async_add_entities([OutsideAirTemperatureSensor(data_handler)], True)

class OutsideAirTemperatureSensor(SensorEntity):

    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS

    _attr_has_entity_name = True
    
    def __init__(self, data_handler):
        self._data_handler = data_handler
        self._attr_translation_key = "outside_air_temperature"
        self._attr_unique_id = f"{DOMAIN}_outside_air_temperature"
        self._attr_native_value = self._data_handler.data.get("aul0")

    @property
    def device_info(self) -> DeviceInfo:
        """Return the device info."""
        return DeviceInfo(
            identifiers={(DOMAIN, DEVICE_ID)},
            manufacturer="Fränkische",
            model="Profi-Air 250/400 Touch",
        )
    
    async def async_update(self):
        await self._data_handler.async_update()
