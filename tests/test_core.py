"""Tests for the core MuZero implementation."""

from muzero.core import MuZero


def test_muzero_initialization() -> None:
    """Test that MuZero can be initialized."""
    agent = MuZero()
    assert agent is not None


def test_muzero_train() -> None:
    """Test that MuZero training returns statistics."""
    agent = MuZero()
    stats = agent.train()
    assert isinstance(stats, dict)
