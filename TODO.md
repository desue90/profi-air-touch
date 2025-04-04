# ToDo

- [ ] Remove Turn On/Off from Entity (at the moment this is displayed, but don't know why)

- [ ] Check if it's possible to send http requests to change things like party-level timer, bypass control, bypass automat temperatures, language, clear faults, change control (program or manual) and create a select entity out of it

- [x] Add Icons for the available preset modes, e.g. mdi:fan-speed-1, *-2, *-3 and mdi:rocket:launch, as soon as this feature exists, see: https://community.home-assistant.io/t/new-thermostat-card-preset-icons/652861  
> [!NOTE]
> Icons for entity state attributes can be provided according to "Icon Translation" `- Examples include fan modes`, see: https://developers.home-assistant.io/docs/core/entity#icon-translations  

> [!IMPORTANT]
> I've added an icons.json according to the description, but it doesn't work  
- [ ] Check why Icon Translation doesn't work

- [ ] Firing event when filter need to be replaced, if possible. See: https://developers.home-assistant.io/docs/integration_events/

- [ ] Add connections (type, identifier) - in this case MAC-Address - in device registry

- [ ] Create common.py with BaseEntityClass for common entity stuff like device registry and attributes like _attr_has_entity_name = True. See: https://developers.home-assistant.io/docs/core/integration-quality-scale/rules/common-modules

- [ ] Add check, if entered IP address is valid

- [ ] Maybe use MAC-Address as unique id according to https://developers.home-assistant.io/docs/entity_registry_index/#unique-id-requirements with homeassistant.helpers.device_registry.format_mac

- [ ] Change code from data_fetcher.py to coordinator.py with DataUpdateCoordinator according to the following documentation:  
https://developers.home-assistant.io/docs/integration_fetching_data/#coordinated-single-api-poll-for-data-for-all-entities

- [ ] Update README.md to new version updates
