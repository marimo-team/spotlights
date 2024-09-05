# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "colorspacious",
#     "matplotlib",
#     "numpy",
# ]
# ///

import marimo

__generated_with = "0.8.11"
app = marimo.App(width="medium", layout_file="layouts/stem-probes.slides.json")


@app.cell
def __(defocus, fig, mo):
    mo.md(
        rf"""
    # STEM Probes

    {mo.as_html(fig).center()}
    {defocus.center()}

    > Georgios Varnavides | 07/11/2024  
    > National Center for Electron Microscopy, Molecular Foundry, Berkeley Lab  

    """
    ).center()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        # Focused Electron Probes

        In scanning transmission electron microscopy (STEM), a focused probe of electrons can be described mathematically in Fourier space using:

        $$
            \psi(\boldsymbol{k}) = A(\boldsymbol{k}) \exp \left( -i \chi (\boldsymbol{k}) \right),
        $$

        where A(**k**) is the probe aperture function and χ(**k**) is the aberration surface evaluated at spatial frequency **k**.  
        The real-space probe function can then be obtained using the inverse Fourier transform:

        $$
            \psi(\boldsymbol{r}) = \mathcal{F}^{-1} \left[ \psi(\boldsymbol{k}) \right].
        $$

        """
    ).center()
    return


@app.cell(hide_code=True)
def __(convergence_angle, fig_aperture, mo):
    mo.md(
        rf"""
        # Aperture Function
        First, let's investigate the effect of the aperture function, which is typically radially-symmetric.  
        We normalize the physical aperture diameter by its distance to the sample to define the _convergence semiangle_.

        {mo.as_html(fig_aperture).center()}
        {convergence_angle.center()}

        Notice how smaller convergence semiangles correspond to larger real-space probes.  
        Typically, for atomic-resolution STEM, we want a sub-atomic spacing probe hence we use large convergence angles.
    """
    ).center()
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        # Probe Aberrations

        As we just saw, in theory for ideal lenses, larger convergence semiangles result in more tightly-focused probes.  
        In practice, however, the electromagnetic lenses used in electron microscopes introduce considerable aberrations.  
        These become more pronnounced the further away from the optic axis, thus limiting the maximum operating convergence semiangles.

        Mathematically, the aberration surface can be expressed as a Zernike-like series expansion in polar form:

        $$
            \chi(k,\phi) = \frac{2\pi}{\lambda} \sum_{n,m} \frac{1}{n+1}C_{n,m}(k \lambda)^{n+1} \cos \left[m\left(\phi - \phi_{n,m} \right) \right],
        $$

        where n and m are the radial and azimuthal orders of the polar aberration coefficient Cnm, and:

        $$
        \begin{aligned}
            k &= \sqrt{k_x^2+k_y^2} \\
            \phi &= \arctan \left(k_y/k_x\right)
        \end{aligned}
        $$

        """
    ).center()
    return


@app.cell
def __(
    astigmatism,
    astigmatism_angle,
    convergence_angle,
    defocus,
    fig,
    mo,
):
    mo.md(
        f"""
        # Aberrated STEM Probes

        Finally, let's investigate the effect of low-order aberrations (defocus and astigmatism) on STEM probes.

        {mo.as_html(fig).center()}
        {convergence_angle.center()}
        {defocus.center()}
        {astigmatism.center()}
        {astigmatism_angle.center()}
    """
    ).center()
    return


@app.cell(hide_code=True)
def __(mo):
    # controls
    defocus = mo.ui.slider(
        start=-100, stop=100, step=5, label="defocus [Å]", show_value=True
    )

    astigmatism = mo.ui.slider(
        start=0, stop=200, step=5, label="astigmatism [Å]", show_value=True
    )

    astigmatism_angle = mo.ui.slider(
        start=-90, stop=90, step=1, label="astigmatism angle [°]", show_value=True
    )

    convergence_angle = mo.ui.slider(
        start=5,
        stop=40,
        value=20,
        step=0.5,
        label="convergence semiangle [mrad]",
        show_value=True,
    )
    return astigmatism, astigmatism_angle, convergence_angle, defocus


