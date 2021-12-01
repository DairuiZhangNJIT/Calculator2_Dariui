""" This is the increment function"""
from Calculations.addition import Addition
from Calculations.subtraction import Subtraction
from Calculations.multiplication import Multiplication
from Calculations.division import Division
from History.calculations import Calculations


class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def add_numbers(*args):
        """ adds list of numbers"""
        calculation = Addition(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()

    @staticmethod
    def subtract_numbers(*args):
        """ subtract a list of numbers from result"""
        calculation = Subtraction(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()

    @staticmethod
    def multiply_numbers(*args):
        """ multiplication number from result"""
        calculation = Multiplication(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()

    @staticmethod
    def division_numbers(*args):
        """ division number from result"""
        calculation = Division(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()
