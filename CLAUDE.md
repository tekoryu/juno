# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a security research project that evaluates and compares SAST tools and AI models on their ability to detect vulnerabilities in intentionally vulnerable Python web applications. The project implements a framework for systematic evaluation of security analysis tools.

## Repository Structure

### Core Directories

- `src/pygoat/` - PyGoat vulnerable application source code (intentionally vulnerable Django app)
- `src/dvpwa/` - DVPWA (Damn Vulnerable Python Web Application) source code
- `csv/` - Analysis results from various tools and AI models
  - `csv/pygoat/` - Results for PyGoat: bandit.csv, semgrep.csv, semgrep-pro.csv, gpt-5.csv, claude-sonnet-4-5.csv, gemini-2.5-pro.csv, grok-4-0709.csv
  - `csv/dvpwa/` - Results for DVPWA: same tool set as PyGoat
- `groundtruth/` - Ground truth vulnerability datasets
  - `groundtruth/pygoat/pygoat_groundtruth.csv` - Known vulnerabilities in PyGoat
  - `groundtruth/dvpwa/dvpwa_groundtruth.csv` - Known vulnerabilities in DVPWA
- `data/` - Reference data including OWASP Top 10 documentation
- `presentations/` - Research presentation materials

### Analysis Results Format

All CSV files follow a standardized format with columns:
- `id` - Unique identifier
- `vulnerability_name` - Name/description of the vulnerability
- `severity` - Risk level (High, Medium, Low)
- `cwe_code` - CWE (Common Weakness Enumeration) identifier
- `location` - File path and line number (e.g., `src/pygoat/introduction/views.py:158`)

## Standard Workflow

### Analyzing Vulnerable Applications

The `prompt_standard` file contains the template for security analysis:
```
Scan @src/{pygoat|dvpwa}/ project for security flaws. List them in a csv file named `${AI_MODEL}.csv` containing only id, vulnerability name, severity, cwe code and location. Csv file will be kept in /csv/{pygoat|dvpwa}. Do not use SAST tools.
```

When analyzing with AI models:
1. Reference the appropriate vulnerable application in `src/`
2. Output results to `csv/{application_name}/{model_name}.csv`
3. Follow the standard CSV format defined above
4. Compare findings against ground truth in `groundtruth/`

### Comparing Results

To evaluate tool/model effectiveness:
1. Load ground truth from `groundtruth/{application}/`
2. Load tool results from `csv/{application}/`
3. Calculate metrics: true positives, false positives, false negatives, precision, recall

## Important Notes

- The applications in `src/` are **intentionally vulnerable** - they contain known security flaws for testing purposes
- Never deploy or run these applications in production environments
- When analyzing results, cross-reference CWE codes with OWASP documentation in `data/owasp-top-10-2021.md`
- Ground truth files represent the authoritative list of known vulnerabilities for comparison
- This is a research/academic project focused on security tool evaluation, not active vulnerability exploitation

## Research Context

This project supports research on evaluating SAST tools vs. AI models for security vulnerability detection in Python web applications, following the framework outlined in `estrutura_consulta_artigos.md`.
