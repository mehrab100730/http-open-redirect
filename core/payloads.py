# => Credit FuzzDB (@fuzzdb-project):
# => https://github.com/fuzzdb-project/fuzzdb/blob/master/attack/redirect/redirect-injection-template.txt

OPEN_REDIRECT_PAYLOADS = ['hackerone.com',
                          '/hackerone.com',
                          '//hackerone.com',
                          '///hackerone.com',
                          '////hackerone.com',
                          '/http://hackerone.com',
                          '/https://hackerone.com',
                          '%2fhackerone.com',
                          '%2f$2fhackerone.com',
                          '%2fhackerone.com%2f%2f',
                          '$2f%2fhackerone.com%2f%2f',
                          '%2fhackerone.com//',]
