---
layout: post
title: Python hash() is not deterministic
date: '2023-12-25 03:23 +0000'
last_modified_at: '2023-12-25 04:09:59 +0000'
tags:
  - Python
  - TIL
published: true
---

Python hash() is not deterministic. Output of `hash` function is not guaranteed
to be the same across different Python versions, platforms or executions of the
same program.

Lets take a look at the following example:

```bash
$ python -c "print(hash('foo'))"
-677362727710324010
$ python -c "print(hash('foo'))"
2165398033220216763
$ python -c "print(hash('foo'))"
5782774651590270115
```

As you can see, the output of `hash` function is different for the same input
`"foo"`. This is not a bug, but a feature in Python 3.3 and above. The reason
for this is that Python 3.3 introduced a Hash randomization as a security feature
to prevent attackers from using hash collision for denial-of-service attachs. 
Every time you start a Python program, a random value is generated and used to
salt the hash values. This ensures that the hash values are consistent within
a single Python run. But, the hash values will be different across different
Python runs.

You could disable hash randomization by setting the environment variable
`PYTHONHASHSEED` to `0`, but this is not recommended.

If you want to hash arbitrary objects deterministically, you can use the
[ubelt](https://ubelt.readthedocs.io/en/latest/ubelt.util_hash.html#ubelt.util_hash.hash_data) or
[joblib.hashing](https://joblib.readthedocs.io/en/latest/generated/joblib.hashing.hash.html) modules.

Here's an example of using `ubelt`

```python
import ubelt as ub

print(ub.hash_data('foo', hasher='md5', base='abc', convert=False))
```

Result:

```bash
$ python -c "import ubelt as ub; print(ub.hash_data('foo', hasher='md5', base='abc', convert=False))"
blhtggyvbuyhspdolqxdrhoajdka
$ python -c "import ubelt as ub; print(ub.hash_data('foo', hasher='md5', base='abc', convert=False))"
blhtggyvbuyhspdolqxdrhoajdka
$ python -c "import ubelt as ub; print(ub.hash_data('foo', hasher='md5', base='abc', convert=False))"
blhtggyvbuyhspdolqxdrhoajdka
```

## References

- <https://docs.python.org/3/whatsnew/3.3.html>: release when hash randomization made default
- <https://docs.python.org/3/reference/datamodel.html#object.__hash__>: hash function documentation
- <https://stackoverflow.com/a/27522708/2695603>
- [What You Need To Know About Hashing in Python](https://kinsta.com/blog/python-hashing/)
- [Deterministic hashing of Python data objects](https://death.andgravity.com/stable-hashing)
