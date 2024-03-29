TECHNICAL CHALLENGE SENIOR PYTHON ENGINEER
==========================================

.. contents::

Python Tech Challenge
+++++++++++++++++++++

- The challenge is to create a program that computes some
  basic statistics on a collection of small positive integers. You
  can assume all values will be less than 1,000.

- Implement this challenge in whatever programming language
  best highlights your skills. Also, please supply a README with
  details on how to setup and run your application.

Requirements
------------

The DataCapture object accepts numbers and returns an object for querying
statistics about the inputs. Specifically, the returned object supports
querying how many numbers in the collection are less than a value, greater
than a value, or within a range.

Here’s the program skeleton in Python to explain the structure:

.. code-block:: python
   :linenos:
   :emphasize-lines: 1,7-10

  capture = DataCapture()
  capture.add(3)
  capture.add(9)
  capture.add(3)
  capture.add(4)
  capture.add(6)
  stats = capture.build_stats()
  stats.less(4) # should return 2 (only two values 3, 3 are less than 4)
  stats.between(3, 6) # should return 4 (3, 3, 4 and 6 are between 3 and 6)
  stats.greater(4) # should return 2 (6 and 9 are the only two values greater than 4)

Challenge conditions:
---------------------

- You cannot import a library that solves it instantly

- The methods add(), less(), greater(), and between() should have constant time O(1)

- The method build_stats() can be at most linear O(n)

- Apply the best practices you know

- Share a public repository with your project

**PLEASE FOLLOW THE INSTRUCTIONS**

- Technical challenge should be completed within the next 3 days.
- Tests must be included in the submission.
- Do not split error input validation between the command line code and the
  class methods, this is not something considered as a best practice.
- Do not create a driver script via the command line, it is not necessary, we
  are only seeking working classes and tests, as we can run the program via the
  Python replication.
- Use Python 3.6 or higher
- Use typing
- Optimize python structures, for example, use list comprehension if applicable.
- Please apply any best practice you think will add value, but do not add extra
  feature than the requested.
- Please upload the solution to a repository and share the link to
  recruiting_CO@teaminternational.com

- If you have questions or inconveniences to complete the test, don’t hesitate
  to ask your recruiter.

How to run
----------

.. code:: bash

  python3 tests.py