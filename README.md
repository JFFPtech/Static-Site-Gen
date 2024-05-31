# Static Site Generator

## Overview
This project is a demonstration of a static site generator. The primary output of a static site generator is HTML (HyperText Markup Language), which is all you need to render a web page in a browser.

HTML is a simple markup language that's excellent for structuring content. It's not a programming language but rather a way to format text, images, links, and media so that a web browser can render it as a GUI.

## HTML Structure
HTML is a tree-like structure where each tag can contain other tags. Here's the structure breakdown of the provided HTML file:
- `<html>`: Root element of the document.
- `<head>`: Contains metadata about the document.
  - `<title>`: Title of the document, displayed in the browser tab.
- `<body>`: Contains the content of the document, rendered in the browser window.
  - `<h1>`: Top-level heading.
  - `<p>`: Paragraph of text.
  - `<a>`: Hyperlink with the URL specified in the `href` attribute.

## Setup
1. Create a new directory in your project called `public` and save the above HTML into a file called `index.html` in the `public` directory.
2. Copy/paste the provided Python webserver into a file called `server.py` in the root of your project.
3. Start the server by running:
    ```bash
    python server.py --dir public
    ```
4. Open your browser and paste the URL of your server (likely http://localhost:8888) into the address bar. You should see your file rendered as a web page.
