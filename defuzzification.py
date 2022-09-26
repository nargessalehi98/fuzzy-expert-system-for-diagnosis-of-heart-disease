from fuzzification import OutputSick


class Defuzzification:
    def __init__(self):
        self.fuzzification_output_sick = OutputSick()
        self.result = 0
        self.points = [-100.0 + i * (200.0 / 10000) for i in range(10000 + 1)]

    def defuzzify(self, x):

        for point in self.points:
            print(point)
            sick1 = self.fuzzification_output_sick.sick1(point)
            sick2 = self.fuzzification_output_sick.sick2(point)
            sick3 = self.fuzzification_output_sick.sick3(point)
            sick4 = self.fuzzification_output_sick.sick4(point)
            healthy = self.fuzzification_output_sick.healthy(point)

            sick1 = x['sick1'] if sick1 > x['sick1'] else sick1
            sick2 = x['sick2'] if sick2 > x['sick2'] else sick2
            sick3 = x['sick3'] if sick3 > x['sick3'] else sick3
            sick4 = x['sick4'] if sick4 > x['sick4'] else sick4
            healthy = x['healthy'] if healthy > x['healthy'] else healthy

            center = (max(sick1, sick2, sick3, sick4, healthy) * point * (200.0 / 10000)) / (
                        max(sick1, sick2, sick3, sick4, healthy) * (200.0 / 10000))

            if center < 1.78:
                self.result = 'healthy'
            if 1 <= center <= 2.51:
                self.result = 'sick1'
            if 1.78 <= center < 3.25:
                self.result = 'sick2'
            if 1.5 <= center <= 4.5:
                self.result = 'sick3'
            if 3.25 <= center:
                self.result = 'sick4'
            return self.result



Defuzzification().defuzzify(1)