@app.cell(hide_code=True)
def __(add_scalebar, build_probes, convergence_angle, plt, show_complex):
    # aperture figure
    fig_aperture, (ax_aperture_fourier, ax_aperture_real) = plt.subplots(
        1, 2, figsize=(8, 4)
    )

    probe_aperture, probe_aperture_real, probe_aperture_fourier = build_probes(
        convergence_angle.value, 0, 0, 0
    )
    ax_aperture_real = show_complex(
        probe_aperture_real,
        figax=(fig_aperture, ax_aperture_real),
        ticks=False,
        vmin=0,
        vmax=1,
    )
    ax_aperture_fourier = show_complex(
        probe_aperture_fourier,
        figax=(fig_aperture, ax_aperture_fourier),
        ticks=False,
        vmin=0,
        vmax=1,
    )

    ax_aperture_real.set_title("real-space complex probe")
    ax_aperture_fourier.set_title("reciprocal-space complex probe")
    add_scalebar(ax_aperture_real, probe_aperture.sampling[0], r"$\AA$")
    add_scalebar(ax_aperture_fourier, probe_aperture.angular_sampling[0], "mrad")
    None
    return (
        ax_aperture_fourier,
        ax_aperture_real,
        fig_aperture,
        probe_aperture,
        probe_aperture_fourier,
        probe_aperture_real,
    )


@app.cell(hide_code=True)
def __(
    add_scalebar,
    astigmatism,
    astigmatism_angle,
    build_probes,
    convergence_angle,
    defocus,
    plt,
    show_complex,
):
    # aberrations figure
    fig, (ax_fourier, ax_real) = plt.subplots(1, 2, figsize=(8, 4))

    probe, probe_real, probe_fourier = build_probes(
        convergence_angle.value,
        defocus.value,
        astigmatism.value,
        astigmatism_angle.value,
    )
    ax_real = show_complex(
        probe_real,
        figax=(fig, ax_real),
        ticks=False,
        vmin=0,
        vmax=1,
    )

    ax_fourier = show_complex(
        probe_fourier,
        figax=(fig, ax_fourier),
        ticks=False,
        vmin=0,
        vmax=1,
    )

    ax_real.set_title("real-space complex probe")
    ax_fourier.set_title("reciprocal-space complex probe")
    add_scalebar(ax_real, probe.sampling[0], r"$\AA$")
    add_scalebar(ax_fourier, probe.angular_sampling[0], "mrad")
    None
    return ax_fourier, ax_real, fig, probe, probe_fourier, probe_real


