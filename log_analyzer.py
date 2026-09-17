with open("sample.log", "r") as file:
    logs = file.readlines()

failed_attempts = {}

for log in logs:
    if "FAILED" in log:
        parts = log.split()
        ip_address = parts[5].replace("ip=", "")

        if ip_address in failed_attempts:
            failed_attempts[ip_address] += 1
        else:
            failed_attempts[ip_address] = 1

print(failed_attempts)

for ip_address, attempts in failed_attempts.items():
    if attempts >= 3:
        print(f"Suspicious IP: {ip_address} - {attempts} failed attempts")