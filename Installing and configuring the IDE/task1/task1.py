"""Задача 1. Информация о системе
Чтобы преподавателям было проще помогать вам при возникновении различных ошибок,
нужно собрать информацию об операционной системе и версии Python. Для этого используйте код ниже."""

import platform
import sys


def system_information():
    return f"OS info is \n{platform.uname()}\n\nPython version is {sys.version} {platform.architecture()}"


with open("os_info.txt", "w", encoding="utf8") as file:
    file.write(system_information())
