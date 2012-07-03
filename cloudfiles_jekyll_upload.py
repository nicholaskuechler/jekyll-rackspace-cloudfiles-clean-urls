# Jekyll at Rackspace Cloud Files with Clean URLs
#
# Copyright 2012 Nicholas Kuechler
# http://www.nicholaskuechler.com/

""" Jekyll at Rackspace Cloud Files with Clean URLs """

import os
import sys
import cloudfiles

# Rackspace Cloud API credentials
USERNAME = "RACKSPACECLOUD_USERNAME"
API_KEY = "RACKSPACECLOUD_API_KEY"
# This is the name of your container. I create containers in the format: www.domain.com
CONTAINER_NAME = "www.yourdomain.com"

conn = cloudfiles.get_connection(username=USERNAME, api_key=API_KEY, serviceNet=False)

container = conn.get_container(CONTAINER_NAME)

# Upload all files in the jekyll _site directory
for root, dirs, files in os.walk('_site'):
    for name in files:
        filename = os.path.join(root, name)

        # Remove _site/ from the uploaded file name, or else our URL will be www.domain.com/_site/post-name
        upload_filename = filename.replace("_site/", "")

        # Upload the file to Rackspace Cloud Files
        obj = container.create_object(upload_filename)

        # Check if the file contains HTML code. If so, we need to set the correct content type.
        for line in open(filename):
            if "<!DOCTYPE html>" in line:
                print "file %s is an HTML file!" % filename
                # If html file, then set content type
                obj.content_type = "text/html"

        fp = open(filename)
        print "uploading filename: %s" % upload_filename
        obj.write(fp)

