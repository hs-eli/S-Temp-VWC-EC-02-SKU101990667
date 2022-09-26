class S_Temp_VWC_EC_02_SKU101990667:
    READ_INPUT_REGISTER = 4
    
    def __init__(self, instr, slaveAddress):
        self.instr = instr
        self.slaveAddress = slaveAddress
    
    def get_data(self):
        self.instr.address = self.slaveAddress
        
        temperature = 0.0  #soil temperature         [°C]
        vwc = 0.0          #volumetric water content [%]
        ec =  0.0          #electrical conductivity  [us/cm]
        salinity = 0.0     #salinity of soil         [mg/L]
        tds = 0.0          #total dissolved solids   [mg/L]
        epsilon = 0.0      #dielectric constant      []
        
        temperature = (self.instr.read_register(registeraddress = 0, number_of_decimals = 2, functioncode = self.READ_INPUT_REGISTER, signed = True))
        vwc = (self.instr.read_register(registeraddress = 1, number_of_decimals = 2, functioncode = self.READ_INPUT_REGISTER, signed = False))
        ec = (self.instr.read_register(registeraddress = 2, number_of_decimals = 0, functioncode = self.READ_INPUT_REGISTER, signed = False))
        salinity = (self.instr.read_register(registeraddress = 3, number_of_decimals = 0, functioncode = self.READ_INPUT_REGISTER, signed = False))
        tds = (self.instr.read_register(registeraddress = 4, number_of_decimals = 0, functioncode = self.READ_INPUT_REGISTER, signed = False))
        epsilon = (self.instr.read_register(registeraddress = 5, number_of_decimals = 2, functioncode = self.READ_INPUT_REGISTER, signed = False))
        
        return temperature, vwc, ec, salinity, tds, epsilon