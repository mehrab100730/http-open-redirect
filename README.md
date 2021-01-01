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

```shell

🔎 Open Redirect Scanner {v1.0-beta}
   By Demetrius Ford (@demetriusx00)

😈 http://localhost/unvalidated_redir_fwd_2.php?ReturnUrl=https://hackerone.com
😈 http://localhost/unvalidated_redir_fwd_2.php?ReturnUrl=http://hackerone.com
😈 http://localhost/unvalidated_redir_fwd_2.php?ReturnUrl=//hackerone.com
😈 http://localhost/unvalidated_redir_fwd_2.php?ReturnUrl=////hackerone.com
🎉 completed in 0.88 seconds.
```
