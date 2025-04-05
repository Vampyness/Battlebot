# stat_sheet_parser.py

def parse_stat_sheet(text):
    stats = {}
    lines = text.splitlines()
    for line in lines:
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip().lower()
            val = val.strip().replace('%', '').replace('+', '')
            try:
                stats[key] = float(val)
            except:
                continue
    return stats
