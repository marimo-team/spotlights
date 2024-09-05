# xDSL: Python-native Compiler Toolkit

*August 29, 2024*

[xDSL](https://xdsl.dev/) is a Python-native compiler toolkit that aims to lower the barrier to entry for developing Domain-Specific Languages (DSLs). Closely connected to the MLIR/LLVM projects, xDSL's ambitious goal is to help enable exascale computing — computers performing at over a quintillion floating-point operations per second (FLOPS)!

## Interactive Documentation with marimo

xDSL uses marimo to bring their documentation to life with interactive code examples. Thanks to marimo's [WebAssembly (WASM) capabilities](https://docs.marimo.io/guides/wasm.html#creating-and-sharing-wasm-notebooks) and [Pyodide integration](https://marimo.io/blog/newsletter-2), xDSL can easily embed playground notebooks into their documentation using iframes. This approach, similar to what marimo uses in its own [documentation](https://docs.marimo.io/), provides an engaging and hands-on learning experience for users.

You can explore xDSL's interactive documentation here: [https://xdsl.dev/index](https://xdsl.dev/index)

## Local Exploration

To explore the xDSL examples locally, you can use the following commands:

```shell
uvx marimo edit --sandbox xdsl.py
```

if you have `uv` installed, or

```shell
marimo edit xdsl.py
```

if you don't have uv installed (you'll need to manually install its dependencies).

## Why xDSL Matters

xDSL's focus on making DSL development more accessible has significant implications for the field of high-performance computing. By bridging the gap between Python's ease of use and the performance needs of exascale computing, xDSL is paving the way for more efficient and powerful computational tools.

The project's integration with marimo for interactive documentation demonstrates the power of combining cutting-edge compiler technology with modern, interactive programming environments. This combination not only makes learning about xDSL more engaging but also showcases the potential of these tools working together in the broader ecosystem of scientific computing and high-performance applications.

We're excited to see how the xDSL project continues to evolve and contribute to the advancement of exascale computing capabilities!
