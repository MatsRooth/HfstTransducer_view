# HfstTransducer.view
Restore a version of the method for viewing a transducer in a Jupyter notebook.  This is found in the hfst_dev branch, but not in a current HFST 3.16.0.1.

# Setup
```
import hfst
import hfst_transducer_view

hfst_transducer_view.install()
```

# Functionality

```
Vow = hfst.regex("[a|e|i|o|u]")
Cons = hfst.regex("[p|b|t|d|k|g]")
CV = Cons.copy()
CV.concatenate(Vow)
CV.view()
```

![CV](./img/cv.png)

This is part of a more complicated example.

For more, see the notebook demo_view.ipynb.





