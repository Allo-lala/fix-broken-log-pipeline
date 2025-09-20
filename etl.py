import json

SAMPLE_LOG_FILE = "sample.log"
OUTPUT_FILE = "clean.json"

VALID_LEVELS = {"INFO", "WARN", "ERROR"}

def parse_sample_log(file_path):
    """Parse the log file into a list of dictionaries with exact fields."""
    entries = []
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # skip empty lines
            parts = line.split(" ", 2)  # timestamp, level, message
            if len(parts) != 3:
                continue  # skip malformed lines
            timestamp, level, message = parts
            if level not in VALID_LEVELS:
                continue  # skip unknown log levels
            entries.append({
                "timestamp": timestamp,
                "level": level,
                "message": message
            })
    return entries

def write_clean_json(entries, output_file):
    """Write list of dicts to JSON array without extra formatting."""
    with open(output_file, "w") as f:
        json.dump(entries, f, separators=(",", ":"))  # compact, no extra spaces

def main():
    entries = parse_sample_log(SAMPLE_LOG_FILE)
    write_clean_json(entries, OUTPUT_FILE)
    print(f"{OUTPUT_FILE} successfully created with {len(entries)} records.")

if __name__ == "__main__":
    main()
