import pytest

SYSTEM_VERSION = "v1.3.2"

@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.3.3",
    reason="Тест не может быть запущен на версии 1.3.3",
)
def test_system_version_valid():
    ...


@pytest.mark.skipif(
    SYSTEM_VERSION == "v1.3.2",
    reason="Тест не может быть запущен на версии 1.3.2"
)
def test_system_version_invalid():
    ...