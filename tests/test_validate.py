from utils.validator import validate_against_dataset, detect_duplicates

def test_validate_against_dataset():
    dataset = ["1234", "5678", "9012"]
    result = "5678"

    assert validate_against_dataset(result, dataset) is True


def test_detect_duplicates():
    data = ["1234", "5678", "1234"]

    duplicates = detect_duplicates(data)

    assert "1234" in duplicates