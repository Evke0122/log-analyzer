# Security Log Analyzer

A Python-based security log analyzer that detects failed login attempts, identifies suspicious IP addresses, assigns severity levels, and generates JSON security reports.

## Features

- Parse authentication log files
- Detect failed login attempts
- Track failed attempts by IP address
- Detect potential brute-force activity
- Assign LOW, MEDIUM, and HIGH severity levels
- Generate JSON security reports
- Automated unit tests with pytest

## Project Structure

```text
log-analyzer/
│
├── logs/
│   └── auth.log
│
├── reports/
│   └── security_report.json
│
├── src/
│   ├── main.py
│   ├── log_parser.py
│   ├── analyzer.py
│   └── reporter.py
│
├── tests/
│   └── test_analyzer.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## How it works
Authentication Log
        ↓
    Log Parser
        ↓
   Log Analyzer
        ↓
Brute-force Detection
        ↓
 Severity Classification
        ↓
   JSON Report

## Severity Levels

Failed attempts         Severity
1-4                     LOW
5-9                     MEDIUM
10+                     HIGH

## Example

Failed login attempts:
2026-08-06 10:16:02 FAILED user=root ip=45.33.12.8
2026-08-06 10:16:10 FAILED user=root ip=45.33.12.8
2026-08-06 10:16:15 FAILED user=root ip=45.33.12.8

Exaxmple output:
Security Report
----------------
Failed attempts: 10

Failed attempts by IP:
45.33.12.8 -> 10 attempts | Severity: HIGH

## JSON Report

{
    "failed_attempts": 10,
    "suspicious_ips": {
        "45.33.12.8": {
            "attempts": 10,
            "severity": "HIGH"
        }
    }
}

## Requirements
- Python 3.9+
- pytest

## Running the Analyzer

From project root:
python src/main.py

## Running Tests

python -m pytest

## Learning Goals
Learning Goals

- Python programming
- Log analysis
- Security event detection
- Basic brute-force detection
- JSON data handling
- Unit testing
- Git and GitHub 

