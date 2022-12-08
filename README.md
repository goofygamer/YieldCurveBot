# [YieldCurveBot v1.0](https://twitter.com/BotYieldCurve)

This automated Twitter bot posts three factoids:

- A red line representing present day's US Treasury yield curve from 1MO - 30YR.
- A green line representing the closest resembling historical yield curve. 
    - i.e. April 4, 2000 yield spread was the closest to the November 24, 2022 spread
- Number of days from the historical green line to the closest recession. 
    - i.e. Recession of 2001 was ~300 days away from April 4, 2000

## Implementation
1. Pulled the data from the [NASDAQ API](https://data.nasdaq.com/data/USTREASURY/YIELD-treasury-yield-curve-rates).
2. Cleaned the data and compartmentalized the various processes.
3. Formulated code that utilized [panda](https://pandas.pydata.org/docs/) data structures to create the aforementioned three-step factoid process.
4. Utilized the Twitter API and [Tweepy](https://docs.tweepy.org/en/stable/) to create a posting mechanism.
5. Automated the daily posting process using [Amazon EC2 Linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) and [crontab](https://crontab.guru/) for 7:30PM EST Monday-Friday.

## Screenshot

Following picture showcases a recent posting by the YieldCurveBot on Twitter.

<img src="https://user-images.githubusercontent.com/51927159/206569677-bedc0b65-be67-4e7b-87bf-b725a714011c.PNG" alt="drawing" width="400"/>

##
Made with :heart: in 2022
