import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import sys
from canny_edge_detector import CannyEdgeDetector

# Get the image.
image_path = str(sys.argv[1])
I = mpimg.imread(image_path)

# Show the image.
plt.imshow(I, cmap='gray')
plt.show()

# Run the canny edge detector (1-D).
edge_detector = CannyEdgeDetector(I, dimension=0, sigma=20)
final_image = edge_detector.detect_edges()

# Run the canny edge detector (2-D).
edge_detector = CannyEdgeDetector(I, dimension=1, sigma=2)
final_image = edge_detector.detect_edges()