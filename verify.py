import sqlite3
import hashlib
import sys
from crypto_utils import generate_hash  # note: matches your filename

DB_NAME = "evidence.db"

def verify(case_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        "SELECT file_hash, file_path FROM evidence WHERE case_id = ?",
        (case_id,)
    )
    row = cur.fetchone()
    conn.close()

    if not row:
        print("❌ Case ID not found")
        return

    stored_hash, path = row
    print(f"{stored_hash} and path is {path}")

    try:
        with open(path, "rb") as f:
            data = f.read()
    except FileNotFoundError:
        print(f"❌ Evidence file not found at {path}")
        return

    current_hash = hashlib.sha256(data).hexdigest()
    print(f"current hash is {current_hash}")

    if stored_hash == current_hash:
        print("✅ Integrity verified. Evidence untampered.")
    else:
        print("⚠️ WARNING: Evidence has been modified!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 verify.py <case_id>")
    else:
        verify(sys.argv[1])

