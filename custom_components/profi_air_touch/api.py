import aiohttp
import logging

_LOGGER = logging.getLogger(__name__)

class ProfiAirTouchAPI:
    def __init__(self, host: str):
        self._host = host

    async def async_set_fan_preset(self, preset: int) -> bool:
        """Set fan preset mode by sending an async HTTP request"""
        url = f"http://{self._host}/stufe.cgi?stufe={preset}"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=5) as response:
                    if response.status == 200:
                        return True
                    else:
                        _LOGGER.warning("Unexpected response code: %d", response.status)
                        return False
        except aiohttp.ClientError as e:
            _LOGGER.error("Error setting preset mode: %s", e)
            return False
