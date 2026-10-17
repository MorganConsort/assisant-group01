import re
import subprocess


def audit():
    print("=== 1. Checking git tracked files for sensitive names ===")
    files = subprocess.check_output(["git", "ls-files"], text=True).splitlines()
    sensitive_names = [
        f for f in files
        if any(k in f.lower() for k in [".env", "secret", "id_rsa", "token", "key.pem", "credential"])
        and f != ".env.example"
    ]
    print(f"Tracked sensitive file names: {sensitive_names}")

    print("\n=== 2. Checking git log diffs for common secret patterns ===")
    log_diff = subprocess.check_output(["git", "log", "-p", "--all"], text=True, errors="ignore")
    patterns = [
        ("API Key / Token", r"(?i)(api[_-]?key|access[_-]?token|secret[_-]?key|auth[_-]?token)\s*[:=]\s*['\"][A-Za-z0-9_\-]{8,}['\"]"),
        ("Private Key", r"-----BEGIN (?:RSA|EC|DSA|OPENSSH|PGP|PRIVATE) KEY-----"),
        ("Password in code", r"(?i)(password|passwd|pwd)\s*[:=]\s*['\"][^'\"]{4,}['\"]"),
        ("Connection String with password", r"(?i)(postgres|mysql|mongodb|redis):\/\/[^:\s]+:[^@\s]+@")
    ]

    for label, pat in patterns:
        matches = re.findall(pat, log_diff)
        if matches:
            print(f"[ALERT] {label}: found {len(matches)} potential match(es)")
        else:
            print(f"[CLEAN] {label}: none found")

    print("\n=== 3. Checking for Personal Data (Vietnamese phone numbers) ===")
    phone_pattern = r"\b(?:0|\+84)(?:3|5|7|8|9)[0-9]{8}\b"
    phones = re.findall(phone_pattern, log_diff)
    print(f"Phone numbers found: {len(phones)}")

    print("\n=== 4. Checking gitignore configuration ===")
    with open(".gitignore", "r", encoding="utf-8") as f:
        gitignore_content = f.read()
    has_env = ".env" in gitignore_content
    print(f".env covered in .gitignore: {has_env}")

    print("\nScan completed successfully.")


if __name__ == "__main__":
    audit()
