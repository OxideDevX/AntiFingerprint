import platform


__doc__ = """Модуль содержит общие системные функции"""


def is_x64os():
    """
    :return: True if system is 64-bit, False otherwise
    """
    return platform.machine().endswith('64')


def platform_version():
    """
    :return: True if system is 64-bit, False otherwise
    """
    return platform.platform()
