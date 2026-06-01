# Common Data Elements and Data Models Overview

## What is a Common Data Element?

A **Common Data Element (CDE)** is a standardized, semantically defined data field. Think of it as a spreadsheet column header whose meaning is precisely described. CDEs come in two varieties:

1. **With a controlled vocabulary** – also called *permissible values* or *standards*; only those values are considered valid.
2. **Without a controlled vocabulary** – any free-text or numeric value is acceptable, though structure or validation rules may still apply.

### Example – CDE with permissible values

```jsonc
{
  "embedding_medium": {
    "description": "A material that infiltrates and supports a specimen and preserves its shape and structure for sectioning and microscopy.",
    "permissible_values": [
      "Paraffin wax",
      "Carbowax",
      "Methacrylate",
      "Epoxy Resin (Araldite)",
      "Agar embedding",
      "Celloidin media",
      "Gelatin",
      "Other",
      "None",
      "Unknown"
    ]
  }
}
```

### Example – CDE without permissible values

```jsonc
{
  "participant_id": {
    "description": "A number or string (potentially containing metadata) that uniquely identifies a participant in a study.",
    "permissible_values": []
  }
}
```

> **Analogy:** Treat the CDE (`embedding_medium`) as the column header and its permissible values (for example, `Carbowax` or `Agar embedding`) as the valid entries in the rows beneath it. For a CDE like `participant_id`, the rows can contain any value the data creator provides.

## What is a Data Model?

A **data model** is an ordered collection of CDEs that work together to describe a particular data-capture scenario, assay, clinical study domain, or metadata submission workflow.

Think of a data model as the **template for a table or collection of tables**: each CDE defines a field, and the data model specifies which fields belong together, their meaning, their version, and whether any fields have controlled vocabularies.

Key attributes of a data model:

| Attribute       | Description                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------------------- |
| **Scope**       | The scientific or operational context it covers, such as RNA-Seq metadata or clinical encounters.       |
| **CDE set**     | The complete list of CDEs, including those that reference controlled vocabularies and those that do not. |
| **Version**     | A version identifier, such as `11.0.4`, that signals when CDE definitions or permissible values change. |
| **Source**      | The authority that curates the data model, such as NCI or Sage Bionetworks.                             |
| **Structure**   | How the CDEs are organized for data entry, validation, and harmonization.                               |

> **Analogy:** If a CDE is a column header, a *data model* is the full spreadsheet template, laying out every column, its meaning, and the allowed values. Versioning helps ensure that your data aligns with the same template your collaborators expect.

---

## Data Models Currently Available

Data Chord currently makes the following data models available through the hosted early-access web application:

<p align="center">
  <img src="images/data_chord_current_data_models.png" alt="Data Chord data model selector" width="55%">
</p>

> **Terminology note:** This documentation uses **data model** as the generic term. Some official Data Chord data model names still include the word “Schema” because that is part of the displayed name used by the upstream community or integration.

### General Commons versions

The **General Commons Data Model** currently includes the following version options in Data Chord:

<p align="center">
  <img src="images/data_chord_current_gc_versions.png" alt="Data Chord General Commons version selector" width="55%">
</p>

Version `11.0.4` includes the completed permissible value updates for the previously noted high-impact CDE groups, including therapeutic agents, diagnoses, morphology, and anatomical-site fields.

### Data model details

| Data model label in Data Chord | Current version information shown in Data Chord | Source |
| ------------------------------ | ----------------------------------------------- | ------ |
| General Commons Data Model     | `11.0.4`, `6.0.5`; version `11.0.4` includes completed PV updates | [NCI General Commons](https://github.com/CBIIT/cds-model/blob/main/model-desc/cds-model-props.yml) |
| CCDI Data Model                | Selectable in Data Chord                        | [NCI Childhood Cancer Data Initiative](https://github.com/CBIIT/ccdi-model/blob/main/model-desc/ccdi-model-props.yml) |
| Sage ChIPSeq Template Schema   | Selectable in Data Chord                        | [Sage Bionetworks / NF-OSI metadata dictionary](https://github.com/nf-osi/nf-metadata-dictionary) |
| Sage Clinical Assay Template Schema | Selectable in Data Chord                    | [Sage Bionetworks / NF-OSI metadata dictionary](https://github.com/nf-osi/nf-metadata-dictionary) |
| Sage Imaging Assay Template Schema  | Selectable in Data Chord                    | [Sage Bionetworks / NF-OSI metadata dictionary](https://github.com/nf-osi/nf-metadata-dictionary) |
| Sage RNASeq Template Schema    | Selectable in Data Chord                        | [Sage Bionetworks / NF-OSI metadata dictionary](https://github.com/nf-osi/nf-metadata-dictionary) |
| Synapse Schema                 | Selectable in Data Chord                        | [Sage Bionetworks / NF-OSI metadata dictionary](https://github.com/nf-osi/nf-metadata-dictionary) |

## Loading Additional Data Models

Our platform is data model agnostic and can ingest virtually any well-structured CDE collection. To request an import of your own CDEs and data model, please review the [submission checklist and instructions](requesting-data-be-added.md).

## Accessing Data Chord

The hosted early-access Data Chord web application is available here:

[https://netrias-data-chord.netriasbdf.cloud/stage-1](https://netrias-data-chord.netriasbdf.cloud/stage-1)

To request access, email [bdf_strides@netrias.com](mailto:bdf_strides@netrias.com) with the email address you would like to use for authentication. Verification emails may land in spam or junk folders, so please look for messages from `no-reply@verificationemail.com`.

## Programmatic Access with the Netrias Client

For Python-based workflows, use the **[Netrias Client](https://github.com/netrias/netrias_client)**. The client provides programmatic access to discovery, harmonization, and data model store services, including listing available data models, CDEs, and permissible values.

The detailed installation and usage documentation lives in the Netrias Client repository so that client-specific examples stay aligned with the latest release. API keys are required for Netrias Client usage; see the [API key request guide](requesting-API-key.md).

## Changelog

- 2026-06-01 – Added Netrias Client reference for programmatic data model, CDE, and permissible value access.
- 2026-06-01 – Updated General Commons `11.0.4` notes to reflect completed permissible value updates.
- 2026-06-01 – Standardized terminology around data models and updated screenshots for the hosted early-access Data Chord application.
- 2026-06-01 – Updated Data Chord access instructions for the hosted early-access web application.
- 2026-02-18 – Updated to describe data models available in Data Chord.
- 2025-07-08 – Initial draft of CDE and data model overview.
