# south-korea-business-kyb-verification-example

Official Python example and SDK integration for South Korea Business Registration Number (BRN) and KYB Verification API.

[![RapidAPI](https://img.shields.io/badge/RapidAPI-South%20Korea%20KYB-blue)](https://rapidapi.com/c0dem0nkey123/api/south-korea-business-kyb-verification)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)

A lightweight Python example for verifying **South Korean Business Registration Numbers (사업자등록번호)** and performing real-time **Know Your Business (KYB)** checks using public government registers.

## Overview

When onboarding South Korean corporate clients, suppliers, or vendors, international businesses face challenges with language barriers and local register validation. This API solves these friction points by aggregating data from official South Korean public databases (FTC, PPS/G2B) in real-time.

### Key Features
* **Real-Time Verification**: Verifies active commercial status from Fair Trade Commission (FTC) data.
* **Debarment & Sanction Checks**: Checks public procurement debarment records maintained by Public Procurement Service (PPS/G2B).
* **Automated English Translation**: Instantly converts Korean company names, representative names, and business addresses into English.
* **Standardized KYB Flags**: Returns JSON indicators (`kyb_pass`, `tax_authority_active`, `public_procurement_debarred`) for automated risk pipelines.

---

## Request Parameter Guide

All requests are sent via HTTP GET to the `/v1/verify` endpoint.

- **`brn`** (required, string): The 10-digit Business Registration Number (사업자등록번호) issued by the National Tax Service of South Korea.
- **Format**: 10 digits without hyphens (e.g., `1248100998`) or with hyphens (e.g., `124-81-00998`).
- **Test Example**: `1248100998` (Samsung Electronics)

---

## Quick Start

### 1. Prerequisites
Get your free API key from [RapidAPI Marketplace](https://rapidapi.com/c0dem0nkey123/api/south-korea-business-kyb-verification).

### 2. Installation
Clone this repository and install dependencies:

```bash
git clone https://github.com/c0dem0nkey123/south-korea-business-kyb-verification-example.git
cd south-korea-business-kyb-verification-example
pip install -r requirements.txt
```

### 3. Usage
Set your RapidAPI key as an environment variable or edit `main.py`, then run:

```bash
export RAPIDAPI_KEY="your_rapidapi_key_here"
python main.py
```

---

## Sample API Output (JSON)

```json
{
  "brn": "1248100998",
  "status": "ACTIVE",
  "company_name_en": "Samsung Electronics Co., Ltd.",
  "company_name_kr": "삼성전자(주)",
  "address_en": "Samseong-ro, Yeongtong-gu, Suwon-si, Gyeonggi-do",
  "verification_checks": {
    "tax_authority_active": true,
    "public_procurement_debarred": false,
    "data_matched": true
  },
  "kyb_pass": true,
  "disclaimer": "Data aggregated directly from official South Korean public databases (FTC and PPS). For reference only.",
  "debug_info": {
    "ftc_http_status": 200,
    "selected_raw_status": "정상영업"
  }
}
```

---

## Response Field Definitions

- `brn` (string): Verified Business Registration Number.
- `status` (string): Commercial status derived from FTC register (`ACTIVE`, `INACTIVE`, or `UNKNOWN`).
- `company_name_en` (string): Translated English company name.
- `company_name_kr` (string): Official Korean registered company name.
- `address_en` (string): Translated English primary business address.
- `verification_checks` (object): Detailed verification indicators.
  - `tax_authority_active` (boolean): `true` if registered as active in FTC mail-order business data.
  - `public_procurement_debarred` (boolean): `true` if debarment/sanction records exist in PPS (G2B).
  - `data_matched` (boolean): `true` if the queried BRN matches official records.
- `kyb_pass` (boolean): `true` if active and free of procurement debarments.
- `disclaimer` (string): Data source and usage note.
- `debug_info` (object): Raw HTTP status and source status text for reference.

---

## Documentation & Free Plan

To test the API interactive playground or subscribe to the Free Tier (BASIC plan), visit the [RapidAPI Marketplace Listing](https://rapidapi.com/c0dem0nkey123/api/south-korea-business-kyb-verification).

## License

MIT License. Free for reference and integration projects.
