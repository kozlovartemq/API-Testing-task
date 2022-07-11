# Files

**/utils**
- assertions.py — contains assertions functions
- print_helper.py — contains custom print function 
- request_helper.py — contains class that wrap requests methods

**/tests**
- conftest.py — contains the fixture that is used by tests
- test_comments.py — contains API tests for comments
- test_identity.py — contains API tests for identity
- test_search.py — contains API tests for search


**/allure-results** — default Allure directory. Can be changed via --alluredir="dir_name" command
- categories.json — file that fills the "categories" section in Allure report

**pytest.ini** — configuration file. Contains pytest launch options

**requirements.txt** — requirements file


# Prerequisites

1. Install all requirements:

```bash
pip install -r requirements.txt
```

2. Register your app at https://www.reddit.com/prefs/app


3. Set environment variables:
- 'REDDIT_USERNAME'
- 'REDDIT_PASSWORD'
- 'REDDIT_CLIENT_ID'
- 'REDDIT_CLIENT_SECRET'

4. Leave a comment manually for the 'Edit comment' and the 'Delete comment' tests and set its id in test_comments.py file

5. To generate Allure reports install Allure:

https://docs.qameta.io/allure/#_installing_a_commandline



# How to run

Quickrun all the tests in the directory:

    pytest

Specify launch options in **pytest.ini** file and/or using command line.

Pytest documentation can be found at https://docs.pytest.org/

# Make an Allure report

If tests were run with --alluredir="allure-results" option, it is possible to generate an Allure report:

    allure serve allure-results

Allure documentation can be found at https://docs.qameta.io/allure/