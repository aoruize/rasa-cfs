# Rasa CFS Virtual Assistant

An AI chatbot for the [Ontario Centre of Forensic Sciences (CFS)](https://www.mcscs.jus.gov.on.ca/english/centre_forensic/CFS_intro.html), developed using [Rasa](https://rasa.com) and [OpenAI](https://beta.openai.com). Answers forensics investigators' questions by performing semantic search across a large library of [CFS technical documents](https://www.mcscs.jus.gov.on.ca/english/centre_forensic/InformationforInvestigatorsSubmitters/TechnicalInformationSheets/CFS_tech_sheets.html) to find the most relevant search results.

## Setup Instructions

### 1. Environment requirements

- Linux OS
    - Ubuntu 18.04 / 20.04
    - Debian 9 / 10
    - Red Hat 7 / 8
    - CentOS 7 / 8
- `Python 3.8`
- `pip 21.1.3`
- `docker`
- `docker-compose`


### 2. Create and activate virtual environment

    python3 -m venv ~/rasa-cfs-env
    cd ~/rasa-cfs-env
    source ./bin/activate


### 3. Clone this repository into virtual environment
    
    git clone https://github.com/aoruize/rasa-cfs.git


### 4. Install dependencies

    cd rasa-cfs
    pip install -r requirements.txt


### 5. Add OpenAI API key to operating system as an environment variable 

Ensure you have access to the OpenAI Beta API. Login to OpenAI and copy your API key from https://beta.openai.com/docs/developer-quickstart/your-api-keys. 

To temporarily add the environment variable, run the following command in the terminal, using your own API key: 

    export OPENAI_API_KEY='sk-...'

To add the environment variable to the operating system permanently, add it to your shell configuration files. Add the above command to the end of the following files:

    ~/.bashrc
    ~/.profile


### 6. Run Rasa Action Server 

    cd ~/rasa-cfs-env/rasa-cfs
    rasa run actions


### 7. Install and run Rasa X using Docker Compose

#### 7.1  Download
    
    curl -sSL -o install.sh https://storage.googleapis.com/rasa-x-releases/0.41.1/install.sh
    

#### 7.2  Install
Install all files into default folder, `/etc/rasa`:

    sudo bash ./install.sh 


#### 7.3  Start
Start up Rasa X and wait until all containers are running (Using `-d` will run Rasa X in the background):

    cd /etc/rasa
    sudo docker-compose up -d


#### 7.4  Access
Access and set admin password:

    cd /etc/rasa
    sudo python3 rasa_x_commands.py create --update admin me <PASSWORD>

Navigate to the hostname or IP where your server is reachable and log in using your newly created password.

Learn more: https://rasa.com/docs/rasa-x/installation-and-setup/install/docker-compose


## Rasa Documentation

Rasa Open Source: https://rasa.com/docs/rasa/

Rasa X: https://rasa.com/docs/rasa-x/

Rasa Action Server: https://rasa.com/docs/action-server


## Next Steps

Implement in-house semantic search instead of using OpenAI by following this guide:

- Part 1: https://medium.com/mlearning-ai/semantic-search-with-s-bert-is-all-you-need-951bc710e160
- Part 2: https://medium.com/mlearning-ai/search-rank-and-recommendations-35cc717772cb
- Code: https://github.com/99sbr/semantic-search-with-sbert 