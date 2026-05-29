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

CREATE INDEX collection_data_assets_index ON collection_data_assets (data_asset_id);

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

CREATE INDEX specimens_index ON specimens (name, subject_id);

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

CREATE INDEX subject_procedures_index ON subject_procedures (subject_id);

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

CREATE INDEX acquisitions_index ON acquisitions (data_asset_id, instrument_id);

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

CREATE INDEX quality_controls_index ON quality_controls (data_asset_id);

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

CREATE INDEX processes_index ON processes (output_data_asset_id);

CREATE TABLE process_inputs (
	data_asset_id INTEGER NOT NULL, 
	process_id INTEGER NOT NULL, 
	PRIMARY KEY (data_asset_id, process_id), 
	FOREIGN KEY(data_asset_id) REFERENCES data_assets (id), 
	FOREIGN KEY(process_id) REFERENCES processes (id)
)

;

CREATE INDEX process_inputs_index ON process_inputs (process_id);

CREATE TABLE subject_procedure_outputs (
	specimen_id INTEGER NOT NULL, 
	subject_procedure_id INTEGER NOT NULL, 
	PRIMARY KEY (specimen_id, subject_procedure_id), 
	FOREIGN KEY(specimen_id) REFERENCES specimens (id), 
	FOREIGN KEY(subject_procedure_id) REFERENCES subject_procedures (id)
)

;

CREATE INDEX subject_procedure_outputs_index ON subject_procedure_outputs (subject_procedure_id);

CREATE TABLE specimen_procedure_inputs (
	specimen_id INTEGER NOT NULL, 
	specimen_procedure_id INTEGER NOT NULL, 
	PRIMARY KEY (specimen_id, specimen_procedure_id), 
	FOREIGN KEY(specimen_id) REFERENCES specimens (id), 
	FOREIGN KEY(specimen_procedure_id) REFERENCES specimen_procedures (id)
)

;

CREATE INDEX specimen_procedure_inputs_index ON specimen_procedure_inputs (specimen_procedure_id);

CREATE TABLE specimen_procedure_outputs (
	specimen_id INTEGER NOT NULL, 
	specimen_procedure_id INTEGER NOT NULL, 
	PRIMARY KEY (specimen_id, specimen_procedure_id), 
	FOREIGN KEY(specimen_id) REFERENCES specimens (id), 
	FOREIGN KEY(specimen_procedure_id) REFERENCES specimen_procedures (id)
)

;

CREATE INDEX specimen_procedure_outputs_index ON specimen_procedure_outputs (specimen_procedure_id);

CREATE TABLE acquisition_subjects (
	acquisition_id INTEGER NOT NULL, 
	subject_id INTEGER NOT NULL, 
	PRIMARY KEY (acquisition_id, subject_id), 
	FOREIGN KEY(acquisition_id) REFERENCES acquisitions (id), 
	FOREIGN KEY(subject_id) REFERENCES subjects (id)
)

;

CREATE INDEX acquisition_subjects_index ON acquisition_subjects (subject_id);

CREATE TABLE acquisition_specimens (
	acquisition_id INTEGER NOT NULL, 
	specimen_id INTEGER NOT NULL, 
	PRIMARY KEY (acquisition_id, specimen_id), 
	FOREIGN KEY(acquisition_id) REFERENCES acquisitions (id), 
	FOREIGN KEY(specimen_id) REFERENCES specimens (id)
)

;

CREATE INDEX acquisition_specimens_index ON acquisition_specimens (specimen_id);

CREATE VIEW data_asset_view
AS SELECT
    data_assets.id AS data_asset_id,
    acquisitions.id AS acquisition_id,
    instruments.id AS instrument_id,
    processes.id AS process_id,
    data_assets.name AS data_asset_name,
    data_assets.location AS data_asset_location,
    data_assets.external_links AS data_asset_external_links,
    instruments.name AS instrument_name,
    data_assets.data AS data_asset_data,
    acquisitions.data AS acquisition_data,
    processes.data AS processes_data,
    instruments.data AS instrument_data,
    agg1.items as quality_control_metrics,
    agg2.items as subjects,
    agg3.items as subject_procedures
FROM data_assets
LEFT OUTER JOIN acquisitions ON data_assets.id = acquisitions.data_asset_id
LEFT OUTER JOIN instruments ON instruments.id = acquisitions.instrument_id
LEFT OUTER JOIN processes ON data_assets.id = processes.output_data_asset_id
LEFT JOIN LATERAL (
    SELECT COALESCE(jsonb_agg(jsonb_build_object('quality_control_id', quality_controls.id, 'data', quality_controls.data)), '[]') as items
    FROM quality_controls
    WHERE quality_controls.data_asset_id = data_assets.id
) agg1 ON true
JOIN acquisition_subjects ON acquisitions.id = acquisition_subjects.acquisition_id
LEFT JOIN LATERAL (
    SELECT COALESCE(jsonb_agg(jsonb_build_object('subject_id', subjects.id, 'data', subjects.data)), '[]') as items
    FROM subjects
    WHERE subjects.id = acquisition_subjects.subject_id
) agg2 ON true
LEFT JOIN LATERAL (
    SELECT COALESCE(jsonb_agg(jsonb_build_object('subject_id', subject_procedures.subject_id, 'subject_procedures_id',  subject_procedures.id,'data', subject_procedures.data)), '[]') as items
    FROM subject_procedures
    WHERE subject_procedures.subject_id = acquisition_subjects.subject_id
) agg3 ON true
;
