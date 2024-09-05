# xDSL: Python-native Compiler Toolkit

*August 29, 2024*

[xDSL](https://xdsl.dev/) is a Python-native compiler toolkit that aims to lower the barrier to entry for developing Domain-Specific Languages (DSLs). Closely connected to the MLIR/LLVM projects, xDSL's ambitious goal is to help enable exascale computing — computers performing at over a quintillion floating-point operations per second (FLOPS)!

## Interactive Documentation with marimo

xDSL uses marimo to bring their documentation to life with interactive code examples. Thanks to marimo's [WebAssembly (WASM) capabilities](https://docs.marimo.io/guides/wasm.html#creating-and-sharing-wasm-notebooks) and [Pyodide integration](https://marimo.io/blog/newsletter-2), xDSL can easily embed playground notebooks into their documentation using iframes. This approach, similar to what marimo uses in its own [documentation](https://docs.marimo.io/), provides an engaging and hands-on learning experience for users.

You can explore xDSL's interactive documentation here: [https://xdsl.dev/index](https://xdsl.dev/index)

[![Open with marimo](https://marimo.io/shield.svg)](https://marimo.io/@haleshot/notebook-3juvpw)

## Local Exploration

To explore the xDSL examples locally, you can use the following commands:

```shell
uvx marimo run --sandbox xdsl.py
```

if you have `uv` installed, or

```shell
marimo run xdsl.py
```

if you don't have uv installed (you'll need to manually install its dependencies).

To edit the notebook source code, replace `run` with `edit` in the above commands.

## Why xDSL Matters

xDSL's focus on making DSL development more accessible has significant implications for the field of high-performance computing. By bridging the gap between Python's ease of use and the performance needs of exascale computing, xDSL is paving the way for more efficient and powerful computational tools.

The project's integration with marimo for interactive documentation demonstrates the power of combining cutting-edge compiler technology with modern, interactive programming environments. This combination not only makes learning about xDSL more engaging but also showcases the potential of these tools working together in the broader ecosystem of scientific computing and high-performance applications.

We're excited to see how the xDSL project continues to evolve and contribute to the advancement of exascale computing capabilities!

## Community Spotlight

This project is part of our [Community Spotlights](https://marimo.io/c/@haleshot/community-spotlights) collection, where we feature outstanding projects and contributions from the marimo community.

We're thrilled to have xdsl as an active and innovative member of the marimo community!

> [!NOTE]
> The current link to the Community Spotlights collection is temporary and will soon be moved to the official marimo-team workspace for improved visibility and structure.*

## Spotlight Promotion

This spotlight has been featured on our social media platforms. Join the conversation:

- Twitter Post: [Link](https://x.com/marimo_io/status/1829209846174105826)
- Discord Discussion: [Discord message](https://discord.com/channels/1059888774789730424/1268639867898695761/1278770178259292251)

We encourage you to engage with these posts, share your thoughts, and help us celebrate this amazing contribution to the Marimo community!
