import numpy as np
from unittest.mock import patch
from utils import io


@patch('utils.io.os.path.exists')
@patch('utils.io.cv2.imread')
def test_load_image(mock_imread, mock_exists):
    """Test image loading by mocking both the file system and OpenCV."""

    # 1. Mock os.path.exists to return True so the function continues
    mock_exists.return_value = True

    # 2. Mock cv2.imread to return a dummy image array
    expected_array = np.zeros((5, 5, 3), dtype=np.uint8)
    mock_imread.return_value = expected_array

    # Execute
    file_path = "data/sample_cow.jpg"
    result = io.load_image(file_path)

    # Assertions
    mock_exists.assert_called_once_with(file_path)
    mock_imread.assert_called_once_with(file_path)

    assert result is not None
    assert np.array_equal(result, expected_array)
    assert result.shape == (5, 5, 3)


@patch('utils.io.cv2.imread')
def test_load_image_fail(mock_imread):

    mock_imread.return_value = None

    result = io.load_image("fake.jpg")

    assert result is None