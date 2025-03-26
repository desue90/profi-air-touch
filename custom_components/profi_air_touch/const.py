DOMAIN = "profi_air_touch"
PLATFORMS = [
    "fan",
    "sensor"
    ]

CONF_HOST = "host"

DEVICE_ID = f"{DOMAIN}_ventilation_system"

PRESET_MODES = {
    1: "feuchteschutz",
    2: "abwesend",
    3: "wohnen",
    4: "party"
}