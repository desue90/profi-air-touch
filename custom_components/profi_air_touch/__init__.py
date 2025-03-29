from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN, PLATFORMS, CONF_HOST
from .data_fetcher import ProfiAirTouchData

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Profi-Air Touch from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    config = entry.data
    host = config[CONF_HOST]
    session = async_get_clientsession(hass)
    data_handler = ProfiAirTouchData(f"http://{host}/status.xml", session)
    await data_handler.update_status_xml()  # First update to get initial data
    hass.data[DOMAIN][entry.entry_id] = {
        "config": config,
        "data_handler": data_handler,
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok and entry.entry_id in hass.data[DOMAIN]:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok