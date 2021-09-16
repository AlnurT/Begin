from task4.task4 import reverse, separation_and_assembly, summa_new_numbers


def test_reverse_numbers():
    assert reverse("1256") == "6521"


def test_separation_and_assembly_of_reverse_numbers():
    assert separation_and_assembly("1256.874") == 6521.478


def test_summa_new_numbers():
    assert summa_new_numbers(6521.478, 417.12) == 6938.598
