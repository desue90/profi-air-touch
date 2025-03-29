from homeassistant.components.fan import FanEntity, FanEntityFeature
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.device_registry import DeviceInfo
from .const import DOMAIN, CONF_HOST, DEVICE_ID, PRESET_MODES
from .api import ProfiAirTouchAPI
import logging

_LOGGER = logging.getLogger(__name__)

# Constant for the fan
FAN_PROFI_AIR = "ventilation_system"

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
#    """Set up Profi-Air Touch Fan"""
    data_handler = hass.data[DOMAIN][entry.entry_id]["data_handler"]
    api = ProfiAirTouchAPI(entry.data[CONF_HOST])
    async_add_entities([ProfiAirTouchFan(data_handler, api)], True)

class ProfiAirTouchFan(FanEntity):

    _attr_has_entity_name = True
    _attr_supported_features = FanEntityFeature.PRESET_MODE

    def __init__(self, data_handler, api):
        self._attr_unique_id = f"{DOMAIN}_{FAN_PROFI_AIR}"
        self._attr_translation_key = FAN_PROFI_AIR
        self._data_handler = data_handler
        self._api = api
        self._attr_preset_modes = list(PRESET_MODES.values())

    @property
    def device_info(self) -> DeviceInfo:
        """Return the device info."""
        return DeviceInfo(
            identifiers={(DOMAIN, DEVICE_ID)},
            manufacturer="Fränkische",
            model="Profi-Air 250/400 Touch",
        )

    async def async_set_preset_mode(self, preset_mode: str):
        if preset_mode not in self._attr_preset_modes:
            _LOGGER.warning("Unvalid Preset-Mode: %s", preset_mode)
            return
        # Search for key from PRESET_MODES for the entered preset_mode
        key = next((k for k, v in PRESET_MODES.items() if v == preset_mode), None)
        if key is None:
            _LOGGER.warning("Unvalid Preset-Mode: %s", preset_mode)
            return
        # Perform the API-Request, to set the preset mode
        success = await self._api.async_set_fan_preset(key)
        if not success:
            _LOGGER.error("Error at setting preset mode: %s", preset_mode)

    async def async_update(self):
        await self._data_handler.update_status_xml()
        fan_level = self._data_handler.get_fan_level()
        self._attr_preset_mode = PRESET_MODES.get(fan_level, None)
