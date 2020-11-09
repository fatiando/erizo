.. _install:

Installing
==========

Which Python?
-------------

You'll need **Python 3.6 or greater**.

We recommend using the
`Anaconda Python distribution <https://www.anaconda.com/download>`__
to ensure you have all dependencies installed and the ``conda`` package manager
available.
Installing Anaconda does not require administrative rights to your computer and
doesn't interfere with any other Python installations in your system.


Dependencies
------------

* `numpy <http://www.numpy.org/>`__
* `numba <https://numba.pydata.org/>`__
* `scikit-learn <http://scikit-learn.org/>`__
* `verde <https://www.fatiando.org/verde/>`__
* `pooch <https://www.fatiando.org/pooch/>`__

Most of the examples in the :ref:`gallery` and :ref:`tutorials` also use:

* `matplotlib <https://matplotlib.org/>`__
* `cartopy <https://scitools.org.uk/cartopy/>`__ for plotting maps
* `pyproj <https://jswhit.github.io/pyproj/>`__ for cartographic projections


Installing the latest development version
-----------------------------------------

You can use ``pip`` to install the latest source from Github::

    pip install https://github.com/fatiando/erizo/archive/master.zip

Alternatively, you can clone the git repository locally and install from there::

    git clone https://github.com/fatiando/erizo.git
    cd erizo
    pip install .


Testing your install
--------------------

We ship a full test suite with the package.
To run the tests, you'll need to install some extra dependencies first:

* `pytest <https://docs.pytest.org/>`__

After that, you can test your installation by running the following inside a Python
interpreter::

    import erizo
    erizo.test()
