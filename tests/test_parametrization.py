import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('number', [1, 2, 3, -1])
# в квадратных скобках (списке) указываем те значения, которые хотим параметризировать
def test_numbers(number: int):
    assert number > 0
    # в случае выполнения она запустит 4 теста на каждое значение, которое мы прередали в списке

@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
# то есть значение, которое было написано первым будет относится к number, потому что оно первое прописано
# а второе значание будет в expected (ожидаание)
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected
    #  то есть мы первое значение возводим в квадрат и ожидаем получить второе значение из списка!!!

@pytest.mark.parametrize('os', ['macos', 'linux', 'windows', 'debian'])
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
def test_multiplication_of_numbers(os: str, browser: str):
# так прописываем, когда нам нужно запустить тесты на разных ОС и под разные браузеры
#  сумме получится 12 тестов, так как 4 ОС и 3 браузера
    assert len(os + browser) > 0

@pytest.fixture(params = ['chromium', 'webkit', 'firefox'])
def browser(request):
    return request.param

def test_open_browser(browser: str):
    print(f'Running test on browser: {browser}')


@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOpenations:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operations(self, user: str, account: str):
        print(f'User with operations: {user}')

    def test_user_without_operations(self, user: str):
        print(f'User without operations: {user}')


users = {
    '+700000001': 'User with money on bank account',
    '+700000002': 'User without money on bank account',
    '+700000003': 'User with operations on bank account',
}
@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
    ids=lambda phone_number: f'{[phone_number]}: {users[phone_number]}'
)
# Так пишем, чтобы у нас в тесте вместо номеров подсвечивалось название по значениям номеров!!!
# Названий должно быть столько же сколько значений!!! Иначе тест упадёт
def test_identifiers(phone_number: str):
    ...
# Видно и номер телефона и описание