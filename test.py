import serialRead

a_s = 0
g_s = 0
g = 0

settings_file = open('imu.settings', 'r')

for l in settings_file.readlines():
    setting = l.split()
    if setting[0] == 'Accelerometer_Scale':
        if setting[1] == '0':
            a_s = 8192
        elif setting[1] == '1':
            a_s = 4096
        elif setting[1] == '2':
            a_s = 2048
        elif setting[1] == '3':
            a_s = 1024
        print "A scale = +-", a_s, "g"

    if setting[0] == 'Gyro_Scale':
        if setting[1] == '0':
            g_s = 131
        elif setting[1] == '1':
            g_s = 65.5
        elif setting[1] == '2':
            g_s = 32.8
        elif setting[1] == '3':
            g_s = 16.4
        print "Gyro scale = +-", g_s, "degrees/second"

    if setting[0] == 'gravity':
        g = float(setting[1])

#Example
ser = serialRead.serial_read('/dev/tty.usbserial-AL00WV7C', 115200)
ser.open_port()
ser.prepare_port()
num = 0
while num < 1500:
    data_read = ser.read_data(6)

    accel_data = data_read[0:3]
    gyro_data = data_read[3:6]

    data_read_scaled = list()

    for data_ in accel_data:
        data_scale_g = (data_ / a_s) * g
        data_read_scaled.append(data_scale_g)

    for data_ in gyro_data:
        data_scale = data_ / g_s
        data_read_scaled.append(data_scale)

    print data_read_scaled
    num += 1
ser.close_port()