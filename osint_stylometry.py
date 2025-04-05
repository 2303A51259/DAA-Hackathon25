def run_osint(ip):
    # Dummy logic for now
    if ip.startswith("192."):
        return "Low Risk"
    elif ip.startswith("10."):
        return "Medium Risk"
    else:
        return "High Risk"
