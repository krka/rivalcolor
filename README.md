This is a project to make rival mice automatically transition between different colors.

It is mostly made for personal usage, but I put it on github for convenience.

# Dependencies

* Python
* [Rivalcfg](https://github.com/flozz/rivalcfg)

You can install rivalcfg with:
```
pip install rivalcfg
```

# Running

You can run with `python rival.py`

# Running automatically with upstart

```
description "Rivalcolor daemon"

start on runlevel [2345]
stop on runlevel [!2345]

respawn

kill timeout 20


script
        exec python $REPO_ROOT/rival.py
end script
```

