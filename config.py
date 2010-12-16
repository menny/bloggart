import logging

# In production, use 'True'
memcaching = True

# In production, use 'logging.WARNING'
logging_level = logging.WARNING

# Name of the blog
blog_name = 'My Blog'

# Your name (used for copyright info)
author_name = 'Author First name and Surname'

# (Optional) slogan
slogan = 'A fancy slogan for your new fancy blog'

# The hostname this site will primarially serve off (used for Atom feeds)
host = 'localhost:8080'

# Selects the theme to use. Theme names correspond to directories under
# the 'themes' directory, containing templates and static content.
theme = 'squared'

# Defines the URL organization to use for blog postings. Valid substitutions:
#   slug - the identifier for the post, derived from the title
#   year - the year the post was published in
#   month - the month the post was published in
#   day - the day the post was published in
post_path_format = '/%(year)d/%(month)02d/%(slug)s'

# Sidebar configuration.
# It is a sequence of DIV Blocks with various types of content supported.
# The format is an array of Dictionary like:
#  [
#     {
#        'enabled'   : True (absent or set to False will make the Section disappear)   ,
#        'type'      : 'links' (just a set of links)
#                       or 'gfc' (Google Friends Connect Widget)
#                       or 'twitter' (Twitter Widget)
#                       or 'code' (Generic HTML Code Block: stuff like Ads or Licenses),
#        'title'     : Title to give to this Section in the Sidebar                    ,
#        TYPE-SPECIFIC key-values (see examples below)                                 ,
#     },
#     ...
#  ]
# More can be supported easily, tweaking the theme. Or just using the block of type 'code'.
sidebar_blocks = [
   # Block of Links
   {
      'enabled'   : True,
      'type'      : 'links',     
      'title'     : 'Blogroll',
      'links'     : [
         { 'title' : 'Nick Johnsonz', 'url' : 'http://blog.notdot.net/', 'external' : True, 'rel' : 'bookmark' },
         { 'title' : 'Bill Katz', 'url' : 'http://www.billkatz.com/', 'external' : True, 'rel' : 'bookmark' },
         { 'title' : 'Coding Horror', 'url' : 'http://www.codinghorror.com/blog/', 'external' : True, 'rel' : 'bookmark' },
         { 'title' : 'Craphound', 'url' : 'http://craphound.com/', 'external' : True, 'rel' : 'bookmark' },
         { 'title' : 'Neopythonic', 'url' : 'http://www.neopythonic.blogspot.com/', 'external' : True, 'rel' : 'bookmark' },
         { 'title' : 'Schneier on Security', 'url' : 'http://www.schneier.com/blog/', 'external' : True, 'rel' : 'bookmark' },
      ]
   },
   # Google Friends Connect Widget
   {
      'enabled'   : False,
      'type'      : 'gfc',                   
      'title'     : 'Members',
      'id'        : None,              # Google Friends Connect ID
      'nrows'     : 4,                 # Number of Rows in the Widget
      'comments'  : True               # Enable Comments in Post
   },
   # Twitter Widget
   {
      'enabled'   : True,
      'type'      : 'twitter',
      'title'     : 'Twitter',
      'username'  : 'nicksdjohnson',   # Twitter Username
      'ntweets'   : 5,                 # Number of Tweets to Show
      'height'    : 400                # Widget Height (='ntweets * 100' is adviced)
   },
   # An HTML Code Block (this license one is a good example)
   {
      'enabled'   : True,
      'type'      : 'code',
      'title'     : 'License',
      'path'      : '../../custom_blocks/license.html',   # Path to any custom HTML Code that you want to include
   },
]

# Links to External Services on which the User has an Account.
# This will be listed in a theme-specific way.
external_accounts = [
   { 'service' : 'github', 'url' : 'https://github.com/detro' },
   { 'service' : 'linkedin', 'url' : 'http://www.linkedin.com/in/ivandemarino' },
   { 'service' : 'twitter', 'url' : 'http://twitter.com/detronizator' },
   { 'service' : 'kickstarter', 'url' : 'http://www.kickstarter.com/profile/ivandemarino' }
]

# Number of entries per page in indexes.
posts_per_page = 10

# The mime type to serve HTML files as.
html_mime_type = "text/html; charset=utf-8"

# To use disqus for comments, set this to the 'short name' of the disqus forum
# created for the purpose.
disqus_forum = None

# Length (in words) of summaries, by default
summary_length = 200

# If you want to use Google Analytics, enter your 'web property id' here
analytics_id = None

# If you want to use PubSubHubbub, supply the hub URL to use here.
hubbub_hub_url = 'http://pubsubhubbub.appspot.com/'

# If you want to ping Google Sitemap when your sitemap is generated change this to True, else False
# see: http://www.google.com/support/webmasters/bin/answer.py?hl=en&answer=34609 for more information
google_sitemap_ping = True

# If you want to use Google Site verification, go to
# https://www.google.com/webmasters/tools/ , add your site, choose the 'upload
# an html file' method, then set the NAME of the file below.
# Note that you do not need to download the file provided - just enter its name
# here.
google_site_verification = None

# Default markup language for entry bodies (defaults to html).
default_markup = 'html'

# Syntax highlighting style for RestructuredText and Markdown,
# one of 'manni', 'perldoc', 'borland', 'colorful', 'default', 'murphy',
# 'vs', 'trac', 'tango', 'fruity', 'autumn', 'bw', 'emacs', 'pastie',
# 'friendly', 'native'.
highlighting_style = 'friendly'

# Absolute url of the blog application use '/blog' for host/blog/
# and '' for host/.Also remember to change app.yaml accordingly
url_prefix = ''

# Defines where the user is defined in the rel="me" of your pages.
# This allows you to expand on your social graph.
rel_me = None

# For use a feed proxy like feedburne.google.com
feed_proxy = None

# The dotted module name of a concrete implementation of tzinfo.
tzinfo_class = 'timezones.sst.SST'

# To format the date of your post.
# http://docs.djangoproject.com/en/1.1/ref/templates/builtins/#now
date_format = "D j F Y"

# Enable Sharing Buttons.
sharing_buttons = True
