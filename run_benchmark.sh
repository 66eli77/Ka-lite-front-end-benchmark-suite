#save me the trouble to input these env variables everytime!
chromedriver_path="./chromedriver"
benchmark_url="http://localhost:8888/"
benchmark_actions="./user_defined_behaviors.py"
save_log=true

export chromedriver_path
export benchmark_url
export benchmark_actions
export save_log

python benchmark.py