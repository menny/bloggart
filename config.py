import logging

# In production, use 'True'
memcaching = False

# In production, use 'logging.WARNING'
logging_level = logging.DEBUG

# Name of the blog
blog_name = 'Let me explain myself...'

# Your name (used for copyright info)
author_name = 'Menny Even Danan'

# (Optional) slogan
slogan = 'Programming tricks, software design, and system architecture blog'

# The hostname this site will primarially serve off (used for Atom feeds)
host = 'blog.evendanan.net'

# Selects the theme to use. Theme names correspond to directories under
# the 'themes' directory, containing templates and static content.
theme = 'clips'

# Defines the URL organization to use for blog postings. Valid substitutions:
#   slug - the identifier for the post, derived from the title
#   year - the year the post was published in
#   month - the month the post was published in
#   day - the day the post was published in
post_path_format = '/%(year)d/%(month)02d/%(slug)s'

# A nested list of sidebar menus/links.
# For more complex/versatile scenarios, just edit the theme directly.
sidebar_links = [
  ('Other myselfs', [
    { 'title' : 'G+', 'url' : 'https://plus.google.com/u/0/100465343617945336905/posts', 'target' : '_blank', 'rel' : 'bookmark' },
    { 'title' : 'github', 'url' : 'https://github.com/menny', 'target' : '_blank', 'rel' : 'bookmark' },
    { 'title' : 'CV', 'url' : 'http://www.evendanan.net/', 'target' : '_blank', 'rel' : 'bookmark' }
  ]),
]

# Custom Blocks.
# Useful to do some personalisation without the need of modifying the specific theme.
# This feature needs to be supported by the specific theme.
custom_blocks = [
  ('License', '../../custom_blocks/license.html')    # A 'title' and a 'path' to a html file with the custom content
]

# Number of entries per page in indexes.
posts_per_page = 10

# The mime type to serve HTML files as.
html_mime_type = "text/html; charset=utf-8"

# To use disqus for comments, set this to the 'short name' of the disqus forum
# created for the purpose.
disqus_forum = 'menny'

# Length (in words) of summaries, by default
summary_length = 200

# If you want to use Google Analytics, enter your 'web property id' here
analytics_id = 'UA-19733018-1'

# If you want to use PubSubHubbub, supply the hub URL to use here.
hubbub_hub_url = 'http://pubsubhubbub.appspot.com/'

# If you want to ping Google Sitemap when your sitemap is generated change this to True, else False
# see: http://www.google.com/support/webmasters/bin/answer.py?hl=en&answer=34609 for more information
google_sitemap_ping = True

# Content in Bloggart is generated using App Engine Deferred Task API
# For website with a lot of content, is preferable to generate the sitemap with a delay, to
# ensure that the rest of the content is ready, before the 'sitemap.xml' is generated
sitemap_generation_delay_sec = 900 # 15min

# If you want to use Google Site verification, go to
# https://www.google.com/webmasters/tools/ , add your site, choose the 'upload
# an html file' method, then set the NAME of the file below.
# Note that you do not need to download the file provided - just enter its name
# here.
google_site_verification = None

# Syntax highlighting style for RestructuredText and Markdown,
# one of 'manni', 'perldoc', 'borland', 'colorful', 'default', 'murphy',
# 'vs', 'trac', 'tango', 'fruity', 'autumn', 'bw', 'emacs', 'pastie',
# 'friendly', 'native'.
highlighting_style = 'emacs'

# Absolute url of the blog application use '/blog' for host/blog/
# and '' for host/.Also remember to change app.yaml accordingly
url_prefix = ''

# For use a feed proxy like feedburne.google.com
feed_proxy = None

# To use Google Friends Connect.                                          
# If you want use Google Friends Connect, go to http://www.google.com/friendconnect/ 
# and register your domain for get a Google Friends connect ID.
google_friends_id = None
google_friends_comments = True # For comments.
google_friends_members  = True # For a members container.

# To use Twitter.
# Add here your Twitter ID and, based on the specific theme,
# it will be used to mark tweets or show a side widget.
twitter_id = "mennyed"

# The dotted module name of a concrete implementation of tzinfo.
tzinfo_class = 'timezones.sst.SST'

# To format the date of your post.
# http://docs.djangoproject.com/en/1.1/ref/templates/builtins/#now
date_format = "D j F Y"

# Enable Sharing Buttons.
sharing_buttons = True
