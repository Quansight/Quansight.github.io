---
layout: post
title: Episode 8 - SciPy - Open Source Directions
---

<iframe width="560" height="315" src="https://www.youtube.com/watch?v=t0r6KJwsCBg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Introductions

Welcome to Open Source Directions, the webinar that informs you about the future of open source projects.
This episode, the project being highlighted is [SciPy](https://www.scipy.org/)

* **Host:** Anthony Scopatz
* **Co-Host:** David Charboneau
* **Guest:** Ralf Gommers, is a data scientist in the forestry industry, working for FPInnovations in Canada and Scion in New Zealand and is currently based in Vancouver.

### Project Overview

The SciPy library is one of the core packages that make up modern scientific computing in Python. It provides many user-friendly and efficient numerical routines for numerical integration and optimization. It has about 5 thousand stars on GitHub, and almost 700 contributors. SciPy currently has about 2.6 million downloads from anaconda.org alone.  This has been a very popular project for decades now.

This project started back when there was just Python, and there was not an array object.  At this time there were many people using Python for science, but there was not much there.  To address this situation, SciPy started in 2001 with a simple goal: to produce a library of fundamental algorithms needed for scientific computing.

SciPy kind of functions like the standard library for scientific computing. It is maybe a little like the Boost C++ of Python.  Unlike the case with the Python stdlib, code doesn’t go to SciPy to die!

For some parts of SciPy there are alternatives. Although they’re more complementary in many cases: scikit-image builds on top of and goes far beyond scipy.ndimage, which is the same for statsmodels and scipy.stats, and Scikit-learn for scipy.cluster. For other parts, like special functions and linear algebra, there are not as yet any real alternatives.  

There is a long list of technology that SciPy is built on.  To start with there are five languages that it uses: Python, Cython, C, C++, and Fortran.  Having this many languages can get harry and cause problems, but it seems to be worth it.  As far as APIs go, there are some for Python, C, and Cython.  To make this work has required about 30-40 years of numeric algorithm development history.  For most of the Fortran libraries, it would be great to just have a C equivalent, but there really isn’t one.  

SciPy was started by three people: Travis Oliphant, Eric Jones, and Pearu Peterson.  Recently they have taken a hands-off approach, with Travis still working on the project up until about 2010.   There is now a large team which maintains this project.  At the moment there are about 120 contributors per release, and 36 people have commit rights, of which about roughly half are regularly active.

Because SciPy is at the core of the scientific Python and PyData ecosystem, there are users and contributors from many different disciplines, spanning most fields of science and most industries. The SciPy community is an affiliate member of NumFOCUS, and great efforts are made to follow the NumFOCUS diversity activities closely. The contributors try to follow best practices and participate where they can. A lot of effort was spent on the Code of Conduct last year, and people seem to be pretty happy with how that turned out. That said, while the user and contributor base is quite diverse, the makeup of the maintainer team is not as diverse as is desired. One area that is a target of improvement is gender diversity, only 2 of the 36 people with commit rights are female, and they’re not active currently.


### Demo

[brief overview of the docs, showing what submodules exist](http://scipy.github.io/devdocs/)
[robust regression with `least_squares’](https://scipy-cookbook.readthedocs.io/items/robust_regression.html)
[`solve_ivp` with Lotka-Volterra](https://github.com/rgommers/scipy/blob/webinar/doc/SciPy_webinar_material.ipynb)
[use `shgo` and `dual_annealing` on hard problem](https://github.com/rgommers/scipy/blob/webinar/doc/SciPy_webinar_material.ipynb)

### Roadmap

You can view the current roadmap [here](https://www.quansight.com/projects)

1. **Evolve BLAS and LAPACK support:**  This is probably one of the most important features that SciPy provides because this enables work with linear algebra.  There are many other libraries that use SciPy’s BLAS and LAPACK interfaces, and for this reason, this has become the top priority on the roadmap.  When making a comparison, NumPy provides a small subset of what SciPy provides.  In addition to this, SciPy utitlizes Fortran, whereas NumPy cannot, however, if you have a precompiled binary then it can use that and you will find similar performance.


2. **Sparse arrays:**  Sparse arrays are basically arrays with mostly zeros.  Trying to store all of those zeros can be cumbersome, so there are specific data storage formats that create a compact representation.  SciPy has always had sparse matricies that act like NumPy.matrix, this is something that people should not be using anymore so the hope is to get rid of them.  To replace this, there is a new project called PyData/Sparse which would be an in-development replacement.  This project still needs a couple of storage formats, but once that is done, then it would be adopted in SciPy.  SciPy also has two other modules that are dependent upon sparse matricies, sparse.csgraph (graph algorythims) and sparse.linalg (linear algorythims for sparse data structures).  At the end of this, the sparse matricies won’t go away because they are widely used but an effort will also be made to direct people to use arrays. This is an area in which it is very clear what needs to be done and is, therefore, a great area for people to contribute time or finances to get this done.  The main format that PyData/Sparse would need to impliment would be a compressed storage format, and this is still missing.


3. **Fourier transforms:**  These have been in Scipy since the beginning.  This is written in Fortran and is hard to understand code.  In its current state, it works if you just want a regular fourier transform, but it is not optimized for performance.  At the moment if you were to try and process an array which has the length of a prime number then it would take forever to find you an answer.  There are algorithms out there which can help with this, but SciPy just does not have them.  There is a new library called Pocket FFT, the author of which just opened a pull request to add it to NumPy, and part of FFT is duplicated between NumPy and SciPy, so the hope is to add that to SciPy.  This would not only resolve the prime number issue but would also improve accuracy.  After that, the only thing left to do would be to implement the back-end system.  Right now there are numberous other libraries which provide Fourier transforms but trying to integrate those would likely cause many bugs.


4. **Support for distributed arrays and GPU arrays:**  This is actually;y really new, and there has not been anything like this on the roadmap so far.  SciPy itself is not requiring distributed arrays or GPU arrays because it is not designed to take code which does this, but NumPy is splitting their API from execution area.  What will happen very soon is that someone can wite a function just using NumPy array interfaces and then you take a GPU array like CuPy, then the SciPy functions will look the same and they will try to use it.  When this happens, it might work, but this is kind of an unkown so the question is about the extent to which this will work.  Not all of SciPy will be eligible for distributed execution, but some parts are.  This is an effort which will require a lot of support and many hands to contribute before sufficient progress is made.



5. **Improve benchmark system:**  There is currently a benchmark system, and it works pretty well, but it is not easy to use.  It is not user friendly, and it can take days to run, so an overhaul to this would be beneficial to the community in general.  The thought is that once this is done, then it will be just that much easier for people to become contributers.  If there had been a roadmap back in 2010, it is likely that this would have been the first item on it.  


### Viewer Questions

**Q.** I have experimental data to which I am trying to fit a curve using UnivariateSpline function in scipy.  I was wondering what other curve fitting options scipy might have? I am relatively new to scipy.

**A.**  So this is spread over quite a few modules.  scipy.optimize has many functions for regression (e.g. curve_fit, least_squares, minimize). scipy.odr for orthogonal distance regression. scipy.stats for fitting distributions, and linear regression.

---

**Q.** Can the solvers in SciPy deal with complex values (i.e x=x'+i*x")? I am specifically interested in using a Nelder-Mead type minimization function.

**A.**   Not directly. It’s not a well-defined problem though - do you want to compare magnitudes, angles, or some other metrics? If you map your complex number to a single float, then you can feed that into any optimization function.

---

**Q.** I think SciPy has been traditionally targeted at solving engineering problems. With the rising of ML and AI, did you see people trying to use SciPy within TensorFlow, PyTorch, etc.?

**A.**  At the moment I think I see it used in ML workflows quite a lot.  It is, however, mainly for utility things like resizing images etc.  If you want to write a neural network, then all the images need to be the same size then this would be useful.  It is not often utilized in the parts for things like PyTorch or Tensorflow that do the heavy lifting, because those would normally be handled on GPUs.  We would be very interested to see the compatibility with GPU arrays in SciPy work with this.  

---

**Q.** What fraction of Scipy functions can use multiple CPU cores? Is OpenMP used for that or some other technology?

**A.**  There are not that many functions, although, everything that uses linear algebra (linear algebra libraries) split things under the hood and use all the cores that are available.  There are some functions like the KDTree function in scipy.spacial and differential evolution optimizer which allows you to explicitly allocate the number of cores to use.  At the moment this just uses multiprocessing, but I think we want to switch to Joblib or something like that.

---

**Q.** You mentioned distributed SciPy. We have seen Dask integration in several libraries (numpy, scikit-learn, xarray...). Would a Dask-SciPy make sense?

**A.**  Yes and no.  With what we were talking about in the Sparse and distributed arrays, using CuPy as an example, Dask would be great for the distributed arrays.  I think that there would be a lot more of SciPy that should work distributed than should work on GPUs.  That would definitely be a focus, but a specific project that would be Dask - SciPy, sounds like it would require rewriting some of the original project.  We are specifically trying to avoid doing this partially because of the whole thing with the Python interface.  The goal is to able to feed in things like Dask array and it will act like a NumPy array, then things should just work.  I hope we won’t see a separate project like this.

---

**Q.** Are there any plans for a Scipy 2.0? Or will it likely be 1.x and backward compatible in the next years?

**A.**  We spent 16 or 17 years getting to 1.0, so we are not yet thinking about 2.0.  This does not, however, mean that we will maintain strict backwards compatability for absolutely everything.  The philosiphy of SciPy, NumPy, and most of the Python ecosystem is to gradually evolve.  We keep deprecating things and then leave it in for a few releases, while we show users warnings, and then we give them advice on how to switch.  If we want to do a 2.0, then maybe we will but maybe it is for marketing reasons.  It won’t be the same thing as Python 2 to Python 3 where all of a sudden we kept a lot of things unchanged for a long time and then all of a sudden in SciPy 2.0 we change everything.  

### Footnotes & Links

* User Introduction [here](https://www.scipy.org/getting-started.html)
* [SciPy Website](https://www.scipy.org/)
* [GitHub page](https://github.com/scipy/scipy)
* [Email Ralf](ralf.gommers@gmail.com)
