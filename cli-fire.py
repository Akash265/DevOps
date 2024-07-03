#!/home/codespace/.venv/bin/python

import fire
from mylib.logic import analyze_sentiment

if __name__ == "__main__":
    fire.Fire(analyze_sentiment)
