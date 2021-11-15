# Plan

1. Intercept user's request to webpage.
2. Get HTML source code of target webpage. (Figured this out: get_html.py)
3. Send phishing website with duplicated HTML of target webpage back to user.
  - Modify action to be taken once login form submitted. Leave user hanging until next response received (Steps 4-6)?
4. Intercept user's request with login credentials. 
5. Enter stolen credentials in target website's login form.
6. Duplicate target website's response's HTML code again (2FA part) and send to user.
7. Intercept user's request with second login credentials.
8. Enter stolen credentials in target website's login form. => If 2FA, should fully authenticate us.
9. (Optional) Display duplicated successful login page back to user.
