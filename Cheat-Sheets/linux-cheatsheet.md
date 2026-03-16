# Linux Commands Cheat Sheet

A comprehensive reference guide for 30 essential Linux commands with syntax, examples, and useful flags.

---

## Command: ls
**What it does:** Lists files and directories in the current or specified directory  
**Syntax:** `ls [options] [path]`  
**Example:** `ls -la /home/user`  
**Useful flags:**
- `-l` (long format with detailed info)
- `-a` (show hidden files and directories)
- `-h` (human-readable file sizes)
- `-R` (recursive listing)
- `-t` (sort by modification time)

---

## Command: cd
**What it does:** Changes the current working directory  
**Syntax:** `cd [directory]`  
**Example:** `cd /var/www` or `cd ..` (parent directory)  
**Useful flags:**
- `-` (go to previous directory)
- `~` (home directory shortcut)
- `.` (current directory)
- `..` (parent directory)

---

## Command: pwd
**What it does:** Prints the current working directory path  
**Syntax:** `pwd [options]`  
**Example:** `pwd`  
**Useful flags:**
- `-L` (logical path including symlinks)
- `-P` (physical path)

---

## Command: mkdir
**What it does:** Creates new directories  
**Syntax:** `mkdir [options] directory_name`  
**Example:** `mkdir -p /home/user/projects/new-project`  
**Useful flags:**
- `-p` (create parent directories if needed)
- `-m` (set permissions for new directory)
- `-v` (verbose output)

---

## Command: rm
**What it does:** Removes files and directories  
**Syntax:** `rm [options] file_or_directory`  
**Example:** `rm -rf /path/to/directory`  
**Useful flags:**
- `-r` (recursive, for directories)
- `-f` (force removal without prompting)
- `-i` (interactive, prompt before deletion)
- `-v` (verbose output)

---

## Command: cp
**What it does:** Copies files and directories  
**Syntax:** `cp [options] source destination`  
**Example:** `cp -r /home/user/docs /backup/docs`  
**Useful flags:**
- `-r` (recursive, for directories)
- `-i` (interactive, prompt before overwrite)
- `-v` (verbose output)
- `-p` (preserve permissions and timestamps)

---

## Command: mv
**What it does:** Moves or renames files and directories  
**Syntax:** `mv [options] source destination`  
**Example:** `mv oldname.txt newname.txt`  
**Useful flags:**
- `-i` (interactive, prompt before overwrite)
- `-v` (verbose output)
- `-f` (force overwrite without prompting)

---

## Command: cat
**What it does:** Displays file contents or concatenates multiple files  
**Syntax:** `cat [options] file`  
**Example:** `cat /etc/hostname` or `cat file1.txt file2.txt`  
**Useful flags:**
- `-n` (show line numbers)
- `-A` (show all non-printing characters)
- `-E` (show line endings)
- `-s` (suppress repeated blank lines)

---

## Command: grep
**What it does:** Searches for text patterns within files  
**Syntax:** `grep [options] pattern file`  
**Example:** `grep -r "error" /var/log/`  
**Useful flags:**
- `-r` (recursive search)
- `-i` (case-insensitive search)
- `-v` (invert match, show non-matching lines)
- `-n` (show line numbers)
- `-c` (count matching lines)
- `-E` (extended regex patterns)

---

## Command: find
**What it does:** Searches for files and directories by various criteria  
**Syntax:** `find [path] [options] [expression]`  
**Example:** `find /home -name "*.txt" -type f`  
**Useful flags:**
- `-name` (search by filename)
- `-type` (search by type: f for file, d for directory)
- `-size` (search by file size)
- `-mtime` (search by modification time)
- `-exec` (execute command on found files)

---

## Command: chmod
**What it does:** Changes file and directory permissions  
**Syntax:** `chmod [options] mode file`  
**Example:** `chmod 755 script.sh` or `chmod u+x script.sh`  
**Useful flags:**
- `u` (user/owner)
- `g` (group)
- `o` (others)
- `+` (add permission)
- `-` (remove permission)
- `x` (execute), `r` (read), `w` (write)

---

## Command: chown
**What it does:** Changes file and directory ownership  
**Syntax:** `chown [options] owner:group file`  
**Example:** `chown -R user:group /home/user/documents`  
**Useful flags:**
- `-R` (recursive)
- `-v` (verbose)
- `-h` (change symlinks, not targets)

---

## Command: sudo
**What it does:** Executes commands with administrative (root) privileges  
**Syntax:** `sudo [options] command`  
**Example:** `sudo apt-get update` or `sudo systemctl restart apache2`  
**Useful flags:**
- `-u` (execute as specific user)
- `-i` (start interactive shell)
- `-l` (list allowed commands)
- `-s` (start shell as root)

