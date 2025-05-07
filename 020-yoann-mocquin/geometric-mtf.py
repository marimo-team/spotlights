import marimo

__generated_with = "0.13.5-dev6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Introduction

    This marimo notebook presents an interactive visualisation of `geometric mtf`. It is based on [Smith, Warren J. 2008. Modern Optical Engineering: The Design of Optical Systems. 4th ed. New York: McGraw-Hill.](Smith, Warren J. 2008. Modern Optical Engineering: The Design of Optical Systems. 4th ed. New York: McGraw-Hill. https://www.accessengineeringlibrary.com/content/book/9780071476874).

    The `Modulation Transfer Function` (or `MTF`) is a measure of optical quality of an imaging optical system. Many methods exists to compute the `MTF` of an optical system, and the `geomtric mtf` uses a purely geometric approach based on ray tracing (as opposite to Fourier-Transform based approaches for example). Note that the python implemntation is based on [physipy](https://physipy.readthedocs.io/en/latest/) which allows us to use units (like millimeter) and make the code way more explicit and prevents dimension analysis errors.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Mathematical derivation of geometrical MTF""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    The distribution of brightness can be expressed mathematically as 
    $$G(x) = b_0 + b_1\cos{(2\pi\nu x)}$$
    where v is the frequency of the brightness variation in cycles per unit
    length, (b0  b1 ) is the maximum brightness, (b0  b1) is the minimum
    brightness, and x is the spatial coordinate perpendicular to the bands.

    Hence the modulation of the object is simply:
    $$M_o = \frac{b_1}{b_0}$$

    The image energy distribution at a position x is the summation of the product of G(x) and A() and can be expressed as:
    $$F(x)= \int A(\delta)G(x-\delta)d\delta$$

    where A() is the line spread function.

    Hence : 
    $$F(x) = \int A(\delta)  \left(b_0 + b_1\cos{(2\pi\nu (x-\delta))}\right)d\delta=
    \int A(\delta)  b_0 d\delta + \int A(\delta) b_1\cos{(2\pi\nu (x-\delta))}d\delta$$
    $$=b_0 \int A(\delta)d\delta +b_1 \int A(\delta)cos{(2\pi \nu (x-\delta))}d\delta$$
    $$=b_0 \int A(\delta)d\delta +b_1 \int A(\delta)\left(\cos{(2\pi \nu x)\cos{(2\pi \nu \delta)}}+ \sin{(2\pi \nu x)\sin{(2\pi \nu \delta)}}\right)d\delta$$
    $$=b_0 \int A(\delta)d\delta +b_1 \cos{(2\pi \nu x) \int A(\delta)\cos{(2\pi \nu \delta)}}d\delta+ b_1\sin{(2\pi \nu x) \int A(\delta)\sin{(2\pi \nu \delta)}}d\delta$$


    We then define : 
    $$A_c(\nu) = \frac{\int A(\delta)\cos{(2\pi \nu \delta)}}{\int A(\delta)d\delta}$$
    $$A_s(\nu) = \frac{\int A(\delta)\sin{(2\pi \nu \delta)}}{\int A(\delta)d\delta}$$

    We then normalize $F$ by $\int A(\delta)d\delta$:

    $$\frac{F(x)}{\int A(\delta)d\delta} = b_0 + b_1 A_c(\nu) \cos{(2\pi \nu x)} +  b_1 A_s(\nu) \sin{(2\pi \nu x)} $$

    Or using $A\cos{x}+B\cos{x}=\sqrt{A^2+B^2}\cos{(x-\phi)}$ with:

    $$|A(\nu)|=\sqrt{A_s^2(\nu)+A_c^2(\nu)}$$

    $$\phi=\arctan{\frac{A_s(\nu)}{A_c(\nu)}}$$

    $$\frac{F(x)}{\int A(\delta)d\delta} = b_0 + b_1 |A(\nu)| \cos{(2\pi \nu x - \phi)}$$

    The image modulation is then:

    $$M_i = \frac{b_1}{b_0}|A(\nu)| = M_o |A(\nu)|$$

    Hence the final modulation transfer function is:

    $$MTF(\nu) = \frac{M_i}{M_o} = |A(\nu)|$$

    About square-waves : the response to square-wave input is also often of interest, and the square-amplitude response MTF can be computed from the MTF:

    $$S(\nu) = \frac{4}{\pi} \left[ M(\nu) - \frac{M(3\nu)}{3} + \frac{M(5\nu)}{5} - \frac{M(7\nu)}{7}  + ... \right]$$
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""In the following cells, we demonstrate the behavior of this model using sliders as inputs.""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Sliders definition""")
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    import warnings

    warnings.filterwarnings("ignore")
    plt.style.use("dark_background")


    from physipy import m, units, setup_matplotlib, set_favunit

    setup_matplotlib()
    mm = units["mm"]
    mum = units["mum"]
    cy = 1  # One cycle
    cymm = cy / mm  # one cycle per millimeter
    cymm.symbol = "cy/mm"


    nu_slider = mo.ui.slider(
        0.0, 5.0, step=0.01, value=1, label=r"$\nu$", show_value=True
    )
    b0_slider = mo.ui.slider(
        0.0, 5.0, step=0.01, value=0, label="$b_0$", show_value=True
    )
    b1_slider = mo.ui.slider(
        0.0, 5.0, step=0.01, value=1, label="$b_1$", show_value=True
    )
    nb_samples_lsf_slider = mo.ui.slider(
        1, 50, value=10, label=r"$\text{\# samples}$", show_value=True
    )
    phi_slider = mo.ui.slider(
        0.0, 2 * np.pi, step=0.01, value=1, label="$\phi$", show_value=True
    )
    xs_range_slider = mo.ui.slider(
        0.0, 5, step=0.1, value=1, label="$x_{lim}$", show_value=True
    )
    sigma_slider = mo.ui.slider(
        0.0, 1, step=0.01, value=0.05, label=r"$\sigma_x$", show_value=True
    )

    phi_pup_slider = mo.ui.slider(
        0.0, 20, step=0.01, value=5, label=r"$\phi_{pup}$", show_value=True
    )
    foc_slider = mo.ui.slider(
        0.0, 20, step=0.01, value=5, label=r"$foc$", show_value=True
    )
    lmbda_slider = mo.ui.slider(
        0.1, 20, step=0.01, value=10, label=r"$\lambda$", show_value=True
    )

    sliders_col1 = mo.vstack(
        [
            mo.md(r"$\text{Input signal}=b_0 + b_1\cos{(2\pi\nu x+\phi)}$"),
            b0_slider,
            b1_slider,
            nu_slider,
            phi_slider,
        ]
    )
    sliders_col2 = mo.vstack(
        [
            mo.md(r"$\text{LSF}(x)\propto e^{-x^2/\sigma_x}$"),
            sigma_slider,
        ]
    )

    sliders_col3 = mo.vstack(
        [
            mo.md(r"$\text{Sampling of LSF}$"),
            nb_samples_lsf_slider,
        ]
    )
    sliders_col4 = mo.vstack(
        [
            mo.md(r"$\text{Display}$"),
            xs_range_slider,
            mo.md(r"$\text{Optics}$"),
            phi_pup_slider,
            foc_slider,
            lmbda_slider,
        ]
    )

    sliders = mo.hstack(
        [sliders_col1, sliders_col2, sliders_col3, sliders_col4]
    ).center()


    def display_vars_latex(d):
        return mo.vstack(
            [mo.md(rf"$${key} = {value:.2f}$$") for key, value in d.items()]
        ).center()


    # nu, b0, b1, sigma, xs_range_slider, phi_slider
    return (
        b0_slider,
        b1_slider,
        cy,
        cymm,
        display_vars_latex,
        foc_slider,
        lmbda_slider,
        m,
        mm,
        mo,
        mum,
        nb_samples_lsf_slider,
        np,
        nu_slider,
        phi_pup_slider,
        phi_slider,
        plt,
        set_favunit,
        sigma_slider,
        sliders,
        xs_range_slider,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Numerical computations""")
    return


@app.cell(hide_code=True)
def _(
    b0_slider,
    b1_slider,
    cy,
    cymm,
    foc_slider,
    lmbda_slider,
    m,
    mm,
    mum,
    nb_samples_lsf_slider,
    np,
    nu_slider,
    phi_pup_slider,
    phi_slider,
    set_favunit,
    sigma_slider,
    xs_range_slider,
):
    class OpticMTF:
        @staticmethod
        @set_favunit(cy / mm)
        def fco(phi_pup, foc, lmbda):
            """Optical cut-off frequency"""
            fco = phi_pup / (foc * lmbda)
            # fco.favunit = cy/mm
            return fco

        @classmethod
        def diffraction(cls, f_cymm, phi_pup, foc, lmbda):
            """Diffraction MTF"""
            fco = cls.fco(phi_pup, foc, lmbda)
            FTM = (
                2
                / np.pi
                * (
                    np.arccos(f_cymm / fco)
                    - (f_cymm / fco) * (1 - (f_cymm / fco) ** 2) ** 0.5
                )
            )
            return np.where(f_cymm < fco, FTM, 0)


    class DetectorMTF:
        @staticmethod
        def det_sinc(f_cymm, zs):
            """Sensor MTF"""
            fc_det = 1 / zs
            sinc = abs(np.sinc(f_cymm * zs))
            return np.where(f_cymm < fc_det, sinc, 0)


    def G(x, nu, b0, b1, phi):
        """Sinusoidal input"""
        return b0 + b1 * np.cos(2 * np.pi * nu * x + phi)


    def lsf_(delta, sigma_x=0.05 * mm, mu=0 * m):
        """Line Spread Function, assumed to be gaussian"""
        return (1 / (sigma_x * np.sqrt(2 * np.pi))) * np.exp(
            -0.5 * ((delta - mu) / sigma_x) ** 2
        )


    def S_func(M_func, order=1000):
        """Square-wave response function computed from the MTF function."""
        harmonics = np.arange(1, order, 2)[..., np.newaxis]
        signs = (-1) ** (harmonics // 2)

        def S(nu):
            return (
                4
                / np.pi
                * (M_func(nu * harmonics) * signs / harmonics).sum(axis=0)
            )

        return S


    phi_pup = (phi_pup_slider.value * mm).set_favunit(mm)
    foc = (foc_slider.value * mm).set_favunit(mm)
    lmbda = (lmbda_slider.value * mum).set_favunit(mum)

    xs_range = xs_range_slider.value
    xs = (np.linspace(-xs_range, xs_range, 200) * mm).set_favunit(mm)
    sampled_G = G(
        xs,
        nu_slider.value * cy / mm,
        b0_slider.value,
        b1_slider.value,
        phi_slider.value,
    )
    lsf = lambda xs: lsf_(xs, sigma_x=sigma_slider.value * mm)
    xs_lsf = (
        np.linspace(
            -3 * sigma_slider.value,
            3 * sigma_slider.value,
            nb_samples_lsf_slider.value,
        )
        * mm
    )
    pitch = (np.diff(xs_lsf)[0]).set_favunit(mum)
    sampled_lsf_ = lsf(xs_lsf)
    sampled_lsf = sampled_lsf_ / np.trapezoid(sampled_lsf_, xs_lsf)

    sampled_lsf_cos_ = (
        sampled_lsf
        * np.cos(2 * np.pi * nu_slider.value * cy / mm * xs_lsf + phi_slider.value)
        / np.trapezoid(sampled_lsf_, xs_lsf)
    )
    sampled_lsf_sin_ = (
        sampled_lsf
        * np.sin(2 * np.pi * nu_slider.value * cy / mm * xs_lsf + phi_slider.value)
        / np.trapezoid(sampled_lsf_, xs_lsf)
    )

    Ac = np.trapezoid(sampled_lsf_cos_, xs_lsf)
    As = np.trapezoid(sampled_lsf_sin_, xs_lsf)
    A = (Ac**2 + As**2) ** 0.5


    def A_from_nu(nu):
        nu = nu[..., np.newaxis]
        sampled_G = G(xs, nu, b0_slider.value, b1_slider.value, phi_slider.value)
        lsf = lambda xs: lsf_(xs, sigma_x=sigma_slider.value * mm)
        sampled_lsf_ = lsf(xs_lsf)
        sampled_lsf = sampled_lsf_ / np.trapezoid(sampled_lsf_, xs_lsf)

        sampled_lsf_cos_ = (
            sampled_lsf
            * np.cos(2 * np.pi * nu * xs_lsf + phi_slider.value)
            / np.trapezoid(sampled_lsf_, xs_lsf)
        )
        sampled_lsf_sin_ = (
            sampled_lsf
            * np.sin(2 * np.pi * nu * xs_lsf + phi_slider.value)
            / np.trapezoid(sampled_lsf_, xs_lsf)
        )

        Ac = np.trapezoid(sampled_lsf_cos_, xs_lsf)
        As = np.trapezoid(sampled_lsf_sin_, xs_lsf)
        A = (Ac**2 + As**2) ** 0.5
        return A


    nus = (np.linspace(0, 10, 100) * cy / mm).set_favunit(cymm)
    As_ = A_from_nu(nus)

    # Compute the square-wave response function
    M_diff = lambda nu: OpticMTF.diffraction(nu, phi_pup, foc, lmbda)
    S_diff = S_func(M_diff)

    # Compute optical and detector MTFs
    mtf_diff = OpticMTF.diffraction(nus, phi_pup, foc, lmbda)
    mtf_sinc = DetectorMTF.det_sinc(
        nus,
        zs=pitch,
    )
    return (
        Ac,
        As,
        As_,
        S_diff,
        lsf,
        mtf_diff,
        mtf_sinc,
        nus,
        pitch,
        sampled_G,
        sampled_lsf,
        sampled_lsf_cos_,
        sampled_lsf_sin_,
        xs,
        xs_lsf,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Plotting""")
    return


@app.cell(hide_code=True)
def _(
    Ac,
    As,
    As_,
    S_diff,
    lsf,
    mtf_diff,
    mtf_sinc,
    np,
    nu_slider,
    nus,
    plt,
    sampled_G,
    sampled_lsf,
    sampled_lsf_cos_,
    sampled_lsf_sin_,
    xs,
    xs_lsf,
):
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))


    fig = plt.figure(constrained_layout=True, figsize=(10, 6))
    # Use GridSpec to arrange: 2 columns in first row, 1 column spanning both in second row
    gs = fig.add_gridspec(2, 2)
    axes = [
        fig.add_subplot(gs[0, :]),
        fig.add_subplot(gs[1, 0]),
        fig.add_subplot(gs[1, 1]),
    ]

    ax = axes[0]
    ax.plot(xs, sampled_G, label="Object")
    ax2 = ax.twinx()
    ax2.plot(xs, lsf(xs), label="lsf", color="red")
    ax2.scatter(xs_lsf, sampled_lsf, label="Sampled lsf", color="red")
    ax2.plot(
        xs_lsf, sampled_lsf_cos_, "-*", label="Sampled lsf*cos", color="green"
    )
    ax2.plot(
        xs_lsf, sampled_lsf_sin_, "-*", label="Sampled lsf*sin", color="purple"
    )

    ax.legend()
    ax2.legend()
    ax2.grid(False)

    axes[1].plot((0, Ac), (0, As))
    axes[1].grid()
    axes[1].set_aspect("equal")
    circle = plt.Circle((0, 0), 1, fill=False)
    axes[1].set_xlabel("Ac")
    axes[1].set_ylabel("As")
    axes[1].add_patch(circle)
    lim = max(*np.abs(axes[1].get_xlim()), *np.abs(axes[1].get_ylim()))
    axes[1].set_xlim(-lim, lim)
    axes[1].set_ylim(-lim, lim)

    axes[2].plot(nus, As_, label="Geometric MTF")
    axes[2].plot(
        nus,
        As_ * mtf_diff,
        label="Geometric MTF with diffraction",
    )
    axes[2].plot(nus, mtf_diff, label="Diffraction")
    axes[2].plot(nus, mtf_sinc, label="Sinc")
    axes[2].plot(nus, S_diff(nus), label="Square-diff")
    axes[2].axvline(nu_slider.value, linewidth=1, color="red")
    axes[2].set_ylabel(r"$MTF=|A|$")
    axes[2].set_ylim(0, 1.1)
    axes[2].legend()

    fig.tight_layout()
    return (fig,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Geometric MTF UI""")
    return


@app.cell(hide_code=True)
def _(display_vars_latex, fig, mo, pitch, sliders):
    mo.vstack(
        [
            mo.vstack(
                [
                    sliders,
                    display_vars_latex({r"\text{Equivalent pitch}": pitch}),
                ]
            ),
            fig,
        ]
    )
    return


if __name__ == "__main__":
    app.run()
