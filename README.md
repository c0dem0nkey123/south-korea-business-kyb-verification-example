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

## Quick Start

### 1. Prerequisites
Get your free API key from [RapidAPI Marketplace](https://rapidapi.com/c0dem0nkey123/api/south-korea-business-kyb-verification).

### 2. Installation
Clone this repository and install dependencies:

```bash
git clone [https://github.com/c0dem0nkey123/south-korea-business-kyb-verification-example.git](https://github.com/c0dem0nkey123/south-korea-business-kyb-verification-example.git)
cd south-korea-business-kyb-verification-example
pip install -r requirements.txt
