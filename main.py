# pylint: disable-msg=C0103
# pylint: disable-msg=C0301
# pylint: disable-msg=W1201

"""This main.py tests if the calculator can do add/sub/multiply/divison correctly"""
# INPUT FILE : input/testFile.csv
# For IS601-851 Homework -Dairui Zhang

import time
import logging
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from calculator import Calculator
from History.calculations import Calculations


# ============= TEST METHODS ================
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()


def addTest(clear_history_fixture, a, b):
    """testing that our calculator has a static method for addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    return Calculator.add_numbers(a, b) == a + b


def subTest(clear_history_fixture, a, b):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    return Calculator.subtract_numbers(a, b) == 0 - a - b


def multiTest(clear_history_fixture, a, b):
    """Testing the multiply method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    return Calculator.multiply_numbers(a, b) == a * b


def diviTest(clear_history_fixture, a, b):
    """Testing the division method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    if b == 0:
        return -1
    return Calculator.division_numbers(a, b) == 1 / a / b


if __name__ == '__main__':

    # ============= WATCH DOG ================
    watch_patterns = "*"  # 监控文件的模式
    ignore_patterns = ""  # 设置忽略的文件模式
    ignore_directories = False  # 是否忽略文件夹变化
    case_sensitive = True  # 是否对大小写敏感
    event_handler = PatternMatchingEventHandler(watch_patterns, ignore_patterns, ignore_directories, case_sensitive)


    def on_created(event):
        """is created"""
        print(f"{event.src_path}is created")


    def on_deleted(event):
        """is deleted"""
        print(f"{event.src_path}is deleted")


    def on_modified(event):
        """is deleted"""
        print(f"{event.src_path} is modified")


    def on_moved(event):
        """on moved"""
        print(f"{event.src_path}is moved to{event.dest_path}")


    event_handler.on_created = on_created
    event_handler.on_deleted = on_deleted
    event_handler.on_modified = on_modified
    event_handler.on_moved = on_moved

    watch_path = "/Users/zhangdairui/PycharmProjects/Calculator2_Dariui/output"  # watch the output
    go_recursively = True  # 是否监控子文件夹

    my_observer = Observer()
    my_observer.schedule(event_handler, watch_path, recursive=go_recursively)
    my_observer.start()

    # ============= PREPARE LOG FILE ================
    logging.basicConfig(
        filename='/Users/zhangdairui/PycharmProjects/Calculator2_Dariui/output/' + __name__ + '.log',
        format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')

    logging.info("TEST STARTED at " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    # ============= READ CSV ================
    df = pd.read_csv('input/testFile.csv')
    logging.info("TEST INPUT CSV:")
    logging.info(df.to_string())
    data_num = len(df)

    # ============= DO TEST ================
    for i in range(data_num):
        a = df.loc[i].value_a
        b = df.loc[i].value_b
        add_r = df.loc[i].add_result
        sub_r = df.loc[i].sub_result
        mul_r = df.loc[i].mult_result
        div_r = df.loc[i].divide_result

        if addTest(clear_history_fixture, a, b):
            message_result = "Addition Function got tested! Succeed in a=" + str(a) + " b=" + str(b) + "!"
            logging.info(message_result)
        else:
            message_result = "Addition Test Filed in a=" + str(a) + " b=" + str(b) + "!"
            logging.warning(message_result)

        if subTest(clear_history_fixture, a, b):
            message_result = "Subtract Function got tested! Succeed in a=" + str(a) + " b=" + str(b) + "!"
            logging.info(message_result)
        else:
            message_result = "Subtract Test Filed in a=" + str(a) + " b=" + str(b) + "!"
            logging.warning(message_result)

        if multiTest(clear_history_fixture, a, b):
            message_result = "Multiply Function got tested! Succeed in a=" + str(a) + " b=" + str(b) + "!"
            logging.info(message_result)
        else:
            message_result = "Multiply Test Filed in a=" + str(a) + " b=" + str(b) + "!"
            logging.warning(message_result)

        if diviTest(clear_history_fixture, a, b):
            message_result = "Division Function got tested! Succeed in a=" + str(a) + " b=" + str(b) + "!"
            logging.info(message_result)
        else:
            message_result = "Division Test Filed in a=" + str(a) + " b=" + str(b) + "!"
            logging.warning(message_result)

        if diviTest(clear_history_fixture, a, b) == -1:
            message_result = "Division Function can not divide by zero! Test succeed in a=" + str(a) + " b=" + str(
                b) + "!"
            logging.info(message_result)

    logging.info("TEST END!")

    # ============= END ================
    my_observer.stop()
