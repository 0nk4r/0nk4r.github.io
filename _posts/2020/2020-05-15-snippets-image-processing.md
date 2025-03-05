---
layout: post
title: 'Snippets: Image processing'
date: 2020-05-15 21:06 +0000
last_modified_at: 2020-11-28 07:38:35 +0000
tags: [Productivity, Tools]
---

Useful snippets reference while working with Images

<!-- more -->

## Convert Image to CSV

I recently had to convert a binary image into a csv file. Here is a quick and
simple way of doing this.

```python
import numpy as np
from PIL import Image

im = np.array(Image.open('fromfile.bmp'), dtype=int)
np.savetxt('tofile.csv', im, fmt='%d', delimiter=',')
```

## Convert CSV to image

We can use numpy and Pillow to convert from a CSV to Image. The following snippet
is for binary images or grayscale images

```python
import numpy as np
from PIL import Image

arr = np.genfromtxt('fromfile.csv',
                    dtype=np.uint8,
                    delimiter=',',
                    invalid_raise=False)  # if your csv has unequal number of cols
arr = np.nan_to_num(arr)

img = Image.fromarray(arr)
img.convert('L')
img.save('tofile.png')
```
