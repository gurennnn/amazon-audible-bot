# Building a Bot for Scraping Amazon Audible

## Description

In this project, we are going to build a Bot using Python and Selenium 3, in order to scrape [amazon audible](https://www.audible.com/search) books data.  
We'll basically get each books' title, authors, date and length of audio (recall that these are audio books).  
This project can be extended to include the summaries of books as well.

## Output Datasets

In the data folder, we'll have a single csv file that contains all of the books' data.

## Setup & Run

Run the following command for running the bot in the background:

```bash
pip install -r requirements.txt
python3 scripts/scraping.py
```

Alternatively, you can check the notebook file for running the bot step by step, and visualize it's actions.

## Tools & Libraries

- Python 3.10
- pandas
- selenium 3

## Aknowledgements

Thanks to [Frank Andrade](https://www.udemy.com/user/frank-andrade-13/) aka The Pycoach for his great course on web scraping.
