from collections import Counter


def is_language_diverse(lst):
    language_counts = Counter(dev["language"] for dev in lst)
    max_count = max(language_counts.values())
    min_count = min(language_counts.values())
    return max_count <= 2 * min_count
