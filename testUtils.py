def test(name, result, expected):
	print("TEST %s: %s" %(name, "OK" if result == expected else str(result)))