def split_chunk(chunk, max_len=6000):
    result = []
    index = 0
    while index < len(chunk):
      start = index
      if index + max_len < len(chunk):
        end = chunk.rfind("。", index, index + max_len) + 1
      else:
        end = len(chunk)
      result.append(chunk[start:end])
      index = end

    return result

# Split chunks into smaller chunks based on character limits.
def chunk_splitting(chunks, max_len=6000):
    result = []
    for chunk in chunks:
      result.extend(split_chunk(chunk, max_len))
    return result

# Combine short chunks into larger groups based on token counts.
def chunk_grouping(chunks, token_counts, max_len=6000):
    grouped_chunks = []
    current_group = ""
    current_token_sum = 0

    # Process each chunk and group them based on token limits
    for index in range(len(chunks)):
        chunk = chunks[index]
        count = token_counts[index]
        if token_counts[index] == 0:
            continue

        current_group += "\n\n" + chunk
        current_token_sum += count  # Count in 1 token for newlines
        # Add a new chunk if there is space available in the current group.
        if current_token_sum + 1 + count > max_len:
            grouped_chunks.append(current_group)
            current_group = ""
            current_token_sum = 0


    return grouped_chunks