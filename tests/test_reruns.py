import random

import pytest


@pytest.mark.flaky(reruns = 3, reruns_delay = 2)
#     reruns = 3 означает, что мы перезапускаем упавшие тесты 3 раза, а reruns_delay = 2 это тайминг между перезапусками
def test_reruns():
    assert random.choice([True, False])