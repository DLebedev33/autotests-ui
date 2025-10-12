import pytest


@pytest.mark.skip(reason="Фитча в разработке")
# Встроенный маркер, который скипает тест, также лучше всегда указывать причину скипа
def test_feature_in_development():
    ...


@pytest.mark.skip(reason="Фитча в разработке")
class TestSuiteSkip:
    def test_feature_in_development_1(self):
        ...
    def test_feature_in_development_2(self):
        ...