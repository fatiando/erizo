Erizo
=====

    Elastic multi-component interpolation of ground displacement

`Documentation <https://www.fatiando.org/erizo>`__ |
`Documentation (dev version) <https://www.fatiando.org/erizo/dev>`__ |
`Contact <http://contact.fatiando.org>`__ |
Part of the `Fatiando a Terra <https://www.fatiando.org>`__ project

.. image:: http://img.shields.io/pypi/v/erizo.svg?style=flat-square
    :alt: Latest version on PyPI
    :target: https://pypi.python.org/pypi/erizo
.. image:: http://img.shields.io/travis/fatiando/erizo/master.svg?style=flat-square&label=TravisCI
    :alt: TravisCI build status
    :target: https://travis-ci.org/fatiando/erizo
.. image:: https://img.shields.io/codecov/c/github/fatiando/erizo/master.svg?style=flat-square
    :alt: Test coverage status
    :target: https://codecov.io/gh/fatiando/erizo
.. image:: https://img.shields.io/pypi/pyversions/erizo.svg?style=flat-square
    :alt: Compatible Python versions.
    :target: https://pypi.python.org/pypi/erizo
.. image:: https://img.shields.io/badge/doi-10.5281%2Fzenodo.3530780-blue.svg?style=flat-square
    :alt: Digital Object Identifier
    :target: https://doi.org/10.5281/zenodo.3530780


.. placeholder-for-doc-index


Disclaimer
----------

🚨 **This package is in early stages of design and implementation.** 🚨

We welcome any feedback and ideas!
Let us know by submitting
`issues on Github <https://github.com/fatiando/erizo/issues>`__
or send us a message on our
`Slack chatroom <http://contact.fatiando.org>`__.


About
-----

Erizo is a Python package for interpolation (*gridding*) of multi-component
ground displacement measurements (from GPS/GNSS or InSAR, for example).
It uses an elastic Green's functions approach for interpolation based on
[Verde](https://www.fatiando.org/verde).


Project goals
-------------

* 2- and 3-component velocity/displacement interpolation.
* Use simple elastic Green's functions.
* Include cross-validated versions of all interpolators.
* Provide an interface similar to scikit-learn for machine learning style
  interpolation.


Contacting Us
-------------

* Most discussion happens `on Github <https://github.com/fatiando/erizo>`__.
  Feel free to `open an issue
  <https://github.com/fatiando/erizo/issues/new>`__ or comment
  on any open issue or pull request.
* We have `chat room on Slack <http://contact.fatiando.org>`__
  where you can ask questions and leave comments.


Contributing
------------

Code of conduct
+++++++++++++++

Please note that this project is released with a
`Contributor Code of Conduct <https://github.com/fatiando/erizo/blob/master/CODE_OF_CONDUCT.md>`__.
By participating in this project you agree to abide by its terms.

Contributing Guidelines
+++++++++++++++++++++++

Please read our
`Contributing Guide <https://github.com/fatiando/erizo/blob/master/CONTRIBUTING.md>`__
to see how you can help and give feedback.

Imposter syndrome disclaimer
++++++++++++++++++++++++++++

**We want your help.** No, really.

There may be a little voice inside your head that is telling you that you're
not ready to be an open source contributor; that your skills aren't nearly good
enough to contribute.
What could you possibly offer?

We assure you that the little voice in your head is wrong.

**Being a contributor doesn't just mean writing code**.
Equality important contributions include:
writing or proof-reading documentation, suggesting or implementing tests, or
even giving feedback about the project (including giving feedback about the
contribution process).
If you're coming to the project with fresh eyes, you might see the errors and
assumptions that seasoned contributors have glossed over.
If you can write any code at all, you can contribute code to open source.
We are constantly trying out new skills, making mistakes, and learning from
those mistakes.
That's how we all improve and we are happy to help others learn.

*This disclaimer was adapted from the*
`MetPy project <https://github.com/Unidata/MetPy>`__.


License
-------

This is free software: you can redistribute it and/or modify it under the terms
of the **BSD 3-clause License**. A copy of this license is provided in
`LICENSE.txt <https://github.com/fatiando/erizo/blob/master/LICENSE.txt>`__.


Documentation for other versions
--------------------------------

* `Development <http://www.fatiando.org/erizo/dev>`__ (reflects the *master* branch on
  Github)
* `Latest release <http://www.fatiando.org/erizo/latest>`__
* `v0.0.1 <http://www.fatiando.org/erizo/v0.0.1>`__
