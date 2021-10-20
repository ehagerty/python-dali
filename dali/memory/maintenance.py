from .location import MemoryBank, MemoryLocation, MemoryRange, MemoryType, \
    FixedScaleNumericValue, TemperatureValue

# Memory bank definitions from DiiA Specification, DALI Part 253 -
# Diagnostics & Maintenance, Version 1.1, October 2019
BANK_207 = MemoryBank(207, 0x07, has_lock=True)

"""Rated Median Useful Life Of Luminaire in h

The parameter represents the rated median useful life time of the
luminaire (including light source and other components) as defined in
IEC62722-2-1:2014.

It is based on the L80/B50 criteria @ tq = 25°C

tq: rated ambient temperature of the luminaire as defined in
IEC62722-2-1:2014.

NOTE RatedMedianUsefulLifeOfLuminaire represents the rated median
useful life time of the luminaire including light source, control gear
and other components.
"""
RatedMedianUsefulLifeOfLuminaire = FixedScaleNumericValue(
    "RatedMedianUsefulLifeOfLuminaire",
    unit='h',
    scaling_factor=1000,
    locations=(MemoryLocation(bank=BANK_207, address=0x04, default=0xff,
                              type_=MemoryType.NVM_RW),)
)

"""Internal Control Gear Reference Temperature in °C

The parameter represents the internal control gear reference temperature.

The value is derived by the luminaire manufacturer by measuring the
value ControlGearTemperature at tq = 25°C, at rated luminaire power
(at 100% dimming level).

tq: rated ambient temperature of the luminaire as defined in
IEC62722-2-1:2014.
"""
InternalControlGearReferenceTemperature = TemperatureValue(
    "InternalControlGearReferenceTemperature",
    locations=(MemoryLocation(bank=BANK_207, address=0x05, default=0xff,
                              type_=MemoryType.NVM_RW),)
)

"""Rated Median Useful Light Source Starts

The parameter represents the rated median useful light source starts
of the luminaire.

A start is defined by 0 to 1 transition of the lampOn bit.
"""
RatedMedianUsefulLightSourceStarts = FixedScaleNumericValue(
    "RatedMedianUsefulLightSourceStarts",
    scaling_factor=100,
    locations=MemoryRange(bank=BANK_207, start=0x06, end=0x07, default=0xff,
                          type_=MemoryType.NVM_RW).locations
)