@app.cell
def __(np):
    # Complex Probes Utilities
    def energy2wavelength(energy):
        """ """
        hplanck = 6.62607e-34
        c = 299792458.0
        me = 9.1093856e-31
        e = 1.6021766208e-19

        return (
            hplanck
            * c
            / np.sqrt(energy * (2 * me * c**2 / e + energy))
            / e
            * 1.0e10
        )


    class ComplexProbe:
        """ """

        # fmt: off
        _polar_symbols = (
            "C10", "C12", "phi12",
            "C21", "phi21", "C23", "phi23",
            "C30", "C32", "phi32", "C34", "phi34",
            "C41", "phi41", "C43", "phi43", "C45", "phi45",
            "C50", "C52", "phi52", "C54", "phi54", "C56", "phi56",
        )

        _polar_aliases = {
            "defocus": "C10", "astigmatism": "C12", "astigmatism_angle": "phi12",
            "coma": "C21", "coma_angle": "phi21",
            "Cs": "C30",
            "C5": "C50",
        }
        # fmt: on

        def __init__(
            self,
            energy,
            gpts,
            sampling,
            semiangle_cutoff,
            soft_aperture=True,
            parameters={},
            **kwargs,
        ):
            self._energy = energy
            self._gpts = gpts
            self._sampling = sampling
            self._semiangle_cutoff = semiangle_cutoff
            self._soft_aperture = soft_aperture

            self._parameters = dict(
                zip(self._polar_symbols, [0.0] * len(self._polar_symbols))
            )
            parameters.update(kwargs)
            self.set_parameters(parameters)
            self._wavelength = energy2wavelength(self._energy)

        def set_parameters(self, parameters):
            """ """
            for symbol, value in parameters.items():
                if symbol in self._parameters.keys():
                    self._parameters[symbol] = value

                elif symbol == "defocus":
                    self._parameters[self._polar_aliases[symbol]] = -value

                elif symbol in self._polar_aliases.keys():
                    self._parameters[self._polar_aliases[symbol]] = value

                else:
                    raise ValueError(
                        "{} not a recognized parameter".format(symbol)
                    )

            return parameters

        def get_spatial_frequencies(self):
            return tuple(
                np.fft.fftfreq(n, d) for n, d in zip(self._gpts, self._sampling)
            )

        def get_scattering_angles(self):
            kx, ky = self.get_spatial_frequencies()
            kx, ky = kx * self._wavelength, ky * self._wavelength
            alpha = np.sqrt(kx[:, None] ** 2 + ky[None, :] ** 2)
            phi = np.arctan2(ky[None, :], kx[:, None])
            return alpha, phi

        def hard_aperture(self, alpha, semiangle_cutoff):
            return alpha <= semiangle_cutoff

        def soft_aperture(self, alpha, semiangle_cutoff, angular_sampling):
            denominator = (
                np.sqrt(angular_sampling[0] ** 2 + angular_sampling[1] ** 2) * 1e-3
            )
            return np.clip((semiangle_cutoff - alpha) / denominator + 0.5, 0, 1)

        def evaluate_aperture(self, alpha, phi):
            if self._soft_aperture:
                return self.soft_aperture(
                    alpha, self._semiangle_cutoff * 1e-3, self.angular_sampling
                )
            else:
                return self.hard_aperture(alpha, self._semiangle_cutoff * 1e-3)

        def evaluate_chi(self, alpha, phi):
            p = self._parameters

            alpha2 = alpha**2

            array = np.zeros_like(alpha)
            if any([p[symbol] != 0.0 for symbol in ("C10", "C12", "phi12")]):
                array += (
                    1
                    / 2
                    * alpha2
                    * (p["C10"] + p["C12"] * np.cos(2 * (phi - p["phi12"])))
                )

            if any(
                [p[symbol] != 0.0 for symbol in ("C21", "phi21", "C23", "phi23")]
            ):
                array += (
                    1
                    / 3
                    * alpha2
                    * alpha
                    * (
                        p["C21"] * np.cos(phi - p["phi21"])
                        + p["C23"] * np.cos(3 * (phi - p["phi23"]))
                    )
                )

            if any(
                [
                    p[symbol] != 0.0
                    for symbol in ("C30", "C32", "phi32", "C34", "phi34")
                ]
            ):
                array += (
                    1
                    / 4
                    * alpha2**2
                    * (
                        p["C30"]
                        + p["C32"] * np.cos(2 * (phi - p["phi32"]))
                        + p["C34"] * np.cos(4 * (phi - p["phi34"]))
                    )
                )

            if any(
                [
                    p[symbol] != 0.0
                    for symbol in ("C41", "phi41", "C43", "phi43", "C45", "phi41")
                ]
            ):
                array += (
                    1
                    / 5
                    * alpha2**2
                    * alpha
                    * (
                        p["C41"] * np.cos((phi - p["phi41"]))
                        + p["C43"] * np.cos(3 * (phi - p["phi43"]))
                        + p["C45"] * np.cos(5 * (phi - p["phi45"]))
                    )
                )

            if any(
                [
                    p[symbol] != 0.0
                    for symbol in (
                        "C50",
                        "C52",
                        "phi52",
                        "C54",
                        "phi54",
                        "C56",
                        "phi56",
                    )
                ]
            ):
                array += (
                    1
                    / 6
                    * alpha2**3
                    * (
                        p["C50"]
                        + p["C52"] * np.cos(2 * (phi - p["phi52"]))
                        + p["C54"] * np.cos(4 * (phi - p["phi54"]))
                        + p["C56"] * np.cos(6 * (phi - p["phi56"]))
                    )
                )

            array = 2 * np.pi / self._wavelength * array
            return array

        def evaluate_aberrations(self, alpha, phi):
            return np.exp(-1.0j * self.evaluate_chi(alpha, phi))

        def evaluate_ctf(self):
            alpha, phi = self.get_scattering_angles()
            array = self.evaluate_aberrations(alpha, phi)
            array *= self.evaluate_aperture(alpha, phi)
            return array

        def build(self):
            self._array_fourier = self.evaluate_ctf()
            array = np.fft.ifft2(self._array_fourier)
            array /= np.sqrt(np.sum(np.abs(array) ** 2))
            self._array = array
            return self

        @property
        def sampling(self):
            return self._sampling

        @property
        def reciprocal_space_sampling(self):
            return tuple(1 / (n * s) for n, s in zip(self._gpts, self._sampling))

        @property
        def angular_sampling(self):
            return tuple(
                dk * self._wavelength * 1e3
                for dk in self.reciprocal_space_sampling
            )


    def build_probes(semiangle_cutoff, defocus, astigmatism, astigmatism_angle):
        """ """
        probe = ComplexProbe(
            energy=300e3,
            gpts=(128, 128),
            sampling=(0.1, 0.1),
            semiangle_cutoff=semiangle_cutoff,
            defocus=defocus,
            astigmatism=astigmatism,
            astigmatism_angle=np.deg2rad(astigmatism_angle),
        ).build()
        return (
            probe,
            np.fft.fftshift(probe._array),
            np.fft.fftshift(probe._array_fourier),
        )
    return ComplexProbe, build_probes, energy2wavelength


