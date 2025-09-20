import json

SAMPLE_LOG_FILE = "sample.log"
OUTPUT_FILE = "clean.json"

def parse_sample_log(file_path):
    """
    Parse each line of sample.log into a dictionary.
    Preserves order, spaces, and all characters in messages.
    Handles lines with missing or malformed content gracefully.
    """
    entries = []
    with open(file_path, "r") as f:
        for line in f:
            line = line.rstrip("\n")  # Remove trailing newline only
            if not line.strip():
                continue  # skip fully empty lines
            
            # Split into maximum of 3 parts: timestamp, level, message
            parts = line.split(" ", 2)
            
            if len(parts) == 3:
                timestamp, level, message = parts
            elif len(parts) == 2:
                timestamp, level = parts
                message = ""
            elif len(parts) == 1:
                timestamp = parts[0]
                level = ""
                message = ""
            else:
                # Empty line or malformed, skip
                continue
                
            entries.append({
                "timestamp": timestamp,
                "level": level,
                "message": message
            })
    return entries

def write_clean_json(entries, output_file):
    """
    Writes entries to clean.json using compact separators.
    This avoids any extra spaces or formatting issues.
    """
    with open(output_file, "w") as f:
        json.dump(entries, f, separators=(",", ":"))

def main():
    entries = parse_sample_log(SAMPLE_LOG_FILE)
    write_clean_json(entries, OUTPUT_FILE)

if __name__ == "__main__":
    main()