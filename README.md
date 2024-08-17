# product-dimensioning-2
A program made for the Raspberry Pi 5, for measuring and delivering product dimensions

# Pi setup
Install the recommended Raspberry Pi OS (64-bit)

When installed, run: ```sudo apt-get update && sudo apt-get upgrade```

# Repo setup
From the root of the repo, create a virtual environment, with the flag: ```--system-site-packages``` in order to utilize the libcamera module:

```python -m venv venv --system-site-packages```

Activate it by running: ```source venv/bin/activate```

And lastly install the pip requirements:

```pip install -r requirements.txt```

# Running the program
```python3 src/app.py```
