import pytest


@pytest.fixture(autouse=True)
# данная фикстура будет запускаться автоматически на каждый тест до теста
def sent_analytics_data():
    print("[AUTOUSE] Отправляем данные в сервис аналитики")


@pytest.fixture(scope="session")
# Запускается один раз на всю тестовую сессию
def settings():
    print("[SESSION] Инициализируем настройки автотестов")


@pytest.fixture(scope="class")
# Запускается один раз на тестовый класс
def user():
    print("[CLASS] Создаём данные пользователя один раз на каждый тестовый класс")


@pytest.fixture(scope="function")
# Запускаеся один раз на тестовую функцию
def browser():
    print("[FUNCTION] Открываем браузер на каждый автотест")


class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        ...

    def test_user_can_create_course(self, settings, user, browser):
        ...


class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        ...