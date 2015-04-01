open /Applications/Google\ Chrome\ Canary.app --args --remote-debugging-port=9222
osascript -e 'tell app "Terminal" to do script "ChromeDriver"'
python /Users/Eli/Desktop/selenium-remoted-debug/selenium-remote-debugging.py  