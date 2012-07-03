jekyll-rackspace-cloudfiles-clean-urls
======================================

Jekyll at Rackspace Cloud Files with Clean URLs

Copyright 2012 Nicholas Kuechler
http://www.nicholaskuechler.com/

GETTING STARTED
===============

* Place the  _plugins/ext.rb in your Jekyll site's _plugins/ directory. If the directory does not exist, you can create it.
* Edit your Jekyll site's _config.yml file and set your permalink structure. I use:

permalink: /:categories/:title

OR

permalink: /:title

Depending on my site

* Edit cloudfiles_jekyll_upload.py and fill in the appropriate values for USERNAME, API_KEY, CONTAINER_NAME
* Place cloudfiles_jekyll_upload.py in the same directory as your _config.yml file for your site.


READ MORE
=========

Read my blog post on this project:

http://nicholaskuechler.com/2012/07/03/jekyll-with-clean-urls-hosted-at-rackspace-cloud-files/
