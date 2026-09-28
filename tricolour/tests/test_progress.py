import io
import time

import dask
import dask.array as da

from tricolour.apps.tricolour.app import _LogProgressBar


def test_log_progress_bar_does_not_wait_out_dt():
    """The non-interactive bar draws every dt, but the compute must not wait
    out a whole dt after the last task (it used to: up to 5 minutes idle)."""
    x = da.ones((1000, 1000), chunks=100).sum()
    start = time.time()
    with _LogProgressBar(minimum=0, dt=60, out=io.StringIO()):
        dask.compute(x, scheduler="threads")
    assert time.time() - start < 10
