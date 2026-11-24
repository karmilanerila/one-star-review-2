import os

ENTRY = "One star. Gravity holds everything down all day and never takes a day off, yet drops my phone face-first every single time."

def main():
    text = ENTRY.strip()
    if not 1 <= len(text) <= 160:
        raise ValueError(f"entry must be 1-160 chars, got {len(text)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
