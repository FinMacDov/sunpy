"""
NoRH Tests
"""
from __future__ import absolute_import

import pytest
import sunpy
import pandas

@pytest.mark.online
def test_norh():
    norh=lightcurve.NoRHLightCurve.create('2012-07-06')
    assert isinstance(norh, sunpy.lightcurve.NoRHLightCurve)
    assert norh.meta['obs-freq'] == '17GHZ'
    assert norh.time_range().start() == pandas.Timestamp('2012-07-05 21:59:50.710000')
    assert norh.time_range().end() == pandas.Timestamp('2012-07-06 06:19:49.710000')

    norh34=lightcurve.NoRHLightCurve.create('2012-07-06',wavelength='34')
    assert isinstance(norh34, sunpy.lightcurve.NoRHLightCurve)
    assert norh34.meta['obs-freq'] == '34GHZ'
    assert norh.time_range().start() == pandas.Timestamp('2012-07-05 21:59:50.760000')
    assert norh.time_range().end() == pandas.Timestamp('2012-07-06 06:19:49.760000')
