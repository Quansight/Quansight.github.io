---
layout: post
title: Open Source Directions Episode 2: XND
---```

### Introductions

Welcome to Open Source Directions, I am your host Anthony Scopatz, and joining me is Travis Oliphant and Saul Shanabrook.  First Travis will introduce himself.

I am Travis Oliphant, founder and board member of Anaconda, founder and advisory board member at Numfocus, and currently CEO of Quansight.  I have been involved in a number of open source projects, over the past 20 years and am passionate about them.

Now Saul will introduce himself.

I am Saul Shanabrook, I have been working at Quansight for just a little while now with XND and I am happy to be here.

### Headlines

Now we will move on to the headline section and go around sharing recent events.  First Saul:

There is a project called Learna which is a mono-repo management tool for JavaScript, and is actually something we use in Jupyter Lab.  Earlier last week, they changed their license from MIT to MIT minus people who work with ICE and businesses that work with ICE.  This change did not last, but it happened for about a day or so.  The basic idea here is that this instance illustrates the ability for developer communities to exert authority over how their tools are used.  I am interested to see where this discussion will go, and the larger implications with ethics.

I am excited by the recent Numfocus announcements about their new board selection process and various efforts which show the maturity of the organization.  They have 5 great new board members and it is great to see them join Andy and Murena who are continuing with all the work they achieve behind the scenes.  In addition to the board, I am impressed by all the work on the part of staff and volunteers and love the great work they do to make PyData and everything work in that organization.

I just wanted to highlight Pyodide, which is the Python scientific stack compiled to web assembly so this is just an example of some of the great working coming out of companies like Mozilla, Mic Drop Boom, etc.

### Project Overview

Now we will move on to describe and introduce XND so that we can get some background through just a few questions for Travis and Saul.

Q. Why was XND started?
XND is sort of part of a saga made up over the last 6 or 7 years, where I had this idea that I wanted to make NumPy better.  I wanted to improve the ecosystem around Numpy, I also wanted to resolve some issues.  I considered writing a library, but the issue becomes that maybe 4 or 5 years later you could realize that you should have done things a little different, then you end up in a situation where you don’t know what to do because you can’t make changes without affecting millions of users.  To overcome that we decided to take the core components of NumPy, like the type system, container of raw memory, and low level dispatch mechanism, and then refactor them into low level C libraries that can be used by other languages.  After that we would write Python bindings that could be used by developers of other Python libraries.  So XND is meant to have the capabilities of  NumPy, refactored to be used by others.  It wasn’t intended to be a replacement for NumPy because it was not a user facing tool.  The hope was to create some developer libraries so that people could build NumPy like things.  

Q. What need does XND fill?
Right now the way we think about it is that people who use Python in NumPy are mostly just users who want to create some kind of algorithm, or fulfill some kind of use case they are pursuing at a high level.  For these users, XND is probably not the right tool.  XND is primarily a tool for people who are building array libraries.  One example is the ragged array library, which is a new effort to talk about different types of arrays besides just blocked arrays.  One use case where XND is helpful would be: If you have structures in your arrays with nested structures, how can you do efficient computations?  The reason it is helpful in this circumstance is that XND provides low level primitives from Python that allow you to do more flexible computations on data than NumPy does.   It allows variable dimensions, and more types of nesting, and it also has as Travis mentioned, C libraries that can be used in other languages.  This format allows you to use the library work that has already been done so all you have to build is the language binding and then gain access to all the computation kernels that people have written for whatever language you are targeting.

Q. Are there any alternative projects out there?
If you are talking in general terms about containers of data, then there are a lot of them; Tensorflow, Torch, MX Net, etc.  If you are talking about the idea of a set of tools to support other array libraries, then maybe there are some machine learning libraries have some building blocks that could be loosely interpreted as similar but would be kind of like cousin projects.  Keeping it wide still, there are other projects like Arrow which is also like a cousin to XND, however it is a specific kind of container optimized for data frames and data analysis.  The only real relation here being that XND has the ability to describe pretty much any container, and more so we are starting with the ND array concept.  In theory someone could even write and XND description of an Arrow container.  Now this has not been done yet, so it is purely theoretical, but that somewhat embodies the main idea of using this system to describe dispatch over arbitrary memory blocks with anything. 

Q. What are the technologies that XND is built on?
So there are two parts to XND, there is the C part that just runs on C, and the Python bindings built around that.  The setup is pretty cleanly divided and there are three separate projects in XND called ND Types, XND, and GeoMath.  ND Types is just the type description language and that has a C part and a Python part.  Then there is XND which is the type description plus block of memory which also has a C and Python component.  Lastly there is GeoMath  which applies computation to those blocks of memory and this too has elements of C and Python.  

Q. Who started XND?
I think I am the guilty party, because about 3 years ago I had this idea about: how to take NumPy Dtypes and make them more general, and I wanted to figure it out but did not have any time to work on it.  I thought about trying to hire a few people, but eventually I found Stephan Craw, who was willing to work on these kind of ideas and he was a Memory View maintainer, and a Python core developer as well as a talented C developer.  It ended up that he was willing to remotely work with me on this.  We first looked at Dine to see if it could be reused, and tried it out, but ultimately we ended up rewriting it from scratch.  Now for the past two years Stephan has been tirelessly working on this more or less alone, with just a couple of contributors and a few other people.  Once we got Quansight up and running at the beginning of this year, the XND project began to gain support from some of our staff.  At this point I just call myself the organizer of XND, oe maybe the idea enthusiast, but Stephan is really the lead developer and he has put a lot of effort into it.  

Q. Are there any other supported languages besides Python and C at the moment?
The original idea was to have lots of other supported ;languages, but XND is still very new.  I consider this project to be just about in the alpha stage of development, and maybe moving from alpha to beta, for the Python bindings particularly.  We did actually have somebody reach out this summer who is a Ruby developer and say that they wanted to use XND to connect Ruby to a machine learning framework they were building.  We invited him to work with us on this, so there is someone who is starting the Ruby bindings.  We also had a conversation with Microsoft about possible C# bindings, and we look forward to Go, Node, Java, and many other bindings.  

### Demo

Now we will have Saul give a demo of XND.  To view the notebook from which the demo was given, visit the XND homepage: www.xnd.io 

### Roadmap

Now we will move on to the XND project roadmap and Travis and Noah will give us some additional insights about the roadmap items.  These items are points which can be supported by time contributions and donations.  To view the roadmap yourself, you can find it here: www.quansight.com/projects 

1. GPU support

So David Brochart had been working on the GPU integration so that has some preliminary work done.  It is a prototype of one approach, and now we are just trying to figure out where to go from here.  These would be basic GPU support kernels.  This is for when you have your data on the GPU and you want your computations to be there as well.  Some questions are, what is the IPC and how do we navigate that.  

2. Lapack and MKL Kernels and Kernel Generators

This sort of springs from a conversation that I was having with someone about XND, because they asked “Where are all the kernels?”.  Many people look at NumPy and enjoy all the functions that they can call, but XND on the surface seems to be missing the callable functions.  Instead of having the functions, it is a system for building functions, so now people just need to make those functions so people can call them.  The idea with Numba integration would help address this by making it easier to build the functions with Python code.  The next part of this point is about being able to automatically produce kernels that call out to low level libraries.  This was sort of the direction that SciPy went; build the NumPy container then SciPy, then they auto generated a bunch of tools.  So ultimately the goal is to not only get them to built these tools, but then to be able to auto-generate these tools for other libraries.  

3. Numba Integration

Currently this is working, but there is more to do on a couple of fronts.  For the last couple of weeks I have been looking at the way we are doing memory allocation in Numba in an effort to use its reference counting allocator.  This has proven to be quite a lot of work, and I am still ironing out some of the folds.  It was sort of working, and I do not see any major roadblocks in the way, but at the moment there is not much in the applications side so there is not much to wrap.  If we wanted to do string processing to support some string kernels, then that could be really useful.  
(Travis)  XND is currently in a state where it will be driven by applications.  We kind of want to get the basics together, but mostly it is about what the applications are and what the use cases are.  Anderson, one of our interns, made a really great connection to Data Frames.  He even ended up building custom types for Pandas.  We could potentially build custom Dtypes in NumPy with XND, that is another possibility to look at.  We really want to start driving user stories, so that XND and be developed by those users.  One thing that XND should also be able to do is make it easier to work with awkward arrays.

4. Serialization of XND Containers

One thing we have been talking about with disk formats like .CSV is how we can get them into XND efficiently?  XND can map to any disk format, so this is more referring to weather we want to compress it before we store it, or do other transformations with the data before we store it.  We would want to establish integrations with familiar formats as well.  The deserialization is also a big point though, it could be a really good application of XND to go from a JSON file to the XND data structure pretty quickly.  
Just one more point on the plasma storage, plasma is an example of what I would call a data fabric, it is the idea that I can have living data in a multi cluster memory system, but then I want to be able to point to a pointer and understand that pointer.  This pointer system is what XND does with its in memory data structure.    

Thank you for helping us work through this roadmap, and just for our watchers, these items are things that you can help out with.  By helping contribute to the project, or by helping to fund it, you can become part of these development efforts.  

### Viewer Questions

Now we will move on and open it up to user questions.  

Q. How would you compare XND to the buffer protocol and Ctypes?
The buffer protocol was actually one of the answers to solving the split with Numarray and Merrick.  One potential answer was NumPy, and the other was enhance the buffer protocol, we took both of these routes as a fix it twice concept.  What we are trying to achieve with XND is to make the buffer protocol cross language.  In some sense this is taking the buffer protocol and spreading it across the computer science ecosystem.  For Ctypes I would say it would be nice to have a translator between a Ctypes description and an XND.  I would like to seen an NDtypes grow a few more, that is not currently on the roadmap but I would like to see it.  

I think that will be good for questions for now, but there is a gitter channel (gitter.im/Plures/xnd) where you can post your questions about XND, there is also a github page (github.com/plures/xnd).
We really need users and developers so that it can be developed to the needs of people that have these sorts of problems.  

### Final Word

We will now move on to our famous rant section.  We will start with Travis.

My soapbox is to become a sustaining member of Numbfocus, if you use NumPy or SciPy, Pandas, or Jupyter, ect. Then see if you can contribute.  Maybe $5 per month, $10 per month, $100 per month, just a regular contribution to Numfocus as a sustaining member goes a long way.  By participating you also become part of the action and part of the solution to sustaining open source.  

This is a little different, but I think it is a good contrast.  In these spaces we are often a little heady, so my soapbox is silence: engaging with other people without having to talk with them all the time.  If you are in a social situation, try to see how you can communicate with someone without actually talking.  

I think that is a great point.  For my soapbox, I have been doing a lot of spackling and laying of floors, so I just want to say that carpentry is not like software carpentry at all.  

Thanks for watching and listening, you can find us on Twitter @quansightai and if you are interested in supporting a project, you can find all of our roadmaps at: www.quansight.com/projects 
