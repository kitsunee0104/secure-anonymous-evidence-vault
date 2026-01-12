from flask import Flask, render_template, request
import os
import uuid

from crypto_utils import generate_key, encrypt_data, generate_hash
from database import init_db, store_file

app = Flask(__name__)
VAULT_DIR = "vault"

# Generate encryption key (MVP version)
KEY = generate_key()

# Ensure vault exists
os.makedirs(VAULT_DIR, exist_ok=True)

# Initialize database
init_db()

@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        data = file.read()

        case_id = str(uuid.uuid4())
        encrypted_data = encrypt_data(data, KEY)
        file_hash = generate_hash(encrypted_data)

        file_path = os.path.join(VAULT_DIR, case_id + ".enc")
        with open(file_path, "wb") as f:
            f.write(encrypted_data)

        store_file(case_id, file_hash, file_path)

        return f"""
        <h3>Evidence Stored Securely</h3>
        <p><b>Case ID:</b> {case_id}</p>
        <p><b>SHA-256 Hash:</b> {file_hash}</p>
        <p>Save this information safely.</p>
        """

    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)
