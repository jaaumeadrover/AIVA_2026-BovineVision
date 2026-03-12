from unittest.mock import patch
from utils import ocr

@patch('utils.ocr.cv2.imread')
def test_read_text(mock_imread):
    """Test the OCR mock output and internal file loading."""
    # The return value of imread doesn't matter for the current mock logic
    mock_imread.return_value = None

    # Execute the function
    file_path = "data/tag_image.png"
    result = ocr.read_text(file_path)

    # Assertions
    mock_imread.assert_called_once_with(file_path)
    assert result == "test"