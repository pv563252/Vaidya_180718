"""

"""


def begin_test_message(test_name):
    """

    :param test_name:
    :return:
    """
    print('###########################################################')
    print("Starting Test " + test_name)
    print('###########################################################')


def test_result_handler(test, result, message=None, values=None):
    """

    :param test:
    :param result:
    :param message:
    :param values:
    :return:
    """
    if result:
        print('###########################################################')
        print("The Test Passed: " + test)
        print("Test Result: " + str(result))
        print('###########################################################')
    elif result is False:
        print('###########################################################')
        print("The Test Passed: " + test)
        print("Test Result: " + str(result))
        print("Test Failed Due to: " + str(message))
        print("Test Failed Due to Values: " + str(values))
        print('###########################################################')


def end_test_message(test_name):
    """

    :param test_name:
    :return:
    """
    print('###########################################################')
    print("Ending Test " + test_name)
    print('###########################################################')
