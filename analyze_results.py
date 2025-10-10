#!/usr/bin/env python3
import csv
import re
from pathlib import Path
from collections import defaultdict

def normalize_location(location):
    """Normalize file location by removing common prefixes and standardizing format."""
    if not location:
        return ""

    # Remove common prefixes
    location = location.replace("src/dvpwa/", "")
    location = location.replace("src/", "")

    # Extract just the file path and line range
    # Handle formats like "sqli/app.py:24", "sqli/app.py:25-29", "sqli/app.py:42-45"
    return location.strip().lower()

def normalize_cwe(cwe):
    """Normalize CWE code to just the number."""
    if not cwe or cwe == "N/A":
        return ""
    # Extract numbers from formats like "CWE-89", "89", "CWE-79"
    match = re.search(r'(\d+)', str(cwe))
    return match.group(1) if match else ""

def locations_match(loc1, loc2):
    """Check if two locations refer to the same vulnerability."""
    if not loc1 or not loc2:
        return False

    # Normalize both locations
    loc1_norm = normalize_location(loc1)
    loc2_norm = normalize_location(loc2)

    # Extract file path and line numbers
    def parse_location(loc):
        parts = loc.split(':')
        if len(parts) < 2:
            return None, None
        file = parts[0]
        line_part = parts[1] if len(parts) > 1 else ""

        # Extract line numbers or ranges
        lines = set()
        if '-' in line_part:
            # Range like "25-29"
            start, end = line_part.split('-')
            try:
                lines = set(range(int(start), int(end) + 1))
            except:
                pass
        elif ';' in line_part:
            # Multiple locations like "42;661"
            for ln in line_part.split(';'):
                try:
                    lines.add(int(ln.strip()))
                except:
                    pass
        else:
            # Single line
            try:
                lines.add(int(line_part))
            except:
                pass

        return file, lines

    file1, lines1 = parse_location(loc1_norm)
    file2, lines2 = parse_location(loc2_norm)

    if not file1 or not file2:
        return False

    # Check if files match
    if file1 != file2:
        return False

    # Check if there's any line overlap
    if lines1 and lines2:
        return len(lines1 & lines2) > 0

    return True

def find_match_in_groundtruth(finding, groundtruth):
    """Find if a finding matches any entry in the groundtruth."""
    finding_loc = finding['location']
    finding_cwe = normalize_cwe(finding.get('cwe_code', ''))

    for gt in groundtruth:
        gt_loc = gt['location']
        gt_cwe = normalize_cwe(gt.get('cwe_code', ''))

        # Primary matching: location
        if locations_match(finding_loc, gt_loc):
            # Secondary validation: CWE if available
            if finding_cwe and gt_cwe:
                if finding_cwe == gt_cwe:
                    return True
            else:
                # If no CWE to compare, location match is enough
                return True

    return False

def load_csv(file_path):
    """Load a CSV file and return list of findings."""
    findings = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Normalize column names
            normalized_row = {}
            for key, value in row.items():
                # Skip None keys (malformed CSV)
                if key is None:
                    continue
                # Handle different column name variations
                key_lower = key.lower().strip().replace(' ', '_')
                normalized_row[key_lower] = value
            # Only add if we have location data
            if normalized_row.get('location'):
                findings.append(normalized_row)
    return findings

def calculate_metrics(tool_name, tool_findings, groundtruth):
    """Calculate TP, FP, and FN for a tool by comparing against groundtruth."""
    tp = 0
    fp = 0
    matched_gt_indices = set()

    # Check each tool finding
    for finding in tool_findings:
        # Find if this finding matches any groundtruth entry
        found_match = False
        for idx, gt in enumerate(groundtruth):
            if idx in matched_gt_indices:
                continue

            if locations_match(finding.get('location', ''), gt.get('location', '')):
                # Validate with CWE if available
                finding_cwe = normalize_cwe(finding.get('cwe_code', ''))
                gt_cwe = normalize_cwe(gt.get('cwe_code', ''))

                if finding_cwe and gt_cwe:
                    if finding_cwe == gt_cwe:
                        tp += 1
                        matched_gt_indices.add(idx)
                        found_match = True
                        break
                else:
                    # No CWE to compare, location match is sufficient
                    tp += 1
                    matched_gt_indices.add(idx)
                    found_match = True
                    break

        if not found_match:
            fp += 1

    # False negatives: groundtruth vulnerabilities that the tool didn't find
    fn = len(groundtruth) - len(matched_gt_indices)

    return {
        'tool': tool_name,
        'tp': tp,
        'fp': fp,
        'fn': fn,
        'total_findings': len(tool_findings),
        'groundtruth_total': len(groundtruth)
    }

def main():
    base_path = Path('/home/tekoryu/development/juno')

    # Load groundtruth
    groundtruth_path = base_path / 'groundtruth' / 'dvpwa' / 'dvpwa_groundtruth.csv'
    groundtruth = load_csv(groundtruth_path)

    print(f"Loaded {len(groundtruth)} groundtruth vulnerabilities")

    # Define tools and models to analyze
    tools = {
        'bandit': 'csv/dvpwa/bandit.csv',
        'semgrep': 'csv/dvpwa/semgrep.csv',
        'semgrep-pro': 'csv/dvpwa/semgrep-pro.csv',
        'gemini-2.5-pro': 'csv/dvpwa/gemini-2.5-pro.csv',
        'claude-4.5-sonnet': 'csv/dvpwa/claude-4.5-sonnet.csv',
        'gpt-5': 'csv/dvpwa/gpt-5.csv',
        'grok-4': 'csv/dvpwa/grok-4.csv',
    }

    results = []

    for tool_name, csv_file in tools.items():
        tool_path = base_path / csv_file
        if not tool_path.exists():
            print(f"Warning: {csv_file} not found")
            continue

        tool_findings = load_csv(tool_path)
        print(f"\n{tool_name}: {len(tool_findings)} findings")

        metrics = calculate_metrics(tool_name, tool_findings, groundtruth)
        results.append(metrics)

        print(f"  TP: {metrics['tp']}, FP: {metrics['fp']}, FN: {metrics['fn']}")

    # Write results to score_dvpwa.csv
    output_path = base_path / 'csv' / 'dvpwa' / 'score_dvpwa.csv'

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['tool', 'tp', 'fp', 'fn', 'total_findings', 'groundtruth_total',
                      'precision', 'recall', 'f1_score']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for result in results:
            tp = result['tp']
            fp = result['fp']
            fn = result['fn']

            # Precision: accuracy of reported findings
            precision = tp / (tp + fp) if (tp + fp) > 0 else 0

            # Recall: completeness of detection (coverage of groundtruth)
            recall = tp / (tp + fn) if (tp + fn) > 0 else 0

            # F1 Score: harmonic mean of precision and recall
            f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

            result['precision'] = round(precision, 4)
            result['recall'] = round(recall, 4)
            result['f1_score'] = round(f1_score, 4)

            writer.writerow(result)

    print(f"\n✓ Results written to {output_path}")

if __name__ == '__main__':
    main()
