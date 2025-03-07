import voluptuous as vol
from homeassistant import config_entries

from .const import DOMAIN, CONF_HOST, CONF_NAME

class ProfiAirTouchConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle the config flow for Profi-Air Touch"""

    Version = 1

    async def async_step_user(self, user_input=None):
        """UI for Input of IP-Address"""
        errors = {}

        if user_input is not None:
            host = user_input[CONF_HOST]
            name = user_input[CONF_NAME]

            return self.async_create_entry(title=name, data={CONF_HOST: host, CONF_NAME: name})

        DATA_SCHEMA = vol.Schema(
            {
                vol.Required(CONF_NAME, default="Profi-Air Touch"): str,
                vol.Required(CONF_HOST): str,
            }
        )

        return self.async_show_form(step_id="user", data_schema=DATA_SCHEMA, errors=errors)
