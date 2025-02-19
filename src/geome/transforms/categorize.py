from typing import Literal

from anndata import AnnData

from .transform import Transform


class Categorize(Transform):
    """Converts the given list of observation columns in the AnnData object to categorical.

    One should do this if they expect one-hot encoding to be performed on the given columns.
    """

    def __init__(self, keys: str, axis: Literal[0, 1, "obs", "var"] = "obs"):
        self.keys = keys
        if axis not in (0, 1, "obs", "var"):
            raise TypeError("axis needs to be one of obs, var, 0 or 1")
        if isinstance(axis, int):
            axis = ("obs", "var")[axis]
        self.axis = axis

    def __call__(self, adata: AnnData):
        """Converts the given list of observation columns in the AnnData object to categorical.

        Args:
        ----
        adata: The AnnData object.
        obs_list (list[str]): The list of observation columns to convert to categorical.
        """
        for key in self.keys:
            getattr(adata, self.axis)[key] = getattr(adata, self.axis)[key].astype("category")
        return adata
