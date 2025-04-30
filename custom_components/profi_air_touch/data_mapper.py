BYPASS_TEXT_TO_OPTION = {
    "man.: offen": "bypa0",
    "man.: open": "bypa0",
    "man.: zu": "bypa1",
    "man.:close": "bypa1",
    "auto: offen": "bypa2",
    "auto: open": "bypa2",
    "auto: zu": "bypa2",
    "auto: close": "bypa2"
}

CONTROL_TEXT_TO_OPTION = {
    "programm aktiv": "1",
    "program active": "1",
    "manuelle stufenwahl": "0",
    "manual level choice": "0"
}

LANGUAGE_TEXT_TO_OPTION = {
    "deutsch": "lang1",
    "english": "lang2",
    "francais": "lang3",
    "italiano": "lang4",
    "nederlands": "lang5"
}

def get_option_for_value(xml_tag: str, raw_value: str) -> str | None:
    """Map raw value to internal option value."""
    value = raw_value.strip().lower()
    
    mapping_table = {
        "bypass": BYPASS_TEXT_TO_OPTION,
        "control0": CONTROL_TEXT_TO_OPTION,
        "SprachWahl": LANGUAGE_TEXT_TO_OPTION,
    }

    tag_mapping = mapping_table.get(xml_tag)
    if not tag_mapping:
        return None

    return tag_mapping.get(value)
