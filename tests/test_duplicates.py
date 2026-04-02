def test_duplicate_detection():
    """
    Test duplicate detection logic.

    The system should identify when a crotal number
    appears more than once in the processed dataset.
    """

    crotal_numbers = ["1234", "5678", "1234"]

    duplicates = [x for x in crotal_numbers if crotal_numbers.count(x) > 1]

    assert "1234" in duplicates
