from sqlmodel import SQLModel, Field, Column, Relationship
from typing import Dict, Any, List
from sqlalchemy.dialects.postgresql import JSONB

# Link Tables #################################################################

# class ProcessInputs(SQLModel, table=True):
#     data_asset_id: int | None = Field(
#         default=None, foreign_key="DataAssets.id", primary_key=True
#     )
#     process_id: int | None = Field(
#         default=None, foreign_key="Processes.id", primary_key=True
#     )
#
# class SubjectProcedureOutputs(SQLModel, table=True):
#     data_asset_id: int | None = Field(
#         default=None, foreign_key="DataAssets.id", primary_key=True
#     )
#     process_id: int | None = Field(
#         default=None, foreign_key="Processes.id", primary_key=True
#     )
#
# class SpecimenProcedureInputs(SQLModel, table=True):
#     specimen_id: int | None = Field(
#         default=None, foreign_key="Specimens.id", primary_key=True
#     )
#     specimen_procedure_id: int | None = Field(
#         default=None, foreign_key="SpecimenProcedures.id", primary_key=True
#     )
#
# class SpecimenProcedureOutputs(SQLModel, table=True):
#     specimen_id: int | None = Field(
#         default=None, foreign_key="Specimens.id", primary_key=True
#     )
#     specimen_procedure_id: int | None = Field(
#         default=None, foreign_key="SpecimenProcedures.id", primary_key=True
#     )
#
# class AcquisitionSubjects(SQLModel, table=True):
#     acquisition_id: int | None = Field(
#         default=None, foreign_key="Acquisitions.id", primary_key=True
#     )
#     subject_id: int | None = Field(
#         default=None, foreign_key="Subjects.id", primary_key=True
#     )
#
# class AcquisitionSpecimens(SQLModel, table=True):
#     acquisition_id: int | None = Field(
#         default=None, foreign_key="Acquisitions.id", primary_key=True
#     )
#     specimen_id: int | None = Field(
#         default=None, foreign_key="Specimens.id", primary_key=True
#     )

class CollectionDataAssets(SQLModel, table=True):
    collection_id: int | None = Field(
        default=None, foreign_key="collections.id", primary_key=True
    )
    data_asset_id: int | None = Field(
        default=None, foreign_key="dataassets.id", primary_key=True
    )
