# API Key Provisioning Guide

## 📢 Annoucements
### Feb 18, 2026

- Due to the major updates of the system we have deprecated all API keys provisioned prior to Feb 18, 2026 and ask that users reach out to us to acquire a new key.

## Overview

In order to use any part of the systems (Data Chord, Python Clien, or API) users must obtain an API key from Netrias. This is to safeguard against abuse or unintended acess.

## Who Can Request a Key?

* BDF Performers.
* NIH Staff.
* For third‑party integrators, a mutual NDA and data‑use agreement must be in place first.

## Request Process

1. **Prepare your details** – Collect the following information:

   | Field                              | Why we need it                                                            |
   | ---------------------------------- | ------------------------------------------------------------------------- |
   | **Name**                           | Identify the responsible individual.                                      |
   | **Organization / Team**            | Helps us assign the correct quota.                                        |
   | **Intended use‑case**              | Brief description (e.g., “Testing Data Chord on XYZ Data”).               |
   | **Estimated data volume**          | e.g., 50 CSV files with 3K rows each                                      |

2. **Submit your request** – Email the above details to **Netrias** at **[bdf_strides@netrias.com](mailto:bdf_strides@netrias.com)** with subject line **“API Key Request – Netrias BDF”**.

3. **Approval & issuance** – Netrias will confirm receipt within *1 business day* and issue:

   * Your **API key**.
   * **Expiration / rotation schedule** (default: keys will **not** automatically expire at the 12 month mark but we will email you to cofirm you are still using it).

4. **Store the key securely**

   * **Never** commit keys to source control.
   * Rotate immediately if you suspect compromise.

## Key Lifecycle Management

| Action                | Contact                                                 | Typical SLA                           |
| --------------------- | ------------------------------------------------------- | ------------------------------------- |
| **Rotate / Revoke**   | Email [bdf_strides@netrias.com](mailto:bdf_strides@netrias.com)   | 4 business hours                      |
| **Report compromise** | Same as above                                           | Immediate – key disabled upon receipt |

## Changelog
* 2026-02-18 - Updated with deprecation anoucement.
* 2025‑07‑08 – Initial draft of API Key Provisioning Guide.
