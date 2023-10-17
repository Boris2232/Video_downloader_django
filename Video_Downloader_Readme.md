Hello, here you i will introduce you to video downloading process using python and django.

!!! Before reading please be familiar with Readme.txt !!!

Lets start !! -- 

As soon as registration and login procceses are finished, you are redirected to a main page. There you will see a button with a button with a picture of a 
youtube logotype and "Download from YouTube below". Click and move to a next page. 


Here you can see a input field. Copy and paste youtube link here and wait for a few seconds. If the video is not --age restricted (PROBLEM 1, Solved, See below) and -- link field
is not empty (PROBLEM 2, solved, see below), page will list to a bottom. There are many resolutions available, choose one and download a video with desired resolution.


link_collector folder's structure:

1) migrations (automatically added features after makemigration terminal command)
2) static folder (contains javascript scripts for this page and a css file)
3) templates (html template is located here)
4) __init__.py (not modified)
5) admin.py (not edited)
6) apps.py (automatically created py file)
   
8) models.py (contains three classes: Resolution (to store chosen resolution here), Mistakes (class PROBLEM 1 and PROBLEM 2 declaration) and Link (to work with given link with python libraries))
   
9) tests.py
10) views.py (functionality will be explained after)


PROBLEMS with downloading videos and it's solutions.

PROBLEM 1: AGE RESTRICTION. According to a youtube's policy, people under 18 are not alowed to watch videos, which are age restricted. To follow this rules, i have written a script, that show that video is under age restrictions. 

PROBLEM 2: EMPTY LINK: If the provided link is empty or it is invalid, this will raise a error (function in javascript which prints "Input link").

PROBLEM 3: RESOLITIONS AND FILE EXTENSIONS. When we download videos from youtube, we an face a proble, with file extensions. For example, videos that have resolution higher than 1080p are automatically downloading in webm extension (not possible to watch it on devices). To solve this issue, i created a python code which convers webm -> mp4 file (saving video quality).

PROBLEM 4: No audio track in some videos. Some videos are downloaded without audio (it is not synchronized with video), so i provided python script to download audio separetely and combine it with the video.
