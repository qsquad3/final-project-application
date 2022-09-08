# import unittest

# class TestApp(unittest.TestCase):

def test_app_is_created(app):
    assert app.name == 'app'

def test_config_is_loaded(config):
    assert config["DEBUG"] is False

def test_request_returns_404(client):
    assert client.get("/url_que_nao_existe").status_code == 404

    # def test_hello(self):
    #     rv = self.app.get('/')
    #     self.assertEqual(rv.status, '200 OK')
    #     self.assertEqual(rv.data, b'Hello World!\n')

    # def test_healthcheck(self):
    #     rv = self.app.get('/healthcheck/')
    #     self.assertEqual(rv.status, '200 OK')
    #     self.assertEqual(rv.data, b'Hello World!\n')

    # def test_limpar(self):
    #     rv = self.app.get('/limpar/')
    #     self.assertEqual(rv.status, '200 OK')
    #     self.assertEqual(rv.data, b'Hello World!\n')

    # def test_popular(self):
    #     rv = self.app.get('/popular/')
    #     self.assertEqual(rv.status, '200 OK')
    #     self.assertEqual(rv.data, b'Hello World!\n')

# if __name__ == "__main__":
#     import xmlrunner

#     unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test_reports'))