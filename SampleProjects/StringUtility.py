class StringUtility():
    """"""
    def __init__(self):
        """"""

    def verigyEquals(self, expected, actual):
        """"""
        if expected==actual:
            print("PASS")
            print("Expected result is: "+ expected)
            print("Actual result is "+actual)
        else:
            print("FAIL")
            print("Expected result is: "+ expected)
            print("Actual result is "+actual)