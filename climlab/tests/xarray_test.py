from __future__ import division
import climlab


def to_xarray(model):
    model.to_xarray()
    model.to_xarray(diagnostics=True)
    if hasattr(model, 'timeave'):
        climlab.to_xarray(model.timeave)