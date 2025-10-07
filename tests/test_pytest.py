def test_user_login():
    print("Hello world")


class TestuserLogin:
        def test_1(self):
            ...

        def test_2(self):
            ...


def test_assert_positive_case():
    assert (2 + 2) == 4


def test_assert_negative_case():
    assert (2 + 2) == 5, "(2 + 2) != 5"
    # после запятой будет указываться сообщение об ошибке. Запускать командой python -m pytest -s -v -k "test_assert"