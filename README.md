# ReadMe for Submission
Our project was the mitm 2fa phishing site. The github repo can be found [here](https://github.com/rinakawamura/2FAMITMAttack).
Our code is split into three modules (cas, linkedin, and wechall) corresponding to the websites they target, but in actuality, much of the code within
each module is the same. We created these divisions because our code dynamically creates URLs and views (as necessary for Django) and this helped with organization
and debugging. If the main target url in each module is changed to that of another, the modified module should still function correctly with the new target site.

## Some highlights of our code:
* get_html.py provides functionality for logging request and response headers as well as html code. For the deployed projects, we used some of the functions in this module to only log headers for requests and responses. 

* helper.py provides the main functionality of this project. Firstly, it crawls the target website and creates 'fake' pages with the same content for each link. Additonally, this file also handles all requests and responses being ferried between the victim and the target website. 

* urls.py provides mappings to pages created through crawling. These link mappings and the corresponding views are dynamically created by helper.py.  

===========================The items below this point are notes we made during the project===========================

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

