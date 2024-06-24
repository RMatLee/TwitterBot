
# Twitter Bot

This project contains a Python-based Twitter bot built using the Tweepy library and a simple Tkinter GUI. It allows users to automatically respond, retweet, favorite, and follow based on tweets that match certain keywords.

## Features

- **Automatic Replies**: Send replies to tweets based on specific search keywords.
- **Retweeting**: Automatically retweet tweets that match certain criteria.
- **Favoriting Tweets**: Automatically favorite tweets found by search queries.
- **Following Users**: Automatically follow users who tweet something related to the specified keywords.

## Prerequisites

Before you can run this bot, you'll need to have the following installed:
- Python 3
- Tweepy
- python-dotenv

You will also need a Twitter Developer account and access tokens for your Twitter app.

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/RMATLee/TwitterBot.git
cd TwitterBot
```

Install the required packages:

```bash
pip install tweepy python-dotenv
```

## Configuration

1. Create a `.env` file in the project root directory and add your Twitter API keys and tokens:

```plaintext
CONSUMER_KEY=your_consumer_key_here
CONSUMER_SECRET_KEY=your_consumer_secret_key_here
ACCESS_TOKEN=your_access_token_here
ACCESS_TOKEN_SECRET=your_access_token_secret_here
```

2. Ensure your `.env` file is never committed to your repository. It should be included in your `.gitignore`:

```
.env
```

## Usage

To run the Twitter bot, execute the following command:

```bash
python main.py
```

The GUI will launch, allowing you to enter search parameters and choose actions like replying, retweeting, favoriting, and following.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your features or fixes.

## License

This project is released under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project uses the [Tweepy library](https://www.tweepy.org/) for interacting with the Twitter API.
- Thanks to the contributors of python-dotenv for simplifying environment variable management.
