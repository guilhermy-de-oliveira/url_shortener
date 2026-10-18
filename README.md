# URL Shortener

A simple command-line URL shortener built with Python and the `pyshorteners` library. This project was created as a learning exercise while following a tutorial.

## Acknowledgments

Special thanks to **Leandro Hirt** for creating the tutorial that inspired this project and guided its initial implementation.

- **Tutorial:** [URL Shortener Tutorial on YouTube](https://www.youtube.com/watch?v=5uflDBAEDFs)
- **Creator:** Leandro Hirt

This project was developed for personal learning and experimentation. Any further modifications, improvements, or features added beyond the original tutorial will be documented as part of my own development process.

## Requirements

- Python 3.15.0
- `pyshorteners`

## Installation

```bash
pip install pyshorteners
```

## Usage

Run the Python script and enter the URL you want to shorten when prompted.

**Before submitting a URL**, please review the list of known supported and blocked formats below:

### Supported URLs

*   **Standard Secure Web Protocols:** Links must begin with `https://` or `http://`.
*   **Links with Parameters and Query Strings:** Long URLs containing trackers, UTM parameters, or anchors (e.g., `?utm_source=fb&id=123#top`).
*   **Direct Links to Files and Media:** Paths ending in file extensions (e.g., `.pdf`, `.png`, `.mp4`, `.zip`).
*   **Subdomains and Modern Domain Extensions (TLDs):** Support for various subdomains and newer domain extensions (e.g., `.tech`, `.photography`, `.gov.br`).
*   **Public Web Ports:** URLs that specify access ports (e.g., `https://example.com`).

### Unsupported URLs

*   **Links Missing a Protocol:** Submitting only the domain (e.g., `google.com`) without the `http://` or `https://` prefix.
*   **Non-Web Protocols:** Links for other services, such as `ftp://`, `ssh://`, `mailto:`, `magnet:?`, or `file://`.
*   **Local or Private Addresses:** URLs pointing to internal or development networks (e.g., `localhost`, `127.0.0.1`, `192.168.0.1`).
*   **Blacklisted Links (Security):** URLs identified by the global TinyURL API as suspicious—including those associated with phishing, spam, or the distribution of malware.

## Purpose

This project is part of my ongoing journey to learn Python, practice programming concepts, and build small applications for personal use.