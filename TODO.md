# ToDo

- [ ] Remove Turn On/Off from Entity (at the moment this is displayed, but don't know why)

- [ ] Create other sensors out of information from status.xml like filter time

- [x] Add Icons for the available preset modes, e.g. mdi:fan-speed-1, *-2, *-3 and mdi:rocket:launch, as soon as this feature exists, see: https://community.home-assistant.io/t/new-thermostat-card-preset-icons/652861  
> [!NOTE]
> Icons for entity state attributes can be provided according to "Icon Translation" `- Examples include fan modes`, see: https://developers.home-assistant.io/docs/core/entity#icon-translations  
> [!IMPORTANT]
> I've added an icons.json according to the description, but it doesn't work  
- [ ] Check why Icon Translation doesn't work

- [ ] Add check, if entered IP address is valid

- [ ] Change code from data_fetcher.py to coordinator.py with DataUpdateCoordinator according to the following documentation:  
https://developers.home-assistant.io/docs/integration_fetching_data/#coordinated-single-api-poll-for-data-for-all-entities

- [ ] Update README.md to new version updates
