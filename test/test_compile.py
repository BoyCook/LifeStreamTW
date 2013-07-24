def test_compile():
	try:
		import tiddlywebplugins.lifestream
		assert True
	except ImportError, exc:
		assert False, exc
