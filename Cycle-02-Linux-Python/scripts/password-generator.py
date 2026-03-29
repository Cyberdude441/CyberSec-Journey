#!/usr/bin/env python3

"""
password-generator.py
----------------------
Generates strong random passwords with uppercase, lowercase,
numbers, and symbols. Supports bulk generation.
Bonus: clipboard copy via pyperclip (if installed).
Usage: python3 password-generator.py
"""

import random
import string
import sys

# Try to import pyperclip for clipboard support (bonus feature)
try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False


# ── character sets ─────────────────────────────────────────────────────────────

UPPERCASE = string.ascii_uppercase          # A-Z
LOWERCASE = string.ascii_lowercase          # a-z
DIGITS    = string.digits                   # 0-9
SYMBOLS   = "!@#$%^&*()-_=+[]{}|;:,.<>?"  # common safe symbols


# ── core generator ─────────────────────────────────────────────────────────────

def generate_password(length: int) -> str:
    """
    Generate one password of the given length.
    Guarantees at least one character from each category
    so the password always meets complexity requirements.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    # Guarantee one of each type
    mandatory = [
        random.choice(UPPERCASE),
        random.choice(LOWERCASE),
        random.choice(DIGITS),
        random.choice(SYMBOLS),
    ]

    # Fill the rest from the full character pool
    all_chars    = UPPERCASE + LOWERCASE + DIGITS + SYMBOLS
    remaining    = [random.choice(all_chars) for _ in range(length - 4)]

    # Combine and shuffle so mandatory chars aren't always at the front
    password_chars = mandatory + remaining
    random.shuffle(password_chars)

    return "".join(password_chars)


def password_strength(length: int) -> str:
    """Return a simple strength label based on length."""
    if length < 8:
        return "⚠️  Weak"
    elif length < 12:
        return "🟡 Moderate"
    elif length < 16:
        return "🟢 Strong"
    else:
        return "🔵 Very Strong"


# ── input helpers ──────────────────────────────────────────────────────────────

def get_positive_int(prompt: str, default: int) -> int:
    """Prompt the user for a positive integer, falling back to default."""
    while True:
        raw = input(prompt).strip()
        if raw == "":
            return default
        try:
            value = int(raw)
            if value <= 0:
                print("    [!] Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("    [!] Invalid input. Please enter a number.")


# ── main ───────────────────────────────────────────────────────────────────────

def main():
    print("=" * 50)
    print("       🔐 PASSWORD GENERATOR")
    print("=" * 50)

    # ── password length ──────────────────────────────────────────────────────
    length = get_positive_int(
        "\n[?] Password length (default 16): ", default=16
    )

    if length < 4:
        print("[!] Minimum length is 4. Setting length to 4.")
        length = 4

    # ── how many passwords ────────────────────────────────────────────────────
    count = get_positive_int(
        "[?] How many passwords to generate? (default 1): ", default=1
    )

    # ── generate ──────────────────────────────────────────────────────────────
    print("\n" + "-" * 50)
    print(f"  Generating {count} password(s) of length {length}...")
    print(f"  Strength: {password_strength(length)}")
    print("-" * 50 + "\n")

    passwords = []
    for i in range(1, count + 1):
        pwd = generate_password(length)
        passwords.append(pwd)
        label = f"  #{i}" if count > 1 else "  Password"
        print(f"{label}: {pwd}")

    print()

    # ── clipboard (bonus) ─────────────────────────────────────────────────────
    if CLIPBOARD_AVAILABLE:
        copy_choice = input("[?] Copy last password to clipboard? (y/n): ").strip().lower()
        if copy_choice == "y":
            pyperclip.copy(passwords[-1])
            print("  ✅ Copied to clipboard!")
    else:
        print("  ℹ️  Tip: install 'pyperclip' (pip install pyperclip) to enable clipboard copy.")

    # ── tips ──────────────────────────────────────────────────────────────────
    print("\n" + "=" * 50)
    print("  💡 Security Tips:")
    print("  • Use a password manager (Bitwarden, KeePass)")
    print("  • Never reuse passwords across sites")
    print("  • Enable 2FA wherever possible")
    print("=" * 50)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Cancelled by user. Goodbye!")
        sys.exit(0)
