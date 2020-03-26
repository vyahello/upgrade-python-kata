from typing import Dict
import pytest

pytestmark = pytest.mark.asyncio


async def foo() -> Dict[str, str]:
    return {"name": "luke"}


async def test_foo() -> None:
    assert await foo() == {"name": "luke"}
