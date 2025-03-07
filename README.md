# fraenkische-profi-air-touch

[![GitHub Release](https://img.shields.io/github/release/desue90/profi-air-touch.svg)](https://github.com/desue90/profi-air-touch/releases)
[![License](https://img.shields.io/github/license/desue90/profi-air-touch.svg)](https://github.com/desue90/profi-air-touch/blob/main/LICENSE)

Home Assistant Integration for Fränkische Profi-Air 250/400 Touch

## Features

This integration allows you to set the ventilation level of your controlled domestic ventilation via home assistant. This works via the following HTTP request:
`http://{self._host}/stufe.cgi?stufe={preset}`
`{self._host}` = IP address of the ventilation system
`{preset}` = level number 1 to 4

## Requirements

The following requirements must be met:
* The ventilation system must be connected to the home network and accessible via a fixed IP address
* The "Control" must be set to "manual" in the "Week Schedule"

## Installation

Follow these steps to deploy the integration to Home Assistant.
You can choose to deploy it with HACS or manually

### HACS

1. Make sure you have HACS installed or [install it now](https://hacs.xyz/docs/use/download/download/)
2. Open HACS in Home Assistant
3. Click on the 3 dots in the top right corner
4. Select "Custom repositories"
5. Add the URL `https://github.com/desue90/profi-air-touch` to "Repository" and select "Integration" as "Type"
6. Click the "ADD" button
7. Close the "Custom repositories" window
8. Search for "Profi-Air Touch" in HACS and open the integration by clicking on it
9. Press the download button

### Manual

1. [Download the latest release](https://github.com/desue90/profi-air-touch/releases)
2. Extract the `custom_components` folder to your Home Assistant's config folder. The resulting folder structure should be `config/custom_components/profi_air_touch`

## Setting up the Integration

1. Restart Home Assistant
2. After restart go to Settings > Devices & services
3. Click [ADD INTEGRATION](https://my.home-assistant.io/redirect/config_flow_start/?domain=profi_air_touch) and select "Profi-Air Touch"
5. Enter a name and the IP address for the ventilation system

## Tested Setup

* Fränkische Profi-Air 400 Touch

## Contribute

If you want to help, put a ⭐ to the repository and open issues or pull requests to contribute to the development.
