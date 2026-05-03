-- SQLModel Generated Schema

\c registry;


CREATE TABLE users (
	id SERIAL NOT NULL, 
	name VARCHAR(254) NOT NULL, 
	contact VARCHAR(254) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (contact)
)

;

CREATE TABLE organizations (
	id SERIAL NOT NULL, 
	name VARCHAR(254) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (name)
)

;

CREATE TABLE schema_entities (
	name VARCHAR(50) NOT NULL, 
	id SERIAL NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (name)
)

;

CREATE TABLE spaces (
	id SERIAL NOT NULL, 
	name VARCHAR(254) NOT NULL, 
	organization_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(organization_id) REFERENCES organizations (id)
)

;

CREATE TABLE organization_admins (
	id SERIAL NOT NULL, 
	user_id INTEGER, 
	organization_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id), 
	FOREIGN KEY(organization_id) REFERENCES organizations (id)
)

;

CREATE TABLE collections (
	id SERIAL NOT NULL, 
	name VARCHAR(254) NOT NULL, 
	description VARCHAR(254) NOT NULL, 
	owner_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(owner_id) REFERENCES users (id)
)

;

CREATE TABLE schemas (
	id SERIAL NOT NULL, 
	name VARCHAR(50) NOT NULL, 
	version VARCHAR(50) NOT NULL, 
	data JSONB, 
	schema_entity_id INTEGER, 
	PRIMARY KEY (id), 
	CONSTRAINT unique_schema_name_version UNIQUE (name, version), 
	FOREIGN KEY(schema_entity_id) REFERENCES schema_entities (id)
)

;

CREATE TABLE space_admins (
	id SERIAL NOT NULL, 
	user_id INTEGER, 
	space_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id), 
	FOREIGN KEY(space_id) REFERENCES spaces (id)
)

;

CREATE TABLE data_assets (
	id SERIAL NOT NULL, 
	name VARCHAR(254), 
	location VARCHAR(254), 
	external_links JSONB, 
	data JSONB, 
	schema_id INTEGER, 
	space_id INTEGER, 
	PRIMARY KEY (id), 
	CONSTRAINT unique_data_asset_name_space_id UNIQUE (name, space_id), 
	FOREIGN KEY(schema_id) REFERENCES schemas (id), 
	FOREIGN KEY(space_id) REFERENCES spaces (id)
)

;

CREATE TABLE subjects (
	id SERIAL NOT NULL, 
	name VARCHAR(254) NOT NULL, 
	data JSONB, 
	schema_id INTEGER, 
	space_id INTEGER, 
	PRIMARY KEY (id), 
	CONSTRAINT unique_subject_name_space_id UNIQUE (name, space_id), 
	FOREIGN KEY(schema_id) REFERENCES schemas (id), 
	FOREIGN KEY(space_id) REFERENCES spaces (id)
)

;

CREATE TABLE specimen_procedures (
	id SERIAL NOT NULL, 
	data JSONB, 
	schema_id INTEGER, 
	space_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(schema_id) REFERENCES schemas (id), 
	FOREIGN KEY(space_id) REFERENCES spaces (id)
)

;

CREATE TABLE instruments (
	id SERIAL NOT NULL, 
	name VARCHAR(254) NOT NULL, 
	data JSONB, 
	schema_id INTEGER, 
	space_id INTEGER, 
	PRIMARY KEY (id), 
	CONSTRAINT unique_instrument_name_space_id UNIQUE (name, space_id), 
	FOREIGN KEY(schema_id) REFERENCES schemas (id), 
	FOREIGN KEY(space_id) REFERENCES spaces (id)
)

;

CREATE TABLE collection_data_assets (
	collection_id INTEGER NOT NULL, 
	data_asset_id INTEGER NOT NULL, 
	PRIMARY KEY (collection_id, data_asset_id), 
	FOREIGN KEY(collection_id) REFERENCES collections (id), 
	FOREIGN KEY(data_asset_id) REFERENCES data_assets (id)
)

;

CREATE TABLE specimens (
	id SERIAL NOT NULL, 
	name VARCHAR(254) NOT NULL, 
	data JSONB, 
	schema_id INTEGER, 
	space_id INTEGER, 
	subject_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(schema_id) REFERENCES schemas (id), 
	FOREIGN KEY(space_id) REFERENCES spaces (id), 
	FOREIGN KEY(subject_id) REFERENCES subjects (id)
)

;

CREATE TABLE subject_procedures (
	id SERIAL NOT NULL, 
	data JSONB, 
	schema_id INTEGER, 
	space_id INTEGER, 
	subject_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(schema_id) REFERENCES schemas (id), 
	FOREIGN KEY(space_id) REFERENCES spaces (id), 
	FOREIGN KEY(subject_id) REFERENCES subjects (id)
)

;

