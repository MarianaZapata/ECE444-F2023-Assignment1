class Utils:
    @staticmethod
    def reversed(number):
        if isinstance(number, int):
            reversed_number = int(str(number)[::-1])
            return reversed_number
        else:
            raise ValueError("Input must be an integer")

    @staticmethod
    def formatter(number):
        if isinstance(number, int):
            binary_format = bin(number)
            octal_format = oct(number)
            return binary_format, octal_format
        else:
            raise ValueError("Input must be an integer")


