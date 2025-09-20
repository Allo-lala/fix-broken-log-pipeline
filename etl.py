import json

SAMPLE_LOG_FILE = "sample.log"
OUTPUT_FILE = "clean.json"

def parse_sample_log(file_path):
    """
    Parse every line in sample.log and include it in the output.
    Preserves order, spacing, and any unusual log levels or message formats.
    """
    entries = []
    with open(file_path, "r") as f:
        for line in f:
            # Remove only the trailing newline, preserve all spaces
            line = line.rstrip("\n")
            if not line.strip():
                continue  # skip fully empty lines
            # Split into 3 parts: timestamp, level, message
            parts = line.split(" ", 2)
            timestamp = parts[0] if len(parts) > 0 else ""
            level = parts[1] if len(parts) > 1 else ""
            message = parts[2] if len(parts) > 2 else ""
            entries.append({
                "timestamp": timestamp,
                "level": level,
                "message": message
            })
    return entries

def write_clean_json(entries, output_file):
    """
    Writes the entries as a JSON array with compact formatting.
    Ensures no extra spaces or newlines that might fail Oracle.
    """
    with open(output_file, "w") as f:
        json.dump(entries, f, separators=(",", ":"))

def main():
    entries = parse_sample_log(SAMPLE_LOG_FILE)
    write_clean_json(entries, OUTPUT_FILE)

if __name__ == "__main__":
    main()
