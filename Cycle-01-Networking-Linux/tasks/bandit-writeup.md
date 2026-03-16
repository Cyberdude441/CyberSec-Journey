# OverTheWire Bandit - Levels 0-10 Writeup

## Overview
This writeup documents solutions for Bandit levels 0 through 10. Each level introduces fundamental Linux command-line skills and security concepts.

---

## Level 0 → Level 1

**Objective:** Read the password from a file named `readme` in the home directory.

**Solution:**
```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
cat readme
```

**Password:** `ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If`

**Concepts:** Basic SSH connection, reading files with `cat`

---

## Level 1 → Level 2

**Objective:** Read the password from a file named `-` (dash), which is problematic because `-` is often interpreted as a flag.

**Solution:**
```bash
ssh bandit1@bandit.labs.overthewire.org -p 2220
cat ./-
```

**Explanation:** By prefixing with `./`, we tell `cat` to treat `-` as a filename rather than a flag.

**Password:** `263JGJPfgU6LtdEvgfWU1XP5yac29mFx`

**Concepts:** Handling special filenames, path prefix usage

---

## Level 2 → Level 3

**Objective:** Read the password from a file with spaces in its name: `--spaces in this filename--`

**Solution:**
```bash
ssh bandit2@bandit.labs.overthewire.org -p 2220
cat ./--spaces\ in\ this\ filename--
```

**Explanation:** Spaces in filenames must be escaped with backslashes or the filename must be quoted.

**Password:** `MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx`

**Concepts:** Escaping special characters, handling filenames with spaces

---

## Level 3 → Level 4

**Objective:** Find the password in a hidden file within the `inhere` directory.

**Solution:**
```bash
ssh bandit3@bandit.labs.overthewire.org -p 2220
cd inhere
ls -a
cat ...Hiding-From-You
```

**Explanation:** Hidden files (starting with `.`) are not shown by default. The `-a` flag shows all files, including hidden ones. The file was named `...Hiding-From-You`.

**Password:** `2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ`

**Concepts:** Hidden files in Linux, `ls -a` usage

---

## Level 4 → Level 5

**Objective:** Among 10 files with dash prefixes, find the one containing human-readable text.

**Solution:**
```bash
ssh bandit4@bandit.labs.overthewire.org -p 2220
cd inhere
file ./-file*
cat ./-file07
```

**Explanation:** The `file` command determines file types. Most files were binary data, but `-file07` was identified as ASCII text.

**Password:** `4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw`

**Concepts:** The `file` command, identifying file types

---

## Level 5 → Level 6

**Objective:** Find a file with specific properties: human-readable, 1033 bytes, non-executable, located somewhere in the `inhere` directory tree.

**Solution:**
```bash
ssh bandit5@bandit.labs.overthewire.org -p 2220
cd inhere
find . -type f -size 1033c ! -executable
cat ./maybehere07/.file2
```

**Explanation:** The `find` command searches with multiple criteria:
- `-type f`: regular files only
- `-size 1033c`: exactly 1033 bytes
- `! -executable`: not executable

**Password:** `HWasnPhtq9AVKe0dmk45nxy20cvUa6EG`

**Concepts:** Advanced `find` command usage, file filtering

---

## Level 6 → Level 7

**Objective:** Find a file owned by user `bandit7`, group `bandit6`, and 33 bytes in size, anywhere on the system.

**Solution:**
```bash
ssh bandit6@bandit.labs.overthewire.org -p 2220
find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
cat /var/lib/dpkg/info/bandit7.password
```

**Explanation:** The `find` command searches the entire filesystem (`/`) with criteria:
- `-user bandit7`: owned by bandit7
- `-group bandit6`: group is bandit6
- `-size 33c`: exactly 33 bytes
- `2>/dev/null`: suppresses permission error messages

**Password:** `morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj`

**Concepts:** System-wide file searching, ownership and permissions

---

## Level 7 → Level 8

**Objective:** Find the password associated with the word "millionth" in a large data file.

**Solution:**
```bash
ssh bandit7@bandit.labs.overthewire.org -p 2220
grep millionth data.txt
```

**Explanation:** The `grep` command searches for lines containing "millionth" in the file.

**Password:** `dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc`

**Concepts:** Pattern searching with `grep`

---

## Level 8 → Level 9

**Objective:** Find the unique line in a file where all others appear multiple times.

**Solution:**
```bash
ssh bandit8@bandit.labs.overthewire.org -p 2220
sort data.txt | uniq -u
```

**Explanation:** 
- `sort`: arranges lines alphabetically
- `uniq -u`: shows only unique lines (appearing once)

Combined, this pipeline identifies the single line that appears only once while others repeat.

**Password:** `4CKMh1JI91bUIZZPXDqGanal4xvAg0JM`

**Concepts:** Pipes, `sort` command, `uniq` filtering

---

## Level 9 → Level 10

**Objective:** Find the password hidden in a binary file containing human-readable strings.

**Solution:**
```bash
ssh bandit9@bandit.labs.overthewire.org -p 2220
strings data.txt | grep =
```

**Explanation:** The `strings` command extracts readable text from binary files. By piping to `grep =`, we filter for lines containing the `=` character, which helps identify the password pattern.

**Password:** `FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey`

**Concepts:** Binary file analysis, `strings` command, text extraction

---

## Level 10 → Level 11

**Objective:** Decode a base64-encoded password.

**Solution:**
```bash
ssh bandit10@bandit.labs.overthewire.org -p 2220
base64 -d data.txt
```

**Explanation:** The `base64 -d` command decodes base64-encoded data. The file contains the base64-encoded password.

**Password:** `dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr`

**Concepts:** Base64 encoding/decoding, `base64` command

---

## Summary of Key Commands

| Command | Purpose |
|---------|---------|
| `cat` | Display file contents |
| `ls -a` | List all files including hidden ones |
| `file` | Determine file type |
| `find` | Search for files with specific criteria |
| `grep` | Search for text patterns |
| `sort` | Arrange lines in order |
| `uniq` | Filter duplicate lines |
| `strings` | Extract readable text from binary files |
| `base64` | Encode/decode base64 data |

---

## Progression Summary

- **Level 0-1:** File reading and special character handling
- **Level 2-3:** Working with filenames containing special characters
- **Level 4-5:** File identification and advanced searching
- **Level 6:** System-wide file discovery
- **Level 7-8:** Text processing and data analysis
- **Level 9-10:** Binary file analysis and encoding/decoding
