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

1. Download
    
        curl -sSL -o install.sh https://storage.googleapis.com/rasa-x-releases/0.41.1/install.sh

2. Install all files into default folder, `/etc/rasa`:

        sudo bash ./install.sh 

3. Start up Rasa X and wait until all containers are running (Using `-d` will run Rasa X in the background):

        cd /etc/rasa
        sudo docker-compose up -d

4. Access and set admin password:

        cd /etc/rasa
        sudo python3 rasa_x_commands.py create --update admin me <PASSWORD>

Navigate to the hostname or IP where your server is reachable and log in using your newly created password.

Learn more: https://rasa.com/docs/rasa-x/installation-and-setup/install/docker-compose

### 8. Connect Custom Action Server

1. This repository is set up with a GitHub Actions workflow, so that whenever a change is pushed to the `actions` directory, a new Docker image for the Custom Action Server will be built and pushed to a container registry.

To specify which container registry and image name, open `.github/workflows/action_server.yml` and change `docker_image_name:` to your desired Docker registry and image name. 

Also, follow the instructions in [Building an Action Server Image](https://rasa.com/docs/rasa/how-to-deploy/#building-an-action-server-image) to specify your `docker_registry_login: ` and `docker_registry_password: `. 

2. Add OpenAI API key environment variable to .env file:

        cd /etc/rasa
        vim .env
    
    Add your API key to the bottom of the file:

        OPENAI_API_KEY=sk-...

3. Replace the default `app` image with the image of your custom action server:

    To avoid your changes in the docker-compose file being overwritten when you update versions, you should not apply your changes to `docker-compose.yml`. Instead, create a new file called `docker-compose.override.yml` inside your `/etc/rasa` directory and apply your changes there. Docker will automatically take that file into account and override any attributes in `docker-compose.yml` with changes from the override file.

    The contents of `docker-compose.override.yml` should look like this:

        version: '3.4'
        services:
            app:
                restart: always
                image: <image:tag>
                expose:
                    - "5055"
                environment:
                    OPENAI_API_KEY: "${OPENAI_API_KEY}"

3. If your Docker containers are already running, take them down and then start Rasa X again:

        cd /etc/rasa
        sudo docker-compose down
        sudo docker-compose up -d

Learn more: https://rasa.com/docs/rasa-x/installation-and-setup/customize#connecting-a-custom-action-server 

## Rasa Documentation

Rasa Open Source: https://rasa.com/docs/rasa/

Rasa X: https://rasa.com/docs/rasa-x/

Rasa Action Server: https://rasa.com/docs/action-server

## Next Steps

Implement in-house semantic search instead of using OpenAI by following this guide:

- Part 1: https://medium.com/mlearning-ai/semantic-search-with-s-bert-is-all-you-need-951bc710e160
- Part 2: https://medium.com/mlearning-ai/search-rank-and-recommendations-35cc717772cb
- Code: https://github.com/99sbr/semantic-search-with-sbert 