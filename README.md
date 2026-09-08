\# Python API \& UI Automation Framework



A Python-based automation testing framework covering REST API testing and UI automation using pytest and Playwright.



\## Tech Stack



\- Python

\- pytest

\- requests

\- Playwright

\- pytest-html

\- JSON Schema

\- Git

\- GitHub Actions



\## Project Structure



```text

Python API Automation/

│

├── .github/

│   └── workflows/

│       └── tests.yml

│

├── api/

│   └── api\_client.py

│

├── pages/

│   ├── login\_page.py

│   └── inventory\_page.py

│

├── test\_data/

│   ├── posts\_data.json

│   ├── post\_schema.json

│   └── ui\_data.json

│

├── tests/

│   ├── test\_posts.py

│   ├── test\_auth.py

│   ├── test\_ui.py

│   ├── test\_dropdown.py

│   ├── test\_radio.py

│   ├── test\_form\_controls.py

│   ├── test\_e2e.py

│   └── test\_pom.py

│

├── utils/

│   ├── api\_assertions.py

│   └── schema\_validator.py

│

├── config.py

├── conftest.py

├── logger.py

├── pytest.ini

├── requirements.txt

└── .gitignore

