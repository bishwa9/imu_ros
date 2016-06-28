import serial


class serial_read:
    def __init__(self, serialPort_, baudRate_):
        self.serialPort = serial.Serial()
        self.serialPort.port = serialPort_
        self.serialPort.baudrate = baudRate_
        self.serialPort.bytesize = serial.EIGHTBITS  # number of bits per bytes
        self.serialPort.parity = serial.PARITY_NONE  # set parity check: no parity
        self.serialPort.stopbits = serial.STOPBITS_ONE  # number of stop bits
        self.serialPort.timeout = 1  # non-block read
        self.serialPort.xonxoff = False  # disable software flow control
        self.serialPort.rtscts = False  # disable hardware (RTS/CTS) flow control
        self.serialPort.dsrdtr = False  # disable hardware (DSR/DTR) flow control
        self.serialPort.writeTimeout = 2  # timeout for write

    def open_port(self):
        try:
            self.serialPort.open()
        except Exception, e:
            print "Error opening port:", str(e)

    def close_port(self):
        try:
            self.serialPort.close()
        except Exception, e:
            print "Error closing port:", str(e)

    def prepare_port(self):
        try:
            self.serialPort.flushInput()  # flush input buffer, discarding all its contents
            self.serialPort.flushOutput()  # flush output buffer, aborting current output
        except Exception, e:
            print "Error preparing port:", str(e)

    def read_data(self, expected_length):
        data_ = list()
        try:
            if self.serialPort.isOpen():
                data_e = self.serialPort.readline()
                data_e = data_e.rstrip()
                data_l = data_e.split()
                if len(data_l) is expected_length:
                    data_ = [float(num_) for num_ in data_l]
                else:
                    print "Unexpected data length"
            else:
                print "Port not open"

        except Exception, e:
            print "Error reading data:", str(e)
        return data_

#Example
ser = serial_read('/dev/tty.usbserial-AL00WV7C', 115200)
ser.open_port()
ser.prepare_port()
num = 0
while num < 1500:
    data_read = ser.read_data(3)
    print num, data_read
    num += 1
ser.close_port()