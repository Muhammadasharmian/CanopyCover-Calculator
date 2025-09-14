# CanopyCover-Calculator

🌱 Average Canopy Cover Estimator

This repository provides a Python tool for calculating canopy cover percentage from field images.
The script processes images in a folder, detects vegetation using HSV color thresholding, and computes:

- Canopy cover per image
- Average canopy cover across all images
- Saves results to a CSV file
- Saves vegetation masks (black/white)
- Saves overlay images (vegetation highlighted in red on top of the original photo)

---

Features
- Works with .jpg, .jpeg, .png, .tif images
- Customizable HSV thresholds for detecting green vegetation
- Outputs canopy cover (%) for each image
- Computes the average canopy cover for the dataset
- Saves results in a CSV file (outputs/canopy_results.csv)
- Saves vegetation masks (outputs/masks/)
- Saves overlay images (outputs/overlays/) for easy visual verification
- Extendable with vegetation indices (ExG, NDVI) or ML segmentation

---

Installation

1. Clone the repo:
   git clone https://github.com/yourusername/canopy-cover-estimator.git
   cd canopy-cover-estimator

2. (Optional) Create a virtual environment:
   python -m venv venv
   source venv/bin/activate   # on Linux/Mac
   venv\Scripts\activate      # on Windows

3. Install dependencies:
   pip install -r requirements.txt

---

Usage

1. Place your field images inside a folder called field_images/.

2. Run the script:
   python canopy_cover.py

3. Example console output:
   image1.jpg: 47.23% (mask: outputs/masks/mask_image1.jpg, overlay: outputs/overlays/overlay_image1.jpg)
   image2.jpg: 52.87% (mask: outputs/masks/mask_image2.jpg, overlay: outputs/overlays/overlay_image2.jpg)
   image3.jpg: 49.15% (mask: outputs/masks/mask_image3.jpg, overlay: outputs/overlays/overlay_image3.jpg)

   Average Canopy Cover: 49.75%
   ✅ Results saved to outputs/canopy_results.csv

4. Example CSV file (outputs/canopy_results.csv):
   Image,CanopyCover(%)
   image1.jpg,47.23
   image2.jpg,52.87
   image3.jpg,49.15

   Average,49.75

5. Example Outputs:
   - Mask (black/white) → outputs/masks/mask_image1.jpg
   - Overlay (vegetation in red) → outputs/overlays/overlay_image1.jpg

---

Adjusting Thresholds

Vegetation detection is based on HSV color ranges.
Inside canopy_cover.py, you can change these values to fit your crop/soil conditions:

lower_green = np.array([35, 40, 40])
upper_green = np.array([90, 255, 255])

- Increase/decrease the hue range if vegetation isn’t detected well.
- Adjust saturation/value thresholds to minimize shadows or soil interference.

---

License
MIT License – feel free to use and adapt for your research.

