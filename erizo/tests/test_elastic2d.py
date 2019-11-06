# pylint: disable=redefined-outer-name
"""
Test the 2-component elastic interpolation
"""
import numpy as np
import numpy.testing as npt
import verde as vd
from verde.base import n_1d_arrays
import pytest

from ..elastic2d import Elastic2D


@pytest.fixture
def data2d():
    "Make 2 component vector data"
    synth = vd.datasets.CheckerBoard()
    coordinates = vd.grid_coordinates(synth.region, shape=(15, 20))
    data = tuple(synth.predict(coordinates).ravel() for i in range(2))
    return tuple(i.ravel() for i in coordinates), data


def test_vector2d(data2d):
    "See if the exact solution works"
    coords, data = data2d
    spline = Elastic2D().fit(coords, data)
    npt.assert_allclose(spline.score(coords, data), 1)
    npt.assert_allclose(spline.predict(coords), data, rtol=1e-2, atol=1)
    # There should be 1 force per data point
    assert data[0].size == spline.force_coords[0].size
    assert data[0].size * 2 == spline.force_.size
    npt.assert_allclose(spline.force_coords, n_1d_arrays(coords, n=2))


def test_vector2d_forces(data2d):
    "See if the exact solution works when providing forces"
    coords, data = data2d
    force_coords = vd.scatter_points(vd.get_region(coords), size=500, random_state=1)
    spline = Elastic2D(force_coords=force_coords).fit(coords, data)
    npt.assert_allclose(spline.score(coords, data), 1)
    npt.assert_allclose(spline.predict(coords), data, rtol=1e-2, atol=1)
    # There should be 1 force per data point
    assert spline.force_coords[0].size == 500
    assert spline.force_.size == 2 * 500
    npt.assert_allclose(spline.force_coords, n_1d_arrays(force_coords, n=2))


def test_vector2d_weights(data2d):
    "Use unit weights and a regular grid solution"
    coords, data = data2d
    outlier = 10
    outlier_value = 100000
    data_outlier = tuple(i.copy() for i in data)
    data_outlier[0][outlier] += outlier_value
    data_outlier[1][outlier] += outlier_value
    weights = tuple(np.ones_like(data_outlier[0]) for i in range(2))
    weights[0][outlier] = 1e-10
    weights[1][outlier] = 1e-10
    spline = Elastic2D(damping=1e-8).fit(coords, data_outlier, weights)
    npt.assert_allclose(spline.score(coords, data), 1, atol=0.01)
    npt.assert_allclose(spline.predict(coords), data, rtol=1e-2, atol=5)


def test_vector2d_fails(data2d):
    "Should fail if not given 2 data components"
    coords, data = data2d
    spline = Elastic2D()
    with pytest.raises(ValueError):
        spline.fit(coords, data[0])
    with pytest.raises(ValueError):
        spline.fit(coords, data + coords)
