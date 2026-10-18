# VAPT Google Dorker

A Python utility that organizes Google Dork queries for authorized web reconnaissance and helps security testers manage their search workflow.

## Overview

VAPT Google Dorker was created to simplify the process of managing frequently used Google Dork queries during Web Vulnerability Assessment and Penetration Testing (VAPT).

Instead of manually typing each query, users can select predefined searches, open them directly in a browser, execute searches in batches, and track which searches have been opened across sessions.

The tool supports reconnaissance for potentially exposed files, backup files, configuration details, API documentation, administrative pages, and other publicly indexed information that may require further investigation.

## Features

- Includes 75 curated Google Dork queries.
- Opens Google search pages directly in the default browser.
- Supports selecting specific queries.
- Opens queries in batches.
- Displays the complete query list.
- Shows remaining searches.
- Saves session progress using a JSON file.
- Allows users to reset saved progress.
- Provides a simple menu-driven interface.

## Technology

- Python 3
- JSON for session progress tracking
- Web browser integration


## Installation

### Prerequisites

- Python 3 installed on your system.
- Internet access to open Google Search.
- A web browser.

### Steps

1. Clone or download this repository.

2. Open a terminal in the project directory.

3. Run the script:

  python3 gdork.py 

4. Follow the on-screen menu to manage and open searches.

No third-party Python packages are required if the script uses only Python's standard library. Verify this against the actual code.

## Usage

After launching the script, use the available menu options to:

- Open the next set of searches.
- Open selected query numbers.
- View all available queries.
- View remaining searches.
- Reset saved session progress.
- Exit the application.

The progress file records which searches have been opened by the tool. It does not confirm that each search was reviewed or that any exposed information was discovered.

## Google Dork Query Collection

The following queries are grouped by reconnaissance purpose. Replace `example.com` with an authorized target domain where applicable. Queries that do not include a domain may return results from across the public web.

**Note:** These are search patterns, not confirmed vulnerabilities. Google indexing and query behavior can change, and results must be reviewed manually.

### 1. Files and Documents

1. `site:example.com filetype:pdf`
2. `site:example.com filetype:doc`
3. `site:example.com filetype:docx`
4. `site:example.com filetype:xls`
5. `site:example.com filetype:xlsx`
6. `site:example.com filetype:csv`
7. `site:example.com filetype:txt`
8. `site:example.com filetype:xml`
9. `site:example.com filetype:json`
10. `site:example.com filetype:sql`
11. `site:example.com filetype:log`
12. `site:example.com filetype:conf`
13. `site:example.com filetype:config`
14. `site:example.com filetype:ini`
15. `site:example.com filetype:env`
16. `site:example.com filetype:bak`
17. `site:example.com filetype:old`
18. `site:example.com filetype:zip`
19. `site:example.com filetype:tar`
20. `site:example.com filetype:gz`

### 2. Directory Listing

21. `site:example.com intitle:"index of"`
22. `site:example.com intitle:"index of" "parent directory"`
23. `site:example.com intitle:"index of" backup`
24. `site:example.com intitle:"index of" upload`
25. `site:example.com intitle:"index of" files`

### 3. Admin, Login and Application Paths

26. `site:example.com inurl:admin`
27. `site:example.com inurl:login`
28. `site:example.com inurl:signin`
29. `site:example.com inurl:dashboard`
30. `site:example.com inurl:backup`
31. `site:example.com inurl:upload`
32. `site:example.com inurl:download`
33. `site:example.com inurl:portal`
34. `site:example.com inurl:account`
35. `site:example.com inurl:manage`

### 4. API Documentation

36. `site:example.com inurl:api`
37. `site:example.com inurl:swagger`
38. `site:example.com inurl:api-docs`
39. `site:example.com inurl:graphql`
40. `site:example.com inurl:documentation`

### 5. Potentially Sensitive Information

41. `site:example.com "confidential"`
42. `site:example.com "internal use only"`
43. `site:example.com "password"`
44. `site:example.com "username"`
45. `site:example.com "api key"`
46. `site:example.com "database"`
47. `site:example.com "backup"`
48. `site:example.com "configuration"`
49. `site:example.com "stack trace"`
50. `site:example.com "error"`

### 6. Application and Script Files

51. `site:example.com filetype:map`
52. `site:example.com filetype:js`
53. `site:example.com filetype:php`
54. `site:example.com filetype:asp`
55. `site:example.com filetype:aspx`

### 7. Repository and Deployment Files

56. `site:example.com inurl:.git`
57. `site:example.com inurl:.svn`
58. `site:example.com "package.json"`
59. `site:example.com "docker-compose.yml"`
60. `site:example.com "Jenkinsfile"`

### 8. Debugging and Error Information

61. `site:example.com "debug=true"`
62. `site:example.com "debug mode"`
63. `site:example.com "exception"`
64. `site:example.com "traceback"`
65. `site:example.com "PHP Version"`

### 9. Temporary and Backup Files

66. `site:example.com filetype:tmp`
67. `site:example.com filetype:temp`
68. `site:example.com filetype:orig`
69. `site:example.com filetype:swp`
70. `site:example.com filetype:save`

### 10. Public Metadata and Discovery Files

71. `site:example.com inurl:security.txt`
72. `site:example.com inurl:robots.txt`
73. `site:example.com inurl:sitemap.xml`
74. `site:example.com inurl:internal`
75. `site:example.com inurl:staging`

## Limitations

- The tool opens Google Search pages; it does not automatically scrape Google results.
- It does not perform active vulnerability scanning.
- It does not automatically verify exposed information or confirm vulnerabilities.
- Search results depend on Google's index and may include irrelevant or outdated information.
- The saved progress tracks searches opened, not searches completed or findings validated.
- A manual review is required to determine whether a result represents a genuine security risk.

## Responsible Use

Use this tool only for authorized security assessments, approved reconnaissance, and legitimate research.

Do not access, download, disclose, or misuse confidential information belonging to others. Follow applicable laws, organizational policies, and the target organization's authorization and scope requirements.

## Future Improvements

- Export selected queries and session summaries.
- Add customizable query collections.
- Improve result-tracking and review notes.
- Add report-friendly summaries of manually reviewed findings.

## Author

Created as a personal utility to organize Google Dork searches during Web VAPT practice and reconnaissance.

## Disclaimer

This project is intended for educational purposes and authorized security testing. The author does not guarantee that the queries will identify vulnerabilities or expose sensitive information.
