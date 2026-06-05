from pathlib import Path
import json

import nibabel as nib
import numpy as np
import pandas as pd
from nilearn import datasets, plotting, image


MODULE_DIR = Path(__file__).resolve().parents[1]
FIG_DIR = MODULE_DIR / "figures"
OUT_DIR = MODULE_DIR / "outputs"

FIG_DIR.mkdir(parents=True, exist_ok=True)
OUT_DIR.mkdir(parents=True, exist_ok=True)


def get_atlas_img_and_path(atlas):
    """
    Return a NiBabel/Nilearn image and a readable path/description.

    Some Nilearn atlases return a file path.
    Others return an already-loaded Nifti1Image.
    This function handles both.
    """
    maps = atlas["maps"]

    if isinstance(maps, (list, tuple)):
        if len(maps) == 1:
            maps = maps[0]
        else:
            img = image.concat_imgs(maps)
            return img, "multiple maps concatenated"

    if isinstance(maps, (str, Path)):
        img = nib.load(str(maps))
        return img, str(maps)

    # For atlases that already return a Nifti1Image
    if hasattr(maps, "shape") and hasattr(maps, "affine"):
        return maps, "Nifti1Image object returned directly by Nilearn"

    raise TypeError(f"Unsupported atlas map type: {type(maps)}")


def summarize_atlas(name, atlas, atlas_family, notes):
    img, map_description = get_atlas_img_and_path(atlas)
    data = img.get_fdata()

    if data.ndim == 3:
        nonzero = data[data != 0]
        unique_nonzero = np.unique(nonzero)
        unique_summary = len(unique_nonzero)
    else:
        unique_summary = "4D/probabilistic"

    labels = atlas.get("labels", [])
    template = atlas.get("template", "not specified")
    atlas_type = atlas.get("atlas_type", "not specified")

    summary = {
        "atlas_name": name,
        "atlas_family": atlas_family,
        "atlas_type": atlas_type,
        "template": template,
        "image_shape": str(img.shape),
        "voxel_sizes_mm": str(tuple(round(x, 3) for x in img.header.get_zooms()[:3])),
        "n_labels_reported": len(labels),
        "n_unique_nonzero_values_3d_only": unique_summary,
        "map_source": map_description,
        "notes": notes,
    }

    return summary, img


def plot_atlas(name, img, probabilistic=False):
    out_file = FIG_DIR / f"{name.replace(' ', '_').replace('/', '-')}.png"

    if probabilistic or len(img.shape) == 4:
        display = plotting.plot_prob_atlas(
            img,
            title=name,
            draw_cross=False,
            display_mode="ortho",
        )
    else:
        display = plotting.plot_roi(
            img,
            title=name,
            draw_cross=False,
            display_mode="ortho",
        )

    display.savefig(out_file)
    display.close()
    return out_file


def main():
    atlas_specs = []

    schaefer = datasets.fetch_atlas_schaefer_2018(
        n_rois=100,
        yeo_networks=7,
        resolution_mm=2,
        verbose=1,
    )
    atlas_specs.append((
        "Schaefer 2018, 100 ROIs, 7 networks",
        schaefer,
        "functional cortical parcellation",
        "Useful for connectivity/decoding because parcels are functionally defined and relatively balanced.",
        False,
    ))

    harvard = datasets.fetch_atlas_harvard_oxford(
        "cort-maxprob-thr25-2mm",
        verbose=1,
    )
    atlas_specs.append((
        "Harvard-Oxford cortical maxprob 25%, 2mm",
        harvard,
        "anatomical cortical atlas",
        "Useful as an interpretable anatomical reference, but less functionally specific than Schaefer.",
        False,
    ))

    aal = datasets.fetch_atlas_aal(
        version="SPM12",
        verbose=1,
    )
    atlas_specs.append((
        "AAL SPM12",
        aal,
        "anatomical atlas",
        "Common and easy to explain, but label indices are not always consecutive, so ROI handling needs care.",
        False,
    ))

    msdl = datasets.fetch_atlas_msdl(
        verbose=1,
    )
    atlas_specs.append((
        "MSDL probabilistic atlas",
        msdl,
        "probabilistic functional atlas",
        "Useful for network-like spatial maps, but 4D/probabilistic atlases need different handling than label atlases.",
        True,
    ))

    summaries = []

    for name, atlas, family, notes, probabilistic in atlas_specs:
        print(f"\nInspecting: {name}")
        summary, img = summarize_atlas(name, atlas, family, notes)
        fig_path = plot_atlas(name, img, probabilistic=probabilistic)
        summary["figure_path"] = str(fig_path)
        summaries.append(summary)

    df = pd.DataFrame(summaries)
    csv_path = OUT_DIR / "atlas_audit_summary.csv"
    json_path = OUT_DIR / "atlas_audit_summary.json"

    df.to_csv(csv_path, index=False)
    json_path.write_text(json.dumps(summaries, indent=2), encoding="utf-8")

    print("\nAtlas audit complete.")
    print(f"Saved CSV: {csv_path}")
    print(f"Saved JSON: {json_path}")
    print(f"Saved figures in: {FIG_DIR}")

    print("\nSummary table:")
    print(df[[
        "atlas_name",
        "atlas_family",
        "atlas_type",
        "template",
        "image_shape",
        "voxel_sizes_mm",
        "n_labels_reported",
    ]])


if __name__ == "__main__":
    main()
