# refuge_project
The project aims at detecting high-quality messages from Telegram and training a Ukrainian summarization model by fine-tuning the mT5 model and implementing TextRank algorithm.

We store our code in the src folder. The detection folder show how we detect potential high-quality message. The MMLSummarization and TextRankSummarization folder show how we use do text summarization.

Algorithm output are listed below.

| fileName                            | Description                                                  | column                                                       |
|-------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|
| scrape.telegram_forwardsRT30.csv    | potential high-quality telegram dataset                      | chat, country, state, city, views, forwards, replies, messageText, predicted_class |
| prediction_uk-mt5-base-xlsum-v3.csv | use mt5-base model to generate summary                       | messageText, predicted_class, cleanText, summary...          |
| prediction_mT5-sum-news-ua.csv      | use mt5-large model (from paper author)  to generate summary | messageText, predicted_class, cleanText, summary...          |
| prediction_textRank-sum.csv         | use fast textRank algorithm to generate summary              | messageText, predicted_class, summary... |
| prediction_textRank-sum-bert.csv    | use bert-textRank algorithm to generate summary              | messageText, predicted_class, summary... |

