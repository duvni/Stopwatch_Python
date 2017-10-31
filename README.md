# Stopwatch
A Stopwatch instance can measure elapsed time for one interval, or the total of elapsed time across multiple intervals. In a typical Stopwatch scenario, you call the start method, then eventually call the stop method, and then you check elapsed time using the elapsed property.

A Stopwatch instance is either running or stopped; use is_running to determine the current state of a Stopwatch. Use start to begin measuring elapsed time; use stop to stop measuring elapsed time. Query the elapsed time value through the properties elapsed or elapsed_milliseconds. You can query the elapsed time properties while the instance is running or stopped. The elapsed time properties steadily increase while the Stopwatch is running; they remain constant when the instance is stopped.

By default, the elapsed time value of a Stopwatch instance equals the total of all measured time intervals. Each call to Start begins counting at the cumulative elapsed time; each call to Stop ends the current interval measurement and freezes the cumulative elapsed time value. Use the reset method to clear the cumulative elapsed time in an existing Stopwatch instance.
