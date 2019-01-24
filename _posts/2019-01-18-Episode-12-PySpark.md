---
layout: post
title: Episode 12 - PySpark - Open Source Directions
---

<iframe width="560" height="315" src="https://www.youtube.com/watch?v=gyOfiRyLvJk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Introductions

Welcome to Open Source Directions, the webinar that informs you about the future of open source projects.
This episode, the project being highlighted is [PySpark](http://spark.apache.org/docs/2.2.0/api/python/index.html)

* **Host:** Anthony Scopatz
* **Co-Host:** David Charboneau
* **Guest:** Holden Karau, works on a variety of open source projects at Google, however, most of the focus is on Apache Spark. Her preferred pronouns are she & her.

### Project Overview

PySpark is the Spark/Python API, and it exposes the Spark programming model to Python.

PySpark was started at the time it was because there was a lack of good big data tools.  The basic intent behind it was to provide that big data capacity to Python tool users.  Since that time the scope has been widened to include the ability for Python users to access JVM libraries.  The opposite is also made possible with PySpark, that the Python code is now accessible from JVM libraries.  This sort of interchangeability comes in handy when you are working in a data science and data engineering heavy workplace because often they may not be used to using the same language.  If you were to run into an issue with Pandas not running on a MacBook, then you could just use Spark, but once you start getting into larger datasets then you need PySpark.

There are many alternative projects out there at the moment, Dask is one pure Python example and is great when you don’t have a mixed language environment.  Hadoop Streaming is another alternative if you don’t have as much of a time restriction.  In general, there is nothing quite like PySpark, but depending on the individual circumstances there are other options out there.

Just looking at the architecture for PySpark could make you go crazy, which means it is best not to think about how it works while you use it.  While the overall structure can be described pretty easily; if it is necessary to know how it is built, then something has likely gone wrong.  At the base level, PySpark is built upon Spark which is built on Scala.  Scala runs on the JVM.  A tool called Py for J which allows Python and Java to talk with each other.  Unfortunately, using this created some performance challenges, so Unix pipe sockets and files were used to try and copy data back and forth.  In a way, this structure can be compared to a Rube Goldberg machine that is overly complex but somehow works.  PySpark is part of the Hadoop ecosystem, but you do not need a Hadoop installation to use it but you can just run it from the cloud.  If you do however have a Hadoop installation, then you can speak to all of those file formats and use it really easily.  Some new innovations have come along like Apache Arrow which makes that integration less intimidating, it is still not easy but it is becoming more reasonable.  As it develops, we are likely to see Apache Arrow used in more and more use cases.  

This project was donated to the Apache Software Foundation by a group from UC Berkley.  Many of the former RISE Lab programmers who worked on ended up at a company called Databricks where Holden also worked at one time.  Staying together for that long allowed for the project to continue its maturation and so it is difficult to say that there was any one person who started this project.

When thinking about open source projects, people often forget about the people who maintain these projects, and in the case of PySpark, it is an Apache product.  The nice thing about this is that it is not just one company, but through Apache, there are many companies who support this project.  Holden, being a primary contributor, is actually an employee of Google and represents this inter-corporate cooperation behind the project.  Spark itself is a very large project, and the Python part is a smaller subset of the larger initiative.  Part of the reason there are fewer people working on this portion of the project is that it requires a knowledge of Java, Scala, and Python mixed together.   In addition to Holden, there are currently only 3 people who are working on this as regular, paid contributors as a result; Davies Liu, Hyukjin Kwon, and Bryan Cutler.  There is a more full list of committers and PMC members which can be found [here](https://projects.apache.org/committee.html?spark) and [here](http://bit.ly/sparkCommitters).

Currently, the contributors come largely from the JVM side as opposed to the Python side.  For certain parts of the project, there were more Python people because they were working on things like packaging Python projects in a standard way. On the geographic side, there is still a lot of bay area focus, but there are contributors from across the globe.

Currently, there are no diversity projects being made on the part of the community overall, however, there are some individuals who have put some effort forth.  For the project itself, the members are just about all from UC Berkley.  Through live code reviews and one on one coaching, Holden has tried to encourage people to contribute and this has been done with underrepresented groups as well.  There have also been other small efforts like putting up a rainbow logo for pride month.  

### Demo

[Demo at timestamp 14:37](https://www.youtube.com/watch?v=gyOfiRyLvJk)
Building a word counter [demo](https://github.com/jdwittenauer/ipython-notebooks/blob/master/notebooks/spark/Spark-Lab1-WordCount.ipynb)

### Wishlist

1. **Better multi-language support:**  This is really important for a lot of the enterprise customers, and many of the supporters of this project fall into that category.  Apache Arrow is another exciting project, and this highlights the convenience of being able to use one another’s libraries.  As a Scala programmer, it can be inconvenient to spend time writing MLP libraries when you could be using that time to write functional code.  So the important idea here is that people will not have to spend time porting code anymore.  They don’t use shared buffer memory yet, but they are using the Arrow format between the languages. If they can reach the point where the shared memory buffer is more than a pile of segfolds then we are likely to see useful multi-language pipelines. 

2. **More SQL:**  SQL is technically a multilanguage pipeline but in practice, it falls short of that function.  Without Types implemented, there is a chance that they will be added in.  There are mixed feelings about this particular item because there are various opinions out there about types, but it would be kind of nice for the Python data science users.  This gets to one of the biggest challenges for Spark and that is not having enough reviewers.  Contributions are great, and funding is always appreciated, but in addition to these things there is a shortage of reviewers.  With over 500 open pull requests it is difficult to manage everything without help from the users.

3. **Support for more streaming:**  Spark has between tree - four streaming execution engines.  Adding a fifth one will not solve the problem, so rather than that there are a few things to look forward to.  One example is a new low-guarantee streaming engine which is great for speed but does not hold as high a standard for keeping track of your data.  There is also the idea of a middle ground which would take better care of your data and still maintain a semblance of speed.  The new engine would be able to give power to the user so that it can be almost tuneable depending on the user needs.  Two of these proposed engines also use different APIs, but to get rid of the old API, they will first need to get the new API to be a full superset of the old one.  

4. **Machine learning changes:**  There are a bunch of ML changes coming in the future based on deep learning.  This will come in a different sort of architectural way than other changes in the past.  Suffice to say, there is a lot of fun neat stuff planned in the deep learning space.  The details of this would easily fill another webinar.


### Viewer Questions

**Q.** Can you compare how pyspark is different from dask?

**A.**  The main difference in my mind is that Dask is purely Python, you can pretty much accomplish the same tasks but if you need to work within an existing data infrastructure that is not pure Python, you will probably want to look at Spark.  If your data is all in Python then using Dask allows you to avoid dealing with the JVM which is more convenient. 

---

**Q.** I have experienced in one of my code that when i remove some simple python code from Pyspark code it runs smooth, but along with python it goes for toss, why does that happens ? What’s that weird happens in the back end because of python and pyspark in combined.

**A.**  There are lots of reasons why this could happen, but the most likely explanation is a serialization problem.  As we were talking about before, PySpark will identify all the things that your function touches and then send those over the network.  When this happens some of the objects become temperamental.  To reiterate, the most common issue here is a serialization error.  There are some tutorials out there, but debugging Spark is one thing that I get paid to do.  Without seeing the error message I just have to assume what the issue actually is.  

---

**Q.** Is the new RISE Lab still involved with Spark or are they just doing new things like Ray.

**A.**  I am not affiliated with Burkly, and do not have a Ph.D., so my answer is just based upon a basic understanding and may not be the official position of the RISE Lab.  My understanding is that they are mostly focused on building new things.  My understanding is that most of those new things are being built with Spark but they are not building Spark anymore.  

---

**Q.**  Is it a bad idea to save the DF using overwrite method if we are saving the DF to same file I read to create it?

**A.** Yes, that is a bad idea.  Do not do that.  Spark will not actually read the data until you go to save it out.  Because of that, there is a chance that Spark will overwrite the data while it’s reading it.

---

**Q.** What's the best way to get started learning SPARK?

**A.**  This is a question that I love because there is a wide variety of books which I have published on the subject.  Joking aside, I am very biased towards reading as a learning method, and so good books are; Learning Spark, Learning PySpark, and Spark: The Definitive Guide.  If books are not your thing then there are also some great videos out there.

---

**Q.** Would be great if you share any ideas on real ETL capabilities like UPDATE, UPSERT to replicate in similar manner in PySpark same as we do in expert ETL tools like Informatica, Datastage.

**A.**  To make lazy evaluations work you need mutable data structures. If I UPSERT into a table then I have changed that table and that will now break some of Spark’s computation models.  To a degree, Spark streaming give you a table which gives you a linear time progression and it can sort of look like that and it is okay.  In general, I don’t see this happening because it does not match Spark’s execution model.  I would love it if we could make this work for you, but Spark will not be changing its computation model.

---

**Q.** Can we use PySpark with GPU computation (CUDA) in quite easily way? If yes, could you recommend good source(s) of the information about this issue.

**A.**  The short answer is that it can be used with CUDA, but whether it can be done easily is another matter.  Probably the easiest way to use PySpark with CUDA is by using Python libraries that are accelerated with CUDA.  There are some other tricky considerations when it comes to the scheduling of CUDA accelerated jobs and that can be really rough.  This is because things like Yarn do not have a way to schedule around CUDA.  Getting that to work now is more of a power user situation.  You can find a step by step easy guide, but in practice, it is not likely to work very well.

---

**Q.** What do you think could be improved about distributed tools today?

**A.**  There’s a lot of things we can do.  The people that I work with the most have a lot of trouble debugging.  I think the most common thing that I see in distributed tools that can be improved are error messages and we could be better at explaining the state of the cluster when things go wrong.  I don’t think anyone does a really great job of that right now, even though Dask does a pretty good job of that I think there is still room for improvement.

---

### Footnotes & Links

* News and Announcements [here](https://spark.apache.org/news/)
* [PySpark Website](http://spark.apache.org/docs/2.2.0/api/python/index.html)
* [GitHub page](https://github.com/apache/spark/tree/master/python/pyspark)





