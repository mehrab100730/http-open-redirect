# usage

Probing a URL using a common redirect dork (e.g., ```ReturnUrl```):

```shell
$ python3 main.py --url="http://localhost/unvalidated_redir_fwd_2.php?ReturnUrl=portal.php" \
                  --cookie="PHPSESSID=EXAMPLE; security_level=0"
```