@app.cell
def __(AnchoredSizeBar, cspace_convert, np, plt):
    # Complex Plotting Utilities
    def Complex2RGB(
        complex_data, vmin=None, vmax=None, power=None, chroma_boost=1
    ):
        """ """
        amp = np.abs(complex_data)
        phase = np.angle(complex_data)

        if power is not None:
            amp = amp**power

        if np.isclose(np.max(amp), np.min(amp)):
            if vmin is None:
                vmin = 0
            if vmax is None:
                vmax = np.max(amp)
        else:
            if vmin is None:
                vmin = 0.02
            if vmax is None:
                vmax = 0.98
            vals = np.sort(amp[~np.isnan(amp)])
            ind_vmin = np.round((vals.shape[0] - 1) * vmin).astype("int")
            ind_vmax = np.round((vals.shape[0] - 1) * vmax).astype("int")
            ind_vmin = np.max([0, ind_vmin])
            ind_vmax = np.min([len(vals) - 1, ind_vmax])
            vmin = vals[ind_vmin]
            vmax = vals[ind_vmax]

        amp = np.where(amp < vmin, vmin, amp)
        amp = np.where(amp > vmax, vmax, amp)
        amp = ((amp - vmin) / vmax).clip(1e-16, 1)

        J = amp * 61.5  # Note we restrict luminance to the monotonic chroma cutoff
        C = np.minimum(chroma_boost * 98 * J / 123, 110)
        h = np.rad2deg(phase) + 180

        JCh = np.stack((J, C, h), axis=-1)
        rgb = cspace_convert(JCh, "JCh", "sRGB1").clip(0, 1)

        return rgb


    def add_scalebar(ax, sampling, units):
        """ """
        bar = AnchoredSizeBar(
            ax.transData,
            20,
            f"{np.round(sampling,1)*20:.0f} {units}",
            "lower right",
            pad=0.5,
            color="white",
            frameon=False,
            label_top=True,
            size_vertical=1,
        )
        ax.add_artist(bar)
        return ax


    def show_complex(
        complex_data,
        figax=None,
        vmin=None,
        vmax=None,
        power=None,
        ticks=True,
        chroma_boost=1,
        **kwargs,
    ):
        """ """
        rgb = Complex2RGB(
            complex_data, vmin, vmax, power=power, chroma_boost=chroma_boost
        )

        figsize = kwargs.pop("figsize", (6, 6))
        if figax is None:
            fig, ax = plt.subplots(figsize=figsize)
        else:
            fig, ax = figax

        ax.imshow(rgb, **kwargs)
        if ticks is False:
            ax.set_xticks([])
            ax.set_yticks([])
        return ax
    return Complex2RGB, add_scalebar, show_complex


@app.cell
def __():
    # Imports
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
    from colorspacious import cspace_convert
    return AnchoredSizeBar, cspace_convert, mo, np, plt


if __name__ == "__main__":
    app.run()
