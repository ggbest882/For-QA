# E2E UI Script
## Инструкция
1. Установите python версии 3.10.4 или выше с офф. сайта [Python](https://www.python.org/downloads/)
2. Установите зависимости из папки E2E UI `pip install -r requirements.txt`
3. Установите Chrome под вашу ОС с офф. сайта -> [Chrome](https://developer.chrome.com/docs/chromedriver/downloads?hl=ru)<br> 
**P.S. Если у вас отсутствует Chrome, скрипт работать не будет. Скачать его можно по той же ссылке**
4. Запустите скрипт `python main.py`

P.S. Если у вас Linux и не получается установить Chrome, то используйте этот скрипт:<br>
```
sudo apt-get update
sudo apt-get install -y wget unzip
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get install -y ./google-chrome-stable_current_amd64.deb
google-chrome --version
```
Скрипт автоматически использует chromedriver и вам не нужно его искать и устанавливать

Если в консоле видете вот эту надпись `Purchase completed!`, то значит скрипт выполнен успешно
