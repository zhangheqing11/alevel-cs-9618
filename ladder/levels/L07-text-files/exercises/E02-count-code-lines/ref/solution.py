def count_code_lines(file_name: str) -> int:
    count = 0
    with open(file_name, encoding="utf-8") as source:
        for raw_line in source:
            line = raw_line.rstrip("\n")
            trimmed = line.lstrip(" ")
            if trimmed != "" and not trimmed.startswith("//"):
                count = count + 1
    return count
