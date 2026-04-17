from sqlmodel import SQLModel, Field

# Link Tables #################################################################

class ProcessInputs(SQLModel, table=True):
    __tablename__ = "process_inputs"
    data_asset_id: int | None = Field(
        default=None, foreign_key="data_assets.id", primary_key=True
    )
    process_id: int | None = Field(
        default=None, foreign_key="processes.id", primary_key=True
    )

class SubjectProcedureOutputs(SQLModel, table=True):
    __tablename__ = "subject_procedure_outputs"
    specimen_id: int | None = Field(
        default=None, foreign_key="specimens.id", primary_key=True
    )
    subject_procedure_id: int | None = Field(
        default=None, foreign_key="subject_procedures.id", primary_key=True
    )

class SpecimenProcedureInputs(SQLModel, table=True):
    __tablename__ = "specimen_procedure_inputs"
    specimen_id: int | None = Field(
        default=None, foreign_key="specimens.id", primary_key=True
    )
    specimen_procedure_id: int | None = Field(
        default=None, foreign_key="specimen_procedures.id", primary_key=True
    )

class SpecimenProcedureOutputs(SQLModel, table=True):
    __tablename__ = "specimen_procedure_outputs"
    specimen_id: int | None = Field(
        default=None, foreign_key="specimens.id", primary_key=True
    )
    specimen_procedure_id: int | None = Field(
        default=None, foreign_key="specimen_procedures.id", primary_key=True
    )

class AcquisitionSubjects(SQLModel, table=True):
    __tablename__ = "acquisition_subjects"
    acquisition_id: int | None = Field(
        default=None, foreign_key="acquisitions.id", primary_key=True
    )
    subject_id: int | None = Field(
        default=None, foreign_key="subjects.id", primary_key=True
    )

class AcquisitionSpecimens(SQLModel, table=True):
    __tablename__ = "acquisition_specimens"
    acquisition_id: int | None = Field(
        default=None, foreign_key="acquisitions.id", primary_key=True
    )
    specimen_id: int | None = Field(
        default=None, foreign_key="specimens.id", primary_key=True
    )

class CollectionDataAssets(SQLModel, table=True):
    __tablename__ = "collection_data_assets"
    collection_id: int | None = Field(
        default=None, foreign_key="collections.id", primary_key=True
    )
    data_asset_id: int | None = Field(
        default=None, foreign_key="data_assets.id", primary_key=True
    )
