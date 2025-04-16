import logging
from aiohttp import ClientSession, ClientError

_LOGGER = logging.getLogger(__name__)

class ProfiAirTouchAPI:
    def __init__(self, host: str, session: ClientSession):
        self._host = host
        self._session = session

    async def async_set_fan_preset_mode(self, preset: int) -> bool:
        """Set fan preset mode by sending an async HTTP request"""
        preset_url = f"http://{self._host}/stufe.cgi?stufe={preset}"
        try:
            async with self._session.get(preset_url, timeout=5) as response:
                if response.status == 200:
                    return True
                else:
                    _LOGGER.warning("Unexpected response code: %d", response.status)
                    return False
        except ClientError as e:
            _LOGGER.error("Error setting preset mode: %s", e)
            return False

    async def async_set_number_native_value(self, post_key: str, value: float) -> bool:
        """Send JSON POST to set a number value on setup.htm."""
        setup_url = f"http://{self._host}/setup.htm"
        data = {post_key: int(value)}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        try:
            async with self._session.post(setup_url, data=data, headers=headers, timeout=5) as response:
                if response.status in (200, 302):
                    return True
                else:
                    _LOGGER.warning("Unexpected response code: %d for payload %s", response.status, data)
                    return False
        except ClientError as e:
            _LOGGER.error("Error in POST to %s: %s", setup_url, e)
            return False
