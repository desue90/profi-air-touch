from homeassistant.components.sensor import SensorEntity, SensorDeviceClass, SensorStateClass
from homeassistant.const import UnitOfTemperature
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.device_registry import DeviceInfo
from .const import DOMAIN, DEVICE_ID

# Constants for the sensors
SENSOR_FRESH_AIR = "fresh_air_temperature"
SENSOR_SUPPLY_AIR = "supply_air_temperature"
SENSOR_EXTRACT_AIR = "extract_air_temperature"
SENSOR_EXHAUST_AIR = "exhaust_air_temperature"

# Constants for the XML-Tags for the sensor data
XML_TAG_FRESH_AIR = "aul0"
XML_TAG_SUPPLY_AIR = "zul0"
XML_TAG_EXTRACT_AIR = "abl0"
XML_TAG_EXHAUST_AIR = "fol0"

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    data_handler = hass.data[DOMAIN][entry.entry_id]["data_handler"]
    # Create sensor entities
    async_add_entities([
        TemperatureSensor(data_handler, SENSOR_FRESH_AIR, XML_TAG_FRESH_AIR),
        TemperatureSensor(data_handler, SENSOR_SUPPLY_AIR, XML_TAG_SUPPLY_AIR),
        TemperatureSensor(data_handler, SENSOR_EXTRACT_AIR, XML_TAG_EXTRACT_AIR),
        TemperatureSensor(data_handler, SENSOR_EXHAUST_AIR, XML_TAG_EXHAUST_AIR),
    ], True)

class TemperatureSensor(SensorEntity):

    _attr_has_entity_name = True
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
    
    def __init__(self, data_handler, sensor_id, xml_tag):
        self._attr_unique_id = f"{DOMAIN}_{sensor_id}"
        self._attr_translation_key = sensor_id
        self._data_handler = data_handler
        self._xml_tag = xml_tag 
        self._attr_native_value = self._data_handler.data.get(self._xml_tag)

    @property
    def device_info(self) -> DeviceInfo:
        """Return the device info."""
        return DeviceInfo(
            identifiers={(DOMAIN, DEVICE_ID)},
            manufacturer="Fränkische",
            model="Profi-Air 250/400 Touch",
        )

    async def async_update(self):
        self._attr_native_value = self._data_handler.data.get(self._xml_tag)