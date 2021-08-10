def speedtest_convert(n):
	div = 1024
	z = 0
	units = {
        0: '',
		1: 'Kb/s',
		2: 'Mb/s',
		3: 'Gb/s',
		4: 'Tb/s'}
	while n > div:
		n = n / div
		z = z + 1
	return f"{round(n, 2)} {units[z]}"