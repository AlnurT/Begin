"""Задача 1. Информация о системе
Чтобы преподавателям было проще помогать вам при возникновении различных ошибок,
нужно собрать информацию об операционной системе и версии Python. Для этого используйте код ниже."""

import platform
import sys

info = f"OS info is \n{platform.uname()}\n\nPython version is {sys.version} {platform.architecture()}"

print(info)

with open("os_info.txt", "w", encoding="utf8") as file:
    file.write(info)
