import minimalmodbus

from S_Temp_VWC_EC_02_SKU101990667 import S_Temp_VWC_EC_02_SKU101990667

port = "/dev/ttyUSB0"  #for Linux      NEED TO BE SET ACCORDING TO YOUR SYSTEM
#port = "COM6"         #for Windows    NEED TO BE SET ACCORDING TO YOUR SYSTEM

instr = minimalmodbus.Instrument(port = port, \
                                 slaveaddress = None, \
                                 mode = minimalmodbus.MODE_RTU, \
                                 close_port_after_each_call = True, \
                                 debug = False)
instr.serial.baudrate = 9600;
instr.serial.bytesize = minimalmodbus.serial.EIGHTBITS
instr.serial.parity = minimalmodbus.serial.PARITY_NONE
instr.serial.stopbits = minimalmodbus.serial.STOPBITS_ONE
instr.serial.timeout = 1

soil_sensor_1 = S_Temp_VWC_EC_02_SKU101990667(instr, slaveAddress = 1)

temperature, vwc, ec, salinity, tds, epsilon = soil_sensor_1.get_data()

print(temperature, vwc, ec, salinity, tds, epsilon)  