import marimo

__generated_with = "0.6.16"
app = marimo.App()


@app.cell
def __(mo):
    mo.md ("# K-d tree art")
    return


@app.cell
def __(mo):
    mo.md (" Adapted for marimo WASM from https://colab.research.google.com/drive/1Ou3WRwicz31enMKVWl5v4F1f1_haSlTI")
    return


@app.cell
def __():
    import micropip
    return micropip,


@app.cell
async def __(micropip):
    await micropip.install(['numpy', 'scipy', 'scikit-learn'])
    return


@app.cell
def __():
    # @title Import Modules (run once)
    from sklearn.datasets import make_blobs
    from sklearn.neighbors import KDTree
    from matplotlib.patches import Rectangle
    from matplotlib import pyplot as plt
    import matplotlib
    import numpy as np
    import pandas as pd
    return KDTree, Rectangle, make_blobs, matplotlib, np, pd, plt


@app.cell
def __(
    KDTree,
    Rectangle,
    centers_max,
    centers_min,
    cluster_std,
    color_by_area,
    color_map,
    figsize,
    invert_colors,
    leaf_size,
    make_blobs,
    mo,
    n_samples,
    np,
    pd,
    plt,
    randomize_colors,
    seed,
):
    # Accessing values
    values = {
        "figsize": figsize.value,
        "color_map": color_map.value,
        "randomize_colors": randomize_colors.value,
        "color_by_area": color_by_area.value,
        "invert_colors": invert_colors.value,
        "cluster_std": cluster_std.value,
        "n_samples": n_samples.value,
        "centers_min": centers_min.value,
        "centers_max": centers_max.value,
        "leaf_size": leaf_size.value,
        "seed": seed.value,
    }
    mo.md(f"Values: {values}")

    # Using values
    _seed_value = int(seed.value)
    if _seed_value == 0:
        _seed_value = None
    np.random.seed(_seed_value)
    _centers = np.random.randint(int(centers_min.value), int(centers_max.value))

    _X, _y = make_blobs(n_samples=int(n_samples.value),
                        centers=_centers, cluster_std=float(cluster_std.value), random_state=_seed_value)

    _kdt = KDTree(_X, leaf_size=int(leaf_size.value))

    _tree_data, _index, _node_data, _node_bounds = _kdt.get_arrays()
    _rearranged_bounds = np.transpose(_node_bounds, axes=[1, 2, 0])
    _df = pd.DataFrame({
        'x_min': _rearranged_bounds[:, 0, 0],
        'x_max': _rearranged_bounds[:, 0, 1],
        'y_min': _rearranged_bounds[:, 1, 0],
        'y_max': _rearranged_bounds[:, 1, 1],
    })
    _fig = plt.figure(figsize=(int(figsize.value), int(figsize.value)))
    _ax = _fig.add_subplot()

    _cmap = plt.get_cmap(color_map.value)
    _colors = [_cmap(i / len(_df.index)) for i in range(len(_df.index))]

    _background_color = _colors[0]
    if invert_colors.value:
        _colors = _colors[::-1]

    if randomize_colors.value:
        np.random.seed(_seed_value)
        _colors = np.random.permutation(_colors)

    if color_by_area.value:
        _areas = np.array([])
        for _, _row in _df.iterrows():
            _x_min, _x_max, _y_min, _y_max = _row
            _area = ((_x_max - _x_min) * (_y_max - _y_min))
            _areas = np.append(_areas, _area)

        def _normalize(arr):
            _mx = np.max(arr)
            _mn = np.mean(arr)
            _div = _mx - _mn
            _out = []
            for _o in range(len(arr)):
                _out.append((arr[_o] - _mn) / _div)
            return np.array(_out) * (len(arr) - 1)

        _normalized_areas = _normalize(_areas).astype(int)
        _normalized_areas = np.abs(_normalized_areas - (len(_normalized_areas) - 1))

        _normalized_areas = np.argsort(_normalized_areas)

        _df = _df.iloc[_normalized_areas]

    _i = 0
    for _, _row in _df.iterrows():
        _x_min, _x_max, _y_min, _y_max = _row
        _rect = Rectangle((_x_min, _y_min), _x_max - _x_min, _y_max - _y_min, alpha=1, color=_colors[_i])
        _ax.add_patch(_rect)
        _i += 1

    plt.scatter(_X[:, 0], _X[:, 1], alpha=0)
    plt.axis('off')
    plt.tight_layout()
    _ax.set_aspect('equal', adjustable='box')
    plt.show()
    return values,


