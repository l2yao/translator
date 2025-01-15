# translator
book translation using Gemini API


## install dependencies

```
pip install -r requirements.txt
```

## define your Google API key
make sure to set environment variable `GOOGLE_API_KEY`

## run the translation
* `input_path` : Path to the input book file
* `input_language` : Input language of the book
* `output_path`: Path to the output translated book file
* `output_language`: Target language of the translation

Example:
```
python translate.py --input_path=input/book1.txt --input_language=Chinese --output_path=output/book1.txt --output_language=English
```