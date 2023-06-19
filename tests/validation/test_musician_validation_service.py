import pytest

from src.validation.musician_validation_service import MusicianValidationService


class TestMusicianValidationService:
    def test_should_raise_an_exception_when_name_is_invalid(self):
        # Given
        name = "adriana97"

        # When
        with pytest.raises(Exception) as context:
            MusicianValidationService.validate_name(name)

        # Then
        assert "Name is invalid." in str(context)

    def test_should_not_raise_an_exception_when_name_is_invalid(self):
        # Given
        name = "Kurt"

        # When
        MusicianValidationService.validate_name(name)
