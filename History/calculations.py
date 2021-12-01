"""Calculation history Class"""


class Calculations:
    """Class"""
    history = []

    @staticmethod
    def clear_history():
        """to clear history"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """to count history"""
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation():
        """to get last calculation"""
        return Calculations.history[-1]

    @staticmethod
    def get_first_calculation():
        """to get first calculation"""
        return Calculations.history[-1]

    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation(calculation):
        """ get a specific calculation from history"""
        return Calculations.history.append(calculation)
