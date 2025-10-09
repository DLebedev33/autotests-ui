import pytest


@pytest.mark.smoke
# маркировка, есть встроенные есть кастомные, как написано сейчас, этим самым мы
# маркируем тест (к примеру чтобы выделить тесты для смока)
# запускаем командой python -m pytest -s -v -m "smoke" как название маркера
def test_smoke_case():
    ...


@pytest.mark.regression
def test_regression_case():
    ...
# можем запускать 2 маркироваки командной "python -m pytest -s -v -m "smoke or regression"


@pytest.mark.smoke
# маркировки также можно ставить и на классы и на функции в классе
class TestSuite:
    # @pyteest.mark.smoke
    def test_case1(self):
        ...

    def test_case2(self):
        ...


@pytest.mark.regression
class TestUserAuthentication:
    @pytest.mark.smoke
    def test_login(self):
        ...

    @pytest.mark.slow
    def test_password_reset(self):
        # запустить внутри класса с маркировкой regression  slow тест python -m pytest -s -v -m "regression and slow"
        ...

    def test_logout(self):
        ...
# командой python -m pytest -s -v -m "regression and not slow" запускаем все регресс
# кейсы и исключаем slow, потому что прописали and not slow. Попал кейс и который без
# маркировки внутри класса


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.critical
def test_critical_login():
    ...


@pytest.mark.ui
class TestUserInterface:
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login_button(self):
        pass

    @pytest.mark.regression
    def test_forgot_password_link(self):
        pass

    @pytest.mark.smoke
    def test_signup_form(self):
        pass
# запустить третий тест в классе "python -m pytest -s -v -m "ui and smoke and not critical"
# то есть мы говорим, чтобы он у нас взял выбрал из всего скопа только ui далее
# только smoke и не critical и это значит, что он возьмёт тот тест в котором нет
# маркировки critical