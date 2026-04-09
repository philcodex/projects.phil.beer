import subprocess
import time

# Configuration
url = "https://phil.beer"
cmd = ['curl', '-s', '-o', '/dev/null', '-w', 'Total time:\t%{time_total}\n', url]
runs = 10
delay = 30  # seconds

print(f"Starting {runs} latency checks for {url}...\n")

for i in range(1, runs + 1):
    try:
        # Run the command and capture output
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # result.stdout already contains the "Total time: ..." string from the -w flag
        timestamp = time.strftime("%H:%M:%S")
        print(f"[{i:02d}] {timestamp} - {result.stdout.strip()}")
        
        # Wait unless it's the very last run
        if i < runs:
            time.sleep(delay)
            
    except subprocess.CalledProcessError as e:
        print(f"Error on run {i}: {e}")
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
        break

print(f"\nFinished {runs} runs.")