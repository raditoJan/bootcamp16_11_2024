class MyTypeError(TypeError):
    def __init__(self, message, err_code=1001):
        super().__init__(message)
        self.err_code = err_code

class MyValueError(ValueError):
    def __init__(self, message, err_code=2001):
        super().__init__(message)
        self.err_code = err_code

class MyValidator:
    @staticmethod
    def is_int(value, name):
        if not isinstance(value, int):
            raise MyTypeError(f"{name} must be integer", err_code=1001)

    @staticmethod
    def not_zero(value, name):
        if value == 0:
            raise MyValueError(f"{name} cannot be zero", err_code=2001)

def my_function(x: int, y: int) -> float:
    MyValidator.is_int(x, "x")
    MyValidator.is_int(y, "y")
    MyValidator.not_zero(y, "y")
    return x / y

# ---- PRZYKŁAD UŻYCIA ----
try:
    result = my_function(4, 5)
    # result = my_function(4, 0)
    result = my_function("A", 0)
except MyTypeError as e:
    print("Caught a MyTypeError", e)
    print("Error code:", e.err_code)
except MyValueError as e:
    print("Caught a MyValueError", e)
    print("Error code:", e.err_code)
except Exception as e:
    print("Error:", e)
else:
    print(f"Result is {result}")
finally:
    print("End")