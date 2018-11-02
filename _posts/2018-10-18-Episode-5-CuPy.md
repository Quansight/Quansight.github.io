---
layout: post
title: Episode 5 - CuPy - Open Source Directions
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZaKhosJ4IBY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Introductions

Welcome to Open Source Directions, the webinar that informs you about the future of open source projects.
This episode, the project being highlighted is [CuPy](https://cupy.chainer.org/)

* **Host:** Anthony Scopatz
* **Co-Host:** Tony Fast
* **Guest:** Crissman Loomis, an engineer for the CuPy and Chainer teams at Preferred Networks and currently based in Japan

### Project Overview

CuPy is an open-source matrix library accelerated with NVIDIA CUDA. CuPy's interface is highly compatible with NumPy; in most cases, it can be used as a drop-in replacement. CuPY has ~2300 stars on GitHub, and according to PyPi over 40,000 downloads last month.

CuPy actually wasn't started as its own project. CuPy was originally written as the back end for Chainer, the Python AI framework. Around version 2 of Chainer, the team realized that separating the NumPy-syntax GPU backend from the rest of Chainer could allow more people to do GPU calculations, and the independent CuPy project was born.

As far as alternative projects go, other Python projects have wanted to use GPUs to speed up their calculations and have implemented partial versions of NumPy. PyCUDA allows calculation on the NVIDIA GPUs from Python programs but doesn't use NumPy syntax. MinPy started using NumPy syntax but has since been merged into MXNet Gluon, and the MinPy GitHub repo is now deprecated.  At this point, CuPy is really unique and has a distinctive edge at the moment because nothing is able to give the same level of functionality.

CuPy works with Nvidia's CUDA library to allow calculations on NVIDIA's GPUs.  This being the case, Nvidia has a strong lead as far as the libraries they provide for it.

Chainer was originally started by a separate person on the staff, and he worked on PyCUDA at the time. CuPy was then written by Ryosuke Okuta-san, who is now an executive at Preferred Networks.  While Ryosuke is still with Preferred Networks and spends late nights working on it, CuPy is now maintained by the staff at Preferred Networks, along with the maintenance of Chainer.  About half of the users who are helping to guide development are working on the Chainer framework, but it really was for the best that it was made into a separate project.  As it turns out, there are now twice as many downloads for CuPy as there are for Chainer.  There are data scientists, university people, and data analysts from large companies helping to contribute to the development.

### Demo

[Using Chainer on Colab](https://colab.research.google.com/drive/1jteww_qxlBDesALtdr1bwqTjC-GdXBM0)

Get started with CuPy [here](http://www.PyViz.org).


### Roadmap

If you would like to help contribute to this project, see the guide [here](https://docs-cupy.chainer.org/en/stable/contribution.html)

1. **Vision for CuPy:**  First, CuPy should be the go-to library for people doing data science on GPUs, but currently it only works with Nvidia GPUs. Longer term, the abilities of CuPy should be expanded so that it is able to work more than just as a Python interface for Nvidia CUDA.  Ultimately the idea is for it to be able to act as a computation unification library for Python, that you can use for Nvidia chips or AMD chips or integrated graphics chips.SciPy usage on GPUs is also on the horizon for future functionalities.

2. **Current users and future users:**  The largest group of users is the Chainer users. After that, we have data scientists that use CuPy to speed up their calculations. And then there are other projects, which are using CuPy as a backend to allow the projects to use GPUs when available, like Pomegranate, a probabilistic modeling library, or spaCy, a natural language processing toolkit.  Primary users are still going to be those who use neural networks about 50% or so.  The hope is that over time others will utilize CuPy for their projects so that they do not need to create their own GPU interface.

3. **Collaborations to form with the industry:**  Work is currently being done to integrate CuPy with other toolkits like Numba for JIT compilation and Dask for scaling and parallelization. More integrations like these are always welcome, and this is a great opportunity for community members to get involved with the development.

4. **Increasing usage in other domains:**  There seem to be many areas where CuPy is not really well known yet.  Currently, the neural net users are aware, but having more data scientists or people in finance with large data sets is desired.  The more large dataset users utilize CuPy, the better we can standardize the industry syntax for working with CPUs/GPUs.

### Viewer Questions

**Q.** That 6x speedup benchmark includes data transfer to the GPU right? For a more complex algorithm that one-time data transfer should be less important, so bigger speedups would be expected right?

**A.**  So the more that you can keep the calculation of the GPU, the more you can get out of it.  The two elements at play here are the size of the matrix and the number of operations you do on the matrix.  The expensive piece is data-locality.

---

**Q.** I'd be very interested to see how much of SciPy will work out of the box once CuPy has __array_ufunc__ and __array_function__, and what the main bottlenecks are (that we could possibly remove in SciPy). any guesses right now?

**A.**   The ufunc is something that we are looking forward to we have been taking a look at this already.  Travis from Quansight has been looking at this and would like to implement greater synergy by implementing the ufunc.  Longer term we want to get to the point where all of the matrix formats are shared between all of the calculation areas.  This would free up the programmer from having to do transitions to difforent calculation areas.  The bottlenecks are not apparent right now, but that is something that we will have to get into as we implement ufunc.

---

**Q.** Does CuPy work with dask delayed interface?

**A.**  I am not sure about the full compatibility with Dask yet, but we’ve been working with them on that.  This would be a great thing to have an issue or a pull request for.

### Footnotes & Links


* Find Crissman on Twitter here: crissman@preferred.jp
* [CuPy Website](https://docs-cupy.chainer.org/en/stable/index.html)
* [GitHub page](https://github.com/cupy/cupy)
