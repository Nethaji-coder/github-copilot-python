import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app import CURRENT, app as flask_app


@pytest.fixture()
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as test_client:
        yield test_client


@pytest.fixture(autouse=True)
def reset_state():
    CURRENT["puzzle"] = None
    CURRENT["solution"] = None
    yield
    CURRENT["puzzle"] = None
    CURRENT["solution"] = None
