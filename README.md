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
Cons = hfst.regex("[p|b|t|d|k|g]")
CV = Cons.copy()
CV.concatenate(Vow)
CV.minimize()
CV.view()
```

For more, see the notebook Syllable.ipynb()





