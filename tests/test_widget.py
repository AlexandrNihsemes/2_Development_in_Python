import pytest

from src.widget import mask_account_card, get_date


@pytest.fixture
def valid_account_card():
    return [
        "Visa Platinum 7000792289606361",
        "Maestro 9999999999999999",
        "Maestro 0000000000000000",
        "Visa Platinum 0909090909090909",
        "Maestro 5555555555555555",
        "Счет 73654108430135874305",
        "Счет 99999999999999999999",
        "Счет 00000000000000000000",
        "Счет 09090909090909090909",
        "Счет 55555555555555555555",
    ]


@pytest.fixture
def expected_masked_card():
    return [
        "Visa Platinum 7000 79** **** 6361",
        "Maestro 9999 99** **** 9999",
        "Maestro 0000 00** **** 0000",
        "Visa Platinum 0909 09** **** 0909",
        "Maestro 5555 55** **** 5555",
        "Счет **4305",
        "Счет **9999",
        "Счет **0000",
        "Счет **0909",
        "Счет **5555",
    ]


def test_valid_account_card(valid_account_card, expected_masked_card):
    for i in range(len(valid_account_card)):
        string = valid_account_card[i]
        expected = expected_masked_card[i]
        assert mask_account_card(string) == expected


@pytest.mark.parametrize(
    "string, expected",
    [
        ("isa Platinum 7000792289606361", "Неверный ввод"),
        ("Maestr 9999999999999999", "Неверный ввод"),
        ("Maestro 00000000000000000", "Неверный ввод"),
        ("Visa Plainum 0909090909090909", "Неверный ввод"),
        ("Maestro 555555555555555", "Неверный ввод"),
        ("Счет 736541084301358743052", "Неверный ввод"),
        ("Счета 999999999999999999999", "Неверный ввод"),
        ("Счетчик 00000000000000000000", "Неверный ввод"),
        ("Счет 0909090909090909090909", "Неверный ввод"),
        ("Счет 55555555555555555555555", "Неверный ввод"),
    ],
)
def test_invalid_account_card(string, expected):
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(string)
    assert str(exc_info.value) == expected


@pytest.fixture
def valid_get_date():
    return [
        "2024-03-11T02:26:18.671407",
        "2020-04-12T02:26:18.671407",
        "2021-05-31T02:26:18.671407",
        "2024-12-01T02:26:18.671407",
        "2024-01-30T02:26:18.671407",
    ]


@pytest.fixture
def expected_get_date():
    return [
        "11.03.2024",
        "12.04.2020",
        "31.05.2021",
        "01.12.2024",
        "30.01.2024",
    ]


def test_valid_get_date(valid_get_date, expected_get_date):
    for i in range(len(valid_get_date)):
        string = valid_get_date[i]
        expected = expected_get_date[i]
        assert get_date(string) == expected


@pytest.mark.parametrize(
    "string, expected",
    [
        ("2024-03-11T02:26:18.6714070", "Неверный ввод"),
        ("2027-03-11T02:26:18.671407", "Неверный ввод"),
        ("", "Неверный ввод"),
        ("2024-14-11T02:26:18.671407", "Неверный ввод"),
        ("2024-03-32T02:26:18.671407", "Неверный ввод"),
        ("0000-03-11T02:26:18.671407", "Неверный ввод"),
        ("2024-00-11T02:26:18.671407", "Неверный ввод"),
        ("2024-03-00T02:26:18.671407", "Неверный ввод"),
        ("2024-33-11T02:26:18.671407", "Неверный ввод"),
        ("2224-03-11T02:26:18.671407", "Неверный ввод"),
    ],
)
def test_invalid_get_date(string, expected):
    with pytest.raises(ValueError) as exc_info:
        get_date(string)
    assert str(exc_info.value) == expected


# pytest
# black tests/test_widget.py
# isort tests/test_widget.py