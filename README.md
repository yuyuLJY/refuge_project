# refuge_project
## data
| fileName                            | Description                                                                 | column                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------|
| scrape.telegram_forwardsRT30.csv | telegram message dataset                                                    | 'chat', 'country', 'state', 'city', 'views', 'forwards', 'replies', 'messageText'|
| prediction_uk-mt5-base-xlsum-v3.csv | use mt5-base model to generate summary                                      | 'messageText', 'predicted_class', 'cleanText', 'summary'... |
| prediction_mT5-sum-news-ua.csv      | use mt5-large model (fineturn model from paper author)  to generate summary |'messageText', 'predicted_class', 'cleanText', 'summary'...                                                                             |
| prediction_textRank.csv             | use textRank algorithm to generate summary                                  |                                                                            |
