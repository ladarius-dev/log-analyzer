with open("sample.log", "r") as file:
    logs = file.readlines()

failed_attempts = {}
total_failed_attempts = 0

for log in logs:
    if "FAILED" in log:
        total_failed_attempts += 1
        parts = log.split()
        ip_address = parts[5].replace("ip=", "")
        username = parts[4].replace("user=", "")


        if ip_address in failed_attempts:
            failed_attempts[ip_address]["attempts"] += 1
            if username not in failed_attempts[ip_address]["usernames"]:
                failed_attempts[ip_address]["usernames"].append(username)
        else:
            failed_attempts[ip_address] = {
                "attempts": 1,
                "usernames": [username]
            }


print("===== SECURITY LOG REPORT =====")
print(f"Total Failed Login Attempts: {total_failed_attempts}")

for ip_address, attempts in failed_attempts.items():
    if attempts["attempts"] >= 3:
        print(f"Suspicious IP: {ip_address} - {attempts['attempts']} failed attempts - Targeted users: {attempts['usernames']}")
    else:
        print(f"IP: {ip_address} - {attempts['attempts']} failed attempt - Targeted users: {attempts['usernames']}")