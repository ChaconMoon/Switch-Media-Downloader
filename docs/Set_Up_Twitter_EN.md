### Configuration to post on Twitter

To post on Twitter, you must register as a developer on Twitter and create a new project.

[Link](https://developer.x.com/en/portal/projects-and-apps)

This application must have the following permissions:

In the application permissions, you must allow read and write access to your account.

![alt text](../.github/img/App_Permissions_Twitter.png)

And for the application type, create an Automation App or a bot.

![alt text](../.github/img/Type_Of_App_Twitter.png)

Fill in the App information and provide a website as information for the App.

![](../.github/img/App_Info_Twitter.png)

Now, in the Keys and Tokens tab, copy the respective tokens into the `.env_example` file.

![](../.github/img/Generate_API_Key_Twitter.png)

![](../.github/img/Paste_API_KEY_Twitter.png)

__Customer Keys__

TWITTER_PRIMARY_API_KEY = API_KEY

TWITTER_PRIMARY_API_SECRET_KEY = API_SECRET

__Authentication Tokens__

TWITTER_BEARER_TOKEN = BEARER_TOKEN

TWITTER_PRIMARY_ACCESS_TOKEN = ACCESS_TOKEN

TWITTER_PRIMARY_ACCESS_TOKEN_SECRET = TOKEN_SECRET

__OAuth 2.0 Client ID and Client Secret__

TWITTER_PRIMARY_CUSTOMER_2_KEY = CLIENT_ID

TWITTER_PRIMARY_CUSTOMER_2_SECRET_KEY = CLIENT_SECRET

Afterwards, rename this file to `.env`.
