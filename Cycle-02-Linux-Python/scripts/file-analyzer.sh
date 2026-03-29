#!/bin/bash

# ============================================================
# file-analyzer.sh
# Analyzes a given directory: lists files with sizes,
# total count, total size, and the largest file.
# Usage: ./file-analyzer.sh /path/to/directory
# ============================================================

# ---------- colour helpers ----------
RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
BOLD='\033[1m'
RESET='\033[0m'

# ---------- argument check ----------
if [ $# -eq 0 ]; then
    echo -e "${RED}[!] Error: No directory path provided.${RESET}"
    echo -e "    Usage: $0 /path/to/directory"
    exit 1
fi

TARGET_DIR="$1"

# Check that the path exists and is a directory
if [ ! -e "$TARGET_DIR" ]; then
    echo -e "${RED}[!] Error: Path '$TARGET_DIR' does not exist.${RESET}"
    exit 1
fi

if [ ! -d "$TARGET_DIR" ]; then
    echo -e "${RED}[!] Error: '$TARGET_DIR' is not a directory.${RESET}"
    exit 1
fi

# Resolve to absolute path for clean display
TARGET_DIR="$(realpath "$TARGET_DIR")"

# ---------- header ----------
echo -e "${BOLD}${CYAN}"
echo "============================================"
echo "         FILE ANALYZER - REPORT"
echo "============================================${RESET}"
echo -e "${YELLOW}Directory:${RESET} $TARGET_DIR"
echo -e "${YELLOW}Scanned at:${RESET} $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# ---------- list all files with sizes ----------
echo -e "${BOLD}${GREEN}[ FILES IN DIRECTORY ]${RESET}"
echo "--------------------------------------------"

# Find all files (not directories), print size in human-readable + path
# Sorted by size descending
FILE_LIST=$(find "$TARGET_DIR" -maxdepth 1 -type f)

if [ -z "$FILE_LIST" ]; then
    echo -e "${YELLOW}  No files found in this directory.${RESET}"
else
    # Print header row
    printf "  %-10s  %s\n" "SIZE" "FILENAME"
    printf "  %-10s  %s\n" "----------" "--------------------"

    # Loop through files and print each with its size
    while IFS= read -r filepath; do
        filename=$(basename "$filepath")
        # Get size in bytes for sorting, human-readable for display
        size_human=$(du -sh "$filepath" 2>/dev/null | cut -f1)
        printf "  %-10s  %s\n" "$size_human" "$filename"
    done <<< "$(find "$TARGET_DIR" -maxdepth 1 -type f | sort)"
fi

echo ""

# ---------- statistics ----------
echo -e "${BOLD}${GREEN}[ STATISTICS ]${RESET}"
echo "--------------------------------------------"

# Total file count (files only, not subdirectories)
FILE_COUNT=$(find "$TARGET_DIR" -maxdepth 1 -type f | wc -l)
echo -e "  ${YELLOW}Total files:${RESET}       $FILE_COUNT"

# Total directory size (all contents including subdirs)
TOTAL_SIZE=$(du -sh "$TARGET_DIR" 2>/dev/null | cut -f1)
echo -e "  ${YELLOW}Total directory size:${RESET} $TOTAL_SIZE"

# Largest file — find by byte count, then display human-readable
if [ "$FILE_COUNT" -gt 0 ]; then
    LARGEST_FILE=$(find "$TARGET_DIR" -maxdepth 1 -type f -printf '%s %p\n' 2>/dev/null \
                   | sort -rn | head -1 | awk '{print $2}')

    if [ -n "$LARGEST_FILE" ]; then
        LARGEST_NAME=$(basename "$LARGEST_FILE")
        LARGEST_SIZE=$(du -sh "$LARGEST_FILE" 2>/dev/null | cut -f1)
        echo -e "  ${YELLOW}Largest file:${RESET}      $LARGEST_NAME ($LARGEST_SIZE)"
    fi
else
    echo -e "  ${YELLOW}Largest file:${RESET}      N/A (no files found)"
fi

echo ""

# ---------- subdirectory count (bonus) ----------
SUBDIR_COUNT=$(find "$TARGET_DIR" -maxdepth 1 -mindepth 1 -type d | wc -l)
echo -e "  ${YELLOW}Subdirectories:${RESET}    $SUBDIR_COUNT"

echo ""
echo -e "${CYAN}============================================${RESET}"
echo -e "${GREEN}  Analysis complete!${RESET}"
echo -e "${CYAN}============================================${RESET}"
