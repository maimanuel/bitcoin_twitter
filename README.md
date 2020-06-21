# Bitcoin Twitter
> What is the twittersphere saying about bitcoin?


## Install

`pip install bitcoin_twitter`

## How to use

This package uses the twitter api and will require that you have API and Secret API keys.
Create a `twitter_credentials.py` file containing least the following two lines
```python
CONSUMER_KEY = '' # Api Key in quotes
CONSUMER_SECRET = '' # API Secret Key in quotes
```

This file will be imported as a python module. If you are working with github, it is advised to include your credentials file in `twitter_credentials.py` your `.gitignore`, to never push it to github.

> Don't commit your credentials file before it's added to `.gitignore`

## Set up a connection



```python
from twitter_credentials import CONSUMER_KEY,CONSUMER_SECRET 
```

```python
conn = connector(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
df_tweets = conn.get_tweets()
```

|    |            tweet_id | tweet_text                                                                                                                                     | tweet_created_at    |       tweet_user_id | user_name                  | user_screen_name   |   retweet_count | tweet_geo   | tweet_coordinates   |
|---:|--------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------|:--------------------|--------------------:|:---------------------------|:-------------------|----------------:|:------------|:--------------------|
|  0 | 1274790798731567104 | In recent AMA @Covir_io team revealed how #Covir can fight against the Covid19 corona virus.                                                 | 2020-06-21 19:46:25 | 1010946155109203968 | Mahim Hassan               | MahimHassan20      |               0 |             |                     |
|    |                     | #Covir is high classy… https://t.co/WZONzPKkop                                                                                               |                     |                     |                            |                    |                 |             |                     |
|  1 | 1274790792306085888 | @DinoMeIaye #Bitcoin #Ethereum Join our team now to know more. Do you know that with your smartphone and ability to… https://t.co/kjpDdSfDDP | 2020-06-21 19:46:24 |          1029302077 | Your Favorite Ex boyfriend | J_Charisma101      |               0 |             |                     |
|  2 | 1274790732000354306 | $STEEM All Targets Hit! 30% Profit💥🔥                                                                                                         | 2020-06-21 19:46:09 | 1247057677336719360 | Isabella                   | cryptoexp54261B    |               0 |             |                     |
|    |                     |                                                                                                                                              |                     |                     |                            |                    |                 |             |                     |
|    |                     | For 10x gains, join https://t.co/knmjRPZ27y                                                                                                  |                     |                     |                            |                    |                 |             |                     |
|    |                     |                                                                                                                                              |                     |                     |                            |                    |                 |             |                     |
|    |                     | $TEL #nem #binance #bitcoin… https://t.co/dGYdShz8Yf                                                                                         |                     |                     |                            |                    |                 |             |                     |
|  3 | 1274790699783712769 | #EURUSD all targets done, 2800USD Profits in a day.                                                                                          | 2020-06-21 19:46:01 | 1249359552702640132 | Aleena                     | Aleena_232         |               0 |             |                     |
|    |                     |                                                                                                                                              |                     |                     |                            |                    |                 |             |                     |
|    |                     | For more Free signals : https://t.co/jMqjWu2LvY                                                                                              |                     |                     |                            |                    |                 |             |                     |
|    |                     |                                                                                                                                              |                     |                     |                            |                    |                 |             |                     |
|    |                     | #USDCAD… https://t.co/c64ikAETck                                                                                                             |                     |                     |                            |                    |                 |             |                     |
|  4 | 1274790661498318851 | @MobilePunch #Bitcoin #Ethereum Join our team now to know more. Do you know that with your smartphone and ability t… https://t.co/e1ve3VC52R | 2020-06-21 19:45:52 |          1029302077 | Your Favorite Ex boyfriend | J_Charisma101      |               0 |             |                     |
