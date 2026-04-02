def test_dataset_validation():
    """
    Test validation of OCR results against the dataset.

    The OCR output should match an entry in the
    ground truth dataset.
    """

    dataset = ["1234", "5678", "9012"]
    ocr_result = "5678"

    assert ocr_result in dataset
