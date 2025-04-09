from homeassistant.components.number import NumberEntity, NumberDeviceClass
from homeassistant.const import UnitOfTemperature, UnitOfTime
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.device_registry import DeviceInfo
from .const import DOMAIN, CONF_HOST, DEVICE_ID
from .api import ProfiAirTouchAPI
import logging

_LOGGER = logging.getLogger(__name__)

NUMBER_ENTITIES = {
    "bypass_auto_outdoor_temp": {
        "xml_tag": "BipaAutAUL",
        "post_data": "ChangeBPAL",
        "icon": "mdi:thermometer-chevron-down",
        "min_value": 13,
        "max_value": 18,
        "step": 1,
        "unit": UnitOfTemperature.CELSIUS,
        "device_class": NumberDeviceClass.TEMPERATURE
    },
    "bypass_auto_exhaust_temp": {
        "xml_tag": "BipaAutABL",
        "post_data": "ChangeBPAB",
        "icon": "mdi:thermometer-chevron-up",
        "min_value": 18,
        "max_value": 28,
        "step": 1,
        "unit": UnitOfTemperature.CELSIUS,
        "device_class": NumberDeviceClass.TEMPERATURE
    },
    "party_timer": {
        "xml_tag": "partytime",
        "post_data": "ChangeMinutes",
        "icon": "mdi:clock-outline",
        "min_value": 10,
        "max_value": 240,
        "step": 1,
        "unit": UnitOfTime.MINUTES,
        "device_class": NumberDeviceClass.DURATION
    },
}

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    data_handler = hass.data[DOMAIN][entry.entry_id]["data_handler"]
    api = ProfiAirTouchAPI(entry.data[CONF_HOST])
    number = [ProfiAirTouchNumber(data_handler, api, sensor_id, props) for sensor_id, props in NUMBER_ENTITIES.items()]
    # Create number entities
    async_add_entities(number)

class ProfiAirTouchNumber(NumberEntity):

    _attr_has_entity_name = True

    def __init__(self, data_handler, api, sensor_id, props):
        self._attr_unique_id = f"{DOMAIN}_{sensor_id}"
        self._attr_translation_key = sensor_id
        self._data_handler = data_handler
        self._api = api
        self._xml_tag = props.get("xml_tag")
        self._post_data = props.get("post_data")
        self._attr_icon = props.get("icon")
        #self._attr_mode = "box" or "slider" or the default "auto"
        self._attr_native_min_value = props.get("min_value")
        self._attr_native_max_value = props.get("max_value")
        self._attr_native_step = props.get("step")
        self._attr_native_value = self._data_handler.data.get(self._xml_tag)
        self._attr_native_unit_of_measurement = props.get("unit")
        self._attr_device_class = props.get("device_class")

    @property
    def device_info(self) -> DeviceInfo:
        """Return the device info."""
        return DeviceInfo(
            identifiers={(DOMAIN, DEVICE_ID)},
            manufacturer="Fränkische",
            model="Profi-Air 250/400 Touch",
        )

    async def async_set_native_value(self, value: float) -> None:
        """Update the current value."""
        success = await self._api.async_set_number_native_value(self._post_data, value)
        if not success:
            _LOGGER.error("Failed to set value for %s: %s", self._post_data, value)


    async def async_update(self):
        """Update internal state from data handler."""
        self._attr_native_value = self._data_handler.data.get(self._xml_tag)