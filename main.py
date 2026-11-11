"""news-summary-01 entry: writes a static summary of 11 November 2026 world news.

The summary is a fixed string written to /output/entry.txt. No network, no
clock, no randomness: every run writes the exact same bytes.
"""

import os

SUMMARY = """Wednesday, November 11, 2026. Iran dominated the day. U.S. Secretary of State Marco Rubio said in Paris that America's economic campaign against Tehran is working so well that 'there's really no need for major combat operations any longer,' though force remains an option if Iran crosses red lines. Tehran's security chief Mohsen Rezaei said Iran is still waiting for a U.S. answer to its seven conditions for talks, and the Strait of Hormuz stays closed until they are met. Three oil tankers caught fire after hitting naval mines, and monitors counted at least 37 attacks on ships in and around Hormuz this month, the most since the war began nine months ago.

In Abu Dhabi, the first day of U.S.-mediated talks between Ukraine and Russia was 'constructive and quite substantive,' President Volodymyr Zelenskyy said, and the sides agreed a large prisoner-of-war exchange as the talks closed. NATO scrambled jets after drones strayed into Baltic airspace during Ukrainian strikes on Russia.

In Washington, the House voted 211-204 to send the impeachment resolution against Defense Secretary Pete Hegseth to committee, effectively killing it. The Justice Department charged three Iran-backed operatives over nearly 20 alleged plots in the U.S. and Europe, including one at Britain's RAF Fairford air base, and Treasury Secretary Scott Bessent moved to a military base after threats to his life. In Gaza, Israeli forces killed at least seven people, including a father and his 13-year-old son.

World leaders gathered in Antalya for the COP31 climate summit, where U.N. chief Antonio Guterres warned the slow response to climate change has put the world 'on a path to destruction.' In the Democratic Republic of Congo, Ebola has now infected 11,042 people and killed at least 5,387, the second-deadliest outbreak on record. A U.K. court struck down Trinidad and Tobago's centuries-old ban on gay sex."""


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(SUMMARY)
        f.write("\n")


if __name__ == "__main__":
    main()
