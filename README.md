# UnhubTheDP
Twitter bot that retweets tweets from The Daily Progress that aren't 'hub' content—ads or national stories with no direct relevance to Charlottesville, VA. Not affiliated with Lee Enterprises or The Daily Progress. Feel free to repurpose for your local paper!

Contact Jake Gold with questions: jake@jakebgold.com.

## Directions to set up your own
Set up in AWS Lambda as a function. You'll need to add Tweepy, requests, and requests-oauthlib as folders in the root directory and fill in the keys with Twitter Developer credentials. In AWS, set the timeout to five minutes and add a trigger that has the bot run as often as you would like, as low as every six minutes. This runs every 30.
