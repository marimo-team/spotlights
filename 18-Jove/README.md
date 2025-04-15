# Jove: Query Kafka with SQL (Timeplus & marimo)

_April 10, 2025_

[Jove](https://x.com/jove) recently [contributed support](https://github.com/marimo-team/marimo/pull/4376) for [Timeplus](https://timeplus.com/), a new real-time data engine, to marimo, making it accessible from marimo's SQL cells. This integration enables users to easily query Kafka with SQL directly from marimo notebooks.

The integration [showcases](https://www.linkedin.com/pulse/tutorial-query-kafka-sql-timeplusmarimo-jove-zhong-emmwc) how marimo's reactive notebook environment pairs perfectly with Timeplus's real-time data processing capabilities.

## Key Highlights

- Query Kafka streams with SQL directly in marimo notebooks
- No JVM, no Docker, minimal CPU/memory/disk usage
- Reactive updates and visualization of real-time data
- SQL-native approach that simplifies complex data operations

## Why It Matters

As Jove explains in his blog:

> "Honestly, I built a similar app with Streamlit 2 years ago—it worked, but every piece had to be hard-coded in Python, then debug with a browser. With marimo + Timeplus, you can use the notebook interface to write the minimal Python code, also use SQL to handle large amount of data, without worrying about memory or complex JOIN issue (yes, I mean pandas or polars users)."

## Local Exploration

You can explore the notebook locally with:

```shell
git clone https://github.com/timeplus-io/proton.git
cd proton/examples/marimo
uvx marimo edit --sandbox github.py
```

> [!NOTE]
> This project is part of our [Community Spotlights](https://marimo.io/c/@spotlights/community-spotlights) collection, where we feature outstanding projects and contributions from the marimo community.

## Spotlight Promotion

This spotlight has been featured on our social media platforms. Join the conversation:

- Twitter Post: [Link](https://x.com/marimo_io/status/1910442291539697708)
- LinkedIn Post: [Link](https://www.linkedin.com/posts/marimo-io_kafka-sql-activity-7316208137596780544-YuJi?utm_source=share&utm_medium=member_desktop&rcm=ACoAADSJzvgBkjBd85IWDyUWA6ttzq8B-NDq-Hs)
- Blog Post: [Tutorial: Query Kafka with SQL (Timeplus & marimo)](https://www.linkedin.com/pulse/tutorial-query-kafka-sql-timeplusmarimo-jove-zhong-emmwc)

We encourage you to engage with these resources, share your thoughts, and help us celebrate this amazing contribution to the marimo community!
