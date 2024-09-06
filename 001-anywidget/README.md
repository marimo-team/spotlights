# Anywidget

_Aug 1, 2024_

This week, we're putting the spotlight on **anywidget**:  developed by Trevor
Manz, PhD candidate at Harvard, [anywidget](https://github.com/manzt/anywidget)
is a Python library that simplifies creating custom widgets that can be used in
interactive programming environments. We strongly believe in anywidget's
mission to provides a single interface for developing embeddable widgets inside
other applications, such as Panel, Jupyter, and, of course, marimo.

[![Open with marimo](https://marimo.io/shield.svg)](https://marimo.io/p/@anywidget/demo)
 
You can also edit this notebook locally with

```shell
uvx marimo run --sandbox reactive_quak.py
```

or

```shell
uvx marimo run --sandbox tldraw_colorpicker.py
```

if you have `uv` installed, or

```shell
marimo run reactive_quak.py
```

or

```shell
marimo run tldraw_colorpicker.py
```

if you don't have uv installed (you'll need to manually install its dependencies).

To edit the notebook source code, replace `run` with `edit` in the above commands.
The anywidget community has built some really cool widgets, including
[quak](https://github.com/manzt/quak), an interactive data table implemented
that scales to millions of rows and code generates SQL based on UI
interactions, and [draw data](https://github.com/koaning/drawdata), which lets
you draw datasets with your mouse and get them back as dataframes!

We're also excited to announce that we've standardized on anywidget for our
plugin API:
- You can now use any anywidget in marimo with just one line of code — just
  wrap it in `mo.ui.anywidget` — and it automatically becomes reactive. For
example, check out Trevor’s demo [at this
link](https://x.com/trevmanz/status/1818664678609858802) to see how marimo
brings quak, an interactive data table implemented with anywidget, to life,
with selections automatically updating a downstream plot.
- You can now develop custom widgets for marimo; learn more at our docs and
  anywidget’s
 
We’re passionate about developer experience, and it’s clear to us that Trevor.
is too — anywidget comes with excellent devX for creating widgets with either
vanilla JavaScript or frameworks like React and Svelte.
 
We’re excited to see the innovations that you’ll bring to marimo with
anywidget. Happy building!

## Community Spotlight

This project is part of our [Community Spotlights](https://marimo.io/c/@spotlights/community-spotlights) collection, where we feature outstanding projects and contributions from the marimo community.

We're thrilled to have Trevor Manz as an active and innovative member of the marimo community!

## Spotlight Promotion

This spotlight has been featured on our social media platforms. Join the conversation:

- LinkedIn Post: [Link](https://www.linkedin.com/posts/marimo-io_anywidget-vega-react-activity-7228825246768791552-MBwW?utm_source=share&utm_medium=member_desktop)
- Twitter Post: [Link](https://x.com/marimo_io/status/1819094841508483242)
- Discord Discussion: [Discord message](https://discord.com/channels/1059888774789730424/1268639867898695761/1268642076078248177)

We encourage you to engage with these posts, share your thoughts, and help us celebrate this amazing contribution to the Marimo community!