---

## Command: apt-get (or apt)
**What it does:** Package manager for Debian-based systems (Ubuntu, Debian)  
**Syntax:** `apt-get [options] [command]`  
**Example:** `sudo apt-get install nginx` or `sudo apt update`  
**Useful flags:**
- `install` (install packages)
- `remove` (remove packages)
- `update` (refresh package lists)
- `upgrade` (upgrade installed packages)
- `autoremove` (remove unused dependencies)

---

## Command: tar
**What it does:** Creates, extracts, or manages compressed archive files  
**Syntax:** `tar [options] filename.tar.gz [files]`  
**Example:** `tar -czf archive.tar.gz /home/user/docs` or `tar -xzf archive.tar.gz`  
**Useful flags:**
- `-c` (create archive)
- `-x` (extract archive)
- `-z` (gzip compression)
- `-f` (specify file)
- `-v` (verbose)
- `-j` (bzip2 compression)

---

## Command: zip
**What it does:** Creates compressed zip archive files  
**Syntax:** `zip [options] archive.zip file(s)`  
**Example:** `zip -r backup.zip /home/user/documents`  
**Useful flags:**
- `-r` (recursive, include directories)
- `-q` (quiet mode)
- `-e` (encrypt with password)
- `-u` (update existing archive)

---

## Command: unzip
**What it does:** Extracts files from zip archives  
**Syntax:** `unzip [options] archive.zip`  
**Example:** `unzip -d /destination/folder backup.zip`  
**Useful flags:**
- `-d` (specify destination directory)
- `-l` (list contents without extracting)
- `-q` (quiet mode)
- `-o` (overwrite files)

---

