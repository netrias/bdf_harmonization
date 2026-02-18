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

* **CDE discovery** – automatically find the best Common Data Element (CDE) for an arbitrary table column.
* **Value harmonization** – map free‑text cell values to controlled vocabularies.
* **End‑to‑end pipelines** – batch‑convert entire spreadsheets into standards‑ready JSON.

---

## 📚 Documentation Tour

Follow this sequence for a smooth on‑boarding. Each step links to a dedicated page with more inforamtion and examples.

| Step | Topic                     | File                                                                                    | Why read it first?                                              |
| :--: | ------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
|   1  | **What We Harmonize**     | [`what-we-harmonize.md`](docs/what-we-harmonize.md)                                     | Learn the core concepts & data models (CDEs + Schemas).         |
|   2  | **Request an API Key**    | [`requesting-API-key.md`](docs/requesting-API-key.md)                                   | Get your credentials to use the tooling .                       |
|   3  | **Install Data Chord**    | [Data Chord Github Page](https://github.com/netrias/data_chord)                         | No-code user interface for guided harmoization.                 |
|   4  | **Install the Python Client**    | *Coming March 2026*                                                              | Advanced usage to build end-to-end harmonization pipelines.     |
|   5  | **Submit Your Own CDEs**  | [`requesting-data-be-added.md`](docs/requesting-data-be-added.md)                       | How to get your custom data loaded into the platform.           |
---

## 🚀 No Code Getting Started Steps

### 1 · Request an API key

See [`requesting-API-key.md`](requesting-API-key.md) and email the necessary info to us. Store the key in a password manager or other secure location.

### 2 · Install Data Chord

Visit the [Data Chord Github Repo](https://github.com/netrias/data_chord) and follow the First-Time Setup instructions.

### 3 · Open Data Chord in your browser

After you've run the application just open http://localhost:8000 in your browser and you should see the Data Chord upload screen.

### 4 · Upload your first CSV file

Data Chord currently only supports CSV files so any spreadhseets will need to be converted to that format. 

### 5 · Follow the guided harmonization workflow

We've designed Data Chord to guide the user through haromnizing the columns of intereste in their uploaded spreadsheet.

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

© 2025 Netrias LLC - Released under the Apache 2.0 license.
