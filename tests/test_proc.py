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