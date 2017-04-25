
# coding: utf-8

# ##### <img src="matplotlib_logo.png" alt="Matplotlib">
# ## Python Plotting with Matplotlib
#
# Thank you Austin Godber for slides
#

# # Visualization in Python
#
# Several Options
#
# * Matplotlib - reliable,configurable
# * Plotting in Pandas - built using matplotlib, not as configurable
# * Seaborn - Advanced statistical visualisation, built on matplotlib, enhances matplotlib
# * Bokeh - Dynamic web/d3 based
#
# [Fun Comparison Post](https://dansaber.wordpress.com/2016/10/02/a-dramatic-tour-through-pythons-data-visualization-landscape-including-ggplot-and-altair/)

# # Starting with Matplotlib
# - http://matplotlib.org/2.0.0/index.html
# - http://pbpython.com/effective-matplotlib.html

# # Two Faces of Matplotlib
# ###### <img src="masks.jpg" alt="Matplotlib">
# * `pyplot`
# * Object Oriented Programming (OOP) Interface

# # `pyplot` - like MATLAB plotting
#
# "collection of command style functions that ... makes some change to a figure ... is stateful in that it keeps track of the current figure and plotting area, and the plotting functions are directed to the current axes"

# In[1]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import numpy as np
plt.plot(np.random.rand(20).cumsum())
plt.show()


# Note that `plot` is a function from the `pyplot` module.  We are NOT calling a `plot` method on a `plt` object.

# - All of the "messy" "plot-y" bits are magically and implicitly created behind the scenes.  See `gca()`, `gcf()`, `gci()` etc.
# - Some gallery examples use pyplot - resist the temptation!

# # Two Faces of Matplotlib
#
# * `pyplot` - implicit, creepy objects lurking in the dark
# * OOP Interface - sensible, well behaved interface

# # Object Oriented Programming interface

# In[2]:

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(np.random.rand(20).cumsum());


# # Figures and Axes

# * `Figures` are the top level container object, where you put `Axes` objects
# * `Axes` objects have the plotting methods and plot elements

# * `plt.subplots()` is the quickest way to start a figure with one or more axis objects while keeping references to them.

# In[3]:

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, figsize=(12,6)) # omit arguments for default
get_ipython().magic('pinfo plt.subplots')


# ## A **figure** may contain one or more **axis**

# In[4]:

import matplotlib.pyplot as plt
import numpy as np

fig, ((ax11, ax21), (ax12, ax22)) =        plt.subplots(nrows=2,ncols=2, figsize=(12,6))
#also try
#fig, axes = plt.subplots(3, 2)


# ### Plot on one of these axes ...

# In[5]:

fig, ((ax11, ax12), (ax21, ax22)) =        plt.subplots(nrows=2,ncols=2, figsize=(12,6))
ax12.plot(np.random.randn(200))


# # What could we do?
# - share x and y axes
# - add lines
# - set limits, ticks and labels
# - add grids
# - add text

# In[6]:

fig, ((ax11, ax12), (ax21, ax22)) =        plt.subplots(nrows=2,ncols=2, sharey = 'row', figsize=(12,6))
thing1 = np.random.randn(200)
thing2 = np.random.randn(200)
thing1_ave = np.mean(thing1) + np.zeros(200)
thing2_ave = np.mean(thing2) + np.zeros(200)
ax11.plot(thing1)
ax11.plot(thing1_ave)
ax12.plot(thing2)
ax12.plot(thing2_ave, color ='r')
ax21.plot(thing1.cumsum())
ax22.plot(thing2.cumsum())
ax21.set_yticks([-25,0,25])
ax22.set_yticks([-25,0,25])
ax21.set_yticklabels(['negative','zero','positive'])
ax11.grid()


# ### histograms using `ax.hist(data, bins=N)` ...

# In[7]:

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, figsize=(12,6))
ax.hist(thing1, bins=50);


# ### Points using `ax.scatter(x, y)` ...

# In[8]:

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, figsize=(12,6))
ax.scatter(np.arange(200), thing1.cumsum());


# or Points using `ax.plot(x, y)` and changing the line type to `o` ...

# In[9]:

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, figsize=(12,6))
ax.plot(np.arange(200), thing1.cumsum(), 'o');


# bars with `ax.bars(x, height)` ...

# In[10]:

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, figsize=(12,6))
ax.bar(np.arange(10), [15, 7, 22, 17, 10, 19, 23, 14, 9, 14]);


# # Matplotlib Gallery
#
# - lots of examples
# - http://matplotlib.org/gallery.html
# - check to see if using 'pyplot' interface - if so, check axes methods
# - http://matplotlib.org/api/axes_api.html

# # More stuff

