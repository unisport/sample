#!/usr/bin/env python

import os, unittest, shutil

import sample

class SampleTestCase(unittest.TestCase):
  def setUp(self):
    self.basedir = os.path.split(os.path.abspath(__file__))[0]
    os.chdir(self.basedir)

    sample.app.config['TESTING'] = True

    try:
      os.remove('/tmp/sample.db')
      shutil.rmtree(self.basedir + '/test_migrations')
    except OSError:
      pass

    os.system("python manage.py db init --directory=test_migrations")
    os.system("python manage.py db migrate --directory=test_migrations")
    os.system("python manage.py db upgrade --directory=test_migrations")
    os.system("python manage.py seed")

    self.app = sample.app.test_client()

  def tearDown(self):
    try:
      os.remove('/tmp/sample.db')
      shutil.rmtree(self.basedir + '/test_migrations')
    except OSError:
      pass

  def test_get_by_id(self):
    rv = self.app.get('/products/2/')
    rv2 = self.app.get('/products/50/')

    assert bytes("puma-spilletroje-vencida-hvidbla-born-tilbud", 'UTF-8') in rv.data
    assert bytes('No item found', 'UTF-8') in rv2.data

  def test_get_by_gender(self):
    rv = self.app.get('/products/kids/')
    rv2 = self.app.get('/products/kid_adult/')
    rv3 = self.app.get('/products/women/')
    rv4 = self.app.get('/products/some_invalid_route/')

    assert bytes('kids : True', 'UTF-8') in rv.data
    assert bytes('kids : False', 'UTF-8') not in rv.data
    assert bytes('No items found', 'UTF-8') in rv2.data
    assert bytes('No items found', 'UTF-8') in rv3.data
    assert bytes('Not valid', 'UTF-8') in rv4.data

  def test_products(self):
    import re
    rv = self.app.get('/products/')
    rv2 = self.app.get('/products/page/2')
    rv3 = self.app.get('/products/page/3')
    rv4 = self.app.get('/products/page/4')
    print(rv4.data)
    
    assert len(re.findall(bytes('iid', 'UTF-8'), rv.data)) == 10
    assert bytes('iid : 11', 'UTF-8') not in rv.data
    assert bytes('iid : 1', 'UTF-8') in rv.data

    assert len(re.findall(bytes('iid', 'UTF-8'), rv2.data)) == 10
    assert bytes('iid : 21', 'UTF-8') not in rv2.data
    assert bytes('iid : 9', 'UTF-8') not in rv2.data
    assert bytes('iid : 11', 'UTF-8') in rv2.data

    assert len(re.findall(bytes('iid', 'UTF-8'), rv3.data)) == 10
    assert bytes('iid : 19', 'UTF-8') not in rv3.data
    assert bytes('iid : 21', 'UTF-8') in rv3.data

    assert bytes('No items found', 'UTF-8') in rv4.data
if __name__ == '__main__':
  unittest.main()

