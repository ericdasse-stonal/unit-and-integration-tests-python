import pandas as pd
from src.model.musician import Musician

from src.repository.mapper.mapper import Mapper


def test_should_convert_dataframe_to_musician():
    # Given
    musician_df = pd.DataFrame(
        {
            "name": ["Grande"],
            "surname": ["Ariana"],
            "age": [27],
            "instrument": [""],
        }
    )
    # When
    musician = Mapper.convert_dataframe_to_musician(musician_df.iloc[0])
    # Then
    assert musician is not None
    assert musician.name == "Grande"
    assert musician.surname == "Ariana"
    assert musician.age == 27
    assert musician.instrument == ""


def test_should_convert_musician_to_dataframe():
    # Given
    musician = Musician(name="Jonas", surname="Kevin", age=35, instrument="guitar")
    # When
    musician_df = Mapper.convert_musician_to_dataframe(musician=musician)
    # Then
    assert musician_df is not None
    assert musician_df.iloc[0]["name"] == "Jonas"
    assert musician_df.iloc[0]["surname"] == "Kevin"
    assert musician_df.iloc[0]["age"] == 35
    assert musician_df.iloc[0]["instrument"] == "guitar"
