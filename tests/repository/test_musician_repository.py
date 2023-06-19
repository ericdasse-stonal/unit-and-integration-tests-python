from unittest.mock import Mock

import pandas as pd

from src.repository.musician_repository import MusicianRepository


class TestMusicianRepository:
    def test_should_get_musician(self):
        # Given
        client = Mock()
        client.retrieve_musician.return_value = pd.DataFrame(
            {
                "name": ["Kurt"],
                "surname": ["Cobain"],
                "age": [27],
                "instrument": ["guitar"],
            }
        )
        musician_repository = MusicianRepository(postgres_client=client)

        # When
        musician = musician_repository.get_musician("Kurt")

        # Then
        assert musician is not None
        assert musician.name == "Kurt"
        assert musician.surname == "Cobain"
        assert musician.age == 27
        assert musician.instrument == "guitar"

    def test_should_get_musicians(self):
        # Given
        client = Mock()
        client.retrieve_musicians.return_value = pd.DataFrame(
            {
                "name": ["Kurt", "Jim", "Noel"],
                "surname": ["Cobain", "Morisson", "Gallagher"],
                "age": [27, 27, 54],
                "instrument": ["guitar", "vocal", "guitar"],
            }
        )
        musician_repository = MusicianRepository(postgres_client=client)

        # When
        musicians = musician_repository.get_musicians_by_names(["Kurt", "Jim", "Noel"])

        # Then
        assert musicians is not None
        assert len(musicians) == 3

        assert musicians[0].name == "Kurt"
        assert musicians[0].surname == "Cobain"
        assert musicians[0].age == 27
        assert musicians[0].instrument == "guitar"

        assert musicians[1].name == "Jim"
        assert musicians[1].surname == "Morisson"
        assert musicians[1].age == 27
        assert musicians[1].instrument == "vocal"

        assert musicians[2].name == "Noel"
        assert musicians[2].surname == "Gallagher"
        assert musicians[2].age == 54
        assert musicians[2].instrument == "guitar"
