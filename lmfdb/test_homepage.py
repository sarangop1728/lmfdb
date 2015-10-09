# -*- coding: utf8 -*-
from lmfdb.base import LmfdbTest
import math
import unittest2

class HomePageTest(LmfdbTest):

    # All tests should pass: these are all the links in the home page as specified in index_boxes.yaml
    #
    # Box 1
    def test_box1(self):
        r"""
        Check that the links in Box 1 work.
        """
        page = self.tc.get("/L/degree2/")
        assert '9.53369' in page.data
        page = self.tc.get("/EllipticCurve/Q/?conductor=1-99")
        assert '[1, 0, 1, -14, -64]' in page.data
        page = self.tc.get("/ModularForm/GL2/Q/Maass/")
        assert 'The entire database consists of 16599 Maass forms.' in page.data
        page = self.tc.get("/zeros/first/")
        assert 'Riemann zeta function' in page.data # the interesting numbers are filled in dynamically
        page = self.tc.get("/NumberField/?degree=2")
        assert '"/NumberField/2.0.8.1">2.0.8.1' in page.data

    #
    # Box 2
    def test_box2(self):
        r"""
        Check that the links in Box 2 work.
        """
        page = self.tc.get("/L/Riemann/")
        assert r'\[\zeta(1/2) \approx -1.4603545088\]' in page.data
        page = self.tc.get("/NumberField/3.1.23.1")
        assert r'Regulator:<td>&nbsp;&nbsp;<td>\( 0.281199574322962 \)' in page.data
        page = self.tc.get("/ModularForm/GL2/Q/holomorphic/1/12/1/a/")
        assert '0.2993668' in page.data
        page = self.tc.get("/L/ModularForm/GL2/Q/holomorphic/1/12/1/a/0/")
        assert 'approx 0.839345512' in page.data
        page = self.tc.get("/EllipticCurve/Q/234446/a/1")
        assert r'y^2 + x y = x^{3} -  x^{2} - 79 x + 289' in page.data
        page = self.tc.get("/L/EllipticCurve/Q/234446.a/")
        assert 'L-function $L(s,E)$ for the Elliptic Curve Isogeny Class 234446.a' in page.data

    # Box 3
    def test_box3(self):
        r"""
        Check that the links in Box 3 work.
        """
        page = self.tc.get("/L/")
        assert 'Holomorphic cusp form' in page.data
        page = self.tc.get("/ModularForm/")
        assert r'Maass Forms on \(\GL(2,\Q) \)' in page.data
        page = self.tc.get("/EllipticCurve/Q/")
        assert 'curve, label or isogeny class label' in page.data
        page = self.tc.get("/NumberField/")
        assert 'x^7 - x^6 - 3 x^5 + x^4 + 4 x^3 - x^2 - x + 1' in page.data

    # Box 4
    def test_box4(self):
        r"""
        Check that the links in Box 4 work.
        """
        page = self.tc.get("/L/degree4/MaassForm/")
        assert 'data on L-functions associated to Maass cusp forms for GSp(4) of level 1' in page.data
        page = self.tc.get("/EllipticCurve/Q/102/c/")
        assert r'1 &amp; 2 &amp; 4 &amp; 4 &amp; 8 &amp; 8' in page.data

    # Box 5
    def test_box5(self):
        r"""
        Check that the links in Box 5 work.
        """
        page = self.tc.get("/bigpicture")
        assert 'some varieties are modular' in page.data
        page = self.tc.get("/knowledge/")
        assert 'Recently modified Knowls' in page.data

    # Box 6
    def test_box6(self):
        r"""
        Check that the links in Box 6 work.
        """
        import urllib2
        page = urllib2.urlopen("https://github.com/LMFDB/lmfdb").read()
        assert 'Modular Forms Database' in page
        page = urllib2.urlopen("http://sagemath.org/").read()
        assert 'mathematics software system' in page
        page = urllib2.urlopen("http://pari.math.u-bordeaux.fr/").read()
        assert 'PARI/GP is a widely used computer algebra system' in page
        # I could not get this one to work -- JEC
        #page = urllib2.urlopen("http://magma.maths.usyd.edu.au/magma/").read()
        #assert 'Magma is a large, well-supported software package' in page
        page = urllib2.urlopen("https://www.python.org/").read()
        assert 'Python Logo' in page
