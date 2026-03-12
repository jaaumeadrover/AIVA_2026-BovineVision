import numpy as np
from unittest.mock import patch
from utils import io

@patch('utils.io.cv2.imread')
def test_load_image(mock_imread):
    """Test image loading without hitting the disk."""
    # Mock the return value of cv2.imread
    expected_array = np.zeros((5, 5, 3), dtype=np.uint8)
    mock_imread.return_value = expected_array

    # Execute the function
    file_path = "data/sample_cow.jpg"
    result = io.load_image(file_path)

    # Assertions
    mock_imread.assert_called_once_with(file_path)
    assert result is not None
    assert result.shape == (5, 5, 3)


@patch('utils.io.cv2.imread')
def test_load_image_fail(mock_imread):

    mock_imread.return_value = None

    result = io.load_image("fake.jpg")

    assert result is None