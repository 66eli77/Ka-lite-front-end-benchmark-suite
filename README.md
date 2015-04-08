# Ka-lite-front-end-benchmark-suite
**-Description**

This benchmark suite is designed for the Ka-lite front-end optimization and development in general, and can only run on Chrome. It uses Selenium to capture Chrome logs and drive the tested webpage. User can then uses the timeline tab of Chrome devtools to display the results. Since this benchmark suite clearly separates the log capturing logic and webpage behavior logic, one can easily adapt this suite for his/her website front-end benchmarking.

**-How to use** (tested on Mac)

First, you need to install Selenium python

```
pip install -U selenium
```
You may also need to download the latest [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads).

Once it’s done, run the benchmark like this:
```
$ ./run_benchmark.sh
```
if you want to use the Chromedriver you downloaded
```
$ ./run_benchmark.sh <full-path-to-your-Chromedriver>
```
Then it will ask for the webpage URL that you want to benchmark for.(be sure the webpage is active and don’t forget to type in `http://`)
For example:  `http://localhost:9022/learn/`

Then it will ask for the full path of a python file where you define the webpage behaviors specifically for your program using Selenium. I’ve included a file `user_defined_behaviors.py` that you can use as a template. **!! IMPORTANT:** you should always include the definition
```python
def web_actions(webdriver):
```
in your code. Here the `webdriver` is defined in and passed by `benchmark.py`, you should not define your own webdriver.  [--How to use Selenium Python--](https://selenium-python.readthedocs.org/api.html#module-selenium.webdriver.remote.webelement)

Finally, it will ask you weather or not to save the benchmarking log in Chrome devtools’ new format. If you want to display your benchmark log on Chrome version 38 and above, type `yes`, otherwise, type `no`.

If you plan to use the [online Chrome devtools](http://www.webpagetest.org/chrome/timeline.php) provided by webpagetest.org, type in `no`

(note: newer Chrome devtools’ timeline use tracing log instead of timeline log)

When it’s done, you will find your benchmark log file with date mark.

examples: `benchmarkLog2015-04-07/16_36_20.json`  or  `benchmarkLog_oldFormat2015-04-07/16_42_33.json`

To view your benchmark log, open Chrome devtools, click on Timeline, right click anywhere, select `Load Timeline Data…`
