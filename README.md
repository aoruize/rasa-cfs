# Rasa CFS Virtual Assistant

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

    python3 -m venv /path/to/new/virtual/environment
    cd /path/to/new/virtual/environment
    source ./bin/activate

### 3. Clone repository
    
    git clone https://github.com/aoruize/rasa-cfs.git

### 4. Install Python dependencies

    cd rasa-cfs
    pip install -r requirements.txt

### 5. Add OpenAI API key to OS as environment variable 

    export OPENAI_API_KEY='sk-...'

### 6. Run Action Server 

    rasa run actions

### 7. Install Rasa X (https://rasa.com/docs/rasa-x/installation-and-setup/install/quick-install-script):

    curl -s get-rasa-x.rasa.com | sudo bash
    