"""

"""


from obj0.src import word_count


def test_environment():
    """

    :return:
    """
    try:
        word_count.word_count()
        print('###########################################################')
        print("Test Ran Successfully!")
        print('###########################################################')
    except Exception as e:
        print('###########################################################')
        print("An Error happened during computation of Word Counts:")
        print(e)
        print('###########################################################')


if __name__ == "__main__":
    test_environment()
