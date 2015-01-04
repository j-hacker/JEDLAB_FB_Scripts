A short set of scripts I use to scrape and do some basic data analysis on the JEDLAB FB group.

Installation:

sudo pip install fbconsole (sudo at your own risk!)
chmod +x *.py

Usage:

I had to strip some CR characters embedded within the results. (Maybe a Windows
vs. Unix thing? TODO: Quote/encode text when we download it from the API.):

  cp fbposts.txt fbposts.bak
  tr -d '\r' <fbposts.bak >fbposts.txt

Download all the posts and comments in the group (takes a while!):

./get_JEDLAB_Data.py

Other scripts use that data:

Analyze comments only (TODO: What about posts?):

./userlikesperpost.py

Something else that seems unfinished (x is undefined) (TODO: What's it supposed to to?):

./histogramTest.py



