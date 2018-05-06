	CREATE TABLE IF NOT EXISTS tasks (
		id INTEGER PRIMARY KEY AUTOINCREMENT, 
		name TEXT NOT NULL DEFAULT '',
		description TEXT NOT NULL DEFAULT '',
		date_to_complete TEXT NOT NULL DEFAULT '',
		status TEXT NOT NULL DEFAULT '',
		created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
	)
