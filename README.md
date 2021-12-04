# Instructions
Man-in-the-middle phishing site
A basic phishing site might mimic the login page for some popular web application, but with the login form sending credentials back to the attacker.  This can be potent, but 2FA can help solve the problem by making it difficult for the attacker to get into your account even after stealing the credentials.  However, instead of a static phishing site you will make a tool to run a more sophisticated phishing attack capable of bypassing 2FA.  The trick is to mimic not just one page, but all the normal interaction with the site by acting as a man-in-the-middle to the real site.  When the user enters their credentials, you can pass them on to the server.  Then when the server asks for the 2FA code, you show that to the user as well.  To keep this going you will have to do some clever rewriting of parts of the page.  Once they enter it you can pass it along to the server to complete the authentication and steal the resulting session cookie.  Ideally you should try to make this tool general enough that you can set any target server in a configuration file.  If you do not achieve that, you should at least have it working on two sites where you can demonstrate it working with dummy accounts.  Remember that this is dealing with live ammunition and you must not deploy this tool publicly or use it to hack anyone but yourself.

# Plan

1. Intercept user's request to webpage.
2. Get HTML source code of target webpage. (Figured this out: get_html.py)
3. Send phishing website with duplicated HTML of target webpage back to user.
  - Modify action to be taken once login form submitted. Leave user hanging until next response received (Steps 4-6)?
  - Also modify links and page redirections
4. Intercept user's request with login credentials. 
5. Enter stolen credentials in target website's login form.
6. Duplicate target website's response's HTML code again (2FA part) and send to user.
7. Intercept user's request with second login credentials.
8. Enter stolen credentials in target website's login form. => If 2FA, should fully authenticate us.
9. (Optional) Display duplicated successful login page back to user.


## Implementation Details

* Alter HTML (HTML_1) so that submitting login form calls custom function (find login form within html (grep for "sign in" or "log in"-esque form id names), change its onsubmit behavior to run our custom function which stores input field values before sending to the actual site)
   * Fetch and save login credentials from params
   * Send params to target website login using requests library (post request)
   * Record session ID for next access to target website
   * Save HTML response from target website once first stage login complete
   * Alter this new HTML response (HTML_2) similarly so that submitting form calls second custom function to fetch and save 2FA authentication code
     * Send code to target website
     * Access target website using session ID from first access and send code to target website
     * Should be logged in once this function executes
 * Render HTML_1 page to user


## Challenges

* Need to figure out how to dynamically link form to each unique website's html
* How to "click" button with python script: might need to use Selenium
  * How to get URL of redirect page after clicking button?

## Notes
* Dynamically rewrite links => Rewrite to [your ip address]/path and create path in django project
* Don't choose site with too much JS
* Take request to your website from user and forward request to target website using requests library

## Tasks
1. Script to rewrite all links to point to urls in our website + Create the pages in our website (Rina)
2. Write function to get user parameters submitted to our webpage and send to matching target website and displaying returned value (using requests library) + Log all user parameters (Mudi + Christine)

