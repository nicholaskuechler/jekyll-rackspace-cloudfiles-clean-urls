# Found this ext.rb module from pattex in #jekyll on irc.freenode.net
# Original file: https://github.com/pattex/kleinerdrei.net/blob/master/_plugins/ext.rb
# In order to get a clean URL and file name with no .html extension,
# Changed: File.join(dest, CGI.unescape("#{url}.html"))
# To: File.join(dest, CGI.unescape(url))

module Jekyll

  class Post

    alias_method :_original_url, :url

    def url
      _original_url.sub(/\/\z/, '')
    end

    alias_method :_original_destination, :destination

    def destination(dest)
      #File.join(dest, CGI.unescape("#{url}.html"))
      File.join(dest, CGI.unescape(url))
    end

  end

end
