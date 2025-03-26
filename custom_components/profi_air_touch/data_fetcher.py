from homeassistant.helpers.aiohttp_client import async_get_clientsession
import aiohttp
import xml.etree.ElementTree as ET
import logging

_LOGGER = logging.getLogger(__name__)

class ProfiAirTouchData:
    def __init__(self, url, session):
        self.url = url
        self.session = session
        self.data = {}

    async def async_update(self):
        try:
            async with self.session.get(self.url, timeout=10) as response:
                response.raise_for_status()
                content = await response.text()
                root = ET.fromstring(content)
                self.data = {child.tag: child.text.strip() for child in root}
        except aiohttp.ClientError as e:
            _LOGGER.error(f"Error retrieving the data: %s", e)
        except ET.ParseError as e:
            _LOGGER.error(f"Error parsing the XML data: %s", e)