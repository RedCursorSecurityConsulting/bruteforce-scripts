## CMS/Admin Login Bruteforcers Project

The goal of this repository is to collect different CMS and administrative portal bruteforce tools. The tools are designed to be reuseable and have the same command line arguments.

#### General Usage

```
usage:  cms_or_admin_name.py [-h] --url URL [--csrf-url CSRF_URL] [-o OUTPUT]
                             (-u USERNAME | -uF USERNAMEFILE)
                             (-p PASSWORD | -pF PASSWORDFILE)

optional arguments:
  -h, --help            show this help message and exit
  --url URL             URL of Login page.
  --csrf-url CSRF_URL   URL of page to get CSRF token from [default: same as --url].
  -o OUTPUT, --output OUTPUT
                        Output file [default: -].
  -u USERNAME, --username USERNAME
                        Username
  -uF USERNAMEFILE, --usernameFile USERNAMEFILE
                        File containting list of usernames.
  -p PASSWORD, --password PASSWORD
                        Password
  -pF PASSWORDFILE, --passwordFile PASSWORDFILE
                        File containing list of passwords.
```

---

### Currently Supported CMS/Admin logins

#### Django

Django bruteforce script. (Usually login url is the same as csrf url).

#### Squiz Matrix

Squiz Matrix bruteforce script. (Needs different login/csrf urls and login url requires a SQ_ACTION=login parameter).
