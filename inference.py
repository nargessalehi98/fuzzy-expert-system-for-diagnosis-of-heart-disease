class Inference:
    def __init__(self):
        self.sick1 = 0,
        self.sick2 = 0,
        self.sick3 = 0,
        self.sick4 = 0,
        self.healthy = 0

    def get(self, chest_pain, blood_pressure, cholesterol, blood_sugar, ecg, maximum_heart_rate, exercise,
            old_peak, thallium, sex, age):
        self.sick4 = max([min(age['very_old'], chest_pain['atypical_anginal']),
                          min(maximum_heart_rate['high'], age['old']),
                          chest_pain['asymptomatic'],
                          blood_pressure['very_high'],
                          cholesterol['very_high'],
                          maximum_heart_rate['high'],
                          ecg['hypertrophy'],
                          old_peak['risk'],
                          thallium['high'],
                          age['very_old']])

        self.sick3 = max([min(chest_pain['non_aginal_pain'], blood_pressure['high']),
                          age['old'],
                          min(sex['male'], maximum_heart_rate['medium']),
                          min(blood_sugar['true'], age['mild']),
                          chest_pain['asymptomatic'],
                          blood_pressure['high'],
                          cholesterol['high'],
                          ecg['hypertrophy'],
                          maximum_heart_rate['high'],
                          old_peak['terrible'],
                          thallium['high']])

        self.sick2 = max([min(sex['female'], maximum_heart_rate['medium']),
                          min(chest_pain['typical_anginal'], maximum_heart_rate['medium']),
                          min(blood_sugar['false'], blood_pressure['very_high']),
                          chest_pain['non_aginal_pain'],
                          sex['male'],
                          blood_pressure['high'],
                          cholesterol['high'],
                          blood_sugar['true'],
                          ecg['abnormal'],
                          maximum_heart_rate['medium'],
                          exercise['true'],
                          old_peak['terrible'],
                          thallium['medium'],
                          age['old']])

        self.sick1 = max([max(chest_pain['asymptomatic'], age['very_old']),
                          max(chest_pain['asymptomatic'], age['very_old']),
                          max(blood_pressure['high'], maximum_heart_rate['low']),
                          chest_pain['atypical_anginal'],
                          blood_pressure['medium'],
                          cholesterol['medium'],
                          ecg['normal'],
                          maximum_heart_rate['medium'],
                          old_peak['low'],
                          thallium['normal'],
                          age['mild'],
                          sex['female']])

        self.healthy = max([chest_pain['typical_anginal'],
                            ecg['normal'],
                            thallium['normal'],
                            age['young'],
                            old_peak['low'],
                            maximum_heart_rate['low'],
                            cholesterol['low'],
                            blood_pressure['low']])

        return dict(
            sick1=self.sick1,
            sick2=self.sick2,
            sick3=self.sick1,
            sick4=self.sick4,
            healthy=self.healthy
        )
