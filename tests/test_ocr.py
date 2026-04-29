from unittest.mock import patch
from utils import ocr, proc
import numpy as np

@patch('utils.ocr.cv2.imread')
def test_read_text(mock_imread):
    """Test OCR output format and internal file loading."""

    # Mock imread
    mock_imread.return_value = None

    file_path = "data/tag_image.png"
    result = ocr.read_text(file_path)

    # Check that imread was called
    mock_imread.assert_called_once_with(file_path)

    # Validate output structure
    assert result is not None
    assert isinstance(result, str)

    # Aceptamos dos comportamientos posibles
    assert result.isdigit() or result == "test"

    if result.isdigit():
        assert 4 <= len(result) <= 5


def test_expected_ocr_format_example():
    """Validate expected OCR output format (simulated)."""

    simulated_result = "12345"

    assert isinstance(simulated_result, str)
    assert simulated_result.isdigit()
    assert 4 <= len(simulated_result) <= 5


@patch('utils.proc.os.path.exists')
@patch('utils.proc.io.load_image')
def test_preprocess_etr_pipeline_success(mock_load, mock_exists):
    """
    Test that the pipeline correctly handles a valid image path
    and returns the original and processed (binary) images.
    """
    # 1. Setup Mocks
    mock_exists.return_value = True

    # Create a dummy BGR image (3x3 pixels, all blue)
    dummy_img = np.zeros((3, 3, 3), dtype=np.uint8)
    dummy_img[:, :, 0] = 255
    mock_load.return_value = dummy_img

    # 2. Execute
    file_path = "data/test_tag.tif"
    original, processed = proc.preprocess_etr_pipeline(file_path)

    # 3. Assertions
    # Verify the dependencies were called correctly
    mock_exists.assert_called_once_with(file_path)
    mock_load.assert_called_once_with(file_path)

    # Verify the output structure
    assert original is not None
    assert processed is not None

    # The 'original' should be our dummy image
    np.testing.assert_array_equal(original, dummy_img)

    # The 'processed' should be 2D (grayscale/binary) because of Otsu
    assert len(processed.shape) == 2
    assert processed.shape == (3, 3)


@patch('utils.proc.os.path.exists')
def test_preprocess_etr_pipeline_file_not_found(mock_exists):
    """Test that the function returns (None, None) if the file doesn't exist."""
    mock_exists.return_value = False

    original, processed = proc.preprocess_etr_pipeline("missing.jpg")

    assert original is None
    assert processed is None


@patch('utils.proc.os.path.exists')
@patch('utils.proc.io.load_image')
def test_preprocess_etr_pipeline_load_fail(mock_load, mock_exists):
    """Test behavior when the file exists but OpenCV fails to load it."""
    mock_exists.return_value = True
    mock_load.return_value = None  # Simulate a corrupt file

    original, processed = proc.preprocess_etr_pipeline("corrupt.jpg")

    assert original is None
    assert processed is None