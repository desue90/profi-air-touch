# ToDo


- [ ] Get software-version and -release from "About" page

- [ ] Add select entity for summer-/wintertime:
      Wintertime    : soze0
      Summertime +1h: soze1

- [ ] Add "events": {"Clear faults"}:
      onclick="newAJAXCommand('filter.cgi?filter=1')
- [ ] Check if it's possible to send http requests to change things like clear faults and create a select entity out of it

- [ ] Remove Turn On/Off from Entity (at the moment this is displayed, but don't know why)

- [x] Add Icons for the available preset modes, e.g. mdi:fan-speed-1, *-2, *-3 and mdi:rocket:launch, as soon as this feature exists, see: https://community.home-assistant.io/t/new-thermostat-card-preset-icons/652861  
> [!NOTE]
> Icons for entity state attributes can be provided according to "Icon Translation" `- Examples include fan modes`, see: https://developers.home-assistant.io/docs/core/entity#icon-translations  

> [!IMPORTANT]
> I've added an icons.json according to the description, but it doesn't work  
- [ ] Check why Icon Translation doesn't work

- [ ] Check if entity "Climate" with HVACMode.FAN_ONLY, HVACAction.FAN, supported_features = PRESET_MODE (or FAN_MODE), PRESETS = ECO, AWAY, HOME, BOOST would be a better alternative to fan entity

- [ ] Firing event when filter need to be replaced, if possible. See: https://developers.home-assistant.io/docs/integration_events/

- [ ] Add connections (type, identifier) - in this case MAC-Address - in device registry

- [ ] Create common.py with BaseEntityClass for common entity stuff like device registry and attributes like _attr_has_entity_name = True. See: https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/common-modules

- [ ] Add check, if entered IP address is valid

- [ ] Maybe use MAC-Address as unique id according to https://developers.home-assistant.io/docs/entity_registry_index/#unique-id-requirements with homeassistant.helpers.device_registry.format_mac

- [ ] Change code from data_fetcher.py to coordinator.py with DataUpdateCoordinator according to the following documentation:  
https://developers.home-assistant.io/docs/integration_fetching_data/#coordinated-single-api-poll-for-data-for-all-entities

- [ ] Update README.md to new version updates

- [ ] On page "setup" it could be possible to change "Sensors" ON/OFF:
      onclick="newAJAXCommand('sensor.cgi?sensor=1') for ON
      onclick="newAJAXCommand('sensor.cgi?sensor=0') for OFF

- [ ] It should be possible to send client time to airCloud. Maybe add this one too

- [ ] Maybe add party_timer_rest_time as a sensor entity
