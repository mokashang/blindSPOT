CREATE TABLE documents (
	id INTEGER NOT NULL, 
	source_view_id VARCHAR NOT NULL, 
	fetched_at DATETIME NOT NULL, 
	expires_at DATETIME NOT NULL, 
	url VARCHAR NOT NULL, 
	title VARCHAR NOT NULL, 
	content TEXT NOT NULL, 
	content_hash VARCHAR NOT NULL, 
	language VARCHAR NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (content_hash)
);
CREATE INDEX ix_documents_source_view_id ON documents (source_view_id);
CREATE TABLE sessions (
	id INTEGER NOT NULL, 
	user_id VARCHAR NOT NULL, 
	created_at DATETIME NOT NULL, 
	situation TEXT NOT NULL, 
	summary TEXT, 
	language VARCHAR NOT NULL, 
	PRIMARY KEY (id)
);
CREATE INDEX ix_sessions_user_id ON sessions (user_id);
CREATE TABLE source_view_stats (
	source_view_id VARCHAR NOT NULL, 
	period VARCHAR NOT NULL, 
	hits INTEGER NOT NULL, 
	ratings_hit INTEGER NOT NULL, 
	ratings_meh INTEGER NOT NULL, 
	ratings_obvious INTEGER NOT NULL, 
	PRIMARY KEY (source_view_id, period)
);
CREATE TABLE tag_vocabulary (
	id INTEGER NOT NULL, 
	facet VARCHAR NOT NULL, 
	tag VARCHAR NOT NULL, 
	added_at DATETIME NOT NULL, 
	embedding_blob BLOB NOT NULL, 
	status VARCHAR NOT NULL, 
	PRIMARY KEY (id), 
	CONSTRAINT uq_tag_vocabulary_facet_tag UNIQUE (facet, tag)
);
CREATE TABLE turns (
	id INTEGER NOT NULL, 
	session_id INTEGER NOT NULL, 
	turn_number INTEGER NOT NULL, 
	user_input TEXT NOT NULL, 
	assistant_response TEXT NOT NULL, 
	created_at DATETIME NOT NULL, 
	user_id VARCHAR NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(session_id) REFERENCES sessions (id)
);
CREATE INDEX ix_turns_session_id ON turns (session_id);
CREATE TABLE blind_spots (
	id INTEGER NOT NULL, 
	turn_id INTEGER NOT NULL, 
	hook VARCHAR NOT NULL, 
	body TEXT NOT NULL, 
	community_tag VARCHAR NOT NULL, 
	rating VARCHAR, 
	rated_at DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(turn_id) REFERENCES turns (id)
);
CREATE INDEX ix_blind_spots_turn_id ON blind_spots (turn_id);
CREATE TABLE tag_audit (
	id INTEGER NOT NULL, 
	facet VARCHAR NOT NULL, 
	proposed_tag VARCHAR NOT NULL, 
	accepted_tag VARCHAR NOT NULL, 
	similarity_to_existing FLOAT, 
	turn_id INTEGER, 
	timestamp DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(turn_id) REFERENCES turns (id)
);
CREATE TABLE turn_tags (
	turn_id INTEGER NOT NULL, 
	facet VARCHAR NOT NULL, 
	tag VARCHAR NOT NULL, 
	PRIMARY KEY (turn_id, facet, tag), 
	FOREIGN KEY(turn_id) REFERENCES turns (id)
);
CREATE TABLE ungrounded_claims (
	id INTEGER NOT NULL, 
	turn_id INTEGER NOT NULL, 
	claim_text TEXT NOT NULL, 
	context TEXT, 
	logged_at DATETIME NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(turn_id) REFERENCES turns (id)
);
CREATE TABLE blind_spot_sources (
	blind_spot_id INTEGER NOT NULL, 
	document_id INTEGER NOT NULL, 
	PRIMARY KEY (blind_spot_id, document_id), 
	FOREIGN KEY(blind_spot_id) REFERENCES blind_spots (id), 
	FOREIGN KEY(document_id) REFERENCES documents (id)
);
