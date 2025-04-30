from homeassistant.components.select import SelectEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.device_registry import DeviceInfo
from .const import DOMAIN, DEVICE_ID
import logging

_LOGGER = logging.getLogger(__name__)

BYPASS_CONTROL_OPTIONS = ["bypa0", "bypa1", "bypa2"]
CONTROL_OPTIONS = ["1", "0"]
LANGUAGE_OPTIONS = ["lang1", "lang2", "lang3", "lang4", "lang5"]

SELECT_ENTITIES = {
    "bypass_control": {
        "xml_tag": "bypass",
        "post_key": "bypassSt",
        "post_url": "setup.htm",
        "icon": "mdi:arrow-decision-auto",
        "options": BYPASS_CONTROL_OPTIONS
    },
    "program_manual_control": {
        "xml_tag": "control0",
        "post_key": "bed",
        "post_url": "wopla.htm",
        "icon": "mdi:cogs",
        "options": CONTROL_OPTIONS
    },
    "language_select": {
        "xml_tag": "SprachWahl",
        "post_key": "sprache",
        "post_url": "setup.htm",
        "icon": "mdi:translate",
        "options": LANGUAGE_OPTIONS
    },
}

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    data_handler = hass.data[DOMAIN][entry.entry_id]["data_handler"]
    api = hass.data[DOMAIN][entry.entry_id]["api"]
    selectors = [ProfiAirTouchSelector(data_handler, api, sensor_id, props) for sensor_id, props in SELECT_ENTITIES.items()]
    # Create select entities
    async_add_entities(selectors)

class ProfiAirTouchSelector(SelectEntity):

    _attr_has_entity_name = True

    def __init__(self, data_handler, api, sensor_id, props):
        self._attr_unique_id = f"{DOMAIN}_{sensor_id}"
        self._attr_translation_key = sensor_id
        self._data_handler = data_handler
        self._api = api
        self._xml_tag = props.get("xml_tag")
        self._post_key = props.get("post_key")
        self._post_url = props.get("post_url")
        self._attr_icon = props.get("icon")
        self._attr_options = props.get("options")
        self._attr_current_option = self._data_handler.get_mapped_value(self._xml_tag)

    @property
    def device_info(self) -> DeviceInfo:
        """Return the device info."""
        return DeviceInfo(
            identifiers={(DOMAIN, DEVICE_ID)},
            manufacturer="Fränkische",
            model="Profi-Air 250/400 Touch",
        )

    async def async_select_option(self, option: str) -> None:
        """Change the selected option."""
        success = await self._api.async_set_select_option(self._post_key, self._post_url, option)
        if not success:
            _LOGGER.error("Failed to set option for %s: %s", self._post_key, option)
        else:
            await self._data_handler.update_status_xml() # Necessary for faster status updates after change (Use DataUpdateCoordinator in the future)

    async def async_update(self):
        """Update internal state from data handler."""
        self._attr_current_option = self._data_handler.get_mapped_value(self._xml_tag)
