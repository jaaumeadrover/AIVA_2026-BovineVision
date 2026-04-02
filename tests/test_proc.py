import numpy as np
from utils import proc

def test_preprocess():
    """Test BGR to RGB conversion."""
    # Create a 2x2 blue image in BGR format: [Blue, Green, Red]
    bgr_img = np.zeros((2, 2, 3), dtype=np.uint8)
    bgr_img[:, :] = [255, 0, 0] 

    # Execute the function
    rgb_img = proc.preprocess(bgr_img)

    # Verify the output is now RGB: [Red, Green, Blue] -> [0, 0, 255]
    assert rgb_img.shape == (2, 2, 3)
    assert np.array_equal(rgb_img[0, 0], [0, 0, 255])


def test_preprocess_image_array_success():
    """Test that a valid BGR image is processed into a binary 2D image."""
    # Create a dummy BGR image (3 channels) with some "text-like" contrast
    # A 10x10 image: top half dark, bottom half light
    input_img = np.zeros((10, 10, 3), dtype=np.uint8)
    input_img[5:, :, :] = 200

    result = proc.preprocess_image_array(input_img)

    assert result is not None
    # Result should be 2D (grayscale/binary)
    assert len(result.shape) == 2
    assert result.shape == (10, 10)
    # Check if it contains binary values (Otsu should produce 0 and 255)
    assert np.all(np.isin(result, [0, 255]))


def test_preprocess_image_array_already_gray():
    """Test that it handles an image that is already in grayscale."""
    # Create a 2D grayscale dummy image
    input_img = np.zeros((10, 10), dtype=np.uint8)
    input_img[5:, :] = 180

    result = proc.preprocess_image_array(input_img)

    assert result is not None
    assert result.shape == (10, 10)
    assert len(result.shape) == 2


def test_preprocess_image_array_invalid_input():
    """Test that the function returns None for non-ndarray inputs."""
    assert proc.preprocess_image_array(None) is None
    assert proc.preprocess_image_array("not an array") is None
    assert proc.preprocess_image_array(123) is None
