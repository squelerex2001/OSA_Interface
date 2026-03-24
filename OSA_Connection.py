import pyvisa

OSA_ADDRESS = ""

rm = pyvisa.ResourceManager()
print(rm.list_resources())

#OSA = rm.open_resource(OSA_ADDRESS)
#print("OSA IDN = " + OSA.query("*IDN?"))

"""
import pyvisa
rm = pyvisa.ResourceManager()
rm.list_resources()
('ASRL1::INSTR', 'ASRL2::INSTR', 'GPIB0::12::INSTR')
inst = rm.open_resource('GPIB0::12::INSTR')
print(inst.query("*IDN?"))
"""