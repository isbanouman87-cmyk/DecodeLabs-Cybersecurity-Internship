import string

def check_password_strength(password: str) -> dict:
    """
    Evaluates a password's strength based on security policy logic:
    - Length check (Minimum 8 characters)
    - Character variety (Uppercase, Numbers, Symbols)
    """
    if len(password) < 8:
        return {
            "strength": "WEAK",
            "risk": "High (Exponential Brute Force Risk)",
            "passed_criteria": 0,
            "failed_reasons": ["Password must be at least 8 characters long."]
        }
    
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    
    symbols = set(string.punctuation)
    has_symbol = any(char in symbols for char in password)
    
    score = sum([has_upper, has_digit, has_symbol])
    
    failed_reasons = []
    if not has_upper: failed_reasons.append("Missing an uppercase letter [A-Z].")
    if not has_digit: failed_reasons.append("Missing a numerical digit [0-9].")
    if not has_symbol: failed_reasons.append("Missing a special symbol (e.g., @, #, $, !).")
    
    if score == 3:
        strength = "STRONG"
        risk = "Low"
    elif score == 2:
        strength = "MEDIUM"
        risk = "Moderate"
    else:
        strength = "WEAK"
        risk = "High"
        
    return {
        "strength": strength,
        "risk": risk,
        "passed_criteria": score,
        "failed_reasons": failed_reasons
    }
if __name__ == "__main__":
    print("=" * 50)
    print(" Password Strength Checker ")
    print("=" * 50)
    
    user_password = input("Enter a password to evaluate: ").strip()
    
    print("\n[!] Running Analytical Security Scan...")
    result = check_password_strength(user_password)
    
    print("-" * 50)
    print(f"PASSWORD STRENGTH : {result['strength']}")
    print(f"RISK CLASSIFICATION: {result['risk']}")
    print(f"CRITERIA MET       : {result['passed_criteria']}/3")
    
    if result['failed_reasons']:
        print("\nSUGGESTED IMPROVEMENTS:")
        for reason in result['failed_reasons']:
            print(f" -> {reason}")
    else:
        print("\n[+] Excellent! Password complies with our enterprise policy guidelines.")
    print("-" * 50)