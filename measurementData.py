#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:35:23 2022

@author: anton
"""
from SLiCAP import *
from sympy import pi

specFileName = "specifications.csv"

# import the specifications, we will add the measurement data to these specs
specs = csv2specs(specFileName)

# Receive coil impedance from data sheet
Rr = 235     # DC resistance
Lr = 0.1     # Inductance
fr = 100e3   # Resonance frequency

# Send coil impedance from measurement
Rs = 8.1     # Resistance
Ls = 314e-6  # Inductance
fs = 860e3   # Resonance frequency

# Transfer measurement for determination of coupling factor
RiRT = 1e6     # Test receiver input resistance
CiRT = 220e-12 # Test receiver input capacitance including 200cm cable
fm   = 1e3     # Measurement frequency
At   = -53.7   # Transfer from source to receive coil voltage (in dB)
               # Through measurement @fm with Ri= set to 1MOhm

# Calculation of parasitic capacitances
Cs = sp.N(1/(2*pi*fs)**2/Ls)
Cr = sp.N(1/(2*pi*fr)**2/Lr)

# Add all this data to the specifications

specs.append(
    specItem(
        "L_s",
        description = "Send coil inductance",
        value    = Ls,
        units       = "H",
        specType    = "interface",
    )
)

specs.append(
    specItem(
        "R_s",
        description = "Send coil resistance",
        value    = Rs,
        units       = "Omega",
        specType    = "interface",
    )
)

specs.append(
    specItem(
        "C_s",
        description = "Send coil capacitance",
        value    = Cs,
        units       = "F",
        specType    = "interface",
    )
)

specs.append(
    specItem(
        "L_r",
        description = "Receive coil inductance",
        value    = Lr,
        units       = "H",
        specType    = "interface",
    )
)

specs.append(
    specItem(
        "R_r",
        description = "Receive coil resistance",
        value    = Rr,
        units       = "Omega",
        specType    = "interface",
    )
)

specs.append(
    specItem(
        "C_r",
        description = "Receive coil capacitance",
        value    = Cr,
        units       = "F",
        specType    = "interface",
    )
)

specs.append(
    specItem(
        "R_iRT",
        description = "Test receiver input impedance",
        value    = RiRT,
        units       = "Omega",
        specType    = "test",
    )
)

specs.append(
    specItem(
        "C_iRT",
        description = "Test receiver input capacitance",
        value    = CiRT,
        units       = "F",
        specType    = "test",
    )
)

specs.append(
    specItem(
        "f_m",
        description = "Test measurement frequency",
        value    = fm,
        units       = "Hz",
        specType    = "test",
    )
)
specs.append(
    specItem(
        "A_t",
        description = "Send-receive voltage transfer at test frequency",
        value    = At,
        units       = "dB",
        specType    = "test",
    )
)

# Save the specifications
specs2csv(specs, "specifications.csv")