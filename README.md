# VAPT Google Dorker

## Overview
VAPT Google Dorker is a Python-based utility designed to organize Google Dork searches for authorized web reconnaissance.

## Features
- Includes 75 curated Google Dork queries.
- Opens selected Google searches directly in a web browser.
- Supports opening searches in batches.
- Tracks opened searches between sessions.
- Allows users to view and manage search progress.

## Use Cases
The tool helps security testers organize searches for potentially exposed files, backup files, configuration details, API documentation, and other publicly indexed information that may require further investigation.

## Technology
- Python
- JSON for session progress tracking
- Web browser integration

## How to Use
1. Install Python 3 if it is not already installed.
2. Download or clone this repository.
3. Run the script using:

   `python3 google_dorker.py`

4. Follow the menu to select and open searches.

## Limitations
This tool opens Google search pages. It does not automatically scrape search results, verify vulnerabilities, or perform active vulnerability scanning. Results require manual review.

## Responsible Use
Use this tool only for authorized security testing and legitimate reconnaissance activities.
