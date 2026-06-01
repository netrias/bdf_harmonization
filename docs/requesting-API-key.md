# API Key Provisioning Guide

## 📢 Announcements

### Jun 1, 2026

- **Data Chord no longer requires an API key.** The hosted early-access Data Chord web application uses email-based authentication.
- API keys are only required for the **[Netrias Client](https://github.com/netrias/netrias_client)** or **direct REST API access**.
- To request access to the hosted Data Chord web app, email [bdf_strides@netrias.com](mailto:bdf_strides@netrias.com) and include the email address you would like to use for authentication.
- Verification emails may land in spam or junk folders. Look for messages from `no-reply@verificationemail.com`.

### Feb 18, 2026

- Due to major system updates, all API keys provisioned prior to Feb 18, 2026 have been deprecated. Users who need Netrias Client or direct REST API access should request a new key.

## Overview

This guide explains how to request an API key for the Netrias Harmonization platform.

API keys are required for:

- Netrias Client access
- Direct REST API access

API keys are **not** required for the hosted Data Chord web application. Data Chord uses email-based authentication instead.

The hosted early-access Data Chord app is available here:

[https://netrias-data-chord.netriasbdf.cloud/stage-1](https://netrias-data-chord.netriasbdf.cloud/stage-1)

## Who Can Request a Key?

- BDF performers
- NIH staff
- Third-party integrators, provided a mutual NDA and data-use agreement are in place first

## Request Process

1. **Prepare your details** – Collect the following information:

   | Field                     | Why we need it                                              |
   | ------------------------- | ----------------------------------------------------------- |
   | **Name**                  | Identifies the responsible individual.                      |
   | **Organization / Team**   | Helps us assign the correct quota.                          |
   | **Intended use case**     | Brief description, e.g., “Testing the Netrias Client on XYZ data.” |
   | **Estimated data volume** | Example: 50 CSV, TSV, or Excel (`.xlsx`) files with 3,000 rows each.                 |

2. **Submit your request** – Email the above details to **Netrias** at [bdf_strides@netrias.com](mailto:bdf_strides@netrias.com) with the subject line **“API Key Request – Netrias BDF”**.

3. **Approval and issuance** – Netrias will confirm receipt within *1 business day* and issue:

   - Your **API key**
   - The **expiration / rotation schedule**

   By default, keys do **not** automatically expire at the 12-month mark, but we may email you to confirm whether you are still using the key.

4. **Store the key securely**

   - **Never** commit keys to source control.
   - Rotate immediately if you suspect compromise.

## Netrias Client

For programmatic access, use the **[Netrias Client](https://github.com/netrias/netrias_client)**. The client supports discovery, harmonization, and data model store workflows from Python. Its installation and usage documentation is maintained in the Netrias Client repository.

You will need an API key before using the Netrias Client. Once your key is issued, follow the setup instructions in the client repository.

## Hosted Data Chord Access

To access the hosted Data Chord web application, email [bdf_strides@netrias.com](mailto:bdf_strides@netrias.com) with the email address you would like to use for authentication.

Once your email is added to the system, you should receive a verification email. These emails may land in spam or junk folders, so please look for messages from `no-reply@verificationemail.com`.

## Key Lifecycle Management

| Action                | Contact                                                       | Typical SLA                                  |
| --------------------- | ------------------------------------------------------------- | -------------------------------------------- |
| **Rotate / Revoke**   | Email [bdf_strides@netrias.com](mailto:bdf_strides@netrias.com) | 4 business hours                             |
| **Report compromise** | Same as above                                                 | Immediate; key disabled upon receipt          |

## Changelog

- 2026-06-01 – Added Netrias Client link and clarified that API keys are required for Netrias Client usage.
- 2026-06-01 – Clarified that hosted Data Chord uses email-based authentication and that API keys are only needed for the Netrias Client or direct REST API access.
- 2026-02-18 – Updated with deprecation announcement.
- 2025-07-08 – Initial draft of API Key Provisioning Guide.
