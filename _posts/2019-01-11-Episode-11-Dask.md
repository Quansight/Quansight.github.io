---
layout: post
title: Episode 11 - Dask - Open Source Directions
author: bsodenkamp
---

<iframe width="560" height="315" src="https://www.youtube.com/watch?v=u-HAzanaRVI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Introductions

Welcome to Open Source Directions, the webinar that informs you about the future of open source projects.
This episode, the project being highlighted is [Dask](https://dask.org)

* **Host:** Anthony Scopatz
* **Co-Host:** David Charboneau
* **Guest:** Jim Crist, is a software developer at Anaconda and works on projects such as Dask.
* **Guest:** Tom Augspurger, is also a software developer at Anaconda and works on open-source packages like Pandas and Dask.

### Project Overview

Dask is a flexible tool for parallelizing the python ecosystem.  It currently has 4,000 stars on Github, about 1 million downloads on pypi, and about 250,000 downloads per month on conda-forge.  This has become a very popular project and has been around for a while.

This project began around the end of 2014/beginning of 2015 when it spun out of the Blaze library and ecosystem project.  The intent was to scale up Python computing and while Dask was designed to just be on the back end, but it was found that it was very useful on its own.  At this time, most libraries in the scientific Python world were single threaded (meaning they only take one core) and were limited to in-memory datasets so you couldn't do the large computation.  The goal for Dask was to take the exsisting ecosystem and scale it up to larger problems by using all the cores or all the machines on a cluster without having to rewrite the ecosystem.  Furthermore, an emphasis was put upon the interface so that it could be more familiar to users and as a result, they would not have to learn a new layout.

There is actually quite a bit of competition out in this space.  First, just looking at the libraries for standard parallel processing, you could get pretty far with something like concurrent.futures.  Some older 3rd party packages might be things like iPython Parallel.  Aside from these, the biggest competator is probably [Apache Spark](https://spark.apache.org/) because it provides a big distributed dataframe for large distributed data processing.  In this way, you might be able to say that it is kind of a competitor if you want to call it that.  There are many new projects which have also been popping up like the [Ray](https://ray.readthedocs.io/en/latest/index.html) project and [Mars](https://mars-project.readthedocs.io/en/latest/#) from Alibaba.

The underlying structure of Dask is somewhat complicated, and there are several levels to it. The very core of Dask, the *task graph* which is used to represent a computation, is just a dictionary where the keys are strings and the values are tuples of (function, arguments). So dask itself is pure-python.  Dask uses NumPy for array computations, and pandas to handle the data frames. To avoid rewriting a “parallel NumPy” and a “parallel Pandas” library from the ground up they used the existing projects for what they’re great at; providing a pleasant API for in-memory computation. Dask sits at a higher-level and coordinates many NumPy arrays or pandas data frames.  The last component is dask.distributed, which provides multi-machine parallelism, and is built on top of Tornado (a networking library that’s also used by Jupyter).

The original author of Dask was Matt Rocklin.  The story goes that over one Christmas break he began to toy around with the idea and after that brought what he had back to the office.  Within the first few months, Jim hopped onto the project, and it has slowly grown out from there ever since.  There are now many more contributors. 

Because Dask has become a sort of ecosystem, there are now many maintainers with various areas of expertise. Frequently there will be individuals who only focus on maintaining one element of the overall project because of the ecosystem model.  Recently Matt has done the majority of the day-to-day maintenance work, but this has fluctuated over time.

Since Dask is an open source project, it’s difficult to say for sure who the user base is and where they come from. Some groups are much more vocal about their use than others, such is the case with academics, who are happy to talk about their work. Specifically, there is a team of researchers at The Pangeo group (Earth scientists) who have taken to using Dask. On occasion finance, companies will reach out, though they seem to be less talkative.  Government applications are also well known via the national labs.

Without formal governance solidified, there has been nothing formally done with regard to inclusion efforts. When a contributor comes along who looks like they’re from an underrepresented group there is an effort made to be especially prompt about reviews and responding to updates, in the hope that they’ll be more likely to stick around. Like many OSS projects, people get busy and come and go as they have time which has made it difficult to move forward on diversification.

### Demo

[Demo at timestamp 11:32](https://www.youtube.com/watch?v=u-HAzanaRVI)
[Github Repository](https://github.com/dask/dask)
[examples that are publicly runnable on binder up here](http://examples.dask.org/)
[Dataframe](https://mybinder.org/v2/gh/dask/dask-examples/master?urlpath=lab/tree/dataframe.ipynb)
[Delayed](https://mybinder.org/v2/gh/dask/dask-examples/master?urlpath=lab/tree/delayed.ipynb)
[Surface Sea Ice](http://binder.pangeo.io/v2/gh/pangeo-data/pangeo-example-notebooks/master)

### Wishlist

1. **Governance:**  This item is pretty early in talks, but there is currently a governance document in the GitHub repository found [here](https://github.com/dask/governance).  As the team has grown, it has become more evident that there would be many benefits to establishing a governance model.  Specifically it is more useful as there are more cooperative efforts with outside organizations.  The first goal is to never need to use the governance but to have a plan just in case, and the second goal is to meet the requirements to become a Numfocus affiliated project.  At the moment there is nothing set in stone here it has mostly just been some beginning discussion.  These discussions are open, and thus the community is encouraged to join in since there is not a lot of experience with this kind of writing within the current group.

2. **Identifying user needs:**  So far this project has done very well in communicating with users to build a relationship and to find out what they need from developers.  The Pangeo project is a good example of this, and Xarray was an early adopter of Dask for internal use.  So if everything is working correctly, then a scientist working on something like solar observation, and they are having issues with scaling, then they can reach out to the developers and then Dask will be distributed to a cluster or whatever is needed.    

3. **Gradient boosted trees:**  Currently, XGBoost is the most popular to use and so there is a Dask XGBoost package that gets data from Dask workers to XGBoost distributed mode.  There is also a new project from Olivier Brosseau and an associate of his, they are working on a pure Python and Numba accelerated gradient boosted library.  HDBScan is a popular clustering algorithm, and this would also be fun to distribute.  These are just a few wishlist items, and anyone is welcome to add to this list which can be found [here](https://github.com/dask/dask-ml/issues?q=is%3Aopen+is%3Aissue+label%3ARoadmap).

4. **Increase number of developers:**  Part of this initiative for this new year will include getting involved with new projects.  Primarily this is just an outreach effort, and one good example is the success with the Xarray project with atmospheric computing for stretching Dask to be better.  This will also help the efficiency because then users can direct efforts to specific things for the team to fix rather than hoping that the efforts are helpful.

5. **Deployment:**  At the moment, Dask can be deployed to just about any major cluster manager.  This is done through a generic interface with things like Kubernetes, Apache Hadoop Yarn, TORQUE, etc.  These are all things that people at universities are likely to have.  There is some desire to unify these because at that moment they sort of push through the generic interface.  It is not clear yet how useful a unification would be, because it is not expected for users to swap their deployment very often.  This is one area specifically where it would be great to get some thoughts from new people.  Martin Durrant is working on a file system spec project with Intake that could also help here. 

### Viewer Questions

**Q.** Will Dask support the integer NA extension type support when Pandas 0.24 gets released? If so, will it be able to read/write parquet files?

**A.**  For those of you who do not know, Pandas j.24 will have optional support for integer coms with missing values.  Dask will be able to benefit from this right away, which is partially a testament to the design of Dask.  It really is just building on Pandas, which is evident in that you don’t have to rewrite Pandas to write Dask dataframe.  The second part of the question is will it be able to read and write parquet files, and the answer is that Dask and Pandas can already read and write parquet.  Perhaps the question was about reading and writing parquet files with these integer n/a columns, and that has not been sorted out at the Pandas level yet, we need to work with the PyArrow and past parquet developers to find out how these new extension array things should be serialized, which has not been done yet.  

---

**Q.** The Dask Stream seems a cool visualization tool for tracking computations. Say, if one would have a Python script doing computations (not using dask), would it be possible to visualize the computations using the Dask Stream feature? Say, by wrapping the script main function with Dask or smth?

**A.** The task stream shows computations that Dask knows about.  From a user perspective if you’re trying to write some custom thing you could use Dask-delayed, and we also have a futures interface if you are worried about futures.  Then you would be delegating certain functions to show up in the past stream.  As those are computed, they would show up in the past stream.  

---

**Q.** Can you say something about typical behavior of the startup time of the distributed scheduler? I imagine it's way faster than, e.g, YARN? How much does it depend on the hardware config?

**A.** That’s a complicated question.  The scheduler and the cluster in general are just Python processes so they spin up in seconds, but if you are talking about a cluster the you are probably using some kind of cluster management to manage how long the cluster lasts.  Then the speed is dependent upon which cluster manager you are using.  Like we mentioned before, we are already deploying Kubernetes, Yarn, and traditional job ques, and that all depends on both how heavily used your cluster is, and what resources you are moving around. I would say my experience with Yarn in a non-real world situation has been seconds or at most under a minute.  Usually about 20 seconds to start cluster.  Kubernetes can be faster or slower, it just really depends on the situation.  

---

**Q.** Does anyone have work/plans/interest in automatic differentiation of calculations done with Dask?

**A.** I don’t think anyone on this webinar has plans for that, but if you are interested in it then it would certainly be worth looking into.  We would be curious to see that as well and maybe help out with it.  One interesting thing on that is there are a couple libraries that do automatic differentiation based on NumPy, so following the NumPy API.  Since Dask follows the NumPy API, if you could make it separate from NumPy then it would likely just work with Dask array. 

### Footnotes & Links

* Wishlist [here](https://github.com/dask/dask-ml/issues?q=is%3Aopen+is%3Aissue+label%3ARoadmap)
* [Dask Website](https://dask.org/)
* [GitHub page](https://github.com/dask/dask)
* [Gitter page](https://gitter.im/dask/dask)