CREATE TABLE acquisitions (
	id SERIAL NOT NULL, 
	data JSONB, 
	schema_id INTEGER, 
	space_id INTEGER, 
	data_asset_id INTEGER, 
	instrument_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(schema_id) REFERENCES schemas (id), 
	FOREIGN KEY(space_id) REFERENCES spaces (id), 
	FOREIGN KEY(data_asset_id) REFERENCES data_assets (id), 
	FOREIGN KEY(instrument_id) REFERENCES instruments (id)
)

;

CREATE TABLE quality_controls (
	id SERIAL NOT NULL, 
	data JSONB, 
	schema_id INTEGER, 
	space_id INTEGER, 
	data_asset_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(schema_id) REFERENCES schemas (id), 
	FOREIGN KEY(space_id) REFERENCES spaces (id), 
	FOREIGN KEY(data_asset_id) REFERENCES data_assets (id)
)

;

CREATE TABLE processes (
	id SERIAL NOT NULL, 
	data JSONB, 
	schema_id INTEGER, 
	space_id INTEGER, 
	output_data_asset_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(schema_id) REFERENCES schemas (id), 
	FOREIGN KEY(space_id) REFERENCES spaces (id), 
	FOREIGN KEY(output_data_asset_id) REFERENCES data_assets (id)
)

;

CREATE TABLE process_inputs (
	data_asset_id INTEGER NOT NULL, 
	process_id INTEGER NOT NULL, 
	PRIMARY KEY (data_asset_id, process_id), 
	FOREIGN KEY(data_asset_id) REFERENCES data_assets (id), 
	FOREIGN KEY(process_id) REFERENCES processes (id)
)

;

CREATE TABLE subject_procedure_outputs (
	specimen_id INTEGER NOT NULL, 
	subject_procedure_id INTEGER NOT NULL, 
	PRIMARY KEY (specimen_id, subject_procedure_id), 
	FOREIGN KEY(specimen_id) REFERENCES specimens (id), 
	FOREIGN KEY(subject_procedure_id) REFERENCES subject_procedures (id)
)

;

CREATE TABLE specimen_procedure_inputs (
	specimen_id INTEGER NOT NULL, 
	specimen_procedure_id INTEGER NOT NULL, 
	PRIMARY KEY (specimen_id, specimen_procedure_id), 
	FOREIGN KEY(specimen_id) REFERENCES specimens (id), 
	FOREIGN KEY(specimen_procedure_id) REFERENCES specimen_procedures (id)
)

;

CREATE TABLE specimen_procedure_outputs (
	specimen_id INTEGER NOT NULL, 
	specimen_procedure_id INTEGER NOT NULL, 
	PRIMARY KEY (specimen_id, specimen_procedure_id), 
	FOREIGN KEY(specimen_id) REFERENCES specimens (id), 
	FOREIGN KEY(specimen_procedure_id) REFERENCES specimen_procedures (id)
)

;

CREATE TABLE acquisition_subjects (
	acquisition_id INTEGER NOT NULL, 
	subject_id INTEGER NOT NULL, 
	PRIMARY KEY (acquisition_id, subject_id), 
	FOREIGN KEY(acquisition_id) REFERENCES acquisitions (id), 
	FOREIGN KEY(subject_id) REFERENCES subjects (id)
)

;

CREATE TABLE acquisition_specimens (
	acquisition_id INTEGER NOT NULL, 
	specimen_id INTEGER NOT NULL, 
	PRIMARY KEY (acquisition_id, specimen_id), 
	FOREIGN KEY(acquisition_id) REFERENCES acquisitions (id), 
	FOREIGN KEY(specimen_id) REFERENCES specimens (id)
)

;
CREATE VIEW data_asset_view AS SELECT data_assets.id AS data_asset_id, acquisitions.id AS acquisition_id, subjects.id AS subject_id, processes.id AS process_id, subject_procedures.id AS subject_procedure_id, quality_controls.id AS quality_control_id, instruments.id AS instrument_id, processes.data AS processes_data, acquisitions.data AS acquisition_data, instruments.name AS instrument_name, instruments.data AS instrument_data, data_assets.location AS data_asset_location, data_assets.name AS data_asset_name, data_assets.data AS data_asset_data, data_assets.external_links AS data_asset_external_links, subjects.name AS subject_name, subjects.data AS subject_data, subject_procedures.data AS subject_procedures_data, quality_controls.data AS quality_control_data 
FROM data_assets LEFT OUTER JOIN acquisitions ON data_assets.id = acquisitions.data_asset_id LEFT OUTER JOIN instruments ON instruments.id = acquisitions.instrument_id LEFT OUTER JOIN quality_controls ON data_assets.id = quality_controls.data_asset_id LEFT OUTER JOIN processes ON data_assets.id = processes.output_data_asset_id JOIN acquisition_subjects ON acquisitions.id = acquisition_subjects.acquisition_id JOIN subjects ON subjects.id = acquisition_subjects.subject_id LEFT OUTER JOIN subject_procedures ON subject_procedures.subject_id = subjects.id;
