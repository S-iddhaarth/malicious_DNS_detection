parser = OptionParser(usage="%prog: [options]")
	parser.add_option("-i", "--iface", dest="iface", default='', help="Interface. Ex: enp0s7")
	parser.add_option("-q", "--quiet", dest="quiet", action="store_true", help="Quiet")
	parser.add_option("-d", "--database", dest="databasePath", default='', help="Path to sqlite database for loggin. Ex: db.sqlite")
	parser.add_option("-e", "--export", dest="exportPath", default='', help="Export sqlite database to CSV. Ex: db.csv")
	(options, args) = parser.parse_args()