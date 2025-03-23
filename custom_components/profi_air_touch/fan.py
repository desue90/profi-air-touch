from homeassistant.components.fan import FanEntity, FanEntityFeature
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.device_registry import DeviceInfo

from .const import DOMAIN, CONF_HOST, DEVICE_ID, PRESET_MODES
from .api import ProfiAirTouchAPI

import logging

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
#    """Set up Profi-Air Touch Fan"""
    config = hass.data[DOMAIN][entry.entry_id]
    host = config[CONF_HOST]
    async_add_entities([ProfiAirTouchFan(host)], True)

class ProfiAirTouchFan(FanEntity):

    _attr_has_entity_name = True
    _attr_supported_features = FanEntityFeature.PRESET_MODE

    def __init__(self, host: str):
        self._attr_translation_key = "ventilation_level"
        self._attr_unique_id = f"{DOMAIN}_ventilation_level"
        self._api = ProfiAirTouchAPI(host)
        self._attr_preset_modes = list(PRESET_MODES.values())
        self._attr_preset_mode = "feuchteschutz"

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
            _LOGGER.warning("Ungültiger Preset-Modus: %s", preset_mode)
            return  # Ignoriere ungültige Werte

        # Suche den entsprechenden Schlüssel aus PRESET_MODES für den übergebenen preset_mode
        key = next((k for k, v in PRESET_MODES.items() if v == preset_mode), None)
        if key is None:
            return

        # Führe die API-Anfrage aus, um den Lüftermodus zu setzen
        success = await self.hass.async_add_executor_job(self._api.set_fan_preset, key)
        if success:
            self._attr_preset_mode = preset_mode
            self.async_write_ha_state()

