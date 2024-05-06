from ... import ProprietarySentence, nmea_utils
from datetime import datetime

class SSN(ProprietarySentence):
    sentence_types = {}

    def __new__(_cls, manufacturer, data):
        name = manufacturer + data[1]
        cls = _cls.sentence_types.get(name, _cls)
        return super(SSN, cls).__new__(cls)

    def __init__(self, manufacturer, data):
        self.sentence_type = manufacturer + data[1]
        super(SSN, self).__init__(manufacturer, data[2:])

    def identifier(self):
        return 'P%s,' % (self.sentence_type)
    
class SSNHRP(SSN, nmea_utils.DatetimeFix):
    
    fields = (
        ("Timestamp", "timestamp", nmea_utils.timestamp),
        ("Datestamp", "datestamp", nmea_utils.datestamp),
        ("Heading", "heading", float),
        ("Roll", "roll", float),
        ("Pitch", "pitch", float),
        ("Heading Standard Deviation", "heading_std", float),
        ("Roll Standard Deviation", "roll_std", float),
        ("Pitch Standard Deviation", "pitch_std", float),
        ("Number of Satellites", "num_sats", int),
        ("Mode Indicator", "mode_indicator"),
        ("Magnetic Variation", "magnetic_variation", float),
        ("Magnetic Variation Dir", "magnetic_variation_dir")
    )