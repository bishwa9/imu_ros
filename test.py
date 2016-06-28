import serialRead
import imu_parser


# Example
imu_parser_ = imu_parser.imu_parser()
ser = serialRead.serial_read('/dev/tty.usbserial-AL00WV7C', 115200)
ser.open_port()
ser.prepare_port()
num = 0
while num < 1500:
    data_read = ser.read_data(6)
    data_read_scaled = imu_parser_.parse_data(data_read)
    print data_read_scaled
    num += 1
ser.close_port()