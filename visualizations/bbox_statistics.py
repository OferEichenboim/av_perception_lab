import numpy as np
import matplotlib.pyplot as plt

def plot_bbox_hw_distribution(
    hw,
    *,
    normalize=False,
    image_shape=None,
    bins=50,
    method="hist2d",   # "hist2d" | "hexbin"
    log_scale=False,
    ax=None,
    title=None
):
    """
    Plot 2D distribution of bounding box Height × Width.

    Parameters
    ----------
    hw : array-like, shape (N, 2)
        Bounding box sizes as (height, width).
    normalize : bool
        If True, normalize H and W by image_shape.
    image_shape : tuple (H_img, W_img)
        Required if normalize=True.
    bins : int
        Number of bins per dimension (hist2d).
    method : str
        "hist2d" or "hexbin".
    log_scale : bool
        Apply log scaling to density.
    ax : matplotlib.axes.Axes
        Existing axes to draw on.
    title : str
        Plot title.
    """

    hw = np.asarray(hw)
    assert hw.ndim == 2 and hw.shape[1] == 2, "hw must be (N, 2): (H, W)"

    h = hw[:, 0]
    w = hw[:, 1]

    if normalize:
        assert image_shape is not None, "image_shape required for normalization"
        H_img, W_img = image_shape
        h = h / H_img
        w = w / W_img

    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 6))

    if method == "hist2d":
        hist = ax.hist2d(
            w, h,
            bins=bins,
            norm="log" if log_scale else None
        )
        plt.colorbar(hist[3], ax=ax, label="Count")

    elif method == "hexbin":
        hb = ax.hexbin(
            w, h,
            gridsize=bins,
            bins="log" if log_scale else None,
            mincnt=1
        )
        plt.colorbar(hb, ax=ax, label="Count")

    else:
        raise ValueError("method must be 'hist2d' or 'hexbin'")

    ax.set_xlabel("Width" + (" (normalized)" if normalize else ""))
    ax.set_ylabel("Height" + (" (normalized)" if normalize else ""))
    ax.set_title(title or "Bounding Box H×W Distribution")
    ax.set_aspect("equal")

    return ax
