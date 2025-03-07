import requests

class ProfiAirTouchAPI:
    def __init__(self, host: str):
        self._host = host

    def set_fan_preset(self, preset: int) -> bool:
        """Set fan preset mode by sending HTTP request"""
        url = f"http://{self._host}/stufe.cgi?stufe={preset}"
        try:
            response = requests.get(url, timeout=5)
            return response.status_code == 200
        except requests.RequestException:
            return False
