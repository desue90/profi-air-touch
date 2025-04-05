from homeassistant.components.sensor import SensorEntity, SensorDeviceClass, SensorStateClass
from homeassistant.const import UnitOfTemperature, UnitOfTime
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.device_registry import DeviceInfo
from .const import DOMAIN, DEVICE_ID

SENSOR_ENTITIES = {
    "fresh_air_temperature": {"xml_tag": "aul0", "unit": UnitOfTemperature.CELSIUS, "device_class": SensorDeviceClass.TEMPERATURE, "state_class": SensorStateClass.MEASUREMENT, "icon": "mdi:thermometer"},
    "supply_air_temperature": {"xml_tag": "zul0", "unit": UnitOfTemperature.CELSIUS, "device_class": SensorDeviceClass.TEMPERATURE, "state_class": SensorStateClass.MEASUREMENT, "icon": "mdi:thermometer"},
    "extract_air_temperature": {"xml_tag": "abl0", "unit": UnitOfTemperature.CELSIUS, "device_class": SensorDeviceClass.TEMPERATURE, "state_class": SensorStateClass.MEASUREMENT, "icon": "mdi:thermometer"},
    "exhaust_air_temperature": {"xml_tag": "fol0", "unit": UnitOfTemperature.CELSIUS, "device_class": SensorDeviceClass.TEMPERATURE, "state_class": SensorStateClass.MEASUREMENT, "icon": "mdi:thermometer"},
    "bypass_auto_outdoor_temp": {"xml_tag": "BipaAutAUL", "unit": UnitOfTemperature.CELSIUS, "device_class": SensorDeviceClass.TEMPERATURE, "icon": "mdi:arrow-decision-auto"},
    "bypass_auto_exhaust_temp": {"xml_tag": "BipaAutABL", "unit": UnitOfTemperature.CELSIUS, "device_class": SensorDeviceClass.TEMPERATURE, "icon": "mdi:arrow-decision-auto"},
    "bypass_control": {"xml_tag": "bypass", "icon": "mdi:arrow-decision-auto"},
    "program_manual_control": {"xml_tag": "control0", "icon": "mdi:cogs"},
    "language_select": {"xml_tag": "SprachWahl", "icon": "mdi:translate"},
    "filter_status": {"xml_tag": "filter0", "icon": "mdi:air-filter"},
    "filter_total_term": {"xml_tag": "filtertime", "unit": UnitOfTime.DAYS, "icon": "mdi:air-filter"},
    "filter_residual_term": {"xml_tag": "rest_time", "unit": UnitOfTime.DAYS, "icon": "mdi:air-filter"},
    "hours_usage_level_1": {"xml_tag": "BsSt1", "unit": UnitOfTime.HOURS, "icon": "mdi:timer-outline"},
    "hours_usage_level_2": {"xml_tag": "BsSt2", "unit": UnitOfTime.HOURS, "icon": "mdi:timer-outline"},
    "hours_usage_level_3": {"xml_tag": "BsSt3", "unit": UnitOfTime.HOURS, "icon": "mdi:timer-outline"},
    "hours_usage_level_4": {"xml_tag": "BsSt4", "unit": UnitOfTime.HOURS, "icon": "mdi:timer-outline"},
    "party_timer": {"xml_tag": "partytime", "unit": UnitOfTime.MINUTES, "icon": "mdi:clock-outline"},
    "mac_address": {"xml_tag": "config_mac", "icon": "mdi:identifier"},
}

    #"events": {"Clear faults"}  To Do Ergänzen

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    """Set up Profi-Air Touch Sensor Entities"""
    data_handler = hass.data[DOMAIN][entry.entry_id]["data_handler"]
    sensors = [ProfiAirTouchSensor(data_handler, sensor_id, props) for sensor_id, props in SENSOR_ENTITIES.items()]
    # Create sensor entities
    async_add_entities(sensors)

class ProfiAirTouchSensor(SensorEntity):

    _attr_has_entity_name = True

    def __init__(self, data_handler, sensor_id, props):
        self._attr_unique_id = f"{DOMAIN}_{sensor_id}"
        self._attr_translation_key = sensor_id
        self._data_handler = data_handler
        self._xml_tag = props.get("xml_tag")
        self._attr_icon = props.get("icon")
        self._attr_device_class = props.get("device_class")
        self._attr_state_class = props.get("state_class")
        self._attr_native_unit_of_measurement = props.get("unit")
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