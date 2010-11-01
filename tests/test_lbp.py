import numpy as np
import mahotas._lbp
import mahotas.thresholding
from mahotas.lbp import lbp, _roll_left

def test_shape():
    A = np.arange(32*32).reshape((32,32))
    B = np.arange(64*64).reshape((64,64))
    features0 = lbp(A, 3, 12)
    features1 = lbp(B, 3, 12)
    assert features0.shape == features1.shape

def test_nonzero():
    A = np.arange(32*32).reshape((32,32))
    features = lbp(A, 3, 12)
    assert features.sum() > 0

def test_histogram():
    A = np.arange(32*32).reshape((32,32))
    for r in (2,3,4,5):
        assert lbp(A,r,8).sum() == A.size

def test_roll_left():
    y = 1232
    values = []
    for i in xrange(12):
        y = _roll_left(y, 12)

    assert y == 1232


def test_histogram_large():
    A = np.arange(32*32).reshape((32,32))
    for r in (2,3,4,5):
        assert lbp(A,r,12).sum() == A.size


def test_map():
    assert len(set(mahotas._lbp.map(np.arange(256,dtype=np.uint32), 8))) == 36


