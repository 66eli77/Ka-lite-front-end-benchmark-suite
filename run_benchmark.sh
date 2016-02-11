#save me the trouble to input these env variables everytime!
chromedriver_path="/Users/Eli/Desktop/try_iDOM/Ka-lite-front-end-benchmark-suite/chromedriver"
benchmark_url="http://localhost:8080/"
benchmark_actions="/Users/Eli/Desktop/try_iDOM/Ka-lite-front-end-benchmark-suite/user_defined_behaviors.py"
save_log=false

export chromedriver_path
export benchmark_url
export benchmark_actions
export save_log

python benchmark.py