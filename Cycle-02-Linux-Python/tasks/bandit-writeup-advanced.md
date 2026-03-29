# OverTheWire Bandit — Advanced Writeup (Levels 10–20)

---

## Level 10 → 11

**Command used:**
```bash
cat data.txt | base64 --decode
```

**Password found:** `dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr`

**New concept learned:** `base64` encoding and decoding. The file contents were encoded in Base64 — a scheme that represents binary data as printable ASCII. Piping through `base64 --decode` reverses it to reveal the plaintext password.

---

## Level 11 → 12

**Command used:**
```bash
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

**Password found:** `7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4`

**New concept learned:** ROT13 cipher and the `tr` (translate) command. ROT13 shifts every letter 13 places in the alphabet. The `tr` command maps character ranges in a single pass — no external tool needed. Both encoding and decoding use the same command since 13+13=26.

---

## Level 12 → 13

**Command used:**
```bash
mkdir /tmp/work12 && cp ~/data.txt /tmp/work12/ && cd /tmp/work12
xxd -r data.txt > data.bin       # reverse the hex dump back to binary

# peel layers one by one using `file` to identify each type:
file data.bin                    # gzip
mv data.bin data.gz && gunzip data.gz

file data                        # bzip2
mv data data.bz2 && bunzip2 data.bz2

file data                        # gzip again
mv data data.gz && gunzip data.gz

file data                        # tar
tar xf data

file data5.bin                   # tar
tar xf data5.bin

file data5                       # bzip2
bunzip2 data5

file data5.out                   # tar
tar xf data5.out

file data6.bin                   # bzip2
bunzip2 data6.bin

file data6                       # tar
tar xf data6

file data8.bin                   # gzip
mv data8.bin data8.gz && gunzip data8.gz

file data8                       # ASCII text — done!
cat data8
```

**Password found:** `FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn`

**New concept learned:** Hex dumps and multi-layer compression. `xxd -r` reverses a hex dump to binary. The `file` command reads magic bytes (not file extensions) to identify formats. This level stacks gzip, bzip2, and tar repeatedly — each `file` check tells you the next tool to use.

---

## Level 13 → 14

**Command used:**
```bash
ssh -i ~/sshkey.private bandit14@localhost -p 2220
cat /etc/bandit_pass/bandit14
```

**Password found:** `MU4VWeTyJk8ROof1qqmcBRegZkdpkLhm`

**New concept learned:** SSH private key authentication with `ssh -i`. Instead of a password, this level provides an RSA private key file. The `-i` flag tells SSH which key to use. This is how most real servers are accessed securely — no password ever travels over the network.

---

## Level 14 → 15

**Command used:**
```bash
echo "MU4VWeTyJk8ROof1qqmcBRegZkdpkLhm" | nc localhost 30000
```

**Password found:** `8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo`

**New concept learned:** `nc` (netcat) for raw TCP communication. Netcat connects to any TCP port and lets you send/receive data directly. It's called the "Swiss Army knife" of networking — used for everything from banner grabbing to reverse shells during CTFs and pentests.

---

## Level 15 → 16

**Command used:**
```bash
echo "8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo" | openssl s_client -connect localhost:30001 -quiet
```

**Password found:** `kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx`

**New concept learned:** SSL/TLS connections with `openssl s_client`. Port 30001 wraps the service in TLS encryption — plain netcat won't work because it can't do the handshake. `openssl s_client` handles TLS and then lets you interact with the underlying service. The `-quiet` flag suppresses certificate info so only the response shows.

---

## Level 16 → 17

**Command used:**
```bash
# Step 1: find which ports in 31000-32000 are open and speak SSL
nmap -p 31000-32000 --open localhost

# Step 2: test each SSL port — one returns an RSA key instead of echoing input
echo "kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx" | openssl s_client -connect localhost:31790 -quiet

# Step 3: save the returned private key and use it
mkdir /tmp/b16
# paste the key into /tmp/b16/key.pem
chmod 600 /tmp/b16/key.pem
ssh -i /tmp/b16/key.pem bandit17@localhost -p 2220
```

**Password found:** `EReVavePLFHtFlFsjn3hyzMlvSuSAcRD`

**New concept learned:** Port scanning with `nmap` combined with manual service testing. Among several open SSL ports, only one responds correctly (returns a key rather than echoing input). This teaches reconnaissance — scanning first, then probing each candidate to find the right one.

---

## Level 17 → 18

**Command used:**
```bash
diff passwords.old passwords.new
```

**Password found:** `x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO`

**New concept learned:** `diff` for line-by-line file comparison. The two password files are nearly identical — only one line differs. `diff` outputs `<` for lines only in the first file and `>` for lines only in the second. The `>` line is the new password. Essential tool for spotting changes between config files, logs, or code.

---

## Level 18 → 19

**Command used:**
```bash
# .bashrc immediately runs `exit` — can't use an interactive shell
# Solution: pass the command directly to ssh (runs before .bashrc kicks you out)
ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat ~/readme"
```

**Password found:** `cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8`

**New concept learned:** Bypassing a hostile `.bashrc`. Interactive logins source `.bashrc`, which here calls `exit` immediately. Appending a command to the `ssh` line runs it in a non-interactive session — `.bashrc` either doesn't apply or the command executes before the logout fires. This is a classic CTF trick and a real-world sysadmin technique.

---

## Level 19 → 20

**Command used:**
```bash
ls -la ~/bandit20-do          # notice the 's' in permissions: rwsr-x---
./bandit20-do cat /etc/bandit_pass/bandit20
```

**Password found:** `0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO`

**New concept learned:** Setuid (SUID) binaries and Linux privilege escalation. The `s` in `rwsr-x---` is the setuid bit — it makes the binary run as its *owner* (bandit20) regardless of who executes it. So even as bandit19, running `./bandit20-do` gives us bandit20's privileges for that command. SUID misconfigurations are a major real-world privilege escalation vector.

---

## Summary

| Level | Key Tool | Core Concept |
|-------|----------|--------------|
| 10 → 11 | `base64 -d` | Base64 decoding |
| 11 → 12 | `tr` | ROT13 / character translation |
| 12 → 13 | `xxd -r`, `file`, `gunzip`, `bunzip2`, `tar` | Hex reversal + multi-layer decompression |
| 13 → 14 | `ssh -i` | Private key authentication |
| 14 → 15 | `nc` | Raw TCP with netcat |
| 15 → 16 | `openssl s_client` | SSL/TLS service interaction |
| 16 → 17 | `nmap` + `openssl s_client` | Port scanning + SSL service discovery |
| 17 → 18 | `diff` | File comparison |
| 18 → 19 | `ssh host "cmd"` | Bypassing hostile `.bashrc` |
| 19 → 20 | SUID binary | Linux privilege escalation |
