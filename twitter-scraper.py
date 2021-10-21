from flask.json import dump
from Scweet.scweet import scrape
from Scweet.user import get_user_information, get_users_following, get_users_followers
from flask import Flask, request, jsonify
import asyncio
import pandas as pd


app = Flask(__name__)

async def accountScrape(accountID):
    loop=asyncio.get_event_loop()
    data = await loop.run_until_complete(asyncio.gather(scrape(since="2021-10-15", from_account = f"@{accountID}", interval=1, 
    	headless=True, display_type="Top", save_images=False, 
    	resume=False, filter_replies=False, proximity=False))) 
    return jsonify(data)

@app.route("/", methods=['GET'])
def check():
    return "Hello"

@app.route("/word", methods=['GET'])
def wordScrapper():
    word = request.args.get("word")
    data = scrape(words=word, since="2021-10-16", until=None, from_account = None, interval=1, 
    headless=True, display_type="Top", save_images=False, 
    resume=False, filter_replies=True, proximity=False)
    result = f"{data}"
    df = pd.read_csv(result)
    return df


@app.route("/fromAccount", methods=['GET'])
async def fromAccount():
    accountID = request.args.get("accountID")
    data =  asyncio.gather(accountScrape(accountID)) 
    await data
    result = f"{data}"

    return "Ok"


@app.route("/toAccount", methods=['GET'])
def toAccount():
    accountID = request.args.get("accountID")
    data = scrape(since="2021-10-06", to_account = f"@{accountID}", interval=1, 
	headless=True, display_type="Top", save_images=False, 
	resume=False, filter_replies=False, proximity=False)
    result = f"{data}"

    return result

@app.route("/hashtag", methods=['GET'])
def account():
    hashTag = request.args.get("hashtag")
    data = scrape(hashtag=hashTag, since="2021-10-14", until=None, from_account = None, interval=1, 
	headless=True, display_type="Top", save_images=False, 
	resume=False, filter_replies=True, proximity=False)
    result = f"{data}"

    return result

if __name__ == "__main__":
    asyncio.run(app.run(debug=True)) 