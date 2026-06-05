from pathlib import Path

import numpy as np
import nibabel as nib
import matplotlib
matplotlib.use("Agg")

from nilearn.datasets import fetch_atlas_difumo
from nilearn import plotting


out_dir = Path("bhs_modules/nibabel/outputs")
out_dir.mkdir(parents=True, exist_ok=True)

print("Fetching DiFuMo atlas with 64 regions...")
atlas = fetch_atlas_difumo(dimension=64, resolution_mm=2)

print("Loading atlas with nibabel...")
maps_img = nib.load(atlas.maps)

print("Atlas maps file:", atlas.maps)
print("Atlas image shape:", maps_img.shape)
print("Atlas voxel sizes:", maps_img.header.get_zooms())

# The module asks for the 16th region.
# Python counts from 0, so the 16th region is index 15.
region_number = 16
region_index = region_number - 1

print("Extracting region number:", region_number)
print("Python index used:", region_index)

# Use nibabel's slicer object to extract the 16th 3D volume from the 4D atlas.
region_img = maps_img.slicer[:, :, :, region_index]

# Convert to array so we can binarize it.
region_data = region_img.get_fdata()
region_binary = (region_data > 0).astype(np.uint8)

# Save as a new NIfTI image.
binary_img = nib.Nifti1Image(
    region_binary,
    affine=region_img.affine,
    header=region_img.header.copy()
)
binary_img.header.set_data_dtype(np.uint8)

out_nii = out_dir / "difumo64_region16_binary.nii.gz"
nib.save(binary_img, out_nii)

print("Binary image shape:", binary_img.shape)
print("Binary voxel count:", int(region_binary.sum()))
print("Saved binary NIfTI:", out_nii)

# Save three views for submission.
views = {
    "x": "sagittal",
    "y": "coronal",
    "z": "axial",
}

for display_mode, view_name in views.items():
    display = plotting.plot_roi(
        binary_img,
        display_mode=display_mode,
        title=f"DiFuMo 64 Region 16 Binary Mask - {view_name}"
    )
    out_png = out_dir / f"difumo64_region16_binary_{view_name}.png"
    display.savefig(out_png)
    display.close()
    print("Saved", view_name, "view:", out_png)

# Also save one combined orthogonal image.
display = plotting.plot_roi(
    binary_img,
    display_mode="ortho",
    title="DiFuMo 64 Region 16 Binary Mask - orthogonal views"
)
out_png = out_dir / "difumo64_region16_binary_orthogonal.png"
display.savefig(out_png)
display.close()
print("Saved orthogonal view:", out_png)

print("DONE 🧠✨")
