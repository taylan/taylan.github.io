## Initialize project 


```
brew install python3
pip3 install virtualenv

git clone <this repo>

virtualenv -p python3 venv
source venv/bin/activate

pip install -r requirements.txt

# upgrade all outdated packages
pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U

pip freeze > requirements.txt
```
