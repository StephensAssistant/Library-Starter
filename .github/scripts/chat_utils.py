#!/usr/bin/env python3
import re

HEADING_PATTERN = re.compile(r"^###\s+CHAT-(\d{4})\b", re.MULTILINE)
FILENAME_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}\.md$")


def extract_id_occurrences(content: str):
    return [int(m) for m in HEADING_PATTERN.findall(content)]


def extract_ids(content: str):
    return set(extract_id_occurrences(content))
