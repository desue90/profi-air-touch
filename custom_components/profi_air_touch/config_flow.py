import voluptuous as vol
from homeassistant import config_entries

from .const import DOMAIN, CONF_HOST

class ProfiAirTouchConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle the config flow for Profi-Air Touch"""

    Version = 1

    async def async_step_user(self, user_input=None):
        """UI for Input of IP-Address"""
        errors = {}

        if user_input is not None:
            host = user_input[CONF_HOST]

            return self.async_create_entry(title="Profi Air Touch", data={CONF_HOST: host})

        DATA_SCHEMA = vol.Schema(
            {
                vol.Required(CONF_HOST): str,
            }
        )

        return self.async_show_form(step_id="user", data_schema=DATA_SCHEMA, errors=errors)
