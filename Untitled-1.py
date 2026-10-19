import hashlib
file_path = r"C:\Users\PC\Downloads\rockyou.txt\rockyou.txt"

target_hash = "8ec47631827329eb114714a20d9b3eeb8a9a4293bd5d6823af0632e8d4f30dfa"

with open(file_path, "r", encoding="latin-1") as f:
    for password in f:
        password = password.rstrip("\r\n")

        candidate_hash = hashlib.sha256(
            password.encode("utf-8")
        ).hexdigest()

        if candidate_hash == target_hash:
            print("Match:", password)
            break
    else:
        print("No match found.")