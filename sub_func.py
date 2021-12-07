# Function to click button (not being used currently)
def click_button(url):
    driver = webdriver.Chrome()
    driver.get(url)
    button = driver.find_element_by_id("nav-link-accountList")
    button.click()
    return driver.current_url


# Process html
def process_html(url):
    url = 'https://www.wechall.net/'

    # initialize a session
    session = requests.Session()
    # set the User-agent as a regular browser
    session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    res = session.get(url)
    html = res.content
    soup = bs(html, "html.parser")
    print(html)
    script_dir = os.path.dirname(__file__)
    with open(os.path.join(script_dir, 'index.html'), "w") as f:
        f.write(res.text)
        f.close()

    # get the JavaScript files
    script_files = []
    for script in soup.find_all("script"):
        if script.attrs.get("src"):
            # if the tag has the attribute 'src'
            script_url = urljoin(url, script.attrs.get("src"))
            script_files.append(script_url)
    
    # get the CSS files
    css_files = []
    for css in soup.find_all("link"):
        if css.attrs.get("href"):
            # if the link tag has the 'href' attribute
            css_url = urljoin(url, css.attrs.get("href"))
            css_files.append(css_url)

    # write file links into files
    with open("javascript_files.txt", "w") as f:
        for js_file in script_files:
            print(js_file, file=f)

    with open("css_files.txt", "w") as f:
        for css_file in css_files:
            print(css_file, file=f)
    
    _download_files(url, script_files)

    return html

# Function to download content from links in file
def _download_files(base, links):
    script_dir = os.path.dirname(__file__)
    for link in links:
        response = requests.get(link)
        path = link.replace(base, "")
        file_dir = '/'.join(path.split('/')[:-1])
        Path(os.path.join(script_dir, file_dir)).mkdir(parents=True, exist_ok=True)
        with open(os.path.join(script_dir, path), "w") as f:
            f.write(response.text)
            f.close()