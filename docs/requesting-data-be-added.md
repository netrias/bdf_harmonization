# Getting Your Data Model Added to the Harmonization API

## Overview

The Netrias Harmonization platform is intentionally **data model agnostic**. If you maintain a data model built around [Common Data Elements](what-we-harmonize.md) (CDEs) or something fairly similar and would like it available as a first‑class *target schema* inside our system, we’re happy to ingest it.

Adding a schema means that:

* You can suggest your CDEs when users present matching columns.
* can map free‑text values to the permissible values you define.

Just follow the request process below to get things started.

---

## Request Process

| Step  | Action                      | Details                                                                                                                                       |
| ----- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | **Email**                   | Email [bdf_strides@netrias.com](mailto:bdf_strides@netrias.com) with subject **“New Data Model Submission Request”**. Introduce yourself, your organization, and a bit about your data model. |
| **2** | **Video Chat about Data** | After your initial email we'll setup a quick video call with you to have you take us through your data model in detail.                                                                                           |
| **3** | **Prepare your submission** | Use the checklist below to gather files.                                                                                           |
| **4** | **Submit your submission** | Email or securly share your submission files with us.                                                                                           |
| **5** | **Review & QA**             | We’ll acknowledge within **1 business day** and aim to load & validate in **3–5 business days**.                                              |
| **6** | **Acceptance**              | You’ll receive a endpoint + changelog for sign‑off.                                                                 |

> **Need an NDA?** Mention it in your email and we’ll send the appropriate paperwork.

---

## Submission Checklist

During the video call we'll mention these items and ask that you have them ready as part of the submission.

| #  | Required? | Item                        | What to provide                                                                                       | Tips                                                     |
| -- | --------- | --------------------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| 1  | **✅**     | **Schema file**             | JSON Schema (`*.json`) *or* YAML (`*.yml`) that enumerates every CDE (field name, description, type). | Make sure it parses with `jsonschema` or `yamllint`.     |
| 2  | **✅**     | **CDE dictionary**          | For each CDE: description, permissible values (if any). CSV or JSON OK.         | Use UTF‑8.         |
| 3  | **✅**     | **Version tag**             | Semantic version (e.g., `v1.0.0`).                                                                    | Increment when permissible values or definitions change. |
| 4  | **✅**     | **Owner contact**           | Name + email of technical owner.                                                                      | We’ll tag you on issue tickets.                          |
| 5  | **☑️**    | **Sample dataset**          | 10–100 representative rows in CSV/TSV.                                                                | Helps us smoke‑test `/harmonize`.                        |
| 6  | **☑️**    | **Changelog**               | `CHANGELOG.md` documenting prior releases.                                                            | Keeps downstream users informed.                         |
| 7  | **☑️**    | **Diagram / README**        | A brief schema or CDE‑relationship diagram.                                                   | Optional but great for docs.                             |


> **Notation:** ✅ = mandatory, ☑️ = optional.

---

### Changelog

* 2025‑07‑22 – Added full data model submission request process.