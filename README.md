# Rasa CFS Virtual Assistant

An AI chatbot for the [Ontario Centre of Forensic Sciences (CFS)](https://www.mcscs.jus.gov.on.ca/english/centre_forensic/CFS_intro.html), developed using Rasa and OpenAI. Answers forensics investigators' questions by performing semantic search across a large library of [CFS technical documents](https://www.mcscs.jus.gov.on.ca/english/centre_forensic/InformationforInvestigatorsSubmitters/TechnicalInformationSheets/CFS_tech_sheets.html) to find the most relevant search results.

## Setup Instructions

### 1. Environment requirements

- Linux OS
    - Ubuntu 18.04 / 20.04
    - Debian 9 / 10
    - Red Hat 7 / 8
    - CentOS 7 / 8
- Python 3.8
- Pip 21.1.3

### 2. Create and activate virtual environment

    python3 -m venv rasa-cfs-env
    cd rasa-cfs-env
    source ./bin/activate

### 3. Clone this repository into virtual environment
    
    git clone https://github.com/aoruize/rasa-cfs.git

### 4. Install dependencies

    cd rasa-cfs
    pip install -r requirements.txt

### 5. Add OpenAI API key to operating system as an environment variable 

    export OPENAI_API_KEY='sk-...'

### 6. Run Rasa Action Server 

    rasa run actions

### 7. Install and run Rasa X 
Learn more: https://rasa.com/docs/rasa-x/installation-and-setup/install/quick-install-script

    curl -s get-rasa-x.rasa.com | sudo bash

When done, the script will print the URL to access Rasa X:

    You can now access Rasa X on this URL: <--URL-->

## Rasa Documentation

Rasa Open Source: https://rasa.com/docs/rasa/

Rasa X: https://rasa.com/docs/rasa-x/

Rasa Action Server: https://rasa.com/docs/action-server