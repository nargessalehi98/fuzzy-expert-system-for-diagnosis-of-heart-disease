class Age:
    def __init__(self):
        self.young = 0
        self.mild = 0
        self.old = 0
        self.very_old = 1

    def get(self, x):
        if 0 < x <= 29:
            self.young = 1
        elif 29 < x <= 38:
            self.young = -0.111 * x + 4.222
        if 33 < x <= 38:
            self.mild = 0.2 * x - 6.600
        elif 38 < x <= 45:
            self.mild = -0.143 * x + 6.429
        if 40 < x <= 48:
            self.old = 0.125 * x - 5.000
        elif 48 < x <= 58:
            self.old = -0.1 * x + 5.800
        if 0 <= x <= 52:
            self.very_old = 0
        elif 52 < x <= 60:
            self.very_old = 0.125 * x - 6.500

        return dict(
            young=self.young,
            mild=self.mild,
            old=self.old,
            very_old=self.very_old
        )


class BloodPressure:
    def __init__(self):
        self.low = 0
        self.medium = 0
        self.high = 0
        self.very_high = 1

    def get(self, x):
        if 0 <= x <= 111:
            self.low = 1
        elif 111 < x <= 134:
            self.low = -0.043 * x + 5.862
        if 127 < x <= 139:
            self.medium = 0.083 * x - 10.583
        elif 139 < x <= 153:
            self.medium = -0.071 * x + 10.929
        if 142 < x <= 157:
            self.high = 0.067 * x - 9.467
        elif 157 < x <= 172:
            self.high = -0.067 * x + 11.467
        if 0 <= x <= 154:
            self.very_high = 0
        elif 154 < x <= 171:
            self.very_high = 0.059 * x - 9.059

        return dict(
            low=self.low,
            medium=self.medium,
            high=self.high,
            very_high=self.very_high
        )


class BloodSugar:
    def __init__(self):
        self.very_high = 0

    def get(self, x):
        if 120 <= x:
            self.very_high = 1
        elif 105 <= x < 120:
            self.very_high = 0.067 * x - 7

        return dict(
            true=self.very_high,
            false=1 - self.very_high
        )


class Cholesterol:
    def __init__(self):
        self.low = 0
        self.medium = 0
        self.high = 0
        self.very_high = 1

    def get(self, x):
        if 0 <= x <= 151:
            self.low = 1
        elif 151 < x <= 197:
            self.low = -0.022 * x + 4.283
        if 188 < x <= 215:
            self.medium = 0.037 * x - 6.963
        elif 215 < x <= 250:
            self.medium = -0.029 * x + 7.143
        if 217 < x <= 263:
            self.high = 0.022 * x - 4.717
        elif 263 < x <= 307:
            self.high = -0.023 * x + 6.977
        if 0 < x <= 281:
            self.very_high = 0
        elif 281 < x <= 347:
            self.very_high = 0.015 * x - 4.258
        return dict(
            low=self.low,
            medium=self.medium,
            high=self.high,
            very_high=self.very_high
        )


class HeartRate:
    def __init__(self):
        self.low = 0
        self.medium = 0
        self.high = 0
        self.very_high = 1

    def get(self, x):
        if 0 <= x <= 100:
            self.low = 1
        elif 100 < x <= 141:
            self.low = -0.024 * x + 3.439
        if 111 < x <= 152:
            self.medium = 0.024 * x - 2.707
        elif 152 < x <= 194:
            self.medium = -0.024 * x + 4.619
        if 0 < x <= 152:
            self.high = 0
        elif 152 < x <= 210:
            self.high = 0.017 * x - 2.621
        return dict(
            low=self.low,
            medium=self.medium,
            high=self.high,
        )


class ECG:
    def __init__(self):
        self.normal = 0
        self.abnormal = 0
        self.hypertrophy = 1

    def get(self, x):
        if -0.5 <= x <= 0:
            self.normal = 1
        elif 0 < x <= 0.4:
            self.normal = -2.500 * x + 1.000
        if 0.2 <= x <= 1:
            self.abnormal = 1.250 * x - 0.250
        elif 1 < x <= 1.8:
            self.abnormal = -1.250 * x + 2.250
        if -0.4 <= x <= 1.4:
            self.hypertrophy = 0
        elif 1.4 < x <= 1.9:
            self.hypertrophy = 2.000 * x - 2.800
        return dict(
            normal=self.normal,
            abnormal=self.abnormal,
            hypertrophy=self.hypertrophy,
        )


class OldPeak:
    def __init__(self):
        self.low = 0
        self.risk = 0
        self.terrible = 1

    def get(self, x):
        if 0 <= x <= 1:
            self.low = 1
        elif 1 < x <= 2:
            self.low = -1.000 * x + 2.000
        if 1.5 <= x <= 2.8:
            self.risk = 0.769 * x - 1.154
        elif 2.8 < x <= 4.2:
            self.risk = -0.714 * x + 3.000
        if 0 < x <= 2.5:
            self.terrible = 0
        elif 2.5 < x <= 4:
            self.terrible = 0.667 * x - 1.667

        return dict(
            low=self.low,
            risk=self.risk,
            terrible=self.terrible,
        )


class OutputSick:
    def __init__(self):
        pass

    def sick1(self, x):
        if 0 <= x <= 0.25:
            return 1
        elif 0.25 < x <= 1:
            return -1.333 * x + 1.333
        return 0

    def sick2(self, x):
        if 0 <= x <= 1:
            return x
        if 1 < x <= 2:
            return -1.000 * x + 2.000
        return 0

    def sick3(self, x):
        if 1 <= x <= 2:
            return 1.000 * x - 1.000
        elif 2 < x <= 3:
            return -1.000 * x + 3.000
        return 0

    def sick4(self, x):
        if 2 <= x <= 3:
            return 1.000 * x - 2
        elif 3 < x <= 4:
            return -1.000 * x + 4.000
        return 0

    def healthy(self, x):
        if 0 <= x <= 3:
            return 0
        elif 3 < x <= 3.75:
            return 1.333 * x - 4.000
        return 1


class ChestPain:
    def __init__(self):
        self.typical_angina = 0
        self.atypical_angina = 0
        self.non_anginal_pain = 0
        self.asymptomatic = 0

    def get(self, x):
        if x == 1:
            self.typical_angina = 1
        if x == 2:
            self.atypical_angina = 1
        if x == 3:
            self.non_anginal_pain = 1
        if x == 4:
            self.asymptomatic = 1

        return dict(
            typical_anginal=self.typical_angina,
            atypical_anginal=self.atypical_angina,
            non_aginal_pain=self.non_anginal_pain,
            asymptomatic=self.asymptomatic
        )


class Exercise:
    def __init__(self):
        self.true = 0
        self.false = 0

    def get(self, x):
        if x == 1:
            self.true = 1
        if x == 0:
            self.false = 1

        return dict(
            true=self.true,
            false=self.false
        )


class Thallium:
    def __init__(self):
        self.normal = 0
        self.medium = 0
        self.high = 0

    def get(self, x):
        if x == 3:
            self.normal = 1
        if x == 6:
            self.medium = 1
        if x == 6:
            self.high = 1

        return dict(
            normal=self.normal,
            medium=self.medium,
            high=self.high
        )


class Sex:
    def __init__(self):
        self.male = 0
        self.female = 0

    def get(self, x):
        if x == 0:
            self.male = 1
        if x == 1:
            self.female = 1

        return dict(
            male=self.male,
            female=self.female
        )
