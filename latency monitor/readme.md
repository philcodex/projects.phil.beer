# Latency Monitor

A lightweight command-line tool to measure HTTP response latency for any URL. Runs a configurable number of curl requests, timestamps each result, and prints a summary with the average response time.

## Requirements

- Python 3.x
- `curl` installed and available in your PATH (standard on macOS and most Linux distributions)

## Usage

```bash
python latency_monitor.py
```

You will be prompted to enter a URL:

```
Enter URL to monitor: https://example.com
```

## Output

```
Monitoring latency for https://example.com (5 runs, 5s delay)...

[01] 14:32:01 - Total time:    0.243817
[02] 14:32:06 - Total time:    0.251043
[03] 14:32:11 - Total time:    0.238560
[04] 14:32:16 - Total time:    0.249712
[05] 14:32:21 - Total time:    0.241388

==============================
Final Results for https://example.com
Total Runs:    5
Average Time:  0.244904 seconds
==============================
```

## Configuration

Edit the variables near the top of the script to change the default behaviour:

| Variable | Default | Description |
|----------|---------|-------------|
| `runs` | `5` | Number of requests to make |
| `delay` | `5` | Seconds to wait between requests |

## Notes

- Latency is measured as `time_total` from curl — the total time from request start to the last byte received
- Press `Ctrl+C` at any time to stop early; results collected so far will still be summarised
- Redirects and HTTPS overhead are included in the timing