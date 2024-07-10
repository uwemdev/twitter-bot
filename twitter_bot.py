import tweepy

# Twitter API credentials
consumer_key = 'PaibzVFFhFDfJZAM587wZlrFm'
consumer_secret = 'QGnNyYaIop47zxxzLJB2FIqRT5xTPk9J6xkWCmTF6RbArW4Ynu'
access_token = '1388729075108286464-I0LqUQgBoI7lsjt9j5Pr3kxVTt5zRW'
access_token_secret = 'i2ehVUmt8nu6IXCcw1YlXCK5p5WYzcijI7VFzahB41s6r'

# Authenticate with Twitter using OAuthHandler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True)

# Function to check if 'delivery' is in user profile description
def check_profile_for_delivery(user):
    try:
        user_profile = api.get_user(user_id=user.id)
        profile_description = user_profile.description.lower()
        return 'delivery' in profile_description, user_profile.url
    except tweepy.TweepError as e:
        print(f"Error fetching user profile for {user.screen_name}: {e}")
        return False, ""

# Example query to search for users (without language filter)
query = "delivery service"

results = []

try:
    # Search for users based on query
    for idx, user in enumerate(tweepy.Cursor(api.search_users, q=query).items(1000)):
        found_delivery, profile_url = check_profile_for_delivery(user)
        if found_delivery:
            results.append(f"{idx + 1}. Username: {user.screen_name}, Profile URL: {profile_url}")
except tweepy.TweepError as e:
    print(f"Error searching users: {e}")

# Print all results
for result in results:
    print(result)
