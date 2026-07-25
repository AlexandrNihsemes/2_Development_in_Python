import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def valid_card_numbers():
    return [
        "7000792289606361",
        "9999999999999999",
        "0000000000000000",
        "0909090909090909",
        "5555555555555555",
    ]


@pytest.fixture
def expected_masked_numbers():
    return [
        "7000 79** **** 6361",
        "9999 99** **** 9999",
        "0000 00** **** 0000",
        "0909 09** **** 0909",
        "5555 55** **** 5555",
    ]


def test_valid_card_numbers(valid_card_numbers, expected_masked_numbers):
    for i in range(len(valid_card_numbers)):
        card_number = valid_card_numbers[i]
        expected = expected_masked_numbers[i]
        assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "string, expected",
    [
        ("1234567890123", "Неверный ввод"),
        ("1234567890123456789", "Неверный ввод"),
        ("", "Неверный ввод"),
        ("qawsedrftgyhujik", "Неверный ввод"),
        ("1s5f6h1r3d5s9r3f", "Неверный ввод"),
        ("01254698DFGHNRdf", "Неверный ввод"),
        ("DFGHRETYUFGHJKGF", "Неверный ввод"),
        ("AWERTYUIOPJHGFDRTYUI", "Неверный ввод"),
        ("123456789012345", "Неверный ввод"),
        ("12345678901234567", "Неверный ввод"),
    ],
)
def test_invalid_card_number(string, expected):
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(string)
    assert str(exc_info.value) == expected


@pytest.fixture
def valid_account_numbers():
    return [
        "73654108430135874305",
        "99999999999999999999",
        "00000000000000000000",
        "09090909090909090909",
        "55555555555555555555",
    ]


@pytest.fixture
def expected_masked_account():
    return [
        "**4305",
        "**9999",
        "**0000",
        "**0909",
        "**5555",
    ]


def test_valid_account_numbers(valid_account_numbers, expected_masked_account):
    for i in range(len(valid_account_numbers)):
        account_number = valid_account_numbers[i]
        expected = expected_masked_account[i]
        assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    "string, expected",
    [
        ("1234567890123456789", "Неверный ввод"),
        ("123456789012345678901", "Неверный ввод"),
        ("", "Неверный ввод"),
        ("qwertyuiopasdfghjklz", "Неверный ввод"),
        ("qwertyuiopasdfghjkl9", "Неверный ввод"),
        ("1234567890123456789r", "Неверный ввод"),
        ("ZXCVBNMASDFGHJKLQWER", "Неверный ввод"),
        ("R12345678901234567890", "Неверный ввод"),
        ("1234567890123456789I", "Неверный ввод"),
        ("DFG123tyu8WER147tyu3", "Неверный ввод"),
    ],
)
def test_invalid_account_number(string, expected):
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(string)
    assert str(exc_info.value) == expected


# pytest
# black tests/test_masks.py
