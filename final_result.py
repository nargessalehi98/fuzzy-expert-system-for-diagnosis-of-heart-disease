import fuzzification
import inference
import defuzzification


class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:
        Fuzzification = fuzzification.ChestPain()
        chest_pain = Fuzzification.get(int(input_dict['chest_pain']))
        Fuzzification = fuzzification.BloodPressure()
        blood_pressure = Fuzzification.get(int(input_dict['blood_pressure']))
        Fuzzification = fuzzification.Cholesterol()
        cholesterol = Fuzzification.get(int(input_dict['cholestrol']))
        Fuzzification = fuzzification.BloodSugar()
        blood_sugar = Fuzzification.get(int(input_dict['blood_sugar']))
        Fuzzification = fuzzification.ECG()
        ECG = Fuzzification.get(float(input_dict['ecg']))
        Fuzzification = fuzzification.HeartRate()
        heart_rate = Fuzzification.get(int(input_dict['heart_rate']))
        Fuzzification = fuzzification.Exercise()
        exercise = Fuzzification.get(int(input_dict['exercise']))
        Fuzzification = fuzzification.OldPeak()
        old_peak = Fuzzification.get(float(input_dict['old_peak']))
        Fuzzification = fuzzification.Thallium()
        thallium = Fuzzification.get(int(input_dict['thallium_scan']))
        Fuzzification = fuzzification.Sex()
        sex = Fuzzification.get(int(input_dict['sex']))
        Fuzzification = fuzzification.Age()
        age = Fuzzification.get(int(input_dict['age']))

        Inference = inference.Inference()
        fuzzy_sick = Inference.get(chest_pain, blood_pressure, cholesterol,
                                   blood_sugar, ECG, heart_rate, exercise,
                                   old_peak, thallium, sex, age)

        Defuzzification = defuzzification.Defuzzification()
        return Defuzzification.defuzzify(fuzzy_sick)
