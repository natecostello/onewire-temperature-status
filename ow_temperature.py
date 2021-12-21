import instrument_logger
import os

class TemperatureMonitor(instrument_logger.Instrument):

    def __init__(self, ow_id: str = None, name: str = None) -> None:
        if (ow_id is not None):
            self._id = ow_id
        else:
            raise ValueError('A one wire ID must be provided')
        
        if (name is not None):
            self._name = name
        else:
            self._name = ow_id

        self._uri = '/sys/bus/w1/devices/%s/w1_slave' % self._id
        
        # These tow lines mount the device:
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')
        
    @property
    def name(self) -> str:
        """Required by Instrument"""
        return self._name
    
    @property
    def allmeasurements(self) -> 'dict':
        """Required by Instrument"""
        all_meas = {}
        for param in self.parameters:
            all_meas[param] = self.getmeasurement(param)
        return all_meas

    @property
    def parameters(self) -> 'list[str]':
        """Required by Instrument"""
        return [
            self.name + '.Temperature.F'
        ]

    def getmeasurement(self, name: str) -> str:
        """Required by Instrument"""
        if (name == self.name + '.Temperature.F'):
             return str(self.readTemp())
    
    def readTemp(self):
        with open(self._uri,'rb') as file:
            text = file.read()
            ''' The text output from the probe looks like this:
                4a 01 4b 46 7f ff 06 10 f7 : crc=f7 YES
                4a 01 4b 46 7f ff 06 10 f7 t=20625
            '''
            lines = text.split('\n')
            # Read the last word of the first line to see if the CRC check passed
            if lines[0].split()[-1] == 'YES':
                # Read the raw temperature reading after the '=' sign on the second line
                rawTemp = float(lines[1].split('=')[-1])
                # Convert to Fahrenheit
                curTemp = ((rawTemp / 1000.0) * 1.8) + 32.0
                return curTemp
            else:
                curTemp = ''
                return curTemp

