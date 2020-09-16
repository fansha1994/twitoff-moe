# web_app/routes/twitter_routes.py

from flask import Blueprint, render_template, jsonify
from web_app.models import db, User, Tweet #, parse_records
from web_app.services.twitter_service import api as twitter_api_client
from web_app.services.basilica_service import connection as basilica_api_client

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>/fetch")
def get_user(screen_name=None):
    print(screen_name)

# fetching data from twitter api
    twitter_user = twitter_api_client.get_user(screen_name)

    # get existing user from the db or initialize a new one:
    db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)

    db_user.screen_name = twitter_user.screen_name
    db_user.name = twitter_user.name
    db_user.location = twitter_user.location
    db_user.followers_count = twitter_user.followers_count

    db.session.add(db_user)
    db.session.commit()
    # return "OK"
    #breakpoint()

    tweets = twitter_api_client.user_timeline(screen_name, tweet_mode="extended", count=150)
    print("TWEETS COUNT:", len(tweets))

    #all_tweet_texts = [status.full_text for status in statuses]
    #embeddings = list(basilica_api.embed_sentences(all_tweet_texts, model="twitter"))
    #print("NUMBER OF EMBEDDINGS", len(embeddings))

    for status in tweets:
        print(status.full_text)
        print("----")

        embedding = basilica_api_client.embed_sentence(status.full_text, model="twitter")
        print(len(embedding))

        # get existing tweet from the db or initialize a new one:
        db_tweet = Tweet.query.get(status.id) or Tweet(id=status.id)
        db_tweet.user_id = status.author.id # or db_user.id
        db_tweet.full_text = status.full_text
        db_tweet.embedding = embedding
        db.session.add(db_tweet)
        
    db.session.commit()
    return "OK"
    #return render_template("user.html", user=db_user, tweets=statuses) # tweets=db_tweets