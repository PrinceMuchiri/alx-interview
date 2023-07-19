<<<<<<< HEAD
Log Parsing
Script that reads stdin line by line and computes metrics for each log entry depending on the follwowing conditions:-

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning
Total file size: File size: <total size>
where is the sum of all previous <file size> (see input format above)
Number of lines by status code
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
=======
# Log Parsing

This project contains interview coding challenges.

```bash
touch 0-stats.py
chmod +x 0-stats.py
chmod +x 0-generator.py

# Lint.
pycodestyle 0-stats.py

# tests.
./0-generator.py | ./0-stats.py 
``
>>>>>>> e8795977d0c2981e8df559756d5c54a1966a7ed3
