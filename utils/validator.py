def validate_against_dataset(ocr_result, dataset):
    """
    Check if OCR result exists in dataset.
    """
    if ocr_result is None:
        return False

    return ocr_result in dataset


def detect_duplicates(results_list):
    """
    Detect duplicated crotal IDs.
    """
    return [x for x in results_list if results_list.count(x) > 1]