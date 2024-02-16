#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from SLiCAP import *

# Transmit amplifier
''' Notes:                                  '''
'''     Load => transmit coil               ''' 
'''     Expected power range, around -10dBm '''

Vi_max      = 1     # Maximum input voltage, peak
Zin         = 10e3  # Minimum input impedance
F_low       = 60    # -3dB start frequency
F_high      = 15e3  # -3dB stop frequency
Fpwr_low    = 60    #-3dB start frequency, full power
Fpwr_high   = 5e3   #-3dB stop frequency, full power

# Receive amplifier
''' Notes:                                  '''
'''     Input signal source => receive coil '''

Vo_max  = 0.25      #Vpk max at output, coil in center of loop.
Zin     = 2e3       #Input impedance
Vn      = 100e-6    # Output RMS noise, no signal; small signal bandwidth.

Fr_low = 60 # -3dB receive amplifier
Fr_high = 15e3 # -3dB receive amplifier
# Create table

specs = []

# Transmit amplifier
specs.append(
    specItem(
        "Vi_max",
        description = "Maximum input voltage; peak",
        value    = Vi_max,
        units       = "Vpk",
        specType    = "functional",
    )
)

specs.append(
    specItem(
        "Zin",
        description = "Minimum input impedance transmit amp",
        value    = Zin,
        units       = "Ohm",
        specType    = "functional",
    )
)

specs.append(
    specItem(
        "F_low",
        description = "-3dB frequency",
        value    = F_low,
        units       = "Hz",
        specType    = "functional",
    )
)

specs.append(
    specItem(
        "F_high",
        description = "-3dB frequency",
        value    = F_high,
        units       = "Hz",
        specType    = "functional",
    )
)

specs.append(
    specItem(
        "Fpwr_low",
        description = "-3dB frequency; full power",
        value    = Fpwr_low,
        units       = "Hz",
        specType    = "functional",
    )
)

specs.append(
    specItem(
        "Fpwr_high",
        description = "-3dB frequency; full power",
        value    = Fpwr_low,
        units       = "Hz",
        specType    = "functional",
    )
)

# Receive amplifier

specs.append(
    specItem(
        "Vo_max",
        description = "Vpk max at output, coil in center of loop.",
        value    = Vo_max,
        units       = "Vpk",
        specType    = "functional",
    )
)

specs.append(
    specItem(
        "Zin",
        description = "Minimum input impedance receive amp",
        value    = Zin,
        units       = "Ohm",
        specType    = "functional",
    )
)

specs.append(
    specItem(
        "Vn",
        description = "Noise voltage rms receive amp; no signal",
        value    = Vn,
        units       = "Vrms",
        specType    = "functional",
    )
)

specs.append(
    specItem(
        "Fr_low",
        description = "-3dB frequency",
        value    = Fr_low,
        units       = "Hz",
        specType    = "functional",
    )
)

specs.append(
    specItem(
        "Fr_high",
        description = "-3dB frequency",
        value    = Fr_high,
        units       = "Hz",
        specType    = "functional",
    )
)

# Save the specifications
specs2csv(specs, "specifications.csv")

# display the date on an html page

htmlPage("Specifications")
specs2html(specs)