import pytest
from pydantic import ValidationError

from app.config import Settings


def test_settings_load_from_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "postgresql+asyncpg://u:p@localhost/db")
    monkeypatch.setenv("SECRET_KEY", "s3cret")
    monkeypatch.delenv("ENVIRONMENT", raising=False)

    settings = Settings(_env_file=None)

    assert settings.database_url == "postgresql+asyncpg://u:p@localhost/db"
    assert settings.secret_key == "s3cret"
    assert settings.environment == "development"


@pytest.mark.parametrize("missing", ["DATABASE_URL", "SECRET_KEY"])
def test_missing_required_setting_is_named(monkeypatch: pytest.MonkeyPatch, missing: str) -> None:
    monkeypatch.setenv("DATABASE_URL", "postgresql+asyncpg://u:p@localhost/db")
    monkeypatch.setenv("SECRET_KEY", "s3cret")
    monkeypatch.delenv(missing)

    with pytest.raises(ValidationError) as exc_info:
        Settings(_env_file=None)

    assert missing.lower() in str(exc_info.value)
