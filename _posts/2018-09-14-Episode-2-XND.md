---
layout: post
title: Open Source Directions Episode 2: XND
---

### Introductions

Welcome to Open Source Directions, the webinar that informs you about the future of open source projects.
This episode, the project being highlighted is [XND] (http://www.xnd.io)


* **Host:** Anthony Scopatz
* **Guest 1:** Travis Oliphant, founder and board member of Anaconda, founder and advisory board member at Numfocus, and currently CEO of Quansight.  He has been involved in a number of open source projects, over the past 20 years and is passionate about them.
* **Guest 2:** Saul Shanabrook, has been working at Quansight for just a little while now with XND.

### Project Overview

XND is sort of part of a saga made up over the last 6 or 7 years, where Travis had this idea that he wanted to make NumPy better.  He wanted to improve the ecosystem around Numpy, and also wanted to resolve some issues.  He considered writing a library, but the issue became that maybe 4 or 5 years later you could realize that you should have done things a little different, then you end up in a situation where you don’t know what to do because you can’t make changes without affecting millions of users.  To overcome that the creators decided to take the core components of NumPy, like the type system, container of raw memory, and low level dispatch mechanism, and then refactor them into low level C libraries that could be used by other languages.  After that they would write Python bindings that could be used by developers of other Python libraries.  So XND was meant to have the capabilities of  NumPy, refactored to be used by others.  It wasn’t intended to be a replacement for NumPy because it was not a user facing tool.  The hope was to create some developer libraries so that people could build NumPy like things.  

Right now the way XND is thought of is that people who use Python in NumPy are mostly just users who want to create some kind of algorithm, or fulfill some kind of use case they are pursuing at a high level.  For these users, XND is probably not the right tool.  XND is primarily a tool for people who are building array libraries.  One example is the ragged array library, which is a new effort to talk about different types of arrays besides just blocked arrays.  One use case where XND is helpful would be: If you have structures in your arrays with nested structures, how can you do efficient computations?  The reason it is helpful in this circumstance is that XND provides low level primitives from Python that allow you to do more flexible computations on data than NumPy does.   It allows variable dimensions, and more types of nesting, and it also has C libraries that can be used in other languages.  This format allows you to use the library work that has already been done so all you have to build is the language binding and then gain access to all the computation kernels that people have written for whatever language you are targeting.

Talking in general terms about containers of data, there are a lot of them; Tensorflow, Torch, MX Net, etc.  If you are talking about the idea of a set of tools to support other array libraries, then maybe there are some machine learning libraries that have some building blocks that could be loosely interpreted as similar but would be kind of like cousin projects to XND.  Keeping it wide still, there are other projects like Arrow which is also like a cousin to XND, however it is a specific kind of container optimized for data frames and data analysis.  The only real relation here being that XND has the ability to describe pretty much any container, and more so we are starting with the ND array concept.  In theory someone could even write and XND description of an Arrow container.  Now this has not been done yet, so it is purely theoretical, but that somewhat embodies the main idea of using this system to describe dispatch over arbitrary memory blocks with anything. 

There are two parts to XND, there is the C part that just runs on C, and the Python bindings built around that.  The setup is pretty cleanly divided and there are three separate projects in XND called ND Types, XND, and GeoMath.  ND Types is just the type description language and that has a C part and a Python part.  Then there is XND which is the type description plus block of memory which also has a C and Python component.  Lastly there is GeoMath  which applies computation to those blocks of memory and this too has elements of C and Python.  

About 3 years ago Travis had this idea about: how to take NumPy Dtypes and make them more general, and he wanted to figure it out but did not have any time to work on it.  He thought about trying to hire a few people, but eventually he found Stephan Craw, who was willing to work on these kind of ideas and he was a Memory View maintainer, and a Python core developer as well as a talented C developer.  It ended up that he was willing to remotely work with Travis on this.  They first looked at Dine to see if it could be reused, and tried it out, but ultimately they ended up rewriting it from scratch.  Now for the past two years Stephan has been tirelessly working on this more or less alone, with just a couple of contributors and a few other people.  Once Quansight got up and running at the beginning of this year, the XND project began to gain support from some staff.  At this point Travis just calls himself the organizer of XND, or maybe the idea enthusiast, but Stephan is really the lead developer and he has put a lot of effort into it.  

The original idea was to have lots of other supported languages, but XND is still very new.  This project is considered to be just about in the alpha stage of development, and maybe moving from alpha to beta, for the Python bindings particularly.  There was actually somebody who reached out this summer who was a Ruby developer and said that he wanted to use XND to connect Ruby to a machine learning framework he was building.  He was invited to work on this project, so now there is someone who is starting the Ruby bindings.  There was also a conversation with Microsoft about possible C# bindings, and we look forward to Go, Node, Java, and many other bindings.  

### Demo

To view the notebook from which the demo was given, visit the [XND homepage] (http://www.xnd.io)

### Roadmap Items

1. **GPU support:** So David Brochart had been working on the GPU integration so that has some preliminary work done.  It is a prototype of one approach, and now the atempts are to try and figure out where to go from here.  These would be basic GPU support kernels.  This is for when you have your data on the GPU and you want your computations to be there as well.  Some questions are, what is the IPC and how to navigate that.  

2. **Lapack and MKL Kernels and Kernel Generators:** This sort of springs from a conversation that was had with someone about XND, because they asked “Where are all the kernels?”.  Many people look at NumPy and enjoy all the functions that they can call, but XND on the surface seems to be missing the callable functions.  Instead of having the functions, it is a system for building functions, so now people just need to make those functions so people can call them.  The idea with Numba integration would help address this by making it easier to build the functions with Python code.  The next part of this point is about being able to automatically produce kernels that call out to low level libraries.  This was sort of the direction that SciPy went; build the NumPy container then SciPy, then they auto generated a bunch of tools.  So ultimately the goal is to not only get them to built these tools, but then to be able to auto-generate these tools for other libraries.  

3. **Numba Integration:** Currently this is working, but there is more to do on a couple of fronts.  For the last couple of weeks we have been looking at the way we are doing memory allocation in Numba in an effort to use its reference counting allocator.  This has proven to be quite a lot of work, and we are still ironing out some of the folds.  It was sort of working, and there do not seem to be any major roadblocks in the way, but at the moment there is not much in the applications side so there is not much to wrap.  If we wanted to do string processing to support some string kernels, then that could be really useful.  

XND is currently in a state where it will be driven by applications.  We kind of want to get the basics together, but mostly it is about what the applications are and what the use cases are.  Anderson, one of our interns, made a really great connection to Data Frames.  He even ended up building custom types for Pandas.  We could potentially build custom Dtypes in NumPy with XND, that is another possibility to look at.  We really want to start driving user stories, so that XND and be developed by those users.  One thing that XND should also be able to do is make it easier to work with awkward arrays.

4. **Serialization of XND Containers:** One thing we have been talking about with disk formats like .CSV is how we can get them into XND efficiently?  XND can map to any disk format, so this is more referring to weather we want to compress it before we store it, or do other transformations with the data before we store it.  We would want to establish integrations with familiar formats as well.  The deserialization is also a big point though, it could be a really good application of XND to go from a JSON file to the XND data structure pretty quickly.  

Just one more point on the plasma storage, plasma is an example of what would be called a data fabric, it is the idea that you can have living data in a multi cluster memory system, but then you want to be able to point to a pointer and understand that pointer.  This pointer system is what XND does with its in memory data structure.    

These items are things that you can help out with.  By helping contribute to the project, or by helping to fund it, you can become part of these development efforts.  

### Viewer Questions

Now we will move on and open it up to user questions.  

**Q.** How would you compare XND to the buffer protocol and Ctypes?

**A.** The buffer protocol was actually one of the answers to solving the split with Numarray and Merrick.  One potential answer was NumPy, and the other was enhance the buffer protocol, we took both of these routes as a fix it twice concept.  What we are trying to achieve with XND is to make the buffer protocol cross language.  In some sense this is taking the buffer protocol and spreading it across the computer science ecosystem.  For Ctypes it would be nice to have a translator between a Ctypes description and an XND.  It would be great to seen an NDtypes grow a few more, that is not currently on the roadmap but would be beneficial.  

There is a gitter channel where you can post your additional [questions about XND here] (http://www.github.com/plures/xnd)
This project really need users and developers so that it can be developed to the needs of people that have these sorts of problems.  

### Footnotes & Links

* Thanks for watching and listening, you can find us on Twitter @quansightai and if you are interested in supporting a project, you can find all of [our roadmaps here] (http://www.quansight.com/projects)
