import subprocess
import time

# Configuration
url = input("Enter URL to monitor: ")
cmd = ['curl', '-s', '-o', '/dev/null', '-w', '%{time_total}', url]
runs = 5
delay = 5 
latencies = []

print(f"\nMonitoring latency for {url} ({runs} runs, {delay}s delay)...\n")

try:
    for i in range(1, runs + 1):
        # Run curl and capture only the number
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # Convert string output to float and store it
        latency = float(result.stdout.strip())
        latencies.append(latency)
        
        # Print the formatted line as requested
        timestamp = time.strftime("%H:%M:%S")
        print(f"[{i:02d}] {timestamp} - Total time:\t{latency:.6f}")
        
        if i < runs:
            time.sleep(delay)

except KeyboardInterrupt:
    print("\nInterrupted by user.")

# Calculate and display the average
if latencies:
    avg_latency = sum(latencies) / len(latencies)
    print("\n" + "="*30)
    print(f"Final Results for {url}")
    print(f"Total Runs:    {len(latencies)}")
    print(f"Average Time:  {avg_latency:.6f} seconds")
    print("="*30)