@app.cell
def __():
    import marimo as mo

    # Figure Size input
    figsize = mo.ui.dropdown(
        label="Figure Size",
        options=['16', '32', '64'],
        value='32'
    )

    # Color options input
    color_map = mo.ui.dropdown(
        label="Color options",
        options=[
            'magma', 'inferno', 'plasma', 'viridis', 'cividis', 'twilight', 
            'twilight_shifted', 'turbo', 'Blues', 'BrBG', 'BuGn', 'BuPu', 
            'CMRmap', 'GnBu', 'Greens', 'Greys', 'OrRd', 'Oranges', 'PRGn', 
            'PiYG', 'PuBu', 'PuBuGn', 'PuOr', 'PuRd', 'Purples', 'RdBu', 
            'RdGy', 'RdPu', 'RdYlBu', 'RdYlGn', 'Reds', 'Spectral', 'Wistia', 
            'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd', 'afmhot', 'autumn', 'binary', 
            'bone', 'brg', 'bwr', 'cool', 'coolwarm', 'copper', 'cubehelix', 
            'flag', 'gist_earth', 'gist_gray', 'gist_heat', 'gist_ncar', 
            'gist_rainbow', 'gist_stern', 'gist_yarg', 'gnuplot', 'gnuplot2', 
            'gray', 'hot', 'hsv', 'jet', 'nipy_spectral', 'ocean', 'pink', 
            'prism', 'rainbow', 'seismic', 'spring', 'summer', 'terrain', 
            'winter', 'Accent', 'Dark2', 'Paired', 'Pastel1', 'Pastel2', 
            'Set1', 'Set2', 'Set3', 'tab10', 'tab20', 'tab20b', 'tab20c',
            'magma_r', 'inferno_r', 'plasma_r', 'viridis_r', 'cividis_r', 
            'twilight_r', 'twilight_shifted_r', 'turbo_r', 'Blues_r', 'BrBG_r', 
            'BuGn_r', 'BuPu_r', 'CMRmap_r', 'GnBu_r', 'Greens_r', 'Greys_r', 
            'OrRd_r', 'Oranges_r', 'PRGn_r', 'PiYG_r', 'PuBu_r', 'PuBuGn_r', 
            'PuOr_r', 'PuRd_r', 'Purples_r', 'RdBu_r', 'RdGy_r', 'RdPu_r', 
            'RdYlBu_r', 'RdYlGn_r', 'Reds_r', 'Spectral_r', 'Wistia_r', 
            'YlGn_r', 'YlGnBu_r', 'YlOrBr_r', 'YlOrRd_r', 'afmhot_r', 
            'autumn_r', 'binary_r', 'bone_r', 'brg_r', 'bwr_r', 'cool_r', 
            'coolwarm_r', 'copper_r', 'cubehelix_r', 'flag_r', 'gist_earth_r', 
            'gist_gray_r', 'gist_heat_r', 'gist_ncar_r', 'gist_rainbow_r', 
            'gist_stern_r', 'gist_yarg_r', 'gnuplot_r', 'gnuplot2_r', 'gray_r', 
            'hot_r', 'hsv_r', 'jet_r', 'nipy_spectral_r', 'ocean_r', 'pink_r', 
            'prism_r', 'rainbow_r', 'seismic_r', 'spring_r', 'summer_r', 
            'terrain_r', 'winter_r', 'Accent_r', 'Dark2_r', 'Paired_r', 
            'Pastel1_r', 'Pastel2_r', 'Set1_r', 'Set2_r', 'Set3_r', 'tab10_r', 
            'tab20_r', 'tab20b_r', 'tab20c_r'
        ],
        value="magma"
    )

    # Boolean inputs
    randomize_colors = mo.ui.switch(label="Randomize colors", value=False)
    color_by_area = mo.ui.switch(label="Color by area", value=True)
    invert_colors = mo.ui.switch(label="Invert colors", value=False)

    # Blob options
    cluster_std = mo.ui.number(
        label="Cluster Std",
        start=0.0,
        stop=1.0,
        step=0.1,
        value=0.4,
        debounce=False,
        full_width=False
    )
    n_samples = mo.ui.number(
        label="Number of Samples",
        start=1000.0,
        stop=10000.0,
        step=100.0,
        value=5000.0,
        debounce=False,
        full_width=False
    )
    centers_min = mo.ui.number(
        label="Centers Min",
        start=10.0,
        stop=1000.0,
        step=10.0,
        value=100.0,
        debounce=False,
        full_width=False
    )
    centers_max = mo.ui.number(
        label="Centers Max",
        start=10.0,
        stop=1000.0,
        step=10.0,
        value=500.0,
        debounce=False,
        full_width=False
    )

    # K-d tree options
    leaf_size = mo.ui.number(
        label="Leaf Size",
        start=1.0,
        stop=50.0,
        step=1.0,
        value=1.0,
        debounce=False,
        full_width=False
    )
    # K-d tree options
    seed = mo.ui.number(
        label="Seed",
        start=0.0,
        stop=100.0,
        step=1.0,
        value=0.0,
        debounce=False,
        full_width=False
    )



    # Displaying all UI elements
    mo.vstack([
        figsize, color_map, randomize_colors, color_by_area, invert_colors,
        cluster_std, n_samples, centers_min, centers_max, leaf_size, seed
    ])
    return (
        centers_max,
        centers_min,
        cluster_std,
        color_by_area,
        color_map,
        figsize,
        invert_colors,
        leaf_size,
        mo,
        n_samples,
        randomize_colors,
        seed,
    )


if __name__ == "__main__":
    app.run()