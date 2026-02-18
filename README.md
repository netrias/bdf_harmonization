<p align="center">
  <a href="https://netrias.com">
    <img src="docs/images/NETRIAS Logotype_Full Color RGB.png" height="150">
  </a>
</p>

<div align="center">

# Netrias Metadata Harmonization Tooling

> **Turn messy biomedical metadata into clean, standards‑compliant records in just a few clicks.**

![Python 3.13+](https://img.shields.io/badge/python-3.13%2B-blue) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

</div>

## 📢 Latest Updates

### Feb 18, 2026

The Netrias Harmonization platform has undergone a significant update. As of Feb 2026, we’re doing the first of several releases:

- **UI upgrade:** Our UI harmonization tool has been significantly upgraded and is now called **Data Chord** (🎶 it harmonizes your data 🎶).
- **Python client:** Major improvements are underway, with a release planned for **March 2026**.
- **API updates:** We’ve made major updates to the underlying API. As a result, API access is **restricted for now**, since most users will find the Python client easier to use.
  - If you need API access, please reach out using the contact information on the **[API key request page](docs/requesting-API-key.md)**.


## ℹ️ About 
The Netrias Harmonization platform provides a user interface (Data Chord), a Python client, and REST endpoints for:

* **CDE discovery** – automatically get recommendations for which Common Data Element (CDE) should apply to each column in your dataset* 
* **Value harmonization** – map free‑text cell values to controlled vocabularies.
* **End‑to‑end pipelines** – batch conform entire spreadsheets into standards conformance.

---

## 📚 Documentation Tour

Follow this sequence for a smooth on‑boarding. Each step links to a dedicated page with more inforamtion and examples.

| Step | Topic                     | File                                                                                    | Why read it first?                                              |
| :--: | ------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
|   1  | **What We Harmonize**     | [`what-we-harmonize.md`](docs/what-we-harmonize.md)                                     | Learn the core concepts & data models (CDEs + Schemas).         |
|   2  | **Request an API Key**    | [`requesting-API-key.md`](docs/requesting-API-key.md)                                   | Get your credentials to use the tooling .                       |
|   3  | **Install Data Chord**    | [Data Chord Github Page](https://github.com/netrias/data_chord/tree/v1.0.0?tab=readme-ov-file#data-chord)                         | No-code user interface for guided harmoization.                 |
|   4  | **Install the Python Client**    | *Coming March 2026*                                                              | Advanced usage to build end-to-end harmonization pipelines.     |
|   5  | **Submit Your Own CDEs**  | [`requesting-data-be-added.md`](docs/requesting-data-be-added.md)                       | How to get your custom data loaded into the platform.           |
---

## 🚀 No Code Getting Started Steps

### 1 · Request an API key

See [`requesting-API-key.md`](requesting-API-key.md) and email the necessary info to us. Store the key in a password manager or other secure location.

### 2 · Install Data Chord

Visit the [Data Chord Github Repo](https://github.com/netrias/data_chord/tree/v1.0.0?tab=readme-ov-file#data-chord) and follow the First-Time Setup instructions.

### 3 · Open Data Chord in your browser

After you've run the application just open http://localhost:8000 in your browser and you should see the Data Chord upload screen.

### 4 · Upload your first CSV file

Data Chord currently only supports CSV files so any spreadhseets will need to be converted to that format. 

### 5 · Follow the guided harmonization workflow

We've designed Data Chord to guide the user through haromnizing the columns of intereste in their uploaded spreadsheet.

## ⚠️ Caveats / Known Limitations

### 1) Some high-cardinality CDEs must be selected manually
To keep the recommendation experience fast and reliable in early releases, the system **does not currently recommend certain CDEs with very large permissible value (PV) lists**. If your CSV has column(s) that map to one of the CDEs below, please **select it manually** in Data Chord.

**General Commons (`gc`) — not recommended (manual selection required):**
- `therapeutic_agents` (PV count: 4475)
- `primary_diagnosis` (3378)
- `morphology` (1152)
- `site_of_resection_or_biopsy` (614)
- `tissue_or_organ_of_origin` (614)
- `sample_anatomic_site` (340)
- `organ_or_tissue` (333)
- `primary_site` (246)
- `role_or_affiliation` (140)

**Synapse (`synapse`) — not recommended:**
- `Institution` (325)
- `Assay` (186)
- `ProtocolAssay` (186)
- `ModelSystemName` (154)
- `FileFormat` (114)
- `Platform` (113)

**Synapse ChIP-Seq Template (`sage_chipseq_template`) — not recommended:**
- `assay` (188)
- `fileFormat` (114)
- `platform` (114)

**Synapse Clinical Assay Template (`sage_clinical_assay_template`) — not recommended:**
- `assay` (188)
- `fileFormat` (114)

**Synapse Imaging Assay Template (`sage_imaging_assay_template`) — not recommended:**
- `assay` (188)
- `fileFormat` (114)
- `platform` (114)

**Childhood Cancer Data Initiative (`ccdi`) — not recommended:**
- `treatment_agent` (4477)
- `laboratory_test_name` (1055)
- `adverse_event` (790)
- `diagnosis` (540)
- `anatomic_site` (359)
- `alteration` (208)
- `comorbidity` (143)
- `relationship` (118)

---

### 2) General Commons model quality may vary for specific CDEs (PV updates in progress)
For **General Commons (`gc`)**, some LLM behavior may be less accurate for a subset of CDEs because the system is currently using **older PV versions**. Updates are in progress to align these CDEs with newer, authoritative sources:

- `therapeutic_agents`  
  - Planned update: all descendants under NCIt **Pharmacological Substance (C1909)** and **Drug or Chemical by Structure (C1913)**
- `primary_diagnosis`  
  - Planned update: all descendants under NCIt **Disease or Diagnosis (C2991)**
- `morphology`  
  - Planned update: **ICD-O-3**
- `site_of_resection_or_biopsy`  
  - Planned update: **Uberon ontology**
- `tissue_or_organ_of_origin`  
  - Planned update: **Uberon ontology**
- `sample_anatomic_site`  
  - Planned update: **Uberon ontology**

If you encounter unexpected recommendations or value mappings in these areas, please open an issue (include the schema + column name + a few sample values) so we can reproduce and prioritize fixes.

---

### 3) Early-release performance limits (large harmonization jobs)
Data Chord is an early release and may become overloaded when harmonizing **many unique values at once**. In these cases you may see a **“harmonization job failed”** error after clicking **Harmonize**.

If this happens:
- Reduce the number of columns you harmonize at one time, **or**
- Harmonize the highest-priority columns first, then continue in smaller batches

This helps keep the job size manageable while we continue improving throughput and reliability.

---

## 🤔 Questions or Suggestions

We encourage users to open github issues in this repo https://github.com/netrias/bdf_harmonization/issues with any questions, bugs, or feature requests they may have. Our goal is to work closely with users and build tooling that helps them harmonize metadata faster, more efficiently, and more accurately.

---

## 💰 Funding

Generously supported by ARPA-H via funding from the [Biomedical Data Fabric (BDF) Toolbox](https://arpa-h.gov/explore-funding/programs/arpa-h-bdf-toolbox) program.

---

## 🤝 Contributing

We gladly accept pull requests that improve docs, examples, or client code. Please open an issue first if you plan a large change.

---

## 📜 License

© 2026 Netrias LLC - Released under the Apache 2.0 license.
