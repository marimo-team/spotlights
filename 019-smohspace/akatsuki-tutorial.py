import marimo

__generated_with = "0.10.19"
app = marimo.App(
    width="medium",
    app_title="Akatsuki tutorial",
    html_head_file="head.html",
)


@app.cell(hide_code=True)
def _():
    # not used directly but for pyodide to pick up the dependency
    import netCDF4
    return (netCDF4,)


@app.cell(hide_code=True)
def _():
    from pathlib import Path
    import warnings
    import marimo as mo
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    return Path, mo, np, pd, plt, warnings


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Getting started with Akatsuki data

        By [Semyeong Oh](https://smoh.page)

        In this tutorial, we will explore the Akatsuki UVI and LIR data, which image the Venus cloud-top in reflected light and thermal emission respectively. Before diving in, please have a look at the slides below for an overview of the mission.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""## Introduction to the Akatsuki mission""")
    return


@app.cell(hide_code=True)
def slide(mo):
    mo.Html(
        """
    <div style="position: relative; width: 100%; height: 0; padding-top: 56.2500%;
     padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden;
     border-radius: 8px; will-change: transform;">
      <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
        src="https://www.canva.com/design/DAGbHXX2Ygw/RvcOpN1BPdgux23JSQFYOw/view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
      </iframe>
    </div>
    <a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAGbHXX2Ygw&#x2F;RvcOpN1BPdgux23JSQFYOw&#x2F;view?utm_content=DAGbHXX2Ygw&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">2025 akatsuki data workshop</a> by Semyeong Oh
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(
            """
    **Synopsis**: We will now download a small subset of the data, and explore the basic data structure and properties with [xarray](https://docs.xarray.dev/en/stable/) as our main tool.
    Everything is set up for you when you load the page. Get ready to start hacking!

    You can toggle between edit and view mode with <kbd>cmd/ctrl</kbd> + <kbd>.</kbd>."""
        ),
        kind="info",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Getting the data

        Akatsuki is JAXA's remote sensing mission to study the Venus atmosphere. The data are served at [**Data ARchives and Transmission System (DARTS)**](https://darts.isas.jaxa.jp/en) along with data from other missions by JAXA.

        To get the data, let's go to DARTS and locate [the Akatsuki data archive](https://www.darts.isas.jaxa.jp/planet/project/akatsuki/). Any news or new release of data will be announced on this page. As you work with the data, you are likely to constantly consult this site for information.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""Now, let's go specifically to UVI data archive. You will mainly work with **Level 3 map data**. What does this mean?""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""## Data processing""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(
        "public/data-levels.png",
        width=700,
        caption="Fig 1. Schematic diagram of the science data‐processing pipeline developed for Akatsuki. From Ogohara et al. 2017",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        There are multiple processing steps involved in going from telemetry data to science-ready images in a convenient format for researchers. You can see the overall flow in Fig 1, and refer to [Ogohara et al. 2017](https://earth-planets-space.springeropen.com/articles/10.1186/s40623-017-0749-5) for more details.

        Level 3 data means that the raw images have been fully calibrated into values with physical units, and the pointing geometry has been corrected using a procedure commonly refered to as **limb fitting**. Why is any pointing correction necessary? Because although the spacecraft was commanded to point at certain direction so that one of its instrument can take an image of Venus, the attitude control of the spacecraft and the aligntmnet of the instruments are never perfect. Assuming the visible Venus disk is an ellipse, we can do a retroactive pointing correction using the data already acquired by fitting an elllipse to the detected limb of the planet.

        To fit an ellipse, we first need to _detect_ the limb of the planet. How would we go about doing that? If you're curious about this and other details of the data processing, please refer to [Ogohara et al. 2017](https://earth-planets-space.springeropen.com/articles/10.1186/s40623-017-0749-5)!
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        f"""### Solving geometry with Limb fitting

    {mo.image("public/limb-fitting.png", width=600, caption="Fig 2. Examples of limb fitting in IR2 and LIR channels. Fig 5 of Ogohara et al. 2017. Notice that on the night side of IR2 (panel c), we cannot detect the limb, naturally.")}
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""Unless you really need to access the low-level data, you will most likely stick with the Level 3 data.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Data organization

        Now that we have some understanding of what level 3 data means and why we want to use them, let's explore the UVI archive. Go to Data Download > Level 3 dataset, and you will find a directory structure like below.

        ```txt

        /pub/pds3/extras/vco_uvi_l3_v1.1/
        ├── md5sum.txt
        ├── vcouvi_7008/
        ├── vcouvi_7008_l3b_netcdf.zip
        ├── vcouvi_7008_l3bx_netcdf.zip
        ├── vcouvi_7009/
        │   ├── 00readme.txt
        │   ├── browse/
        │   │   ├── l3b/
        │   │   └── l3bx/
        │   ├── checksum.txt
        │   ├── data/
        │   │   ├── l3b/
        │   │   └── l3bx/
        │   └── doc/
        ...
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        The data is organized in **volumes** (7008-7011 for the latest version, v1.1), and **orbits**. The orbits start from 'c0000' for up to orbit insertion to the target planet, and goes r0001, r0002, ... for the rest of the orbits around the planet.

        The images are provided either in FITS or netCDF format. I recommend that you use the **netCDF** format as it has become a standard in geoscientific data, and works well with [xarray](https://docs.xarray.dev/en/stable/), de facto standard tool to work with such data.

        In `browse` and `data` folders in each volume, you will find `l3b/` and `l3bx/`. The main difference between l3b and l3bx is that l3b data is a map sampled with a fixed longitude and latitude grids while l3bx data still has pixel X and Y as its axes. Here, we will explore the l3bx data.

        While the actual data is in `data/` folder of each volume, `browse/` contains thumbnail images and header files, which can be useful to quick browsing.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Let's look at some sample data

        The UVI and LIR instruments have been used to capture Venus every few hours since Akatsuki's orbit insertion in 2015 (although we [lost contact](https://www.space.com/jaxa-loses-contact-akatsuki-venus-probe) with the spacecraft recently). They have now accumulated tens of thousands of images in each channel.

        I have compiled a couple of UVI and LIR images from orbit 113 (r0113) and packaged them in a zip file for this workshop.
        """
    )
    return


@app.cell(hide_code=True)
def _(datastore, mo):
    def callout_datadownload(datastore):
        return mo.callout(
            mo.md(
                """
    **Sample data downloaded!** Check them out in the file browser tab on the left ("View files") :eyes:

    Note that any change in the filesystem is reset when you reload the page.
    """
            ),
            kind="info",
        )

    callout_datadownload(datastore)
    return (callout_datadownload,)


@app.cell
def _(Path, example_uvi):
    # Iterate through the directory contents
    def list_files_after_download(example_uvi):
        print("List of files in data/")
        for item in sorted(Path("data").iterdir()):
            if item.is_file():
                print(item.name)

    list_files_after_download(example_uvi)
    return (list_files_after_download,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Listing the files, you can see the file naming convention the Akatsuki team has adopted:
        ```
        <instrument>_<datestr>_<timestr>_<channel>_<data product shorthand>_<processing version>.nc.
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ### Data and metadata

        The core data for UVI and LIR instruments are **single-channel images**.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        There are a number of auxiliary "data" or "attributes" associated with the images. For example,

        - when was the image taken? (timestamp)
        - in what channel (wavelength) was the image taken?
        - what data processing version does this correspond to?
        - was the solution for geometry (limb fitting) adequate?
        - what was the distance between the spacecraft (=camera) and the planet? etc.


        These are often called the **metadata**.
        Metadata come from either the header keywords or "variables" (in netCDF-speak).
        All header keywords available are described in [the official documentation](https://darts.isas.jaxa.jp/missions/akatsuki/uvi_en.html).
        There's a whole slew of them but here are a few which might be immediately useful.
        """
    )
    return


@app.cell(hide_code=True)
def _(pd):
    from io import StringIO

    _t = pd.read_csv(
        StringIO(
            """
    Keyword|Description|Unit
    FIT_STAT|ellipsefit status;-2: OFF but prescribed S_SSCP[X,Y] was used,-1: OFF, 0: NG, 1: OK, 2: OK but inaccurate.|
    S_DISTAV|Sun-spacecraft distance|km
    S_SOLLON|longitude of the sub-Solar point|deg
    S_SOLLAT|latitude of the sub-Solar point|deg
    S_SSCLON|longitude of the sub-Spacecraft point|deg
    S_SSCLAT|latitude of the sub-Spacecraft point|deg
    D_NPVAZM|azmiuth of north pole vector in degrees. This angle is defined from the line going towards the left to be positive clock-wise. Thus, +90 deg is north pole up in the image plane, -90 deg vice versa|deg
    """
        ),
        delimiter="|",
    )
    _t
    return (StringIO,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""### Using xarray for analysis""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""Now let's import [xarray](https://docs.xarray.dev/en/stable/) and load the dataset.""")
    return


@app.cell
def _():
    import xarray as xr
    return (xr,)


@app.cell
def _(example_uvi, warnings, xr):
    print(f"{example_uvi=}")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        ds283 = xr.open_dataset(example_uvi)

    ds283
    return (ds283,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        [xarray](https://docs.xarray.dev/en/stable/) prints a pretty respresentation of the dataset, which makes it a breeze to examine the content, dimensions and coordinates, and data variables.

        There are 80 data variables in this dataset (image). Most are auxiliary data, and the image data variables will have three dimensions: (time, axis2, axis1). The axis2 and axis1 correspond to the vertical and horizontal direction of the image plane (detector).

        We can quickly collect the variable attributes into a dataframe.
        """
    )
    return


@app.cell(hide_code=True)
def _(ds283, pd, xr):
    def collect_variable_attributes():
        df_variables = pd.DataFrame(
            [
                dict(
                    name=k,
                    long_name=v.attrs["long_name"],
                    unit=(v.attrs["units"] if "units" in v.attrs else ""),
                    ndims=len(v.dims),
                    dims=v.dims,
                )
                for k, v in ds283.variables.items()
                if not isinstance(v, xr.IndexVariable)
            ]
        )
        return df_variables

    collect_variable_attributes()
    return (collect_variable_attributes,)


@app.cell
def _(mo):
    mo.md("""The variable capturing the actual image is `radiance`. [xarray](https://docs.xarray.dev/en/stable/) has built-in plotting routines, which makes it easy to make quick decent-looking plots. It automagically annoates the image using the metadata available.""")
    return


@app.cell
def _(ds283):
    ds283["radiance"].plot()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""Once we plot the image, there's something curious about the colorbar: the radiance (calibrated from photon counts) goes to negative, which cannot be! Well, they technically can be as there is always some statistical noise to a measurement but we can still examine how many pixels have negative radiance with the expectation that there should be very few.""")
    return


@app.cell
def _(ds283):
    npix_negative = (ds283["radiance"].stack(i=[...]) < 0).sum()
    npix_negative
    return (npix_negative,)


@app.cell(hide_code=True)
def _(ds283, mo, npix_negative):
    mo.md(
        f"Indeed, there are only {npix_negative.values} pixels out of {ds283['radiance'].size:,} ({npix_negative.values / ds283['radiance'].size * 100:.3f}%) that go to negative."
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""Let's adjust the minimum value of the color scale to a more reasonable value ignoring negative pixels.""")
    return


@app.cell
def _(ds283):
    ds283["radiance"].plot(vmin=ds283["radiance"].quantile(0.01))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Now there's the Venus, showing a hint of its well-known Y pattern. We know that the pointing geometry has been corrected with limb fitting. How do we orient ourselves on this image? Where is the north pole of Venus, for example, and where is the Sun?

        We can use the header keywords such as D_NPVAZM [^1] (north pole vector azimuth angle) to figure this out. In fact, in each data file, the detected limb points are also stored. Below I show an annoated image with the Venus north pole direction from the center and the limb points marked.

        [^1] As an aside, the keyword name prefixes such as 'S_' and 'D_' also have their meanings. [link](https://www.darts.isas.jaxa.jp/planet/project/akatsuki/doc/fits/vco_fits_dic_v07.html#notes)
        """
    )
    return


@app.cell
def _(ds283, plot_radiance):
    plot_radiance(ds283, mark_geom=True, mark_limb=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Each pixel that falls inside the Venus samples the radiance from the reflecting surface of the Venus cloud top. The level 3 data products provide the longitude and latitude of each pixel via `lon` and `lat` data variables. The incidence, emission and phase angles are readily available for each pixel.

        We can plot the contours of these variables on top of the Venus image. The location of incidencen angle zero is the direction of the Sun. The location of emission angle zero corresponds to the sub-spacecraft point.
        """
    )
    return


@app.cell
def _(ds283, plot_radiance, plt):
    def plot_with_contours():
        cvar = ["clear", "lon", "lat", "inangle", "emangle", "phangle"]
        common = dict(add_colorbar=False, add_labels=False)
        fig, ax = plt.subplots(
            2,
            3,
            figsize=(10, 6),
            subplot_kw=dict(aspect="equal"),
            sharex=True,
            sharey=True,
        )
        ax = ax.ravel()
        for clabel, cax in zip(cvar, ax):
            plot_radiance(
                ds283,
                contour_variable=clabel,
                ax=cax,
                **common,
                mark_geom=True if clabel == "emangle" else False,
            )
            cax.set(title=clabel, xlabel=None, ylabel=None)
        return fig

    plot_with_contours()
    return (plot_with_contours,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""With [marimo](https://marimo.io/), I made a quick interface to explore the rest of the sample data files in a similar manner. You will notice that LIR images are much smaller than UVI, and since they capture the thermal emission from the cloud top, you also see the whole disk including the night side.""")
    return


@app.cell(hide_code=True)
def _(contour_variable, mark_geom, mark_limb, mo, select_file, viewer):
    mo.vstack(
        [
            mo.md("### Explore sample UVI and LIR images"),
            mo.hstack(
                [
                    mo.vstack(
                        [
                            select_file,
                            mo.vstack([contour_variable, mark_geom, mark_limb]),
                        ]
                    ),
                    viewer,
                ],
                justify="start",
            ),
        ]
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Where to go from here

        Hopefully, by now you have a good idea what Akatsuki mission is, what kind of data it produced, and how to use them. I've listed a number of Akatsuki and python related resources for further exploration in the introduction slides.

        This is also a live python environment where you can play around with the data on your own!
        """
    )
    return


@app.cell(hide_code=True)
def attic_select_file(datastore, mo):
    select_file = mo.ui.radio(
        datastore, value="uvi_20190428_170113_283_l3bx_v21.nc", label="Select file"
    )
    return (select_file,)


@app.cell(hide_code=True)
def _(mo):
    contour_variable = mo.ui.radio(
        {
            v: k
            for k, v in dict(
                clear="Clear contour",
                inangle="Incidence angle",
                emangle="Emission angle",
                phangle="Phase angle",
                lat="Latitude",
                lon="Longitude",
            ).items()
        },
        label="Add contour:",
        value="Clear contour",
    )
    mark_geom = mo.ui.checkbox(label="Mark geometry")
    mark_limb = mo.ui.checkbox(label="Mark limb points")
    return contour_variable, mark_geom, mark_limb


@app.cell(hide_code=True)
def attic_plotting(np, plt):
    def get_center(ds):
        cx, cy = ds["D_SSCPXF"].values, ds["D_SSCPYF"].values
        return (cx, cy)

    def get_naxis1(ds):
        return ds["axis1"].size

    def draw_arrow(center, angle, length=200, ax=None):
        if ax is None:
            ax = plt.gca()
        x, y = center
        dx, dy = length * np.cos(np.deg2rad(angle)), length * np.sin(np.deg2rad(angle))
        ax.annotate(
            "North",
            xy=(x, y),
            xytext=(x + dx, y + dy),
            color="w",
            arrowprops=dict(
                arrowstyle="<-", mutation_scale=20, color="w", linewidth=1.3
            ),
        )

    def plot_radiance(
        ds, contour_variable=None, mark_limb=False, mark_geom=False, ax=None, **kwargs
    ):
        if ax is None:
            fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))
        else:
            fig, ax = ax.figure, ax

        ds = ds.isel(time=0)
        ds["radiance"].plot(
            ax=ax, cmap="cividis", vmin=ds["radiance"].quantile(0.01), **kwargs
        )
        if contour_variable is not None and contour_variable != "clear":
            cs1 = ds[contour_variable].plot.contour(ax=ax, linewidths=1)
            ax.clabel(cs1)

        if mark_limb:
            ax.plot(
                ds["lpxf"], ds["lpyf"], marker="x", ls="none", ms=1, color="#AFDDFF"
            )
        if mark_geom:
            ax.plot(*get_center(ds), marker="+", color="k", ms=10)
            draw_arrow(
                get_center(ds),
                180 - float(ds["S_NPVAZM"].values),
                length=get_naxis1(ds) * 0.2,
                ax=ax,
            )
        return fig
    return draw_arrow, get_center, get_naxis1, plot_radiance


@app.cell(hide_code=True)
def _(contour_variable, mark_geom, mark_limb, plot_radiance, select_file):
    # NOTE: it is important I put this in a separate cell to minimize re-execution of the helper func plot_radiance!

    def plot_radiance_viewer():
        return plot_radiance(
            select_file.value, contour_variable.value, mark_limb.value, mark_geom.value
        )

    viewer = plot_radiance_viewer()
    return plot_radiance_viewer, viewer


@app.cell(hide_code=True)
def _(Path, mo, warnings, xr):
    # NOTE: xarray+netcdf4's io support for http is janky... Just download to local
    # relevant thread: https://github.com/pydata/xarray/issues/3653
    from pyodide.http import pyfetch

    async def fetch_binary_file(url):
        import io

        response = await pyfetch(url)
        if response.ok:
            array_buffer = await response.buffer()
            binary_data = io.BytesIO(array_buffer.to_py())
            return binary_data
        else:
            raise OSError(
                f"Failed to fetch file: {response.status} {response.statusText}"
            )

    async def download_data():
        from zipfile import ZipFile

        if not Path("data").exists():
            binary_file = await fetch_binary_file(
                mo.notebook_location() / "public/data.zip"
            )
            with open("data.zip", "wb") as ff:
                ff.write(binary_file.read())
            assert Path(
                "data.zip"
            ).exists(), "something went wrong; data.zip doesn't exist!"
            with ZipFile("data.zip", "r") as zip_ref:
                zip_ref.extractall()
        else:
            print("data/ already exists.")
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore")
            datastore = {
                str(k).split("/")[-1]: xr.load_dataset(k)
                for k in sorted(Path("data").glob("*.nc"))
            }
        return "data/uvi_20190428_170113_283_l3bx_v21.nc", datastore
    return download_data, fetch_binary_file, pyfetch


@app.cell(hide_code=True)
async def _(download_data):
    example_uvi, datastore = await download_data()
    return datastore, example_uvi


if __name__ == "__main__":
    app.run()