## Command: ps
**What it does:** Displays running processes  
**Syntax:** `ps [options]`  
**Example:** `ps aux` or `ps -ef | grep nginx`  
**Useful flags:**
- `a` (all users' processes)
- `u` (user-oriented format)
- `x` (include background processes)
- `-e` (select all processes)
- `-f` (full format)
- `-o` (custom output format)

---

## Command: top
**What it does:** Displays real-time system processes and resource usage  
**Syntax:** `top [options]`  
**Example:** `top` or `top -u username`  
**Useful flags:**
- `-u` (show processes for specific user)
- `-p` (monitor specific PID)
- `-n` (run for n iterations then exit)
- `-b` (batch mode)

---

## Command: kill
**What it does:** Terminates running processes  
**Syntax:** `kill [signal] PID`  
**Example:** `kill 1234` or `kill -9 1234` (force kill)  
**Useful flags:**
- `-l` (list available signals)
- `-9` (SIGKILL - force kill)
- `-15` (SIGTERM - graceful termination)

---

## Command: nano / vim
**What it does:** Text editors for creating and editing files  
**Syntax:** `nano filename` or `vim filename`  
**Example:** `nano /etc/config.conf` or `vim script.sh`  
**Useful flags (nano):**
- `Ctrl+X` (save and exit)
- `Ctrl+O` (save)
- `Ctrl+K` (cut line)

**Useful flags (vim):**
- `:wq` (save and quit)
- `:q!` (quit without saving)
- `dd` (delete line)
- `i` (insert mode)

---

## Command: echo
**What it does:** Prints text or variables to standard output  
**Syntax:** `echo [options] text`  
**Example:** `echo "Hello, World!"` or `echo $HOME`  
**Useful flags:**
- `-n` (no trailing newline)
- `-e` (interpret escape sequences)
- `-E` (disable escape sequence interpretation)

---

## Command: pipe (|)
**What it does:** Sends output of one command as input to another  
**Syntax:** `command1 | command2`  
**Example:** `ls | grep .txt` or `cat logfile.txt | grep error`  
**Common usage:**
- Chaining multiple commands
- Filtering output
- Processing text streams

---

## Command: redirects (>, >>)
**What it does:** Redirects output to files or overwrites/appends to files  
**Syntax:** `command > file` (overwrite) or `command >> file` (append)  
**Example:** `ls > output.txt` or `echo "log entry" >> logfile.txt`  
**Useful patterns:**
- `>` (overwrite file)
- `>>` (append to file)
- `2>` (redirect errors)
- `2>&1` (redirect errors to standard output)

---

## Command: wc
**What it does:** Counts words, lines, and characters in files  
**Syntax:** `wc [options] file`  
**Example:** `wc -l logfile.txt` or `wc -w document.txt`  
**Useful flags:**
- `-l` (count lines)
- `-w` (count words)
- `-c` (count bytes)
- `-m` (count characters)

---

## Command: sort
**What it does:** Sorts lines in text files  
**Syntax:** `sort [options] file`  
**Example:** `sort -n numbers.txt` or `sort -r names.txt`  
**Useful flags:**
- `-n` (numeric sort)
- `-r` (reverse order)
- `-u` (remove duplicates)
- `-k` (sort by specific column)
- `-i` (case-insensitive)

---

## Command: cut
**What it does:** Extracts specific columns or fields from text  
**Syntax:** `cut [options] file`  
**Example:** `cut -d: -f1 /etc/passwd` or `cut -c1-10 file.txt`  
**Useful flags:**
- `-d` (specify delimiter)
- `-f` (select fields/columns)
- `-c` (select characters by position)

---

## Command: awk
**What it does:** Processes text files and extracts data by patterns  
**Syntax:** `awk [options] 'pattern { action }' file`  
**Example:** `awk -F: '{print $1}' /etc/passwd` or `awk '{print $2, $1}' file.txt`  
**Useful patterns:**
- `-F` (set field separator)
- `{print}` (print matching lines)
- `{print $1, $2}` (print specific fields)
- `NR` (line numbers)

---

## Command: sed
**What it does:** Stream editor for text substitution and transformation  
**Syntax:** `sed [options] 's/pattern/replacement/' file`  
**Example:** `sed 's/old/new/g' file.txt` or `sed -i 's/error/warning/g' log.txt`  
**Useful flags:**
- `s` (substitute)
- `g` (global replacement)
- `-i` (in-place editing)
- `d` (delete lines)
- `-e` (multiple expressions)

---

## Command: man
**What it does:** Displays manual pages and documentation for commands  
**Syntax:** `man [section] command`  
**Example:** `man ls` or `man -k search_term`  
**Useful flags:**
- `-k` (search manual by keyword)
- `-f` (show short description)
- `1` (user commands)
- `5` (file formats)
- `8` (system administration)

---

## Command: history
**What it does:** Displays previously executed commands  
**Syntax:** `history [options] [number]`  
**Example:** `history` or `history 20` (last 20 commands)  
**Useful flags:**
- `!n` (execute command number n)
- `!!` (execute last command)
- `!string` (execute last command starting with string)
- `-c` (clear history)

---

## Command: whoami / id
**What it does:** Displays current user information  
**Syntax:** `whoami` or `id [user]`  
**Example:** `whoami` or `id root`  
**Useful output:**
- `whoami` shows only username
- `id` shows UID, GID, and group memberships
- `sudo whoami` shows root (if elevated)

---

## Command: uname
**What it does:** Displays system information  
**Syntax:** `uname [options]`  
**Example:** `uname -a` or `uname -s`  
**Useful flags:**
- `-a` (all information)
- `-s` (system name)
- `-r` (kernel release)
- `-v` (kernel version)
- `-m` (machine hardware)

---

## Command: df / du
**What it does:** Displays disk space usage  
**Syntax:** `df [options]` or `du [options] directory`  
**Example:** `df -h` (human-readable disk usage) or `du -sh /home/user`  
**Useful flags (df):**
- `-h` (human-readable)
- `-T` (show filesystem type)

**Useful flags (du):**
- `-h` (human-readable)
- `-s` (summary only)
- `-d` (max depth)

---

## Summary Table

| Command | Purpose |
|---------|---------|
| ls | List files and directories |
| cd | Change directory |
| pwd | Print working directory |
| mkdir | Create directories |
| rm | Remove files/directories |
| cp | Copy files/directories |
| mv | Move/rename files |
| cat | Display file contents |
| grep | Search text patterns |
| find | Find files and directories |
| chmod | Change permissions |
| chown | Change ownership |
| sudo | Run as root |
| apt-get | Install/manage packages |
| tar | Create/extract archives |
| zip/unzip | Compress/extract zip files |
| ps | Show running processes |
| top | Monitor processes in real-time |
| kill | Terminate processes |
| nano/vim | Text editors |
| echo | Print text |
| pipe (\|) | Chain commands |
| redirects (>, >>) | Redirect output |
| wc | Count lines/words |
| sort | Sort text |
| cut | Extract columns |
| awk | Process text files |
| sed | Stream editing |
| man | Display documentation |
| history | Command history |
| whoami/id | User information |
| uname | System information |
| df/du | Disk usage |

---

**Last Updated:** March 16, 2026  
**Total Commands:** 30
