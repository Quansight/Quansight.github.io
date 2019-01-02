---
layout: post
title: Episode 10 - PyData/Sparce - Open Source Directions
---

<iframe width="560" height="315" src="https://www.youtube.com/watch?v=AtVZX9EPZmM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Introductions

Welcome to Open Source Directions, the webinar that informs you about the future of open source projects.
This episode, the project being highlighted is [PyData/Sparse](https://sparse.pydata.org/en/latest/#)

* **Host:** Anthony Scopatz
* **Co-Host:** David Charboneau
* **Guest:** Hameer Abbasi, is a scientific software developer at Quansight and lead developer of PyData/Sparse, and is based in Frankfurt, Germany.

### Project Overview

PyData/Sparse is a project that aims to provide ndarray-compatible containers for storing sparse arrays, and implementing NumPy methods that act on those containers.  It currently has 169 stars on Github, and about 5k downloads on conda-forge.  

The project sort of began with Matt Rocklin working on this idea in his off time while working at Anaconda.  The project was just coming together at the time when Hameer hopped on board because of his interest in the tensor factorization.  He found that there was an easy way to do multidimensional sparse arrays in Matlab, but not in Python, as a result, he decided to join this project as it seemed most promising.

Currently, in the PyData ecosystem, there are not many sparse containers available.  SciPy.Sparse is the most complete at the moment, but it is limited because it goes with the NumPy.Matrix interface instead of the NumPy.NDArray interface.  PySparse would be the other option, however, both of these are limited to supporting 2-dimensional containers, furthermore, neither option is able to comply with the NDArray API.  The out of the box offer from PyData/Sparse is that it is compatible with NDArray right out of the box.  The hope is that eventually, this project can become a viable alternative to SciPy.Sparse and that NumPy.Matrix will be deprecated.  In the Python ecosystem, there really is no other project which aims to do what PyData/Sparse will do.  

Currently, PyData/Sparse is built on top of NumPy and Numba.  NumPy is used in certain areas where it seems appropriate, but in areas where speed is essential, Numba is used.  Until recently the project relied on SciPy, and while it is still a dependency none of the major algorithms utilize it.  Numba is used here on a low level which means that it is mostly under the hood and users are not required to know it.  It is similar to the way that NumPy uses Scython, or any other library would wrap low-level libraries.

In addition to the work by Hameer and Matt, Ralf Gommers has also contributed ideas and direction to the project development.  Some other contributors have assisted in putting this project together; Alex Williams, an unnamed GitHub contributor from China, and a number of other off and on contributors.  Hameer remains the main consistent presence in the project.

Most of the user base seems to come from academic institutions, but the first major library integration was actually made recently with TensorLy.  At this point, these two groups make up most of the PyData/Sparse user base.  Eventually it would be nice to expand the community diversity, however, the project is not quite big enough to have a formal organization yet, but more contributors would be welcomed.

### Demo

Colab Notebook](https://drive.google.com/open?id=1a-yh308HGw2fFLFpvG0k9qAn0pfeb-kx)
[Demo at timestamp 9:24](https://youtu.be/AtVZX9EPZmM)
[Github Repository](https://github.com/pydata/sparse)
[Construct Sparse Arrays](https://sparse.pydata.org/en/latest/construct.html)

### Roadmap

You can view the current roadmap [here](https://www.quansight.com/projects)

1. **More storage formats:**  SciPy has this format called compressed sparse column and compressed sparse row format.  The good thing about both of these formats is that they take up less space than COO in most situations, but the hope is to add generalization of this called compressed sparse fibers or CSF.  This would be more than just a memory characterization because CSC and CSR can be passed into and out of many existing libraries to perform operations.  The problem is that currently, it would need to rely on SciPy’s machinery to convert it to CSR or CSC and then pass them in.  With the goal being to get rid of SciPy.Sparse at some point, this current method is counterproductive.  Creating this new format would allow for zero overhead when passing into these libraries or getting data out of these libraries. Ultimately it would become more of a catalyst to adding future functionalities. 

2. **Better performance/algorithms:**  To put COO in an order that most algorithms expect the coordinates need to be sorted to be C contiguous just as they would in NumPy.  Currently, they use a quick sort in NumPy to do this.  The hope here is to get a radix sort into NumPy so that it has an order of end sorts instead of order of end-log and sorts.  This would further speed up the algorithms in PyData/Sparse by perhaps as much as 2.5X.  Currently, the element-wise calculations are also looped, which is not an optimal way to do it, but at the time that this was written, there was no dependency on Numba.  Let’s say you have three inputs into a function, it will check whether each of these individual functions is zero or something else, and it iterates that eight times.  If it could be optimized so that it looped through the coordinates once then that would be quite a bit faster.  A new pull request has been opened with NumPy to update the radix sort, so this is kind of a step forward in making this item move forward.

3. **Covering more of the NumPy API:**  There are quite a few parts of the API to address.  The most important here would be BLAS support.  The next most important step would not so much be changing the core functionality, but making it easier to access the existing functionality.  Right now if you are doing something like NumPy.dot and pass that through sparse arrays, then that will not work because it would try to make NumPy convert the sparse array into a NumPy array.  There is an array protocol function which will be in NumPy 1.16 in graph form and probably 1.17 in final form, and once this is in place then this issue should be resolved.  The end user will no longer need to worry about what they are passing in, and it should just be able to do the right thing most of the time.

4. **SciPy Integration:**  The most important point here is that SciPy’s most recent linear algebra routines in the sparse submodule and their CS graph submodule use SciPy.sparse internally.  With NumPy.matrix trying to get rid of SciPy.sparse, this has become a blocker.  The goal would be to get PyData/Sparse to work with these subroutines so that you do not need to care about whether it is a SciPy.sparse array being passed in or a PyData/Sparse array being passed in because they should both natively work correctly.  This is more along the lines of replacing SciPy.sparse internally within SciPy.  

5. **Dask integration for high scalability:**  Since this project was started by Matt Rocklin, and he was the mind behind Dask, it already has some Dask integration.  You can already use PyData/Sparse with Dask to use sparse arrays across clusters.  The one downside to this is that it is not as complete as they would like.  One thing that would help is bringing more sparse array features to Dask.  This way the user could take the sparse arrays, which allow for big data and take them to clusters, which allow for even bigger data.  

6. **CuPy integration for GPU-acceleration:**  One goal is to make sparse arrays faster generally speaking.  CuPy could help with this goal by utilizing things like the Cuda routines used with sparse BLAS.  The potential is for CuPy to wrap those existing routines.  The big blocker right now is that Numba is being used “under the hood” to perform some of the calculations, and Numba does not yet work with CuPy.  This would be great to have, but there would be a lot of work to do here and community support will be essential on this.  

7. **Maintenance and General Improvements:**  Specifically one of the items here would be overhauling the test infrastructure.  With all the formats that are being added, there will need to be individualized tests for each one.  Ensuring the correct outputs for given inputs will be essential when testing these new format integrations, and that is just not something that can be done with the current test suite.  


### Viewer Questions

**Q.** Does sparse support solving A x = b where A is sparse array?

**A.**  Okay, so they call out of NumPy.solve, essentially.   Currently, no but that is something we would like to have.  After discussions, we’ve decided that this is the kind of functionality that should go into SciPy rather than PyData/Sparse.  We put basic algorithms in PyData/Sparse and the linear algebra, BLAS, graph-theoretic, or other algorithms will hopefully go into SciPy.  The biggest blocker to getting this into SciPy at the moment is having the finished CSF format, which is something we could use a lot of help with.  

---

**Q.** How are you feeling about the dependency on Numba now after 6 months (or more?) of experience with it?

**A.** I would say that it’s not been too hard to work with compared to Cython.  There are different things to be considered right, right now in Python we have what is called the no-arch package which means that we have just one tarball for all architectures and it works right out of the box.  Numba is what enables us to have that.  If we had something else to do, we would have to build the wheels for every single architecture and probably a lot of different NumPy versions and that would complicate things quite a bit.  Another thing to consider is that we are working within Python, and Numba is very easy to work with.  When I made the decision to defend it Matt Rocklin was pushing quite hard in the discussions, but I have not regretted that decision.  The Numba devs have been quite good and they had those in within a month or two, so after that, I did not feel the need. One thing we could use with Numba is more support for object-oriented programming.  Currently, you can only do functions of some sort, but once you pass the data back to Python it’s no longer “optimized” so to speak.  Numba is a way for us to get around some packaging issues, and we found that in most cases it was even faster than Scython. 

### Footnotes & Links

* Roadmap [here](https://docs.wixstatic.com/ugd/095d2c_ac81d19db47047c79a55da7a6c31cf66.pdf)
* [PyData/Sparce Website](https://sparse.pydata.org/en/latest/index.html)
* [GitHub page](https://github.com/pydata/sparse)
* [Gitter page](https://gitter.im/pydata/sparse)
