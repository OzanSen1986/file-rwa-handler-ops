import pytest

def is_prime(n: int) -> bool:
    if n <=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i ==0:
            return False
    return True


@pytest.mark.parametrize("n, expected", 
    [(2, True),(3, True),(17, True),(10, False),(0, False), (23, True)])
def test_zero_is_prime(n: int, expected: bool) -> None:
    assert is_prime(n) == expected



