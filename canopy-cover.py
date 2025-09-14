import cv2
import numpy as np
import os
import csv

def calculate_canopy_cover(image_path, mask_output_path=None, overlay_output_path=None):
    # Read image
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    # Convert to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define green color range (adjust as needed)
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([90, 255, 255])

    # Mask for green pixels
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Save mask image (black/white)
    if mask_output_path:
        cv2.imwrite(mask_output_path, mask)

    # Create overlay (highlight vegetation in red on top of original image)
    if overlay_output_path:
        overlay = img.copy()
        overlay[mask > 0] = [0, 0, 255]  # red for vegetation
        blended = cv2.addWeighted(img, 0.7, overlay, 0.3, 0)
        cv2.imwrite(overlay_output_path, blended)

    # Calculate canopy cover percentage
    green_pixels = np.count_nonzero(mask)
    total_pixels = mask.size
    canopy_cover = green_pixels / total_pixels * 100  

    return canopy_cover


def average_canopy_cover(folder_path, output_csv="outputs/canopy_results.csv", mask_dir="outputs/masks", overlay_dir="outputs/overlays"):
    covers = []
    results = []

    # Create output folders if missing
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    os.makedirs(mask_dir, exist_ok=True)
    os.makedirs(overlay_dir, exist_ok=True)

    # Process images
    for file in os.listdir(folder_path):
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.tif')):
            path = os.path.join(folder_path, file)
            mask_path = os.path.join(mask_dir, f"mask_{file}")
            overlay_path = os.path.join(overlay_dir, f"overlay_{file}")

            cover = calculate_canopy_cover(path, mask_output_path=mask_path, overlay_output_path=overlay_path)
            covers.append(cover)
            results.append([file, f"{cover:.2f}"])
            print(f"{file}: {cover:.2f}% (mask: {mask_path}, overlay: {overlay_path})")
    
    avg_cover = np.mean(covers) if covers else 0
    print(f"\nAverage Canopy Cover: {avg_cover:.2f}%")

    # Save results to CSV
    with open(output_csv, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Image", "CanopyCover(%)"])
        writer.writerows(results)
        writer.writerow([])
        writer.writerow(["Average", f"{avg_cover:.2f}"])

    print(f"\n✅ Results saved to {output_csv}")
    return avg_cover


# Example usage:
if __name__ == "__main__":
    folder = "field_images"  # Change this to your folder of images
    average_canopy_cover(folder)
