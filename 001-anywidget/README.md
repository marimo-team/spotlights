# Anywidget

_Aug 1, 2024_

This week, we're putting the spotlight on **anywidget**:  developed by Trevor
Manz, PhD candidate at Harvard, [anywidget](https://github.com/manzt/anywidget)
is a Python library that simplifies creating custom widgets that can be used in
interactive programming environments. We strongly believe in anywidget's
mission to provides a single interface for developing embeddable widgets inside
other applications, such as Panel, Jupyter, and, of course, marimo.
 
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
