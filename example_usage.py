from client import FounderWorkplaceOperatingSystemClient

def main():
    client = FounderWorkplaceOperatingSystemClient()
    res = client.synthesize_founder_os(["Fundraising Seed Round", "Hire Tech Lead"], 40000)
    print(f"Estimated Runway: {res['runway_months']} Months")
    print("Daily Priority Stack:")
    for p in res["daily_priority_stack"]:
        print(f"  - {p}")

if __name__ == "__main__":
    main()
