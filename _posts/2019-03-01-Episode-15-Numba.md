---
layout: post
title: Episode 15 - Numba - Open Source Directions
author: bsodenkamp
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/LmlJcZYpAi0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Introductions

Welcome to Open Source Directions, the webinar that informs you about the future of open source projects.
This episode, the project being highlighted is [Numba](http://numba.pydata.org/)

* **Host:** Anthony Scopatz
* **Co-Host:** Carol Willing
* **Guest:** Stan Seibert: has worked for Anaconda, and is a developer on the Numba project.

### Project Overview

Numba is a collection of just-in-time compilers for numerical Python.  Numba translates Python functions "on-the-fly" into high-performance machine code without a separate compilation step, it also does not require you to have a C compiler available.  It supports a wide range of chips (both CPUs and GPUs), and can achieve speedups between 2x and 200x, depending. Numba is a project that has been around for many years, holding 3833 stars on Github and about 625k downloads/month across PyPI and conda as of February 2019.

Numba was created to make it easier for Python developers to take advantage of all the amazing new hardware that is coming out every day. People have access to CPUs with lots of cores, SIMD vector instructions, and massively parallel GPUs, but it is challenging to take advantage of these capabilities without switching languages. Numba lets you write a subset of Python that can be automatically translated directly into machine code that runs nearly as fast as FORTRAN (the gold standard for high-performance computing). Numba provides a collection of compilers for the CPU, compilers for GPUs, and some specialized compilers that can automatically parallelize NumPy-like `ufuncs` to run on the CPU and/or the GPU. The goal is to put another tool in the Python application and library author’s toolbox that lets them stay in Python but make really fast code.

The space of Python compiler projects is quite crowded because it is such a hard problem, with many tradeoffs. The main bifurcation point for Python compilers is whether you operate within the standard Python interpreter (often called "CPython" because it is written in C), or do you replace the entire interpreter with one that is more suited to compilation.  Examples of the first category (which includes Numba) are projects like Cython, which translates an expanded dialect of Python with type annotations into C code for ahead-of-time compilation. Pythran and Theano also do translation of numerical Python to C++ for compilation. Projects like numexpr and parts of deep learning frameworks like TensorFlow and PyTorch can also be seen as very focused JIT compilers for array expressions.  In the other category are projects like PyPy, which is a Python interpreter plus a tracing JIT that functions a little more like the Javascript interpreter in your web browser. (PyPy is much more interesting than that description suggests, and is quite an amazing technical feat.)  Other projects that replace or modify the CPython interpreter include things like Nuitka and ShedSkin which statically translate whole Python applications into C++ (usually still relying on CPython for some things) as well as mostly dormant JITs like Pyston and Pyjion.  There are fewer overlaps in the GPU compiler space, but older projects like Copperhead and Theano had this capability, and the deep learning frameworks (which all run on GPUs) are getting more compiler-like capabilities over time.

Numba is built upon the LLVM compiler project. LLVM is a research project to create a modular compiler framework that has evolved to become one of the major open source compiler projects, comparable to GCC.  Apple uses it (clang, the C/C++ frontend for LLVM) as their reference compiler for both macOS and iOS, and also built their Swift language on it.  The great thing about LLVM is that it supports basically every relevant CPU in existence, and already implements many advanced compiler optimization passes that we don’t have to write.  As a result, Numba can focus on the problem of type inference and translating Python bytecode into the LLVM Intermediate Representation, and let LLVM handle the rest.  As a bonus, the GPU manufacturers have also based their compilers on LLVM as well, so Numba’s GPU compilers can share quite a bit of implementation with the CPU compiler.

Numba has had a bit of a complicated life.  Depending on how you count, the current Numba is the third incarnation of the code base.  The first version was created by Travis Oliphant in March 2012 and Jon Riehl joined shortly after that.  The next generation of the Numba code base was led by Mark Florisson with help from Siu Kwan Lam from 2012 until early 2014.  At that point, the commercial GPU compiler was open sourced and merged into the CPU compiler and Siu Kwan Lam became the lead developer on the project, which has continued to the present day.  Today, Numba has 5 core developers: Siu Kwan Lam, Stuart Archibald, and Stan from Anaconda along with Ehsan Totoni and Todd Anderson from Intel.  Lately, there has been an average of 8-10 non-core contributors during each 2-month development cycle.

Many people have adopted Numba for scientific research as well as quantitative finance applications.  One of the favorite projects that uses Numba is called librosa, which is a package for music and audio analysis.  In fact, librosa is used in the production of the Open Source Directions podcast. Over the years there have been other applications for Numba such as physics simulations and data analysis, economic modeling, adding fast string processing to Pandas (see fletcher), and various data analysis and visualization tools like UMAP. Intel has been working on HPAT, a "Pandas compiler", based on Numba as well.  Another Anaconda project, called Datashader, also uses Numba to accelerate rendering large datasets for display in a web browser.  Smaller communities have also begun to spring up around llvmlite, the Python bindings for the LLVM library.  This was an unexpected development, but there seems to be a group of people experimenting with compilers that like to use llvmlite as their interface to LLVM.  They are making special purpose compilers and other interesting tools.  Even with all this, there are still many use cases out there that the Numba team has not heard about yet!  It is always an adventure for them to hear new user stories when they go out and talk about Numba.

One area that is being worked on is how to make Numba more approachable for new users.  This sort of constitutes a step 0 to creating better onboarding materials for new Numba contributors.  The complexity of Numba’s internal implementation makes it hard to learn how it works, and there is some need to improve that.  A major rewrite has begun for the current developer docs, and they’ll be looking to test those materials over the coming months to see if they make Numba more approachable as they mentor new contributors. Just as a side note, some of the inspiration has come from a great SciPy 2016 Tutorial with Gil Forsyth & Lorena Barba you can find it on [YouTube here](https://www.youtube.com/watch?v=SzBi3xdEF2Y) or [Github here](https://github.com/barbagroup/numba_tutorial_scipy2016). 


### Demo

* [Demo at timestamp 18:53](https://youtu.be/LmlJcZYpAi0?t=1133)
* Numba interactive [Binder demo](https://mybinder.org/v2/gh/numba/numba-examples/master?filepath=notebooks)

### Roadmap Discussion

As the project has been able to achieve more of the key features for numerical code, like better SIMD instruction support, adding more hardware like POWER8, ARM and AMD GPUs, and the ParallelAccelerator optimization pass contributed by Intel, the focus has shifted toward more "quality of life" improvements that don’t necessary make your code faster, but make Numba easier to use and contribute to.  As of 2019 the roadmap is now included in the docs, and can be found [here](https://docs.wixstatic.com/ugd/cccccf_1ce271b9515c43b683ca3b62a7caf288.pdf).


In the short term some items of focus are; better error messages, more debugging options, a new approach to containers (list / dict), continue maturing string support, making disk caching more robust and work in more situations, the ability to distribute a partially populated cache to reduce startup time for users, clean up the internal implementations inside Numba (with over 5 years of development on this code base there are now better practices and more compact ways of doing things), need to go back and clean up old implementations that are needlessly verbose, add to code bloat, make it harder to contribute to Numba, and improve interop with C.


In the medium term some goals would be; finally cut the cord entangling the ufunc/gufunc compiler with NumPy so that all the different compiler decorators (namely `@jit`, `@vectorize`, and `@guvectorize`) produce the same kind of object, look at dispatch speed, review the needs for JIT classes and address those, stabilize caching and automatic parallelization so that it would be safe for users to turn them on everywhere, release Numba 1.0 with clearly documented stable interfaces, and having more code transformation passes that enable a broader range idiomatic Python to still be compiled to high performing machine code.


In the long term it would be nice to have; a clear extension mechanism for adding entirely new hardware targets such as new GPUs, “TPUs”, and possibly FPGAs, tackle cross-language interop with more challenging languages like C++, R, Julia, maybe Rust, hybrid computing by calling GPU and TPU functions from nopython mode on CPU, partial compilation of functions dispatched from nopython mode, and help key projects incorporate Numba as a dependency for generating high performing code.


### Viewer Questions

**Q.** There have been a lot of different array-like objects (e.g. TF, PyTorch), whereas Numba only supports NumPy. Are there plans to generalize the Numba code so it can take in any array object with ease?

**A.**  Yes, so Numba does technically support the buffer protocol, however, it does not get exercised much.  Because of this, there are likely usability issues but if any of those objects follow the buffer proticol then that would be a natural way for us to integrate with those.  It’s something we are definitely interested in because we have the ingredients already there.  If someone wanted to pick this up and tell us about what they tried and what didn’t work then that would be great.  On a related note, there is actually no buffer protocol for the GPU.  We basically copied the array interface from NumPy and put it into Numba, and we have a thing called the CUDA array interface which you can put on a Python object and it will tell Numba that the data is on the GPU and how to access it.  CuPy added that and Pytorch may have as well.  So, on the GPU side, we are also interested in interacting with other people’s arrays.  

---

**Q.** Does Numba work well with 3rd party libraries (e.g. Pandas, Keras,...)? Also, debug best practices?

**A.**  The short version is that Numba basically doesn't work with a third party library unless you have done some work to make your third-party, Numba compilable. Numba doesn't go and compile stuff for you, it requires you to opt-in and say, “hey this is a thing you should compile”.  We ship with Numba most of the implementations of NumPy as a result of this.  The nice thing about that is that you can write an entirely difforent project that could actually compile different things.  For example with Pandas, there is a project called Inkpad that Intel is working on which is basically a Pandas compiler built on top of Numba.  For Keras there is not as much utility there but it depends on which way you want to think about it.  If you want Numba to call out to Keras then that is not going to work you could, however, use Numba to implement optimized operations called from Keras.  

---

**Q.** passing functions as arguments seems to have some performance issues. how do these fit in the project roadmap? (Link to Github post)[https://github.com/numba/numba/issues/2952]

**A.**  This fits in a little bit with the medium-term objective of something called dispacher.  It is the thing that decides which machine code to call when you enter a function from Python.  What he is alluding to here is that you have the ability to pass in a function as an argument when you are using Numba, which is very useful, but the dispatcher is pretty inefficient when it comes to deciding what to call when you have a function as an argument.  I would say this is a medium-term item of improvement as we work on the dispatcher.   

### Footnotes & Links

* [Numba Website](http://numba.pydata.org/)
* [GitHub page](https://github.com/numba/numba)
* [Gitter Chat](https://gitter.im/numba/numba)
* [PyPI](https://pypi.org/project/numba/)
* [Numba Mailing List](https://groups.google.com/a/continuum.io/forum/#!forum/numba-users)




