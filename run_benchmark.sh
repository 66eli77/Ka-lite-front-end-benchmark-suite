chromedriver_path="$1"
echo -n "Please type the URL where you want to perform the benchmark: "
read benchmark_url
echo -n "Please type the full path of your selenium file that defines the webpage behaviors: "
read benchmark_actions
echo -n "Newer version of Chrome devtools uses new log format, do you wish to save the log with the new format? (y/n)"
read log_format

export chromedriver_path
export benchmark_url
export benchmark_actions

if [[ $log_format =~ ^[yY][eE][sS]|[yY]$ ]]
then
	python benchmark.py
else
	python benchmark_oldFormat.py
fi