# Add a label by using the `label=` keyword when you call plot, then show the label by calling `ax.label()`.

# In[11]:

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, figsize=(12,6))
ax.plot(np.random.randn(50), label='A')
ax.plot(np.random.randn(50), label='B')
ax.legend();


# Dots on your plot ... specify a style string as an argument to plot ... `plot(x, 'ko')`.  Change color and move the label too!

# In[12]:

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, figsize=(12,6))
ax.plot(np.random.randn(50), 'ro', label='A')
ax.plot(np.random.randn(50), 'ko', label='B')
ax.legend(loc=2);


# Keywords work too! `linestyle='None', marker='o', color='r'` equals `'ro'`

# In[13]:

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, figsize=(12,6))
ax.plot(np.random.randn(50), linestyle='None', marker='o', color='r', label='A')
ax.plot(np.random.randn(50), linestyle='None', marker='o', color='k', label='B')
ax.legend(loc=2);


# ### Add axes titles

# In[14]:

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, figsize=(12,6))
ax.plot(np.random.randn(50), linestyle='None', marker='o', color='r', label='A')
ax.plot(np.random.randn(50), linestyle='None', marker='o', color='k', label='B')
ax.legend(loc=2)
ax.set_title('Spots!')
ax.set_xlabel('X Spots')
ax.set_ylabel('Y Spots');


# ### Format Titles

# In[15]:

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, figsize=(12,6))
ax.plot(np.random.randn(50), linestyle='None', marker='o', color='r', label='A')
ax.plot(np.random.randn(50), linestyle='None', marker='o', color='k', label='B')
ax.legend(loc=2)
ax.set_title('Hey! Spots here', fontsize=36)
ax.set_xlabel('X Spots', fontsize=24)
ax.set_ylabel('Y Spots', fontsize=24)


# LaTeX can be included in any string by wrapping it in `$...$`.

# In[16]:

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, figsize=(12,6))
ax.plot(np.random.randn(50), linestyle='None', marker='o', color='r', label='A')
ax.plot(np.random.randn(50), linestyle='None', marker='o', color='k', label='B')
ax.set_title(' $\int_{a}^{b} x^2 dx$', fontsize=36)
ax.set_xlabel('X Spots', fontsize=24)
ax.set_ylabel('$e^n$', fontsize=24)


# ### Add text annotation with `ax.text(x, y, 'text')`

# In[17]:

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, figsize=(12,6))
ax.plot(np.random.randn(50), linestyle='None', marker='o', color='r', label='A')
ax.plot(np.random.randn(50), linestyle='None', marker='o', color='k', label='B')
ax.set_title('Mathy Title $\int_{a}^{b} x^2 dx$', fontsize=36)
ax.set_xlabel('X Spots', fontsize=24)
ax.set_ylabel('$e^n$', fontsize=24)
ax.text(10, -2, "hello\n$dx/dy$", fontsize=24)


# Everything done above can be found on this single page http://matplotlib.org/api/axes_api.html.  No googling, no digging through stack overflow.  Once you have an `ax` object (or list of them) you can just rely on this page to modify those objects.

# # Saving a Figure

# In[18]:

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, figsize=(12,6))
ax.plot(np.random.randn(50), linestyle='None', marker='o', color='r', label='A')
ax.plot(np.random.randn(50), linestyle='None', marker='o', color='k', label='B')
ax.set_title('save the spots', fontsize=36)
ax.set_xlabel('X Spots', fontsize=24)
ax.set_ylabel('Y Spots', fontsize=24)
fig.savefig('myfig.png', dpi=200)


# # Extra Material

# ## Configuration
#
# You can override default values with a personal config file or dynamically within your program (notebook).  Configurable params can be found here: http://matplotlib.org/users/customizing.html
#
# For example, to change the default line styling:
#
# ```python
# import matplotlib as mpl
# mpl.rcParams['lines.linewidth'] = 2
# mpl.rcParams['lines.color'] = 'r'
# ```
# equilvalently
# ```python
# import matplotlib as mpl
# mpl.rc('lines', linewidth=2, color='r')
# ```
#
# Or maybe you want a larger default figure size in your matplotlib notebook ... set `rcParams['figure.figsize']`

# ## Animations
#
# * Make them frame-by-frame and generate a movie from those frames with ffmpeg
# * Use matplotlib animate helper routines: http://matplotlib.org/examples/animation/index.html

# ## Warnings

# - there several plotting modules in python
# - plotting methods in pandas are built on matplotlib, but are not as customizable
# - bokeh, seaborn are alternatives plotting modules that are less customizable

# ### Joke

#  <img src="axes_joke.jpg" alt="Matplotlib">

# In[ ]:



