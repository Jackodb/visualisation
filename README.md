# DEXBot visualisation (test phase)

[DEXBot](https://github.com/Codaone/DEXBot)

This visualisation represents a worker's initial order size and current order size. One glance at the chart tells the user how his worker is doing in terms of profits being redistributed to orders or initial orders being decreased due to losses.

This visualisation uses [pywebview](https://github.com/r0x0r/pywebview) which is a lightweight cross-platform wrapper around a webview component that allows to display HTML content in its own native GUI window. This wrapper allows data to be parsed from DEXBot (Python) to this visualisation app (JavaScript and HTML) without the use of a server. Besides _pywebview_, this application uses [chart.js](https://github.com/chartjs) for the charting part.

The application is currently in its testing phase and will be implemented in DEXBot in the near future.

![Image of Visualisation](Visualisation.png)
