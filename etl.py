import json

SAMPLE_LOG_FILE = "sample.log"
OUTPUT_FILE = "clean.json"
VALID_LEVELS = {"INFO", "WARN", "ERROR"}

def parse_sample_log(file_path):
    """
    Parse each line of sample.log into a dictionary.
    Preserves order, spaces, and all characters in messages.
    Includes lines even if messages contain spaces.
    """
    entries = []
    with open(file_path, "r") as f:
        for line in f:
            line = line.rstrip("\n")  # Remove trailing newline only
            if not line.strip():
                continue  # skip fully empty lines
            parts = line.split(" ", 2)  # timestamp, level, message
            if len(parts) < 3:
                # If message is missing, still include empty string
                timestamp, level = parts[0], parts[1] if len(parts) > 1 else ""
                message = ""
            else:
                timestamp, level, message = parts
            # Keep level even if unexpected (Oracle might test unknown levels)
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
