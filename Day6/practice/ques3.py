spam_messages = [
    "Earn ₹5000 daily from home! Click here now!!",
    "Work from home and become rich in 7 days!!!",
    "Congratulations! You’ve won an iPhone 🎉 Click the link to claim now!",
    "You are selected for a cash prize, hurry up!",
    "First 100 people to comment 'YES' will get a surprise 😍",
    "Type AMEN and something amazing will happen!",
    "Check my profile for a secret trick to make money 💰",
    "This site changed my life 👉 [fake link]",
    "Nice post! Check out my page for more!!!",
    "Follow me I follow back 100%",
    "click this", "subscribe this", "buyy now!", "Make a lot of money"
]

message = input("Enter your comment: ").lower()

spam_keywords = ["earn", "click", "won", "congratulations", "cash prize", "free", "subscribe", "buy", "money"]

if any(word in message for word in spam_keywords):
    print("🚨 Alert: Potential spam detected. Stay safe!")
else:
    print("Safe message, Enjoy your day...")