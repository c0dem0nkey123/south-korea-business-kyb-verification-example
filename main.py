import json
import os
import requests

# RapidAPI Endpoint & Key Configuration
URL = "https://south-korea-business-kyb-verification.p.rapidapi.com/v1/verify"
API_KEY = os.environ.get("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY")

def verify_korean_business(brn: str):
    # Check if API key is unconfigured
    if not API_KEY or API_KEY == "YOUR_RAPIDAPI_KEY":
        print("API Request Failed: Missing RapidAPI Key. Please replace 'YOUR_RAPIDAPI_KEY' with your actual key.")
        return None

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "south-korea-business-kyb-verification.p.rapidapi.com"
    }
    params = {"brn": brn}

    try:
        response = requests.get(URL, headers=headers, params=params)
        
        # Handle authentication and authorization errors explicitly
        if response.status_code in (401, 403):
            print("API Request Failed: Invalid RapidAPI Key or access forbidden (HTTP 401/403).")
            return None

        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API Request Failed: {e}")
        return None

if __name__ == "__main__":
    """
    ### Request Parameter Guide
    - **`brn`** (required, string): The 10-digit Business Registration Number (사업자등록번호) issued by the National Tax Service of South Korea.
    - **Format**: 10 digits without hyphens (e.g., `1248100998`)
    - **Test Example**: `1248100998` (Samsung Electronics)
    """
    # Test Business Registration Number (e.g., Samsung Electronics: 1248100998)
    
    test_brn = "1248100998"
    result = verify_korean_business(test_brn)
    
    if result:
        print("=== Full KYB Verification Result ===")
        # Print raw JSON formatted with indentation
        print(json.dumps(result, indent=2, ensure_ascii=False))

        print("\n=== Parsed Fields Summary ===")
        print(f"BRN: {result.get('brn')}")
        print(f"Status: {result.get('status')}")
        print(f"Company (EN): {result.get('company_name_en')}")
        print(f"Company (KR): {result.get('company_name_kr')}")
        print(f"Address (EN): {result.get('address_en')}")
        
        # Extract verification checks object
        checks = result.get("verification_checks", {})
        print(f"FTC Active Status: {checks.get('tax_authority_active')}")
        print(f"PPS Debarred: {checks.get('public_procurement_debarred')}")
        print(f"Data Matched: {checks.get('data_matched')}")
        
        print(f"KYB Pass: {result.get('kyb_pass')}")
        print(f"Disclaimer: {result.get('disclaimer')}")
        
        # Extract debug info object
        debug = result.get("debug_info", {})
        print(f"FTC HTTP Status: {debug.get('ftc_http_status')}")
        print(f"Selected Raw Status: {debug.get('selected_raw_status')}")
        
        """
        ### Response Field Definitions
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
        """
