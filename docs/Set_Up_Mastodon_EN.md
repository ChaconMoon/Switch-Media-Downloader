### Configuration to post on Mastodon

You need to go to the "Your applications" section in your profile settings on your Mastodon instance and create a new application.

Example link:

``https://[Your_Mastodon_instance]/settings/applications``

![alt text](../.github/img/Create_Application_Mastodon.png)

When creating the application, fill out the form as follows:

Application name: You can use any name you want, but it would be appreciated if you use the project name ``Switch Media Downloader``. This name will appear on all posts made with the application.

__Example:__

![alt text](../.github/img/Example_Mastodon_Post.png)

In the application permissions, check the following:

[ x ] read (Read account information)

[ x ] profile (Read profile information)

[ x ] write (Post on your behalf)

Save the changes and go back to get the access keys.

![alt text](../.github/img/Generate_API_Key_Mastodon.png)

In the `.env_example` file, paste those credentials in the Mastodon section along with your instance name.

![alt text](../.github/img/Paste_API_KEY_Mastodon.png)

Finally, rename the file to `.env` if you haven't done so already.
