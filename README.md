# http open redirect

This tool can help you identify endpoints vulnerable to open redirects. <br />
Your main objective should be to escalate severity by chaining attacks.

What do you mean?

> Can you hijack an OAuth Token?  
> Can you invoke an internal service request? (SSRF)  
> Can you modify HTTP responses? (CRLF)  
> Can you invoke arbitrary JavaScript? (XSS)  

# install

**Note**: tested on Python 3.8.6

```shell
$ git clone https://github.com/demetriusx00/http-open-redirect.git
$ cd http-open-redirect/ && pip3 install -r requirements.txt
```

# usage

Probing a URL using a common redirect dork (e.g., ```ReturnUrl```):

```shell
$ python3 main.py --url="http://localhost/unvalidated_redir_fwd_2.php?ReturnUrl=portal.php" \
                  --cookie="PHPSESSID=EXAMPLE; security_level=0"
```

![example](https://i.ibb.co/VMj6tx5/example.png)
