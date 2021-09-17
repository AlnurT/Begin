from task2.task2 import equation


def test_equation_form_kx_plus_b():
    assert equation(10, 20, 15, 25) == "y = 1.0 * x + (10.0)"


def test_equation_vertical_line_x_const():
    assert equation(10, 20, 10, 25) == "x = 10"


def test_equation_horizontal_line_y_const():
    assert equation(10, 20, 15, 20) == "y = 20"
