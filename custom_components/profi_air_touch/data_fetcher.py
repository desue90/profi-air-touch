import xml.etree.ElementTree as ET
import logging
from aiohttp import ClientSession, ClientError
from .data_mapper import get_option_for_value

_LOGGER = logging.getLogger(__name__)

class ProfiAirTouchData:
    def __init__(self, url, session: ClientSession):
        self._url = url
        self._session = session
        self.data = {}

    async def update_status_xml(self):
        try:
            async with self._session.get(self._url, timeout=10) as response:
                response.raise_for_status()
                content = await response.text()
                root = ET.fromstring(content)
                self.data = {child.tag: child.text.strip() for child in root}
        except ClientError as e:
            _LOGGER.error(f"Error retrieving the data: %s", e)
        except ET.ParseError as e:
            _LOGGER.error(f"Error parsing the XML data: %s", e)

    def get_fan_level(self):
        for level in range (1, 5):
            if self.data.get(f"stufe{level}") == "1":
                return level
        return None

    def get_mapped_value(self, xml_tag: str) -> str | None:
        raw_value = self.data.get(xml_tag, "")
        return get_option_for_value(xml_tag, raw_value)
