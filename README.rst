The pytest TODO plugin
======================

Marking unfinished source code or known problems with a *TODO* comment is a
popular method among developers. During development this is an acceptable,
lightweight option. In a release version however *TODO* comments leave a bitter
taste at best or mean a forgotten major issue at worst.

This plugin parses Python source files for *TODO* comments and marks them as a
failed test.

Usage

.. code-block:: bash

    ~$ pytest --todo

Possible Usage
--------------

During development the CI server simply runs the unit tests against the code,
checking if the tests pass. At this stage *TODO* comments are allowed. Once a
release candidate exists (maybe on a release branch) the CI server will also
add the *--todo* flag. Forgotten *TODO* comments will now cause the tests to
fail and a possible source of bugs is cleared out before the release happens.
