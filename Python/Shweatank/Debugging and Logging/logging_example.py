import logging

py_logger = logging.getLogger(__name__)
py_logger.setLevel(logging.INFO)

def test_division(x,y):
    if y!= 0:
        return x/y
    
py_handler = logging.FileHandler(f"{__name__}.log", mode='w')
py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

py_handler.setFormatter(py_formatter)
py_logger.addHandler(py_handler)

py_logger.info(f"Testing the custom logger for module {__name__}...")

x_values = [2,3,6,4,10]
y_values = [5,7,12,0,1]

for this_x, this_y in zip(x_values, y_values):
    x,y = this_x, this_y
    py_logger.info(f"Call test division with args {x} and {y}")