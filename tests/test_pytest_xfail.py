import pytest


@pytest.mark.xfail(reason="номер дефекта")
# данный маркер не будет у нас валить тесты в fail, а будет обозначать, что они
# зафейлены чем то. А если тест отработал успешно и будет статус XPASS, то можно
# убрать эту маркировку с теста
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail
def test_without_bug():
    ...