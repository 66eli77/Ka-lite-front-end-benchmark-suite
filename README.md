# Ka-lite-front-end-benchmark-suite
-Description:

For better guiding the front-end optimization and development in general, we need an automated front-end benchmark suite that reports metrics about the Javascript performance of our platform.

There are some desired characteristics we want this benchmark suite to have.
Be able to run the benchmark in a standard configurable environment.
Be able to run a benchmark on a base sample(it could be a page from kalite master branch), then run a benchmark on a target sample(it could be a page from kalite develop branch), and compare the target benchmark against the base benchmark.
Be able to tell the DOM manipulation(number of DOM nodes, time to construct the DOM tree, time to render the DOM to viewport).
Be able to tell the total memory usage.
Be able to isolate javascript objects or monitor targeting objects.

-Challenges we are facing:
Research on potential useful tools, we want to avoid reinventing the wheel
Usually, sequential actions define user experience, how to benchmark the sequential actions and extract meaningful metrics.
Make the benchmark suite lightweight and easy to use, so that many of our new hands at the front-end are able to incorporate it into their workflow and use it as guideline, which hopefully will lead to snappy user interface.

-Solutionis:

Use Selenium Webdriver to define the benchmark actions(browser behaviors) and use Chrome debugger protocol via remote debugging mode to call Chrome profiler to profile the benchmark actions. We also need another layer to perform some filtering or calculation in order to extract meaningful info.
