#  Gets public ip  
#  target url = "http://ip.42.pl/raw"


def get_public_ip(request_target):
    grabber = urllib2.build_opener()
    grabber.addheaders = [('User-agent', 'Mozilla/5.0')]
    try:
        public_ip_address = grabber.open(target_url).read()
    except urllib2.HTTPError, error:
        print("There was an error trying to get your Public IP:  %s") % (error)
    except urllib2.URLError, error:
        print("There was an error trying to get your Public IP:  %s") % (error)
    return public_ip_address

# print(get_public_ip("http://ip.42.pl/raw"))
