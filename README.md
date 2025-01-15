# translator
book translation using LLMs


## install dependencies

```
pip install -r requirements.txt
```

## define your Google API key
make sure to set environment variable `GOOGLE_API_KEY`

## run the translation
`input_path` : this point to the book need to be translated
`output_path`: this point to the location of translated book

Example:
```
python translate.py --input_path=input/book1.txt --input_language=Chinese --output_path=output/book1.txt --output_language=English
```