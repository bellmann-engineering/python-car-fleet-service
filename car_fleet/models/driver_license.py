from enum import IntFlag


class DriverLicense(IntFlag):
    """
    Führscheinklasssen in Deutschland
    """
    AM = 0
    A1 = 1
    A2 = 2
    A = 4
    B1 = 8
    B = 16
    C1 = 32
    C = 64
    D1 = 128
    D = 256
    BE = 512
    C1E = 1024
    CE = 2048
    D1E = 4096
    DE = 8192
