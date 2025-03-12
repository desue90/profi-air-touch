from homeassistant.components.fan import FanEntity, FanEntityFeature
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN, CONF_NAME, CONF_HOST, PRESET_MODES
from .api import ProfiAirTouchAPI

import logging

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
#    """Set up Profi-Air Touch Fan"""
    config = hass.data[DOMAIN][entry.entry_id]
    name = config[CONF_NAME]
    host = config[CONF_HOST]
    async_add_entities([ProfiAirTouchFan(name, host)], True)

class ProfiAirTouchFan(FanEntity):

    _attr_has_entity_name = True
    _attr_name = None
    _attr_supported_features = FanEntityFeature.PRESET_MODE

    def __init__(self, name: str, host: str):
        self._name = name
        self._attr_unique_id = f"profi_air_touch_{host}"
        self._api = ProfiAirTouchAPI(host)
        self._attr_preset_modes = list(PRESET_MODES.values())
        self._attr_preset_mode = "Feuchteschutz"

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self._attr_unique_id)},
            "name":  self._name,
            "manufacturer": "Fränkische",
            "model": "Profi-Air 250/400 Touch",
        }

    @property
    def unique_id(self) -> str:
        return self._attr_unique_id

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

