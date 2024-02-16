#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:31:22 2022

@author: anton
"""

from SLiCAP import *

fileName = "coupledCoilsSimple"
specFileName = "specifications.csv"

# Only generate the netlist after an update of the schematics
#makeNetlist(fileName + ".asc", "Coupled coils")

# Create an instruction object and associate a circuit with it:
i1 = instruction()
i1.setCircuit(fileName + ".cir")

# import the specifications
specs = csv2specs(specFileName)

# Define the circuit parameters from the specifications
specs2circuit(specs, i1)


# Display the circuit data on an HTML page
htmlPage("Circuit data")
head2html("Simple network model of the transfer measurement system")
text2html("""For frequencies below the resonance frequencies, we can ignore the
the parasitic capacitances. In addition, if at the highest frequency $f_{max}$
the load impedance is much larger than $2 \pi f_{max} L_r$, we can also ignore
the voltage induced in L1. The circuit can then be as simple as shown below.""")
img2html(fileName + ".svg", 400)
netlist2html(fileName + ".cir")
elementData2html(i1.circuit)

# Start a new html page for determination of the coupling factor
htmlPage("Determination of the coupling factor")
head2html("Simple network model of the transfer measurement with the HP3577A")
img2html(fileName + ".svg", 400)
head2html("Determination of the coupling factor using this model and the measurement results")
text2html("""
We will now determine the coupling factor of the two coupled inductors.
To this end, we determine the Laplace transform of the voltage transfer from
the source "V1" to the voltage at node "out". We use numeric analysis and
substitute $s=2\pi j f_m$, where $f_m$ is the measurement frequency.
Since the coupling factor has no numeric value it will remain symbolic in this
gain expression.
We then solve the coupling factor by equating this expresion with the measured
value..""")

i1.setSource("V1" )
i1.setDetector("V_out")
i1.setGainType("gain")
i1.setDataType("laplace")
i1.setSimType("numeric")

result = i1.execute()
# Obtain the laplace transform of the gain and display it on the html page
A_t = result.laplace
text2html("The transfer function is a function of the coupling factor:")
eqn2html("A_t", normalizeRational(A_t))
# Determine the squared magnitude of this transfer at the measurement frequency
A_t = A_t.subs(ini.Laplace, 2*sp.pi*sp.I*i1.getParValue('f_m'))
# The coupling facor is positive real
A_t = assumePosParams(A_t)
A_tsq = sp.N(sp.simplify(A_t*sp.conjugate(A_t))) # Fisrt simplify and then convert to numeric!

text2html("""The squared magnitude of this transfer at the measurement
frequency of this circuit is obtained as:""")
# Ignore an imaginary part (rounding error)
A_tsq = A_tsq.as_real_imag()[0]

# The function will be normalized before displaying it on the html page.
A_display = normalizeRational(clearAssumptions(A_tsq), var=sp.Symbol("k_c"))
eqn2html("A_tsq", A_display)

# Convert the measured dB value of the voltage transfer to the squared magnitude
text2html("""The measured value $A_{sq}$ of the squared voltage transfer at
this frequency amounts:""")
Atsq  = 10**(i1.getParValue('A_t')/10)
eqn2html("A_sq", Atsq)
# The coupling factor is found after equating the expression of the gain with
# the measurement results.

sols = sp.solve(A_tsq - Atsq)

# The correct solution is smaller than unity.
kc   = 0
for sol in sols:
    if sol < 1:
        kc = sol

text2html("Solving $A_{sq}=A_{tsq}$ yields:")
eqn2html("k_c", kc)

head2html("Modeled magnitude characteristic")
# Plot the magnitude of the transfer after substitution
result.laplace = result.laplace.subs(sp.Symbol('k_c'), kc)
text2html("Substitution of the value of $k_c$ in $A_t$ yields:")
eqn2html("A_t", normalizeRational(result.laplace))
text2html("""The figure below shows the magnitude plot. It should correspond
with the one measured with the network analyser. If not, the values of the
model parameters are incorrect, or the model is too simple and a more
elaborated model should be used.""")
figdBmagTransfer = plotSweep(fileName + "dBmagTransfer", "Loop antenna dBmag(transfer)", result, 0.5, 50, 500, sweepScale='k', funcType="dBmag", show=True)
# Display the plot on the html page
fig2html(figdBmagTransfer, 600)

# Add the value of the coupling factor to the specifications
specs.append(
    specItem(
        "k_c",
        description = "Send-receive coil coupling factor",
        value    = kc,
        units       = "",
        specType    = "interface",
    )
)

# Save the specifications
specs2csv(specs, "specifications.csv")

# Display the specifications on a html page.
htmlPage("Updated specifications")
specs2html(specs)