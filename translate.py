from tqdm import tqdm
import argparse
from util import chunk_grouping, chunk_splitting
from llm import model, generate_output, translations

def chunk_book(input_path: str):
    with open(input_path, encoding='utf8') as f:
        book = f.read()
    chunks = book.split("\n\n")
    estimated_token_counts = []

    for chunk in chunks:
        estimated_token_count = len(chunk)
        estimated_token_counts.append(estimated_token_count)

    grouped_chunks = chunk_grouping(chunks, estimated_token_counts)

    chunks = chunk_splitting(grouped_chunks)
    return chunks

def count_tokens(chunks):
    token_counts = []
    for chunk in chunks:
        response = model.count_tokens(chunk,
                                      request_options = {'timeout': 600})
        token_count = response.total_tokens
        token_counts.append(token_count)
    return token_counts


def translate(chunks, inputLanguage='Chinese', targetLanguage='English'):
    results = []
    translation = None

    for chunk in tqdm(chunks):
        try:
            translation = generate_output(translations(chunk, inputLanguage, targetLanguage))
            results.append(translation)
        except Exception as ex:
            print(ex)

    return results

def write_output(translated_chunks: list, output_path: str):
    translated_texts = [result for result in translated_chunks]

    # join the results together by double whitespace
    translated_book = "\n\n".join(translated_texts)

    # save the translated book
    with open(output_path, "w", encoding='utf8') as f:
        f.write(translated_book)

if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description="Translate a book using the Google LLM API")
    argparser.add_argument("--input_path", type=str, help="Path to the input book file")
    argparser.add_argument("--input_language", type=str, help="Input language of the book")
    argparser.add_argument("--output_path", type=str, help="Path to the output translated book file")
    argparser.add_argument("--output_language", type=str, help="Target language of the translation")
    args = argparser.parse_args()

    chunks = chunk_book(args.input_path)
    translated_chunks = translate(chunks, args.input_language, args.output_language)
    write_output(translated_chunks, args.output_path)


