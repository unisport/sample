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
    assert bytes("puma-spilletroje-vencida-hvidbla-born-tilbud", 'UTF-8') in rv.data

if __name__ == '__main__':
  unittest.main()

