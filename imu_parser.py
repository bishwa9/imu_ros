import math

class imu_parser:

    def __init__(self):
        self.a_s = 0
        self.g_s = 0
        self.g = 0
        self.R_a = [0.0] * 9
        self.R_g = [0.0] * 9
        settings_file = open('imu.settings', 'r')

        for l in settings_file.readlines():
            setting = l.split()
            if setting[0] == 'Accelerometer_Scale':
                if setting[1] == '0':
                    self.a_s = 8192
                elif setting[1] == '1':
                    self.a_s = 4096
                elif setting[1] == '2':
                    self.a_s = 2048
                elif setting[1] == '3':
                    self.a_s = 1024
                print "A scale = +-", self.a_s, "g"

            elif setting[0] == 'Gyro_Scale':
                if setting[1] == '0':
                    self.g_s = 131
                elif setting[1] == '1':
                    self.g_s = 65.5
                elif setting[1] == '2':
                    self.g_s = 32.8
                elif setting[1] == '3':
                    self.g_s = 16.4
                print "Gyro scale = +-", self.g_s, "degrees/second"

            elif setting[0] == 'gravity':
                self.g = float(setting[1])

            elif setting[0] == 'R_a':
                self.R_a[0] = setting[1]
                self.R_a[4] = setting[2]
                self.R_a[8] = setting[3]

            elif setting[0] == 'R_g':
                self.R_g[0] = setting[1]
                self.R_g[4] = setting[2]
                self.R_g[8] = setting[3]

    # Return data in m/s^2 and rad / sec
    def parse_data(self, data_read):
        accel_data = data_read[0:3]
        gyro_data = data_read[3:6]

        data_read_scaled = list()

        for data_ in accel_data:
            data_scale_g = (data_ / self.a_s) * self.g
            data_read_scaled.append(data_scale_g)

        for data_ in gyro_data:
            data_scale = data_ / self.g_s
            data_scale *= (math.pi / 180.0)
            data_read_scaled.append(data_scale)

        return data_read_scaled